# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: transaction_verification.proto
# Protobuf Python Version: 4.25.0
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x1etransaction_verification.proto\x12\x18transaction_verification\"\xbe\x03\n\x0f\x43heckoutRequest\x12\x30\n\x04user\x18\x02 \x01(\x0b\x32\".transaction_verification.UserData\x12<\n\ncreditCard\x18\x03 \x01(\x0b\x32(.transaction_verification.CreditCardData\x12\x44\n\x0e\x62illingAddress\x18\x04 \x01(\x0b\x32,.transaction_verification.BillingAddressData\x12\x34\n\x06\x64\x65vice\x18\x05 \x01(\x0b\x32$.transaction_verification.DeviceData\x12\x36\n\x07\x62rowser\x18\x06 \x01(\x0b\x32%.transaction_verification.BrowserData\x12\x31\n\x05items\x18\x07 \x03(\x0b\x32\".transaction_verification.ItemData\x12\x10\n\x08referrer\x18\x08 \x01(\t\x12\x42\n\x0cvector_clock\x18\t \x01(\x0b\x32,.transaction_verification.VectorClockMessage\")\n\x08UserData\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x0f\n\x07\x63ontact\x18\x02 \x01(\t\"E\n\x0e\x43reditCardData\x12\x0e\n\x06number\x18\x01 \x01(\t\x12\x16\n\x0e\x65xpirationDate\x18\x02 \x01(\t\x12\x0b\n\x03\x63vv\x18\x03 \x01(\t\"_\n\x12\x42illingAddressData\x12\x0e\n\x06street\x18\x01 \x01(\t\x12\x0c\n\x04\x63ity\x18\x02 \x01(\t\x12\r\n\x05state\x18\x03 \x01(\t\x12\x0b\n\x03zip\x18\x04 \x01(\t\x12\x0f\n\x07\x63ountry\x18\x05 \x01(\t\"5\n\nDeviceData\x12\x0c\n\x04type\x18\x01 \x01(\t\x12\r\n\x05model\x18\x02 \x01(\t\x12\n\n\x02os\x18\x03 \x01(\t\",\n\x0b\x42rowserData\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x0f\n\x07version\x18\x02 \x01(\t\"*\n\x08ItemData\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x10\n\x08quantity\x18\x02 \x01(\t\"\x9e\x01\n\rDetermination\x12I\n\x13suggestion_response\x18\x01 \x01(\x0b\x32,.transaction_verification.SuggestionResponse\x12\x42\n\x0cvector_clock\x18\t \x01(\x0b\x32,.transaction_verification.VectorClockMessage\"I\n\x12VectorClockMessage\x12\x12\n\nprocess_id\x18\x01 \x01(\x05\x12\r\n\x05\x63lock\x18\x02 \x03(\x05\x12\x10\n\x08order_id\x18\x03 \x01(\x05\"0\n\x04\x42ook\x12\n\n\x02id\x18\x01 \x01(\x05\x12\x0c\n\x04name\x18\x02 \x01(\t\x12\x0e\n\x06\x61uthor\x18\x03 \x01(\t\"(\n\x11SuggestionRequest\x12\x13\n\x0b\x62ook_titles\x18\x01 \x03(\t\"N\n\x12SuggestionResponse\x12\x38\n\x10\x62ook_suggestions\x18\x01 \x03(\x0b\x32\x1e.transaction_verification.Book2\xe0\x01\n\x12TransactionService\x12j\n\x11verifyTransaction\x12,.transaction_verification.VectorClockMessage\x1a\'.transaction_verification.Determination\x12^\n\x08sendData\x12).transaction_verification.CheckoutRequest\x1a\'.transaction_verification.Determinationb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'transaction_verification_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
  DESCRIPTOR._options = None
  _globals['_CHECKOUTREQUEST']._serialized_start=61
  _globals['_CHECKOUTREQUEST']._serialized_end=507
  _globals['_USERDATA']._serialized_start=509
  _globals['_USERDATA']._serialized_end=550
  _globals['_CREDITCARDDATA']._serialized_start=552
  _globals['_CREDITCARDDATA']._serialized_end=621
  _globals['_BILLINGADDRESSDATA']._serialized_start=623
  _globals['_BILLINGADDRESSDATA']._serialized_end=718
  _globals['_DEVICEDATA']._serialized_start=720
  _globals['_DEVICEDATA']._serialized_end=773
  _globals['_BROWSERDATA']._serialized_start=775
  _globals['_BROWSERDATA']._serialized_end=819
  _globals['_ITEMDATA']._serialized_start=821
  _globals['_ITEMDATA']._serialized_end=863
  _globals['_DETERMINATION']._serialized_start=866
  _globals['_DETERMINATION']._serialized_end=1024
  _globals['_VECTORCLOCKMESSAGE']._serialized_start=1026
  _globals['_VECTORCLOCKMESSAGE']._serialized_end=1099
  _globals['_BOOK']._serialized_start=1101
  _globals['_BOOK']._serialized_end=1149
  _globals['_SUGGESTIONREQUEST']._serialized_start=1151
  _globals['_SUGGESTIONREQUEST']._serialized_end=1191
  _globals['_SUGGESTIONRESPONSE']._serialized_start=1193
  _globals['_SUGGESTIONRESPONSE']._serialized_end=1271
  _globals['_TRANSACTIONSERVICE']._serialized_start=1274
  _globals['_TRANSACTIONSERVICE']._serialized_end=1498
# @@protoc_insertion_point(module_scope)
