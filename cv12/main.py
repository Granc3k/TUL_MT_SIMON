# made by Martin "Granc3k" Šimon, Vojtěch "Shock" Hejsek


def decode_inverse_code(received_values):
    def correct_code(a, b):
        print(f"Hodnoty: {a} {b}")

        # Transform na bin
        bins = [f"{a:08b}", f"{b:08b}"]

        # Check počtu nul v první části
        zeros = bins[0].count("0")
        inverted = False

        # If lichý počet nul, invertujeme druhou část
        if zeros % 2 == 1:
            bins[1] = "".join("1" if bit == "0" else "0" for bit in bins[1])
            inverted = True

        # Create kontrolního součtu
        conSum = bin(int(bins[0], 2) + int(bins[1], 2))[2:]
        if len(conSum) > len(bins[0]):
            conSum = conSum[1:]  # Del přetok

        # Detect typu chyby
        ones = conSum.count("1")
        if ones == 1:
            error_position = conSum.index("1")
            print(f"Chyba v části kódu na pozici: {error_position}")

            # Fix zabezpečovací části
            if not inverted:
                bins[0] = (
                    bins[0][:error_position]
                    + ("1" if bins[0][error_position] == "0" else "0")
                    + bins[0][error_position + 1 :]
                )
            print(f"Opravená binárka: {bins[0]}")
            print(f"Správné číslo: {int(bins[0], 2)}")
            return int(bins[0], 2)

        else:
            error_position = conSum.index("0")
            print(f"Chyba informační části kódu na pozici: {error_position}")

            # Fix informační části
            bins[0] = (
                bins[0][:error_position]
                + ("1" if bins[0][error_position] == "0" else "0")
                + bins[0][error_position + 1 :]
            )
            print(f"Opravená binárka: {bins[0]}")
            print(f"Správné číslo: {int(bins[0], 2)}")
            return int(bins[0], 2)

    # Fix pro každý pár
    original_numbers = []
    for i in range(0, len(received_values), 2):
        original_numbers.append(
            correct_code(received_values[i], received_values[i + 1])
        )
        print("-" * 20)

    return original_numbers


# Input hodnoty (uint8)
received_values = [160, 223, 64, 65, 128, 126]

# Decode hodnoty
decoded_numbers = decode_inverse_code(received_values)

# Final print
print("Původní čísla:", decoded_numbers)
