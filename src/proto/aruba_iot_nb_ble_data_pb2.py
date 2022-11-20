# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: aruba-iot-nb-ble-data.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf.internal import enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='aruba-iot-nb-ble-data.proto',
  package='aruba_telemetry',
  syntax='proto2',
  serialized_options=None,
  serialized_pb=_b('\n\x1b\x61ruba-iot-nb-ble-data.proto\x12\x0f\x61ruba_telemetry\"\xa4\x01\n\x07\x42leData\x12\x0b\n\x03mac\x18\x01 \x01(\x0c\x12\x30\n\tframeType\x18\x02 \x01(\x0e\x32\x1d.aruba_telemetry.BleFrameType\x12\x0c\n\x04\x64\x61ta\x18\x03 \x01(\x0c\x12\x0c\n\x04rssi\x18\x04 \x01(\x11\x12.\n\x08\x61\x64\x64rType\x18\x05 \x01(\x0e\x32\x1c.aruba_telemetry.MacAddrType\x12\x0e\n\x06\x61pbMac\x18\x06 \x01(\x0c*d\n\x0c\x42leFrameType\x12\x0b\n\x07\x61\x64v_ind\x10\x00\x12\x12\n\x0e\x61\x64v_direct_ind\x10\x01\x12\x13\n\x0f\x61\x64v_nonconn_ind\x10\x02\x12\x0c\n\x08scan_rsp\x10\x04\x12\x10\n\x0c\x61\x64v_scan_ind\x10\x06*\x81\x01\n\x0bMacAddrType\x12\x14\n\x10\x61\x64\x64r_type_public\x10\x00\x12\x14\n\x10\x61\x64\x64r_type_static\x10\x01\x12$\n addr_type_private_non_resolvable\x10\x02\x12 \n\x1c\x61\x64\x64r_type_private_resolvable\x10\x03')
)

_BLEFRAMETYPE = _descriptor.EnumDescriptor(
  name='BleFrameType',
  full_name='aruba_telemetry.BleFrameType',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='adv_ind', index=0, number=0,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='adv_direct_ind', index=1, number=1,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='adv_nonconn_ind', index=2, number=2,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='scan_rsp', index=3, number=4,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='adv_scan_ind', index=4, number=6,
      serialized_options=None,
      type=None),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=215,
  serialized_end=315,
)
_sym_db.RegisterEnumDescriptor(_BLEFRAMETYPE)

BleFrameType = enum_type_wrapper.EnumTypeWrapper(_BLEFRAMETYPE)
_MACADDRTYPE = _descriptor.EnumDescriptor(
  name='MacAddrType',
  full_name='aruba_telemetry.MacAddrType',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='addr_type_public', index=0, number=0,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='addr_type_static', index=1, number=1,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='addr_type_private_non_resolvable', index=2, number=2,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='addr_type_private_resolvable', index=3, number=3,
      serialized_options=None,
      type=None),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=318,
  serialized_end=447,
)
_sym_db.RegisterEnumDescriptor(_MACADDRTYPE)

MacAddrType = enum_type_wrapper.EnumTypeWrapper(_MACADDRTYPE)
adv_ind = 0
adv_direct_ind = 1
adv_nonconn_ind = 2
scan_rsp = 4
adv_scan_ind = 6
addr_type_public = 0
addr_type_static = 1
addr_type_private_non_resolvable = 2
addr_type_private_resolvable = 3



_BLEDATA = _descriptor.Descriptor(
  name='BleData',
  full_name='aruba_telemetry.BleData',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='mac', full_name='aruba_telemetry.BleData.mac', index=0,
      number=1, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=_b(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='frameType', full_name='aruba_telemetry.BleData.frameType', index=1,
      number=2, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='data', full_name='aruba_telemetry.BleData.data', index=2,
      number=3, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=_b(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='rssi', full_name='aruba_telemetry.BleData.rssi', index=3,
      number=4, type=17, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='addrType', full_name='aruba_telemetry.BleData.addrType', index=4,
      number=5, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='apbMac', full_name='aruba_telemetry.BleData.apbMac', index=5,
      number=6, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=_b(""),
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
  serialized_start=49,
  serialized_end=213,
)

_BLEDATA.fields_by_name['frameType'].enum_type = _BLEFRAMETYPE
_BLEDATA.fields_by_name['addrType'].enum_type = _MACADDRTYPE
DESCRIPTOR.message_types_by_name['BleData'] = _BLEDATA
DESCRIPTOR.enum_types_by_name['BleFrameType'] = _BLEFRAMETYPE
DESCRIPTOR.enum_types_by_name['MacAddrType'] = _MACADDRTYPE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

BleData = _reflection.GeneratedProtocolMessageType('BleData', (_message.Message,), dict(
  DESCRIPTOR = _BLEDATA,
  __module__ = 'aruba_iot_nb_ble_data_pb2'
  # @@protoc_insertion_point(class_scope:aruba_telemetry.BleData)
  ))
_sym_db.RegisterMessage(BleData)


# @@protoc_insertion_point(module_scope)
