# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: utils/pb/database/database.proto
# Protobuf Python Version: 4.25.0
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n utils/pb/database/database.proto\x12\x08\x64\x61tabase\"+\n\x08Response\x12\x0e\n\x06status\x18\x01 \x01(\x08\x12\x0f\n\x07message\x18\x02 \x01(\t\"$\n\x16Request_Commit_Message\x12\n\n\x02id\x18\x01 \x01(\t\".\n\x0e\x43ommit_Message\x12\n\n\x02id\x18\x01 \x01(\t\x12\x10\n\x08rollback\x18\x02 \x01(\x08\"\x07\n\x05\x45mpty2\xdf\x01\n\x08\x44\x61tabase\x12(\n\x04Read\x12\x0f.database.Empty\x1a\x0f.database.Empty\x12)\n\x05Write\x12\x0f.database.Empty\x1a\x0f.database.Empty\x12\x46\n\x0eRequest_Commit\x12 .database.Request_Commit_Message\x1a\x12.database.Response\x12\x36\n\x06\x43ommit\x12\x18.database.Commit_Message\x1a\x12.database.Responseb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'utils.pb.database.database_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
  DESCRIPTOR._options = None
  _globals['_RESPONSE']._serialized_start=46
  _globals['_RESPONSE']._serialized_end=89
  _globals['_REQUEST_COMMIT_MESSAGE']._serialized_start=91
  _globals['_REQUEST_COMMIT_MESSAGE']._serialized_end=127
  _globals['_COMMIT_MESSAGE']._serialized_start=129
  _globals['_COMMIT_MESSAGE']._serialized_end=175
  _globals['_EMPTY']._serialized_start=177
  _globals['_EMPTY']._serialized_end=184
  _globals['_DATABASE']._serialized_start=187
  _globals['_DATABASE']._serialized_end=410
# @@protoc_insertion_point(module_scope)
