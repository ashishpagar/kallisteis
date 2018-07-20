# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: networksystem_protomessages.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='networksystem_protomessages.proto',
  package='dota',
  syntax='proto2',
  serialized_pb=_b('\n!networksystem_protomessages.proto\x12\x04\x64ota\"0\n NetMessageSplitscreenUserChanged\x12\x0c\n\x04slot\x18\x01 \x01(\r\",\n\x1aNetMessageConnectionClosed\x12\x0e\n\x06reason\x18\x01 \x01(\r\"-\n\x1bNetMessageConnectionCrashed\x12\x0e\n\x06reason\x18\x01 \x01(\r\"\x17\n\x15NetMessagePacketStart\"\x15\n\x13NetMessagePacketEndB\x03\x80\x01\x00')
)
_sym_db.RegisterFileDescriptor(DESCRIPTOR)




_NETMESSAGESPLITSCREENUSERCHANGED = _descriptor.Descriptor(
  name='NetMessageSplitscreenUserChanged',
  full_name='dota.NetMessageSplitscreenUserChanged',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='slot', full_name='dota.NetMessageSplitscreenUserChanged.slot', index=0,
      number=1, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=43,
  serialized_end=91,
)


_NETMESSAGECONNECTIONCLOSED = _descriptor.Descriptor(
  name='NetMessageConnectionClosed',
  full_name='dota.NetMessageConnectionClosed',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='reason', full_name='dota.NetMessageConnectionClosed.reason', index=0,
      number=1, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=93,
  serialized_end=137,
)


_NETMESSAGECONNECTIONCRASHED = _descriptor.Descriptor(
  name='NetMessageConnectionCrashed',
  full_name='dota.NetMessageConnectionCrashed',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='reason', full_name='dota.NetMessageConnectionCrashed.reason', index=0,
      number=1, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=139,
  serialized_end=184,
)


_NETMESSAGEPACKETSTART = _descriptor.Descriptor(
  name='NetMessagePacketStart',
  full_name='dota.NetMessagePacketStart',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=186,
  serialized_end=209,
)


_NETMESSAGEPACKETEND = _descriptor.Descriptor(
  name='NetMessagePacketEnd',
  full_name='dota.NetMessagePacketEnd',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=211,
  serialized_end=232,
)

DESCRIPTOR.message_types_by_name['NetMessageSplitscreenUserChanged'] = _NETMESSAGESPLITSCREENUSERCHANGED
DESCRIPTOR.message_types_by_name['NetMessageConnectionClosed'] = _NETMESSAGECONNECTIONCLOSED
DESCRIPTOR.message_types_by_name['NetMessageConnectionCrashed'] = _NETMESSAGECONNECTIONCRASHED
DESCRIPTOR.message_types_by_name['NetMessagePacketStart'] = _NETMESSAGEPACKETSTART
DESCRIPTOR.message_types_by_name['NetMessagePacketEnd'] = _NETMESSAGEPACKETEND

NetMessageSplitscreenUserChanged = _reflection.GeneratedProtocolMessageType('NetMessageSplitscreenUserChanged', (_message.Message,), dict(
  DESCRIPTOR = _NETMESSAGESPLITSCREENUSERCHANGED,
  __module__ = 'networksystem_protomessages_pb2'
  # @@protoc_insertion_point(class_scope:dota.NetMessageSplitscreenUserChanged)
  ))
_sym_db.RegisterMessage(NetMessageSplitscreenUserChanged)

NetMessageConnectionClosed = _reflection.GeneratedProtocolMessageType('NetMessageConnectionClosed', (_message.Message,), dict(
  DESCRIPTOR = _NETMESSAGECONNECTIONCLOSED,
  __module__ = 'networksystem_protomessages_pb2'
  # @@protoc_insertion_point(class_scope:dota.NetMessageConnectionClosed)
  ))
_sym_db.RegisterMessage(NetMessageConnectionClosed)

NetMessageConnectionCrashed = _reflection.GeneratedProtocolMessageType('NetMessageConnectionCrashed', (_message.Message,), dict(
  DESCRIPTOR = _NETMESSAGECONNECTIONCRASHED,
  __module__ = 'networksystem_protomessages_pb2'
  # @@protoc_insertion_point(class_scope:dota.NetMessageConnectionCrashed)
  ))
_sym_db.RegisterMessage(NetMessageConnectionCrashed)

NetMessagePacketStart = _reflection.GeneratedProtocolMessageType('NetMessagePacketStart', (_message.Message,), dict(
  DESCRIPTOR = _NETMESSAGEPACKETSTART,
  __module__ = 'networksystem_protomessages_pb2'
  # @@protoc_insertion_point(class_scope:dota.NetMessagePacketStart)
  ))
_sym_db.RegisterMessage(NetMessagePacketStart)

NetMessagePacketEnd = _reflection.GeneratedProtocolMessageType('NetMessagePacketEnd', (_message.Message,), dict(
  DESCRIPTOR = _NETMESSAGEPACKETEND,
  __module__ = 'networksystem_protomessages_pb2'
  # @@protoc_insertion_point(class_scope:dota.NetMessagePacketEnd)
  ))
_sym_db.RegisterMessage(NetMessagePacketEnd)


DESCRIPTOR.has_options = True
DESCRIPTOR._options = _descriptor._ParseOptions(descriptor_pb2.FileOptions(), _b('\200\001\000'))
# @@protoc_insertion_point(module_scope)