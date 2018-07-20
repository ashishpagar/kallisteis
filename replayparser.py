from dotaproto import demo_pb2
from dotaproto import dota_usermessages_pb2
from dotaproto import dota_broadcastmessages_pb2
from dotaproto import dota_client_enums_pb2
from dotaproto import uifontfile_format_pb2
from dotaproto import te_pb2
from dotaproto import steammessages_pb2
from dotaproto import networksystem_protomessages_pb2
from dotaproto import network_connection_pb2
from dotaproto import gcsystemmsgs_pb2
from dotaproto import gcsdk_gcmessages_pb2
from dotaproto import econ_shared_enums_pb2
from dotaproto import econ_gcmessages_pb2
from dotaproto import dota_shared_enums_pb2
from dotaproto import dota_modifiers_pb2
from dotaproto import dota_match_metadata_pb2
from dotaproto import dota_hud_types_pb2
from dotaproto import dota_gcmessages_server_pb2
from dotaproto import dota_gcmessages_msgid_pb2
from dotaproto import dota_gcmessages_common_pb2
from dotaproto import dota_gcmessages_common_match_management_pb2
from dotaproto import dota_gcmessages_client_watch_pb2
from dotaproto import dota_gcmessages_client_tournament_pb2
from dotaproto import dota_gcmessages_client_team_pb2
from dotaproto import dota_gcmessages_client_pb2
from dotaproto import dota_gcmessages_client_match_management_pb2
from dotaproto import dota_gcmessages_client_guild_pb2
from dotaproto import dota_gcmessages_client_fantasy_pb2
from dotaproto import dota_gcmessages_client_chat_pb2
from dotaproto import dota_commonmessages_pb2
from dotaproto import dota_clientmessages_pb2
from dotaproto import connectionless_netmessages_pb2
from dotaproto import clientmessages_pb2
from dotaproto import c_peer2peer_netmessages_pb2
from dotaproto import base_gcmessages_pb2
from dotaproto import netmessages_pb2
from dotaproto import networkbasetypes_pb2
from dotaproto import gameevents_pb2
from dotaproto import usermessages_pb2
import dotaMsg as dMsg
import snappy
import io


def readByte(f):
    return readBytes(f, 1)


def readBytes(f, n):
    return f.read(n)


def readCommand(f):
    return readVarInt(f)


def readVarInt(f):
    x = 0
    y = 0
    stopThis = 1
    while stopThis:
        b = readByte(f)
        x = x | ((byte_to_int(b) & 127) << y)
        y += 7
        if (byte_to_int(b) & 128) == 0 or y == 35:
            stopThis = 0
    return x


def readMessage(f):
    message = dMsg.dotaMsg()
    compressed = -65
    command = readCommand(f)  # read command
    isCompressed = demo_pb2.EDemoCommands.Value('DEM_IsCompressed') == command & \
                   demo_pb2.EDemoCommands.Value('DEM_IsCompressed')  # check if compressed
    tick = readVarInt(f)
    if tick == 4294967295:
        tick = 0
    size = readVarInt(f)
    message.msgTypeId = command & compressed
    message.tick = tick
    message.buffer = snappy.decompress(readBytes(f, size)) if isCompressed else readBytes(f, size)
    return message


def readMessages(f):
    stopReading = True
    outermessage = None
    while stopReading:
        outermessage = readMessage(f)
        print(outermessage.buffer)
        pktBuffer = demo_pb2.CDemoPacket()
        pktBuffer.ParseFromString(outermessage.buffer)
        print(pktBuffer.data)
        readPackets(pktBuffer.data)
        if outermessage.msgTypeId == 0:
            stopReading = False
    return outermessage


def readPackets(m):
    eof = False
    f = io.BytesIO(m)
    count = 0
    while not eof:
        f, packet, eof = readPacket(f)
        count += 1
    print(count)


def readPacket(f):
    packet = dMsg.dotaPkt()
    packet.type = readByte(f)
    packet.size = readByte(f)
    packet.data = readBytes(f, byte_to_int(packet.size))
    eof = False if packet.data.__len__() > 2 else True
    return f, packet, eof


def byte_to_int(b):
    return int.from_bytes(b, byteorder='big')


# set magicSource that is initial file header
magicSource = b'PBDEMS2\x00'
# open replay file and keep it open
file = open('replay/replay.dem', 'rb')
# read first byte
magic = readBytes(file, 8)
# match it with magicSource
if magic == magicSource:
    print('Its matched')
# Ignore next byte
magic = readBytes(file, 8)
# read outer message
allmessage = readMessages(file)
# Close the file just for funsies
file.close()