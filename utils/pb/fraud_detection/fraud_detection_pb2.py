# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: pb/fraud_detection/fraud_detection.proto
# Protobuf Python Version: 4.25.0
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n(pb/fraud_detection/fraud_detection.proto\x12\x05hello\"\x1c\n\x0cHelloRequest\x12\x0c\n\x04name\x18\x01 \x01(\t\"!\n\rHelloResponse\x12\x10\n\x08greeting\x18\x01 \x01(\t\"\xb9\x02\n\x0f\x43heckoutRequest\x12\x1d\n\x04user\x18\x02 \x01(\x0b\x32\x0f.hello.UserData\x12)\n\ncreditCard\x18\x03 \x01(\x0b\x32\x15.hello.CreditCardData\x12\x31\n\x0e\x62illingAddress\x18\x04 \x01(\x0b\x32\x19.hello.BillingAddressData\x12!\n\x06\x64\x65vice\x18\x05 \x01(\x0b\x32\x11.hello.DeviceData\x12#\n\x07\x62rowser\x18\x06 \x01(\x0b\x32\x12.hello.BrowserData\x12\x1e\n\x05items\x18\x07 \x03(\x0b\x32\x0f.hello.ItemData\x12\x10\n\x08referrer\x18\x08 \x01(\t\x12/\n\x0cvector_clock\x18\t \x01(\x0b\x32\x19.hello.VectorClockMessage\")\n\x08UserData\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x0f\n\x07\x63ontact\x18\x02 \x01(\t\"E\n\x0e\x43reditCardData\x12\x0e\n\x06number\x18\x01 \x01(\t\x12\x16\n\x0e\x65xpirationDate\x18\x02 \x01(\t\x12\x0b\n\x03\x63vv\x18\x03 \x01(\t\"_\n\x12\x42illingAddressData\x12\x0e\n\x06street\x18\x01 \x01(\t\x12\x0c\n\x04\x63ity\x18\x02 \x01(\t\x12\r\n\x05state\x18\x03 \x01(\t\x12\x0b\n\x03zip\x18\x04 \x01(\t\x12\x0f\n\x07\x63ountry\x18\x05 \x01(\t\"5\n\nDeviceData\x12\x0c\n\x04type\x18\x01 \x01(\t\x12\r\n\x05model\x18\x02 \x01(\t\x12\n\n\x02os\x18\x03 \x01(\t\",\n\x0b\x42rowserData\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x0f\n\x07version\x18\x02 \x01(\t\"*\n\x08ItemData\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x10\n\x08quantity\x18\x02 \x01(\t\"x\n\rDetermination\x12\x36\n\x13suggestion_response\x18\x01 \x01(\x0b\x32\x19.hello.SuggestionResponse\x12/\n\x0cvector_clock\x18\t \x01(\x0b\x32\x19.hello.VectorClockMessage\"I\n\x12VectorClockMessage\x12\x12\n\nprocess_id\x18\x01 \x01(\x05\x12\r\n\x05\x63lock\x18\x02 \x03(\x05\x12\x10\n\x08order_id\x18\x03 \x01(\x05\"0\n\x04\x42ook\x12\n\n\x02id\x18\x01 \x01(\x05\x12\x0c\n\x04name\x18\x02 \x01(\t\x12\x0e\n\x06\x61uthor\x18\x03 \x01(\t\"(\n\x11SuggestionRequest\x12\x13\n\x0b\x62ook_titles\x18\x01 \x03(\t\";\n\x12SuggestionResponse\x12%\n\x10\x62ook_suggestions\x18\x01 \x03(\x0b\x32\x0b.hello.Book2E\n\x0cHelloService\x12\x35\n\x08SayHello\x12\x13.hello.HelloRequest\x1a\x14.hello.HelloResponse2\x88\x01\n\x0c\x46raudService\x12\x38\n\x08sendData\x12\x16.hello.CheckoutRequest\x1a\x14.hello.Determination\x12>\n\x0b\x44\x65tectFraud\x12\x19.hello.VectorClockMessage\x1a\x14.hello.Determinationb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'pb.fraud_detection.fraud_detection_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
  DESCRIPTOR._options = None
  _globals['_HELLOREQUEST']._serialized_start=51
  _globals['_HELLOREQUEST']._serialized_end=79
  _globals['_HELLORESPONSE']._serialized_start=81
  _globals['_HELLORESPONSE']._serialized_end=114
  _globals['_CHECKOUTREQUEST']._serialized_start=117
  _globals['_CHECKOUTREQUEST']._serialized_end=430
  _globals['_USERDATA']._serialized_start=432
  _globals['_USERDATA']._serialized_end=473
  _globals['_CREDITCARDDATA']._serialized_start=475
  _globals['_CREDITCARDDATA']._serialized_end=544
  _globals['_BILLINGADDRESSDATA']._serialized_start=546
  _globals['_BILLINGADDRESSDATA']._serialized_end=641
  _globals['_DEVICEDATA']._serialized_start=643
  _globals['_DEVICEDATA']._serialized_end=696
  _globals['_BROWSERDATA']._serialized_start=698
  _globals['_BROWSERDATA']._serialized_end=742
  _globals['_ITEMDATA']._serialized_start=744
  _globals['_ITEMDATA']._serialized_end=786
  _globals['_DETERMINATION']._serialized_start=788
  _globals['_DETERMINATION']._serialized_end=908
  _globals['_VECTORCLOCKMESSAGE']._serialized_start=910
  _globals['_VECTORCLOCKMESSAGE']._serialized_end=983
  _globals['_BOOK']._serialized_start=985
  _globals['_BOOK']._serialized_end=1033
  _globals['_SUGGESTIONREQUEST']._serialized_start=1035
  _globals['_SUGGESTIONREQUEST']._serialized_end=1075
  _globals['_SUGGESTIONRESPONSE']._serialized_start=1077
  _globals['_SUGGESTIONRESPONSE']._serialized_end=1136
  _globals['_HELLOSERVICE']._serialized_start=1138
  _globals['_HELLOSERVICE']._serialized_end=1207
  _globals['_FRAUDSERVICE']._serialized_start=1210
  _globals['_FRAUDSERVICE']._serialized_end=1346
# @@protoc_insertion_point(module_scope)
