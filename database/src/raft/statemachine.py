import threading


class StateMachine:
    def __init__(self):
        self._data_store = {}
        self._ds_lock = threading.Lock()

    def apply(self, operation, key, value=None):
        with self._ds_lock:
            match operation.lower():
                case "set":
                    return self._set(key, value)
                case "update":
                    return self._set(key, value)
                case "get":
                    return self._delete(key)
                case "delete":
                    return self._delete(key)
                case "lock":
                    return self._lock(key)
                case "unlock":
                    return self._unlock(key)
                case "commit":
                    return self._commit(key, value)
                case _:
                    return f"Unknown operation {operation}"

    def _commit(self, key, value):
        if key in self._data_store.keys() and self._data_store[key]["locked"] is True:
            self._data_store[key] = {"value": value, "locked": False}
            self._unlock(key)
            return f"Commited {key} = {value}."

        else:
            return Exception(f"Key is not locked, cannot commit.")

    def _set(self, key, value):
        if key not in self._data_store.keys() or self._data_store[key]["locked"] is False:
            self._data_store[key] = {"value": value, "locked": False}
            return f"Set {key} = {value}"

        else:
            return BlockingIOError(f"Cannot overwrite locked key: {key}.")

    def _get(self, key):
        return self._data_store.get(key, "Key not found")["value"]

    def _delete(self, key):
        if key in self._data_store.keys() and self._data_store[key]["locked"] is True:
            return BlockingIOError(f"Cannot delete locked key: {key}.")

        else:
            del self._data_store[key]
            return f"Deleted {key}"

    def _lock(self, key):
        if key in self._data_store.keys() and self._data_store[key]["locked"] is True:
            return BlockingIOError(f"Cannot lock a locked key: {key}.")

        self._data_store[key]["locked"] = True
        return f"Locked key: {key}"

    def _unlock(self, key):
        self._data_store[key]["locked"] = False
        return f"Unlocked key: {key}"

    def is_locked(self, key):
        return self._data_store[key]["locked"] if key in self._data_store.keys() else False

    def __len__(self):
        """Returns the number of items in the state machine."""
        return len(self._data_store)

    def __repr__(self):
        """Provides a string representation of the state machine."""
        return f"StateMachine with {len(self)} items: {self._data_store}"
