# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

from utils.pb.mq import mq_pb2 as utils_dot_pb_dot_mq_dot_mq__pb2


class MQServiceStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.enqueue = channel.unary_unary(
                '/mq.MQService/enqueue',
                request_serializer=utils_dot_pb_dot_mq_dot_mq__pb2.CheckoutRequest.SerializeToString,
                response_deserializer=utils_dot_pb_dot_mq_dot_mq__pb2.Response.FromString,
                )
        self.dequeue = channel.unary_unary(
                '/mq.MQService/dequeue',
                request_serializer=utils_dot_pb_dot_mq_dot_mq__pb2.Empty.SerializeToString,
                response_deserializer=utils_dot_pb_dot_mq_dot_mq__pb2.CheckoutRequest.FromString,
                )
        self.info = channel.unary_unary(
                '/mq.MQService/info',
                request_serializer=utils_dot_pb_dot_mq_dot_mq__pb2.Empty.SerializeToString,
                response_deserializer=utils_dot_pb_dot_mq_dot_mq__pb2.QueueStatus.FromString,
                )


class MQServiceServicer(object):
    """Missing associated documentation comment in .proto file."""

    def enqueue(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def dequeue(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def info(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_MQServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'enqueue': grpc.unary_unary_rpc_method_handler(
                    servicer.enqueue,
                    request_deserializer=utils_dot_pb_dot_mq_dot_mq__pb2.CheckoutRequest.FromString,
                    response_serializer=utils_dot_pb_dot_mq_dot_mq__pb2.Response.SerializeToString,
            ),
            'dequeue': grpc.unary_unary_rpc_method_handler(
                    servicer.dequeue,
                    request_deserializer=utils_dot_pb_dot_mq_dot_mq__pb2.Empty.FromString,
                    response_serializer=utils_dot_pb_dot_mq_dot_mq__pb2.CheckoutRequest.SerializeToString,
            ),
            'info': grpc.unary_unary_rpc_method_handler(
                    servicer.info,
                    request_deserializer=utils_dot_pb_dot_mq_dot_mq__pb2.Empty.FromString,
                    response_serializer=utils_dot_pb_dot_mq_dot_mq__pb2.QueueStatus.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'mq.MQService', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class MQService(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def enqueue(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/mq.MQService/enqueue',
            utils_dot_pb_dot_mq_dot_mq__pb2.CheckoutRequest.SerializeToString,
            utils_dot_pb_dot_mq_dot_mq__pb2.Response.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def dequeue(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/mq.MQService/dequeue',
            utils_dot_pb_dot_mq_dot_mq__pb2.Empty.SerializeToString,
            utils_dot_pb_dot_mq_dot_mq__pb2.CheckoutRequest.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def info(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/mq.MQService/info',
            utils_dot_pb_dot_mq_dot_mq__pb2.Empty.SerializeToString,
            utils_dot_pb_dot_mq_dot_mq__pb2.QueueStatus.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
