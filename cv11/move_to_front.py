# made by Martin "Granc3k" Šimon, Vojtěch "Shock" Hejsek


def mtf_encode(input_string):
    alphabet = list(
        "ABCDEFGHIJKLMNOPQRSTUVWXYZ ÁČĎÉĚÍŇÓŘŠŤÚŮÝŽ()[]{}\"=.,#:1234567890abcdefghijklmnopqrstuvwxyzáčďéěíňóřšťúůýž_\n-'"
    )
    output = []
    for char in input_string:
        # Find index charu v abecedě
        index = alphabet.index(char)
        # Append indexu do return seznamu
        output.append(index)
        # Move znaku na začátek abecedy
        alphabet.insert(0, alphabet.pop(index))
    return output


def mtf_decode(encoded_list):
    alphabet = list(
        "ABCDEFGHIJKLMNOPQRSTUVWXYZ ÁČĎÉĚÍŇÓŘŠŤÚŮÝŽ()[]{}\"=.,#:1234567890abcdefghijklmnopqrstuvwxyzáčďéěíňóřšťúůýž_\n-'"
    )
    output = []
    for index in encoded_list:
        # Find znaku na daném indexu v abecedě
        char = alphabet[index]
        # Append znaku do return řetězce
        output.append(char)
        # Move znaku na začátek abecedy
        alphabet.insert(0, alphabet.pop(index))
    return "".join(output)


if __name__ == "__main__":
    input_string = input("Enter a string (A-Z): ")
    input_string_test_1 = ' # made by Martin "Granc3k" Šimon, Vojtěch "Shock" Hejsek def mtf_encode(input_string): alphabet = list("ABCDEFGHIJKLMNOPQRSTUVWXYZ ÁČĎÉĚÍŇÓŘŠŤÚŮÝŽ()[]{}"=.,#:1234567890\n")output = [] for char in input_string: # Find index charu v abecedě # index = alphabet.index(char) # Append indexu do return seznamu output.append(index) # Move znaku na začátek abecedy alphabet.insert(0, alphabet.pop(index)) return output def mtf_decode(encoded_list): alphabet = list("ABCDEFGHIJKLMNOPQRSTUVWXYZ ÁČĎÉĚÍŇÓŘŠŤÚŮÝŽ()[]{}"=.,#:1234567890\n") output = [] for index in encoded_list: # Find znaku na daném indexu v abecedě char = alphabet[index] # Append znaku do return řetězce output.append(char) # Move znaku na začátek abecedy alphabet.insert(0, alphabet.pop(index)) return "".join(output) if __name__ == "__main__": #input_string = input("Enter a string (A-Z): ").upper() input_string_test = "" # Encode input řetězce s Move-To-Front encoded = mtf_encode(input_string) # Print Encode print("Encoded:", encoded) # Decode of encoded data decoded = mtf_decode(encoded) # Print decode print("Decoded:", decoded)'
    input_string_test_2 = """
    # made by Martin "Granc3k" Šimon, Vojtěch "Shock" Hejsek


def mtf_encode(input_string):
    alphabet = list('ABCDEFGHIJKLMNOPQRSTUVWXYZ ÁČĎÉĚÍŇÓŘŠŤÚŮÝŽ()[]{}"=.,#:1234567890abcdefghijklmnopqrstuvwxyzáčďéěíňóřšťúůýž_\n-')
    output = []
    for char in input_string:
        # Find index charu v abecedě
        index = alphabet.index(char)
        # Append indexu do return seznamu
        output.append(index)
        # Move znaku na začátek abecedy
        alphabet.insert(0, alphabet.pop(index))
    return output


def mtf_decode(encoded_list):
    alphabet = list('ABCDEFGHIJKLMNOPQRSTUVWXYZ ÁČĎÉĚÍŇÓŘŠŤÚŮÝŽ()[]{}"=.,#:1234567890abcdefghijklmnopqrstuvwxyzáčďéěíňóřšťúůýž_\n-')
    output = []
    for index in encoded_list:
        # Find znaku na daném indexu v abecedě
        char = alphabet[index]
        # Append znaku do return řetězce
        output.append(char)
        # Move znaku na začátek abecedy
        alphabet.insert(0, alphabet.pop(index))
    return "".join(output)


if __name__ == "__main__":
    input_string = input("Enter a string (A-Z): ")
    input_string_test = " # made by Martin \"Granc3k\" Šimon, Vojtěch \"Shock\" Hejsek def mtf_encode(input_string): alphabet = list(\"ABCDEFGHIJKLMNOPQRSTUVWXYZ ÁČĎÉĚÍŇÓŘŠŤÚŮÝŽ()[]{}\"=.,#:1234567890\n\")output = [] for char in input_string: # Find index charu v abecedě # index = alphabet.index(char) # Append indexu do return seznamu output.append(index) # Move znaku na začátek abecedy alphabet.insert(0, alphabet.pop(index)) return output def mtf_decode(encoded_list): alphabet = list(\"ABCDEFGHIJKLMNOPQRSTUVWXYZ ÁČĎÉĚÍŇÓŘŠŤÚŮÝŽ()[]{}\"=.,#:1234567890\n\") output = [] for index in encoded_list: # Find znaku na daném indexu v abecedě char = alphabet[index] # Append znaku do return řetězce output.append(char) # Move znaku na začátek abecedy alphabet.insert(0, alphabet.pop(index)) return \"\".join(output) if __name__ == \"__main__\": #input_string = input(\"Enter a string (A-Z): \").upper() input_string_test = \"\" # Encode input řetězce s Move-To-Front encoded = mtf_encode(input_string) # Print Encode print(\"Encoded:\", encoded) # Decode of encoded data decoded = mtf_decode(encoded) # Print decode print(\"Decoded:\", decoded)"
    
    # Encode input řetězce s Move-To-Front
    encoded = mtf_encode(input_string_test)
    # Print Encode
    print("Encoded:", encoded)
    # Decode of encoded data
    decoded = mtf_decode(encoded)
    # Print decode
    print("Decoded:", decoded)

    
    """

    # Encode input řetězce s Move-To-Front
    # encoded = mtf_encode(input_string)
    # encoded = mtf_encode(input_string_test_1)
    encoded = mtf_encode(input_string_test_2)
    # Print Encode
    print("Encoded:", encoded)
    # Decode of encoded data
    decoded = mtf_decode(encoded)
    # Print decode
    print("Decoded:", decoded)
