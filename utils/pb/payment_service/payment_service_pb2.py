# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: payment_service.proto
# Protobuf Python Version: 4.25.0
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x15payment_service.proto\x12\x0fpayment_service\"+\n\x08Response\x12\x0e\n\x06status\x18\x01 \x01(\x08\x12\x0f\n\x07message\x18\x02 \x01(\t\"$\n\x16Request_Commit_Message\x12\n\n\x02id\x18\x01 \x01(\x05\"\x1c\n\x0e\x43ommit_Message\x12\n\n\x02id\x18\x01 \x01(\x05\x32\xad\x01\n\x0fPayment_Service\x12T\n\x0eRequest_Commit\x12\'.payment_service.Request_Commit_Message\x1a\x19.payment_service.Response\x12\x44\n\x06\x43ommit\x12\x1f.payment_service.Commit_Message\x1a\x19.payment_service.Responseb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'payment_service_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
  DESCRIPTOR._options = None
  _globals['_RESPONSE']._serialized_start=42
  _globals['_RESPONSE']._serialized_end=85
  _globals['_REQUEST_COMMIT_MESSAGE']._serialized_start=87
  _globals['_REQUEST_COMMIT_MESSAGE']._serialized_end=123
  _globals['_COMMIT_MESSAGE']._serialized_start=125
  _globals['_COMMIT_MESSAGE']._serialized_end=153
  _globals['_PAYMENT_SERVICE']._serialized_start=156
  _globals['_PAYMENT_SERVICE']._serialized_end=329
# @@protoc_insertion_point(module_scope)
