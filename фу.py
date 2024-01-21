word = {
    1: "one",
    2: "two",
    3: "three",
    4: "four",
    5: "five",
    6: "six",
    7: "seven",
    8: "eight",
    9: "nine",
    10: "ten",
    11: "eleven",
    12: "twelve",
    13: "thirteen",
    14: "fourteen",
    15: "fifteen",
    16: "sixteen",
    17: "seventeen",
    18: "eighteen",
    19: "nineteen",
    20: "twenty",
    30: "thirty",
    40: "forty",
    50: "fifty",
    60: "sixty",
    70: "seventy",
    80: "eighty",
    90: "ninety",
    100: 'hundred'

}


def number_in_english(number: int) -> str:
    init = number
    if number < 20:
        return word[number]
    result_strs = []
    if (first := number // 100) != 0:
        result_strs.append(word[first])
        result_strs.append(word[100])
    number = number % 100
    if (first := number // 10) != 0:
        last = number % 10
        result_strs.append(word[first * 10])
        if last != 0:
            result_strs.append(word[last])
    init = init % 10
    if init != 0 and init > 100:
        result_strs.append('and')
        result_strs.append(word[init])
    return ' '.join(result_strs)