from .state import NodeState

from ..proto import raft_pb2


class Follower(NodeState):

    def timeout(self):
        return self._random_timeout()

    def handle_vote_request(self, message):
        """Handle incoming RequestVote messages in Follower state."""
        if message.term > self.node.term:
            self.node.term = message.term
            self.node.voted_for = None

        # Reply false if term < currentTerm (§5.1)
        if message.term < self.node.term:
            return raft_pb2.RequestVoteResponse(term=self.node.term, granted=False)

        # If votedFor is null or candidateId, and candidate’s log is at
        # least as up-to-date as receiver’s log, grant vote (§5.2, §5.4)
        if (message.last_log_term < self.get_last_log_term() or
                (message.last_log_term == self.get_last_log_term() and message.last_log_index < self.get_last_log_index())):
            return raft_pb2.RequestVoteResponse(term=self.node.term, granted=False)

        # If votedFor is null or candidateId, and candidate’s log is at
        # least as up-to-date as receiver’s log, grant vote (§5.2, §5.4)
        if self.node.voted_for is None or self.node.voted_for == message.candidate_id:
            self.node.voted_for = message.candidate_id
            return raft_pb2.RequestVoteResponse(term=self.node.term, granted=True)

        return raft_pb2.RequestVoteResponse(term=self.node.term, granted=False)

    def handle_append_entries(self, message):
        self.logger.debug(
            f"Received AppendEntries RPC term: {message.term} from {message.leader_id} with {message.entries}, prev_index: {message.previous_log_index} and prev_term: {message.previous_log_term}")

        # Reply false if term < currentTerm (§5.1)
        if message.term < self.node.term:
            self.logger.debug(f"Rejecting AppendEntries RPC from outdated term {message.term}. Current term is {self.node.term}.")
            return raft_pb2.AppendEntriesResponse(term=self.node.term, success=False)

        self.node.reset_timer()

        # If RPC request or response contains term T > currentTerm:
        #   set currentTerm = T, convert to follower (§5.1)
        if message.term > self.node.term:
            self.logger.debug(f"Request term {message.term} higher than mine {self.node.term}")
            self.node.term = message.term
            self.node.voted_for = None
            self.node.change_state(Follower)

            return self.node.state.handle_append_entries(message)

        # If an existing entry conflicts with a new one (same index but different terms), delete the existing entry and all that
        # follow it (§5.3).
        if self.get_last_log_index() > message.previous_log_index and self.node.log[message.previous_log_index][
            'term'] != message.previous_log_term:
            # This handles a case where local log is bigger than remote, in which case the local log should be truncated.
            self.logger.debug(
                f"Log inconsistency detected at local/remote index {self.get_last_log_index()}/{message.previous_log_index}. Truncating log and rejecting AppendEntries.")
            self.node.log = self.node.log[:message.previous_log_index]
            return raft_pb2.AppendEntriesResponse(term=self.node.term, success=False)
        elif self.get_last_log_index() < message.previous_log_index:
            # This handles a case where local log is much smaller than remote, in which case the remote tracker should be notified to reduce the counts.
            self.logger.debug(
                f"Log inconsistency detected at local/remote index {self.get_last_log_index()}/{message.previous_log_index}. Truncating log and rejecting AppendEntries.")
            return raft_pb2.AppendEntriesResponse(term=self.node.term, success=False)

        # Append any new entries not already in the log.
        if message.entries:
            self.logger.debug(f"Appending {len(message.entries)} to local log.")
            self.node.log.extend(self._convert_log_entries(message.entries))

        # If leaderCommit > commitIndex, set commitIndex = min(leaderCommit, index of last new entry)
        if message.commit_index > self.node.commit_index:
            self.node.commit_index = min(message.commit_index, len(self.node.log) - 1)
            self.logger.debug(f"Commit index updated to {self.node.commit_index} based on leader's commit index {message.commit_index}.")

        self.logger.debug(
            f"AppendEntries RPC processed successfully. Commit index is now {self.node.commit_index}, last_log_term ({self.get_last_log_term()}), last_log_index ({self.get_last_log_index()}).")

        # TODO: State machine commit.

        return raft_pb2.AppendEntriesResponse(term=self.node.term, success=True)

    def handle_timeout(self):
        self.logger.info('Follower timeout, transitioning to Candidate')
        from .candidate import Candidate
        self.node.change_state(Candidate)
