def roman_to_int(s):
    roman_numerals = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000
    }
    result = 0
    prev_value = 0

    for i in s[::-1]:
        value = roman_numerals[i]
        if value < prev_value:
            result -= value
        else:
            result += value
        prev_value = value

    return result

# Example usage
roman_numeral = "MCMXCIV"
integer_value = roman_to_int(roman_numeral)
print(f"The integer representation of {roman_numeral} is: {integer_value}")
