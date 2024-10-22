# made by Martin "Granc3k" Šimon
import struct


def load_data(file_path):
    with open(file_path, "rb") as file:
        file_content = file.read()
        data = list(struct.unpack(f"{len(file_content)}B", file_content))
    # returns as list of nums
    return data


def save_data(filename, data):
    with open(filename, "wb") as file:
        file.write(struct.pack(f"{len(data)}B", *data))


def rle_encode(data):
    encoded_data = []
    i = 0
    while i < len(data):
        count = 1
        # start of counting number of same values
        while i + 1 < len(data) and data[i] == data[i + 1]:
            count += 1
            i += 1
        # append to list
        encoded_data.append(data[i])
        encoded_data.append(count)
        i += 1
    # returns as list of nums
    return encoded_data


def rle_decode(encoded_data):
    decoded_data = []
    i = 0
    while i < len(encoded_data):
        # takes two numbers from list and appends first number to list count times
        value = encoded_data[i]
        count = encoded_data[i + 1]
        decoded_data.extend([value] * count)
        i += 2
    # returns as list of nums
    return decoded_data


def main():
    filename = "./cv06/data/Cv06_RLE_data.bin"

    data = load_data(filename)
    print("Original Data:", data)

    encoded_data = rle_encode(data)
    print("Encoded Data:", encoded_data)
    save_data("./cv06/data/Cv06_RLE_data_encoded.bin", encoded_data)

    decoded_data = rle_decode(encoded_data)
    print("Decoded Data:", decoded_data)
    save_data("./cv06/data/Cv06_RLE_data_decoded.bin", decoded_data)


if __name__ == "__main__":
    main()
