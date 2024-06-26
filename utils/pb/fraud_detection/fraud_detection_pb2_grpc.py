# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

from utils.pb.fraud_detection import fraud_detection_pb2 as pb_dot_fraud__detection_dot_fraud__detection__pb2


class HelloServiceStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.SayHello = channel.unary_unary(
                '/hello.HelloService/SayHello',
                request_serializer=pb_dot_fraud__detection_dot_fraud__detection__pb2.HelloRequest.SerializeToString,
                response_deserializer=pb_dot_fraud__detection_dot_fraud__detection__pb2.HelloResponse.FromString,
                )


class HelloServiceServicer(object):
    """Missing associated documentation comment in .proto file."""

    def SayHello(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_HelloServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'SayHello': grpc.unary_unary_rpc_method_handler(
                    servicer.SayHello,
                    request_deserializer=pb_dot_fraud__detection_dot_fraud__detection__pb2.HelloRequest.FromString,
                    response_serializer=pb_dot_fraud__detection_dot_fraud__detection__pb2.HelloResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'hello.HelloService', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class HelloService(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def SayHello(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/hello.HelloService/SayHello',
            pb_dot_fraud__detection_dot_fraud__detection__pb2.HelloRequest.SerializeToString,
            pb_dot_fraud__detection_dot_fraud__detection__pb2.HelloResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)


class FraudServiceStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.sendData = channel.unary_unary(
                '/hello.FraudService/sendData',
                request_serializer=pb_dot_fraud__detection_dot_fraud__detection__pb2.CheckoutRequest.SerializeToString,
                response_deserializer=pb_dot_fraud__detection_dot_fraud__detection__pb2.Determination.FromString,
                )
        self.DetectFraud = channel.unary_unary(
                '/hello.FraudService/DetectFraud',
                request_serializer=pb_dot_fraud__detection_dot_fraud__detection__pb2.VectorClockMessage.SerializeToString,
                response_deserializer=pb_dot_fraud__detection_dot_fraud__detection__pb2.Determination.FromString,
                )


class FraudServiceServicer(object):
    """Missing associated documentation comment in .proto file."""

    def sendData(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def DetectFraud(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_FraudServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'sendData': grpc.unary_unary_rpc_method_handler(
                    servicer.sendData,
                    request_deserializer=pb_dot_fraud__detection_dot_fraud__detection__pb2.CheckoutRequest.FromString,
                    response_serializer=pb_dot_fraud__detection_dot_fraud__detection__pb2.Determination.SerializeToString,
            ),
            'DetectFraud': grpc.unary_unary_rpc_method_handler(
                    servicer.DetectFraud,
                    request_deserializer=pb_dot_fraud__detection_dot_fraud__detection__pb2.VectorClockMessage.FromString,
                    response_serializer=pb_dot_fraud__detection_dot_fraud__detection__pb2.Determination.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'hello.FraudService', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class FraudService(object):
    """Missing associated documentation comment in .proto file."""

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
        return grpc.experimental.unary_unary(request, target, '/hello.FraudService/sendData',
            pb_dot_fraud__detection_dot_fraud__detection__pb2.CheckoutRequest.SerializeToString,
            pb_dot_fraud__detection_dot_fraud__detection__pb2.Determination.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def DetectFraud(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/hello.FraudService/DetectFraud',
            pb_dot_fraud__detection_dot_fraud__detection__pb2.VectorClockMessage.SerializeToString,
            pb_dot_fraud__detection_dot_fraud__detection__pb2.Determination.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
