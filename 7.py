def main(x):
    y1 = (x >> 0) & 0b111111
    y2 = (x >> 6) & 0b000000000
    y3 = (x >> 15) & 0b11111111
    y4 = (x >> 23) & 0b111111111
    y5 = (x >> 32) & 0b11111
    y6 = (x >> 37) & 0b111111

    res = (y3 << 35) | (y5 << 30) | (y2 << 21) | (y4 << 12) | (y1 << 6) | (y6 << 0)
    return str(hex(res))

print (main(1637805072997))
