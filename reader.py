import replayparser as rp


class reader:

    def __init__(self, f):
        self.f = f
        self.buf = None
        self.size = 0
        self.pos = 0
        self.bitVal = 0
        self.bitCount = 0

    def readBits(self, bits):
        while bits > self.bitCount:
            self.bitVal = self.bitVal | (rp.byte_to_int(rp.readByte(self.f)) << self.bitCount)
            self.bitCount += 8
        x = self.bitVal & ((1 << bits) - 1)
        self.bitVal = self.bitVal >> bits
        self.bitCount -= bits
        print(x)
        return x

    def readUBit(self):
        ret = self.readBits(6)
        if ret & 48 == 16:
            ret = (ret & 15) | (self.readBits(4) << 4)
        if ret & 48 == 32:
            ret = (ret & 15) | (self.readBits(8) << 4)
        if ret & 48 == 48:
            ret = (ret & 15) | (self.readBits(28) << 4)
        return ret

    def readByte(self):
        # if self.bitCount == 0:
        #     return rp.readByte(self.f)
        return self.readBits(8)

    def readBytes(self, n):
        buf = bytes()
        if self.bitCount == 0:
            return rp.readBytes(self.f, n)
        for i in range(n):
            buf += bytes([self.readBits(8)])
        return buf