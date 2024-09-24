# Description: Cteni wav souboru a zobrazeni signalu; Mady by: Šimon
import numpy as np
import matplotlib.pyplot as plt
import struct

def main():
    with open('./cv01/cv01_dobryden.wav', 'rb') as f:
        data = f.read(4)
        print("data: " + str(data))
        RIFF = struct.unpack('i', f.read(4))[0]
        print("RIFF: " + str(RIFF))
        WAVE = f.read(4)
        print("WAVE: " + str(WAVE))
        fmt = f.read(4)
        print("fmt: " + str(fmt))
        end_bytes = struct.unpack("i", f.read(4))[0]
        print("konec bytů: " + str(end_bytes))
        format = f.read(2)
        print("format: " + str(format))
        channels = f.read(2)
        print("kanálů: " + str(channels))
        VF = struct.unpack('i', f.read(4))[0]
        print("VF: " + str(VF))
        PB = struct.unpack('i', f.read(4))[0]
        print("PB: " + str(PB))
        VB = f.read(2)
        print("VB: " + str(VB))
        VV = f.read(2)
        print("VV: " + str(VV))
        data = f.read(4)
        print("data: " + str(data))
        A2 = struct.unpack('i', f.read(4))[0]
        print("A2: " + str(A2))
        SIG = np.zeros(A2)
        for i in range(0, A2):
            SIG[i] = struct.unpack('B', f.read(1))[0]
    t = np.arange(A2).astype(float)/VF
    plt.plot(t, SIG)
    plt.xlabel('t[s]')
    plt.ylabel('A[-]')
    plt.show()

if __name__ == '__main__':
    main()