# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: String.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='String.proto',
  package='tzrpc.proto',
  syntax='proto3',
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\x0cString.proto\x12\x0btzrpc.proto\"\x16\n\x06String\x12\x0c\n\x04text\x18\x01 \x01(\t\"\x1f\n\x0fStringArrayList\x12\x0c\n\x04text\x18\x01 \x03(\tb\x06proto3'
)




_STRING = _descriptor.Descriptor(
  name='String',
  full_name='tzrpc.proto.String',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='text', full_name='tzrpc.proto.String.text', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=29,
  serialized_end=51,
)


_STRINGARRAYLIST = _descriptor.Descriptor(
  name='StringArrayList',
  full_name='tzrpc.proto.StringArrayList',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='text', full_name='tzrpc.proto.StringArrayList.text', index=0,
      number=1, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=53,
  serialized_end=84,
)

DESCRIPTOR.message_types_by_name['String'] = _STRING
DESCRIPTOR.message_types_by_name['StringArrayList'] = _STRINGARRAYLIST
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

String = _reflection.GeneratedProtocolMessageType('String', (_message.Message,), {
  'DESCRIPTOR' : _STRING,
  '__module__' : 'String_pb2'
  # @@protoc_insertion_point(class_scope:tzrpc.proto.String)
  })
_sym_db.RegisterMessage(String)

StringArrayList = _reflection.GeneratedProtocolMessageType('StringArrayList', (_message.Message,), {
  'DESCRIPTOR' : _STRINGARRAYLIST,
  '__module__' : 'String_pb2'
  # @@protoc_insertion_point(class_scope:tzrpc.proto.StringArrayList)
  })
_sym_db.RegisterMessage(StringArrayList)


# @@protoc_insertion_point(module_scope)
