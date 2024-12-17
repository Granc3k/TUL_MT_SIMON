# made by Martin "Granc3k" Šimon, Vojtěch "Shock" Hejsek
import collections
import string


# Fce pro calc indexu koincidence pro identifikaci jazyka
def index_of_coincidence(text):
    N = len(text)
    temp = N * (N - 1)
    IK = 0
    for i in range(26):
        p = 0
        current = 97 + i  # ASCII kód pro písmena 'a' - 'z'
        for j in range(N):
            if ord(text[j]) == current:
                p += 1
        IK += (p * (p - 1)) / temp
    return IK


# Funkce pro otočení textu
def reverse_text(text):
    return text[::-1]


# Fce pro dcrypt Caesar šifry
def caesar_decrypt(text, shift):
    decrypted_text = ""
    for char in text:
        if char.isalpha():
            shift_base = ord("a") if char.islower() else ord("A")
            decrypted_text += chr((ord(char) - shift_base - shift) % 26 + shift_base)
        else:
            decrypted_text += char
    return decrypted_text


# Fce pro nalezení optimal. shiftu v Caesar šifře klíčových slov
def find_best_caesar_shift(text, keywords):
    best_shift = 0
    best_text = ""
    max_keyword_count = 0

    for shift in range(26):
        decrypted_candidate = caesar_decrypt(text, shift)
        keyword_count = sum(decrypted_candidate.count(keyword) for keyword in keywords)

        # Vyber nejlepší text na základě počtu klíčových slov a IK
        if keyword_count > max_keyword_count or (keyword_count == max_keyword_count):
            best_shift = shift
            best_text = decrypted_candidate
            max_keyword_count = keyword_count

    return best_shift, best_text


# Load textu ze souboru
def load_file(filename):
    with open(filename, "r", encoding="utf-8") as file:
        return file.read().lower()


# Returne jazyk podle IK
def get_lang(IK):
    return "Angličtina" if IK > 0.063 else "Čeština"


# Main funkce
if __name__ == "__main__":
    # Klíčová slova
    keywords_czech = ["domov"]
    keywords_english = ["roads"]

    # Load souborů
    encrypted_text_1 = load_file("./cv14/data/cv14_text01.txt")
    encrypted_text_2 = load_file("./cv14/data/cv14_text02.txt")

    # Analýza a dešifrování souboru 1
    print("Analyzujeme soubor cv14_text01.txt")
    reversed_text_1 = reverse_text(encrypted_text_1)
    IK_1 = index_of_coincidence(reversed_text_1)
    best_shift_1, decrypted_text_1 = find_best_caesar_shift(
        reversed_text_1, keywords_czech
    )
    print(f"Nejlepší posun: {best_shift_1}")
    print(f"Index koincidence: {IK_1:.5f}")
    print(f"Identifikovaný jazyk: {get_lang(IK_1)}")
    print("Dešifrovaný text 1:")
    print(decrypted_text_1)

    # Analýza a dešifrování souboru 2
    print("\nAnalyzujeme soubor cv14_text02.txt")
    reversed_text_2 = reverse_text(encrypted_text_2)
    IK_2 = index_of_coincidence(reversed_text_2)
    best_shift_2, decrypted_text_2 = find_best_caesar_shift(
        reversed_text_2, keywords_english
    )
    print(f"Nejlepší posun: {best_shift_2}")
    print(f"Index koincidence: {IK_2:.5f}")
    print(f"Identifikovaný jazyk: {get_lang(IK_2)}")
    print("Dešifrovaný text 2:")
    print(decrypted_text_2)
