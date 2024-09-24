# Description: Cteni wav souboru a zobrazeni signalu; Mady by: Hejsek, Šimon
import numpy as np
import matplotlib.pyplot as plt
import struct

def read_file(file_str : str):
    print()
    print("cteni souboru: "+str(file_str))
    print("=========================")
    with open(file_str, 'rb') as f:
        try:
            wav_data = {
                "riff_str": f.read(4).decode('ascii'),
                "file_size": struct.unpack('<I', f.read(4))[0],
                "wave_header": f.read(4).decode('ascii'),
                "fmt_header": f.read(4).decode('ascii'),
                "chunk_size": struct.unpack('<I', f.read(4))[0],
                "audio_format": struct.unpack('<H', f.read(2))[0],
                "channels": struct.unpack('<H', f.read(2))[0],
                "sample_rate": struct.unpack('<I', f.read(4))[0],
                "byte_rate": struct.unpack('<I', f.read(4))[0],
                "block_align": struct.unpack('<H', f.read(2))[0],
                "bits_per_sample": struct.unpack('<H', f.read(2))[0],
                "data_header": f.read(4).decode('ascii'),
                "data_size": struct.unpack('<I', f.read(4))[0],
            }
        except UnicodeDecodeError:
            print("Nepodarilo se nacist hlavicku souboru")
            return
        except struct.error:
            print("Nepodarilo se nacist hlavicku souboru")
            return

        for key, value in wav_data.items():
            print(f"{key}: {value}")
        print("=========================")
        
        # bitova hloubka
        bits_per_sample = wav_data.get('bits_per_sample')
        if bits_per_sample == 8:
            sample_format = 'B'  # unsigned 8-bit
            max_amplitude = 255
        elif bits_per_sample == 16:
            sample_format = 'h'  # signed 16-bit
            max_amplitude = 32768
        elif bits_per_sample == 24:
            raise NotImplementedError("24-bitove vzorky tu necraftime")
        else:
            raise ValueError(f"Nepodporovaná bitová hloubka: {bits_per_sample}")

        samples_per_channel = wav_data.get('data_size') // (wav_data.get('channels') * (bits_per_sample // 8))
        SIG = np.zeros((samples_per_channel, wav_data.get('channels')))  
        try:
            for i in range(samples_per_channel):
                for ch in range(wav_data.get('channels')):
                    sample = struct.unpack(sample_format, f.read(bits_per_sample // 8))[0]
                    SIG[i, ch] = sample 
        except struct.error:
            print("Nepodarilo se nacist vsechny vzorky")
            return
        
    # casova osa
    t = np.arange(samples_per_channel).astype(float) / wav_data.get('sample_rate')

    # plot
    if wav_data.get('channels') > 1:
        fig, axs = plt.subplots(wav_data.get('channels'), 1, figsize=(20, 5 * wav_data.get('channels')))
    else:
        fig, axs = plt.subplots(1, 1, figsize=(20, 5))
        axs = [axs]  # edge case 1 channel

    fig.canvas.manager.set_window_title("signál ze souboru: "+str(file_str))

    for ch in range(wav_data.get('channels')):
        axs[ch].plot(t, SIG[:, ch])
        axs[ch].set_title(f'Kanál {ch+1}')
        axs[ch].set_xlabel('t[s]')
        axs[ch].set_ylabel('A[-]')

    plt.tight_layout()
    plt.show()




def main():
    read_file('./cv02/cv02_wav_01.wav')
    read_file('./cv02/cv02_wav_02.wav')
    read_file('./cv02/cv02_wav_03.wav')
    read_file('./cv02/cv02_wav_04.wav')
    read_file('./cv02/cv02_wav_05.wav')
    read_file('./cv02/cv02_wav_06.wav')
    read_file('./cv02/cv02_wav_07.wav')
    
    
if __name__ == '__main__':
    main()