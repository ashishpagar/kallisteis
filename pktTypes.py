import io
import replayparser as rp


class pktTypes:
    pass


def DEM_Error(data):
    print('Error')
    return


def DEM_Stop(data):
    print('Stop')
    return


def DEM_FileHeader(data):
    print('FileHeader')
    return


def DEM_FileInfo(data):
    print('FileInfo')
    return


def DEM_SyncTick(data):
    print('SyncTick')
    return


def DEM_SendTables(data):
    print('SendTables')
    return


def DEM_ClassInfo(data):
    print('ClassInfo')
    return


def DEM_StringTables(data):
    print('StringTables')
    return


def DEM_Packet(data):
    print('Packet')
    packet = rp.demo_pb2.CDemoPacket()
    packet.ParseFromString(data)
    rp.readPackets(packet.data)
    return


def DEM_SignonPacket(data):
    print('SignonPacket')
    packet = rp.demo_pb2.CDemoPacket()
    packet.ParseFromString(data)
    rp.readPackets(packet.data)
    return


def DEM_ConsoleCmd(data):
    print('ConsoleCmd')
    return


def DEM_CustomData(data):
    print('CustomData')
    return


def DEM_CustomDataCallbacks(data):
    print('CustomDataCallbacks')
    return


def DEM_UserCmd(data):
    print('UserCmd')
    return


def DEM_FullPacket(data):
    print('FullPacket')
    return


def DEM_SaveGame(data):
    print('SaveGame')
    return


def DEM_SpawnGroups(data):
    print('SpawnGroups')
    return


def DEM_Max(data):
    print('Max')
    return
