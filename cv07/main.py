import struct


def load_file(filename):
    with open(filename, "rb") as file:
        file_content = file.read()
        data = list(struct.unpack(f"{len(file_content)}B", file_content))

    return data


def arithmetic_encode(data):
    if isinstance(data, list):
        data = ''.join(map(str, data))

    frequency = {}

    for character in data:
        frequency[character] = frequency.get(character, 0) + 1

    probability = {k: v / len(data) for k, v in frequency.items()}

    intervals = {}
    lower_limit = 0
    for character, prob in sorted(probability.items()):
        upper_limit = lower_limit + prob
        intervals[character] = (lower_limit, upper_limit)
        lower_limit = upper_limit

    low, high = 0, 1
    for character in data:
        character_lower, character_upper = intervals[character]
        # IN = <L + ZL*(H - L), L + ZH*(H - L))
        interval_range = high - low
        high = low + interval_range * character_upper
        low = low + interval_range * character_lower

    return (low + high) / 2, intervals


def arithmetic_decode(encoded, intervals, length):
    result = []
    for _ in range(length):
        for character, (lower, upper) in intervals.items():
            # <lower, upper)
            if lower <= encoded < upper:
                result.append(character)
                interval_range = upper - lower
                encoded = (encoded - lower) / interval_range
                break

    return ''.join(result)


def main():
    data = load_file('data/Cv07_Aritm_data.bin')
    # data = "CBAABCADAC"

    encoded, intervals = arithmetic_encode(data)
    decoded = arithmetic_decode(encoded, intervals, len(data))

    print(f'Data: {data}')
    print(f'Encoded: {encoded}')
    print(f'Decoded: {decoded}')
    print('Intervals:')
    for char, (lower, upper) in intervals.items():
        print(f'{char}: <{lower:.1f}, {upper:.1f})')


if __name__ == '__main__':
    main()
