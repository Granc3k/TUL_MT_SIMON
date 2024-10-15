#made by: Martin "Granc3k" Šimon
import struct


def load_data(filename):
    with open(filename, "rb") as file:
        file_content = file.read()
        data = list(struct.unpack(f"{len(file_content)}B", file_content))
    return data


def save_data(filename, data):
    with open(filename, "wb") as file:
        file.write(struct.pack(f"{len(data)}B", *data))


# LZW komprese
def lzw_compress(data):
    # Inicializace slovníku s hodnotami 1, 2, 3, 4, 5
    dictionary = {(i,): i for i in range(1, 6)}
    dict_size = 6

    result = []
    w = []

    for k in data:
        wk = w + [k]
        if tuple(wk) in dictionary:
            w = wk
        else:
            if w:
                result.append(dictionary[tuple(w)])
            dictionary[tuple(wk)] = dict_size
            dict_size += 1
            w = [k]

    if w:
        result.append(dictionary[tuple(w)])

    return result, dictionary


# LZW dekomprese
def lzw_decompress(compressed):
    dictionary = {i: [i] for i in range(1, 6)}
    dict_size = 6

    result = []
    w = [compressed.pop(0)]
    result.extend(w)

    for k in compressed:
        if k in dictionary:
            entry = dictionary[k]
        elif k == dict_size:
            entry = w + [w[0]]
        else:
            raise ValueError("Decompress error: Invalid data")

        result.extend(entry)
        dictionary[dict_size] = w + [entry[0]]
        dict_size += 1
        w = entry

    return result, dictionary


def main():
    input_file = "./cv05/data/Cv05_LZW_data.bin"
    compressed_file = "./cv05/data/Cv05_LZW_compressed.bin"
    decompressed_file = "./cv05/data/Cv05_LZW_decompressed.bin"

    data = load_data(input_file)
    print(f"Original data: {data}")

    compressed_data, dictionary_compressed = lzw_compress(data)
    print(f"Compressed data: {compressed_data}")
    print(f"Compressed dictionary: {dictionary_compressed}")

    save_data(compressed_file, compressed_data)

    decompressed_data, dictionary_decompressed = lzw_decompress(compressed_data)
    print(f"Decompressed data: {decompressed_data}")
    print(f"Decompressed dictionary: {dictionary_decompressed}")

    save_data(decompressed_file, decompressed_data)


if __name__ == "__main__":
    main()
