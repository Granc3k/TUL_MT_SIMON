# made by Martin "Granc3k" Šimon, Vojtěch "Shock" Hejsek


def bwt_encode(s):
    # Append '$' na konec input řetězce
    s = s + "$"
    # Create tablu všech cyklických posunů řetězce a sort lexikograficky
    table = sorted(s[i:] + s[:i] for i in range(len(s)))
    # Create last sloupce z tablu
    last_column = [row[-1] for row in table]
    # Return last sloupce jako řetězec a index původního řetězce v tablu
    return "".join(last_column), table.index(s)


def bwt_decode(r, index):
    # Init empty tablu s délkou řetězce r
    table = [""] * len(r)
    # Repeat procesu appendování znaků z řetězce r do tablu a sort tablu
    for _ in range(len(r)):
        table = sorted(r[i] + table[i] for i in range(len(r)))
    # Return řetězec na původním indexu bez koncového znaku '$'
    return table[index].rstrip("$")


if __name__ == "__main__":
    # Load inputu
    input_string = input("Enter a string (A-Z): ").upper()
    # Encode inputu
    encoded, index = bwt_encode(input_string)
    # Print encodu
    print(f"Encoded: {encoded} on index {index}")
    # Decode
    decoded = bwt_decode(encoded, index)
    # Print decode
    print("Decoded:", decoded)
