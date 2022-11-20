# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: aruba-iot-zb-types.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf.internal import enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


import src.proto.aruba_iot_types_pb2 as aruba__iot__types__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='aruba-iot-zb-types.proto',
  package='aruba_telemetry',
  syntax='proto2',
  serialized_options=None,
  serialized_pb=_b('\n\x18\x61ruba-iot-zb-types.proto\x12\x0f\x61ruba_telemetry\x1a\x15\x61ruba-iot-types.proto\"A\n\x05ZbEPC\x12\x10\n\x08\x65ndpoint\x18\x01 \x01(\r\x12\x12\n\nprofile_id\x18\x02 \x01(\r\x12\x12\n\ncluster_id\x18\x03 \x01(\r\"N\n\x06ZbE2PC\x12+\n\x0b\x64\x65stination\x18\x01 \x01(\x0b\x32\x16.aruba_telemetry.ZbEPC\x12\x17\n\x0fsource_endpoint\x18\x02 \x01(\r*%\n\x08ZbResult\x12\r\n\tSUCCEEDED\x10\x00\x12\n\n\x06\x46\x41ILED\x10\x01*\x13\n\tZbAckCode\x12\x06\n\x02OK\x10\x00')
  ,
  dependencies=[aruba__iot__types__pb2.DESCRIPTOR,])

_ZBRESULT = _descriptor.EnumDescriptor(
  name='ZbResult',
  full_name='aruba_telemetry.ZbResult',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='SUCCEEDED', index=0, number=0,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='FAILED', index=1, number=1,
      serialized_options=None,
      type=None),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=215,
  serialized_end=252,
)
_sym_db.RegisterEnumDescriptor(_ZBRESULT)

ZbResult = enum_type_wrapper.EnumTypeWrapper(_ZBRESULT)
_ZBACKCODE = _descriptor.EnumDescriptor(
  name='ZbAckCode',
  full_name='aruba_telemetry.ZbAckCode',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='OK', index=0, number=0,
      serialized_options=None,
      type=None),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=254,
  serialized_end=273,
)
_sym_db.RegisterEnumDescriptor(_ZBACKCODE)

ZbAckCode = enum_type_wrapper.EnumTypeWrapper(_ZBACKCODE)
SUCCEEDED = 0
FAILED = 1
OK = 0



_ZBEPC = _descriptor.Descriptor(
  name='ZbEPC',
  full_name='aruba_telemetry.ZbEPC',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='endpoint', full_name='aruba_telemetry.ZbEPC.endpoint', index=0,
      number=1, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='profile_id', full_name='aruba_telemetry.ZbEPC.profile_id', index=1,
      number=2, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='cluster_id', full_name='aruba_telemetry.ZbEPC.cluster_id', index=2,
      number=3, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=68,
  serialized_end=133,
)


_ZBE2PC = _descriptor.Descriptor(
  name='ZbE2PC',
  full_name='aruba_telemetry.ZbE2PC',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='destination', full_name='aruba_telemetry.ZbE2PC.destination', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='source_endpoint', full_name='aruba_telemetry.ZbE2PC.source_endpoint', index=1,
      number=2, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=135,
  serialized_end=213,
)

_ZBE2PC.fields_by_name['destination'].message_type = _ZBEPC
DESCRIPTOR.message_types_by_name['ZbEPC'] = _ZBEPC
DESCRIPTOR.message_types_by_name['ZbE2PC'] = _ZBE2PC
DESCRIPTOR.enum_types_by_name['ZbResult'] = _ZBRESULT
DESCRIPTOR.enum_types_by_name['ZbAckCode'] = _ZBACKCODE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

ZbEPC = _reflection.GeneratedProtocolMessageType('ZbEPC', (_message.Message,), dict(
  DESCRIPTOR = _ZBEPC,
  __module__ = 'aruba_iot_zb_types_pb2'
  # @@protoc_insertion_point(class_scope:aruba_telemetry.ZbEPC)
  ))
_sym_db.RegisterMessage(ZbEPC)

ZbE2PC = _reflection.GeneratedProtocolMessageType('ZbE2PC', (_message.Message,), dict(
  DESCRIPTOR = _ZBE2PC,
  __module__ = 'aruba_iot_zb_types_pb2'
  # @@protoc_insertion_point(class_scope:aruba_telemetry.ZbE2PC)
  ))
_sym_db.RegisterMessage(ZbE2PC)


# @@protoc_insertion_point(module_scope)