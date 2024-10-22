#made by Martin "Granc3k" Šimon
import struct


def load_data(file_path):
    with open(file_path, "rb") as file:
        file_content = file.read()
        data = list(struct.unpack(f"{len(file_content)}B", file_content))
    return data


def save_data(filename, data):
    with open(filename, "wb") as file:
        file.write(struct.pack(f"{len(data)}B", *data))

def main():
    file_path = "./data/Cv05_LZW_data.bin"
    
    data = load_data(file_path)
    print(f"Original Data: {data}")
    

if __name__ == "name":
    main()