# made by Martin "Granc3k" Šimon, Vojtěch "Shock" Hejsek


def read_file(filename):
    with open(filename, "r", encoding="utf-8") as f:
        return f.read().lower()


# Index koincidence
def index_koincidence(text):
    N = len(text)
    temp = N * (N - 1)
    IK = 0
    for i in range(26):
        p = 0
        current = 97 + i
        for j in range(N):
            if ord(text[j]) == current:
                p += 1
        IK += (p * (p - 1)) / temp
    print("IK: " + str(IK))
    if IK > 0.063:
        print("Angličtina")
        return 1
    else:
        print("Čeština")
        return 2


# Analyze frekvence znaků v textu
def frequency_analysis(text):
    freq = {}
    for char in text:
        if char.isalpha():
            freq[char] = freq.get(char, 0) + 1
    return dict(sorted(freq.items(), key=lambda x: x[1], reverse=True))


def main():
    # Load dat
    text1 = read_file("./cv14/data/cv14_text01.txt")
    text2 = read_file("./cv14/data/cv14_text02.txt")

    print("\nAnalyzing Text 1:")
    lang1 = index_koincidence(text1)

    print("\nAnalyzing Text 2:")
    lang2 = index_koincidence(text2)


if __name__ == "__main__":
    main()
