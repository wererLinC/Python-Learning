import mmap

f = open('/dev/fb0', 'r+b')

size = 8294400
m = mmap.mmap(f.fileno(), size)

m[:size//2] = b'\xff\xff\xff\x00' * (size // 4 //2)
m.close()
f.close()
