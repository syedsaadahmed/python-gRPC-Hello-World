# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: grpctest.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='grpctest.proto',
  package='grpctest',
  syntax='proto3',
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\x0egrpctest.proto\x12\x08grpctest\"\x1a\n\x07Message\x12\x0f\n\x07message\x18\x01 \x01(\t\"4\n\x0fMessageResponse\x12\x0f\n\x07message\x18\x01 \x01(\t\x12\x10\n\x08received\x18\x02 \x01(\x08\x32O\n\x08Grpctest\x12\x43\n\x11GetServerResponse\x12\x11.grpctest.Message\x1a\x19.grpctest.MessageResponse\"\x00\x62\x06proto3'
)




_MESSAGE = _descriptor.Descriptor(
  name='Message',
  full_name='grpctest.Message',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='message', full_name='grpctest.Message.message', index=0,
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
  serialized_start=28,
  serialized_end=54,
)


_MESSAGERESPONSE = _descriptor.Descriptor(
  name='MessageResponse',
  full_name='grpctest.MessageResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='message', full_name='grpctest.MessageResponse.message', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='received', full_name='grpctest.MessageResponse.received', index=1,
      number=2, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
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
  serialized_start=56,
  serialized_end=108,
)

DESCRIPTOR.message_types_by_name['Message'] = _MESSAGE
DESCRIPTOR.message_types_by_name['MessageResponse'] = _MESSAGERESPONSE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

Message = _reflection.GeneratedProtocolMessageType('Message', (_message.Message,), {
  'DESCRIPTOR' : _MESSAGE,
  '__module__' : 'grpctest_pb2'
  # @@protoc_insertion_point(class_scope:grpctest.Message)
  })
_sym_db.RegisterMessage(Message)

MessageResponse = _reflection.GeneratedProtocolMessageType('MessageResponse', (_message.Message,), {
  'DESCRIPTOR' : _MESSAGERESPONSE,
  '__module__' : 'grpctest_pb2'
  # @@protoc_insertion_point(class_scope:grpctest.MessageResponse)
  })
_sym_db.RegisterMessage(MessageResponse)



_GRPCTEST = _descriptor.ServiceDescriptor(
  name='Grpctest',
  full_name='grpctest.Grpctest',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_start=110,
  serialized_end=189,
  methods=[
  _descriptor.MethodDescriptor(
    name='GetServerResponse',
    full_name='grpctest.Grpctest.GetServerResponse',
    index=0,
    containing_service=None,
    input_type=_MESSAGE,
    output_type=_MESSAGERESPONSE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
])
_sym_db.RegisterServiceDescriptor(_GRPCTEST)

DESCRIPTOR.services_by_name['Grpctest'] = _GRPCTEST

# @@protoc_insertion_point(module_scope)
