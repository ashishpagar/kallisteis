import io
import replayparser as rp


def DEM_Error(data):
    return


def DEM_Stop(data):
    return


def DEM_FileHeader(data):
    return


def DEM_FileInfo(data):
    return


def DEM_SyncTick(data):
    return


def DEM_SendTables(data):
    return


def DEM_ClassInfo(data):
    return


def DEM_StringTables(data):
    return


def DEM_Packet(data):
    packet = rp.demo_pb2.CDemoPacket()
    packet.ParseFromString(data)
    rp.readPackets(packet.data)
    return


def DEM_SignonPacket(data):
    packet = rp.demo_pb2.CDemoPacket()
    packet.ParseFromString(data)
    rp.readPackets(packet.data)
    return


def DEM_ConsoleCmd(data):
    return


def DEM_CustomData(data):
    return


def DEM_CustomDataCallbacks(data):
    return


def DEM_UserCmd(data):
    return


def DEM_FullPacket(data):
    return


def DEM_SaveGame(data):
    return


def DEM_SpawnGroups(data):
    return


def DEM_Max(data):
    return
