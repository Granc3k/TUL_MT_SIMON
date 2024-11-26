# made by Martin "Granc3k" Šimon, Vojtěch "Shock" Hejsek


def binary_to_gray(n):
    # Transform bin numu na Gray code s XOR operací
    return n ^ (n >> 1)


def gray_to_binary(n):
    # Transform Gray code na bin num
    mask = n
    # Postupná aplikace XORu s posunutím masky doprava, dokud není 0
    while mask != 0:
        mask >>= 1
        n ^= mask
    return n


if __name__ == "__main__":
    # Print transformu z bin numu na Gray code pro 0 až 255
    print("Binary to Gray code:")
    print("Number -> Binary -> Binary to Gray")
    for i in range(256):
        print(f"{i} -> {i:08b} -> {binary_to_gray(i):08b}")
    print("\n-----------------------------------------------------------\n")
    # Print transformu z Gray codu na bin num pro 0 až 255
    print("Gray code to Binary:")
    print("Number -> Binary -> Gray to Binary")
    for i in range(256):
        print(f"{i} -> {i:08b} -> {gray_to_binary(i):08b}")
