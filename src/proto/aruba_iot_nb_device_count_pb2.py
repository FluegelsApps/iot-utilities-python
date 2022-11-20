# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: aruba-iot-nb-device-count.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


import src.proto.aruba_iot_types_pb2 as aruba__iot__types__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='aruba-iot-nb-device-count.proto',
  package='aruba_telemetry',
  syntax='proto2',
  serialized_options=None,
  serialized_pb=_b('\n\x1f\x61ruba-iot-nb-device-count.proto\x12\x0f\x61ruba_telemetry\x1a\x15\x61ruba-iot-types.proto\"\xfa\x04\n\x0b\x44\x65viceCount\x12\x18\n\x10\x64\x65v_unclassified\x18\x01 \x01(\x05\x12\x17\n\x0f\x64\x65v_arubaBeacon\x18\x02 \x01(\x05\x12\x14\n\x0c\x64\x65v_arubaTag\x18\x03 \x01(\x05\x12\x11\n\tdev_zfTag\x18\x04 \x01(\x05\x12\x16\n\x0e\x64\x65v_stanleyTag\x18\x05 \x01(\x05\x12\x18\n\x10\x64\x65v_virginBeacon\x18\x06 \x01(\x05\x12\x19\n\x11\x64\x65v_enoceanSensor\x18\x07 \x01(\x05\x12\x19\n\x11\x64\x65v_enoceanSwitch\x18\x08 \x01(\x05\x12\x13\n\x0b\x64\x65v_iBeacon\x18\t \x01(\x05\x12\x16\n\x0e\x64\x65v_allBleData\x18\n \x01(\x05\x12\x16\n\x0e\x64\x65v_RawBleData\x18\x0b \x01(\x05\x12\x15\n\rdev_eddystone\x18\x0c \x01(\x05\x12\x15\n\rdev_assaAbloy\x18\r \x01(\x05\x12\x17\n\x0f\x64\x65v_arubaSensor\x18\x0e \x01(\x05\x12\x15\n\rdev_abbSensor\x18\x0f \x01(\x05\x12\x13\n\x0b\x64\x65v_wifiTag\x18\x10 \x01(\x05\x12\x18\n\x10\x64\x65v_wifiAssocSta\x18\x11 \x01(\x05\x12\x1a\n\x12\x64\x65v_wifiUnassocSta\x18\x12 \x01(\x05\x12\x14\n\x0c\x64\x65v_mysphera\x18\x13 \x01(\x05\x12\x13\n\x0b\x64\x65v_sBeacon\x18\x14 \x01(\x05\x12\x11\n\tdev_onity\x18\x15 \x01(\x05\x12\x11\n\tdev_minew\x18\x16 \x01(\x05\x12\x12\n\ndev_google\x18\x17 \x01(\x05\x12\x14\n\x0c\x64\x65v_polestar\x18\x18 \x01(\x05\x12\x12\n\ndev_blyott\x18\x19 \x01(\x05\x12\x12\n\ndev_diract\x18\x1a \x01(\x05\x12\x16\n\x0e\x64\x65v_gwahygiene\x18\x1b \x01(\x05')
  ,
  dependencies=[aruba__iot__types__pb2.DESCRIPTOR,])




_DEVICECOUNT = _descriptor.Descriptor(
  name='DeviceCount',
  full_name='aruba_telemetry.DeviceCount',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='dev_unclassified', full_name='aruba_telemetry.DeviceCount.dev_unclassified', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='dev_arubaBeacon', full_name='aruba_telemetry.DeviceCount.dev_arubaBeacon', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='dev_arubaTag', full_name='aruba_telemetry.DeviceCount.dev_arubaTag', index=2,
      number=3, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='dev_zfTag', full_name='aruba_telemetry.DeviceCount.dev_zfTag', index=3,
      number=4, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='dev_stanleyTag', full_name='aruba_telemetry.DeviceCount.dev_stanleyTag', index=4,
      number=5, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='dev_virginBeacon', full_name='aruba_telemetry.DeviceCount.dev_virginBeacon', index=5,
      number=6, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='dev_enoceanSensor', full_name='aruba_telemetry.DeviceCount.dev_enoceanSensor', index=6,
      number=7, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='dev_enoceanSwitch', full_name='aruba_telemetry.DeviceCount.dev_enoceanSwitch', index=7,
      number=8, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='dev_iBeacon', full_name='aruba_telemetry.DeviceCount.dev_iBeacon', index=8,
      number=9, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='dev_allBleData', full_name='aruba_telemetry.DeviceCount.dev_allBleData', index=9,
      number=10, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='dev_RawBleData', full_name='aruba_telemetry.DeviceCount.dev_RawBleData', index=10,
      number=11, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='dev_eddystone', full_name='aruba_telemetry.DeviceCount.dev_eddystone', index=11,
      number=12, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='dev_assaAbloy', full_name='aruba_telemetry.DeviceCount.dev_assaAbloy', index=12,
      number=13, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='dev_arubaSensor', full_name='aruba_telemetry.DeviceCount.dev_arubaSensor', index=13,
      number=14, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='dev_abbSensor', full_name='aruba_telemetry.DeviceCount.dev_abbSensor', index=14,
      number=15, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='dev_wifiTag', full_name='aruba_telemetry.DeviceCount.dev_wifiTag', index=15,
      number=16, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='dev_wifiAssocSta', full_name='aruba_telemetry.DeviceCount.dev_wifiAssocSta', index=16,
      number=17, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='dev_wifiUnassocSta', full_name='aruba_telemetry.DeviceCount.dev_wifiUnassocSta', index=17,
      number=18, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='dev_mysphera', full_name='aruba_telemetry.DeviceCount.dev_mysphera', index=18,
      number=19, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='dev_sBeacon', full_name='aruba_telemetry.DeviceCount.dev_sBeacon', index=19,
      number=20, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='dev_onity', full_name='aruba_telemetry.DeviceCount.dev_onity', index=20,
      number=21, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='dev_minew', full_name='aruba_telemetry.DeviceCount.dev_minew', index=21,
      number=22, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='dev_google', full_name='aruba_telemetry.DeviceCount.dev_google', index=22,
      number=23, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='dev_polestar', full_name='aruba_telemetry.DeviceCount.dev_polestar', index=23,
      number=24, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='dev_blyott', full_name='aruba_telemetry.DeviceCount.dev_blyott', index=24,
      number=25, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='dev_diract', full_name='aruba_telemetry.DeviceCount.dev_diract', index=25,
      number=26, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='dev_gwahygiene', full_name='aruba_telemetry.DeviceCount.dev_gwahygiene', index=26,
      number=27, type=5, cpp_type=1, label=1,
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
  serialized_start=76,
  serialized_end=710,
)

DESCRIPTOR.message_types_by_name['DeviceCount'] = _DEVICECOUNT
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

DeviceCount = _reflection.GeneratedProtocolMessageType('DeviceCount', (_message.Message,), dict(
  DESCRIPTOR = _DEVICECOUNT,
  __module__ = 'aruba_iot_nb_device_count_pb2'
  # @@protoc_insertion_point(class_scope:aruba_telemetry.DeviceCount)
  ))
_sym_db.RegisterMessage(DeviceCount)


# @@protoc_insertion_point(module_scope)
