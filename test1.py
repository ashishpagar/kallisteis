import replayparser as rp


# set magicSource that is initial file header
magicSource = b'PBDEMS2\x00'
# open replay file and keep it open
file = open('replay/replay.dem', 'rb')
# read first byte
magic = rp.readBytes(file, 8)
# match it with magicSource
if magic == magicSource:
    print('Its matched')
# Ignore next byte
magic = rp.readBytes(file, 8)
# read outer message
allmessage = rp.readMessages(file)
# Close the file just for funsies
file.close()
