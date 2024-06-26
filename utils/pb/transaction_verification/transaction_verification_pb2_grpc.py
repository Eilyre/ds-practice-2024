# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

import utils.pb.transaction_verification.transaction_verification_pb2 as transaction__verification__pb2


class TransactionServiceStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.verifyTransaction = channel.unary_unary(
                '/transaction_verification.TransactionService/verifyTransaction',
                request_serializer=transaction__verification__pb2.VectorClockMessage.SerializeToString,
                response_deserializer=transaction__verification__pb2.Determination.FromString,
                )
        self.sendData = channel.unary_unary(
                '/transaction_verification.TransactionService/sendData',
                request_serializer=transaction__verification__pb2.CheckoutRequest.SerializeToString,
                response_deserializer=transaction__verification__pb2.Determination.FromString,
                )


class TransactionServiceServicer(object):
    """Missing associated documentation comment in .proto file."""

    def verifyTransaction(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def sendData(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_TransactionServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'verifyTransaction': grpc.unary_unary_rpc_method_handler(
                    servicer.verifyTransaction,
                    request_deserializer=transaction__verification__pb2.VectorClockMessage.FromString,
                    response_serializer=transaction__verification__pb2.Determination.SerializeToString,
            ),
            'sendData': grpc.unary_unary_rpc_method_handler(
                    servicer.sendData,
                    request_deserializer=transaction__verification__pb2.CheckoutRequest.FromString,
                    response_serializer=transaction__verification__pb2.Determination.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'transaction_verification.TransactionService', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class TransactionService(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def verifyTransaction(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/transaction_verification.TransactionService/verifyTransaction',
            transaction__verification__pb2.VectorClockMessage.SerializeToString,
            transaction__verification__pb2.Determination.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def sendData(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/transaction_verification.TransactionService/sendData',
            transaction__verification__pb2.CheckoutRequest.SerializeToString,
            transaction__verification__pb2.Determination.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
