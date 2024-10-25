# made by Martin "Granc3k" Šimon
import struct


def load_data(file_path):
    with open(file_path, "rb") as file:
        file_content = file.read()
        data = list(struct.unpack(f"{len(file_content)}B", file_content))
    return data


def save_data(filename, data):
    with open(filename, "wb") as file:
        file.write(struct.pack(f"{len(data)}B", *data))


def huff_encode(data):
    counter = {str(i): 0 for i in range(1, 6)}

    # ziskavani cetnosti
    for i in range(len(data)):
        counter[str(data[i])] += 1

    # print(f"Counter: {counter}")

    # vyytvoreni listu s procentualnim vyskytem
    percentual_occurence = {}
    for _ in range(len(counter)):
        max_key = max(counter, key=counter.get)
        max_val = max(counter.values())
        percentual_occurence.update({max_key: round(max_val / len(data), 2)})
        counter.pop(max_key)

    # print(f"Probabilities: {percentual_occurence}")

    # vytvoreni klicu pro cisla
    key_table = {str(i): "" for i in range(1, 6)}
    for _ in range(len(percentual_occurence) - 1):
        lowest_key = min(percentual_occurence, key=percentual_occurence.get)
        lowest_val = min(percentual_occurence.values())
        for j in range(len(lowest_key)):
            key_table[lowest_key[j]] = "0" + key_table[lowest_key[j]]
        percentual_occurence.pop(lowest_key)

        lowest_key2 = min(percentual_occurence, key=percentual_occurence.get)
        lowest_val2 = min(percentual_occurence.values())
        for j in range(len(lowest_key2)):
            key_table[lowest_key2[j]] = "1" + key_table[lowest_key2[j]]
        percentual_occurence.pop(lowest_key2)

        percentual_occurence.update(
            {(lowest_key2 + lowest_key): lowest_val + lowest_val2}
        )

    # encodovani dat
    encoded_data = "".join([key_table[str(symbol)] for symbol in data])

    return encoded_data, key_table


def huff_decode(encoded_data, key_table):
    reverse_key_table = {v: k for k, v in key_table.items()}
    decoded_data = []
    buffer = ""

    for bit in encoded_data:
        buffer += bit
        if buffer in reverse_key_table:
            decoded_data.append(int(reverse_key_table[buffer]))
            buffer = ""

    return decoded_data


def main():
    file_path = "./cv06/data/Cv05_LZW_data.bin"

    data = load_data(file_path)
    print(f"Original Data: {data}")

    encoded_data, key_table = huff_encode(data)
    print(f"Huffman Codes: {key_table}")
    print(f"Encoded Data: {encoded_data}")

    decoded_data = huff_decode(encoded_data, key_table)
    print(f"Decoded Data: {decoded_data}")


if __name__ == "__main__":
    main()
