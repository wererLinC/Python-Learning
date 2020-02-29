import struct

def find_subchunk(f, chunk_name):
    f.seek(12)
    while True:
        name = f.read(4)
        chunk_size, = struct.unpack('i', f.read(4))
        print(name)

        if name == chunk_name:
            return f.tell(), chunk_size

        f.seek(chunk_size, 1)

f = open('demo.wav', 'rb')
offset, size = find_subchunk(f, b'data')
