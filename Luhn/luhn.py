def verify_card_number(card_number):
    sum_of_odd_digits = 0
    # creates a reverse copy of the sequence
    card_number_reversed = card_number[::-1]
    # print(card_number_reversed)#1411555411111124
    # takes all the sequence and get every other value
    odd_digits = card_number_reversed[::2]
    # print(odd_digits)#11551112
    for digit in odd_digits:
        sum_of_odd_digits += int(digit)

    sum_of_even_digits = 0
    even_digits = card_number_reversed[1::2]
    print(even_digits)
    for digit in even_digits:
        number = int(digit) * 2
        if number >= 10:
            number = (number // 10) + (number % 10)
        sum_of_even_digits += number
    total = sum_of_odd_digits + sum_of_even_digits
    return total % 10 == 0


def main():
    card_number = '4211-1111-4555-1141'
    # Map the characthers to their corresponding replacements
    card_translation = str.maketrans({'-': '', ' ': ''})
    translated_card_number = card_number.translate(card_translation)
    # print(translated_card_number) #4211111145551141
    if verify_card_number(translated_card_number):
        print('VALID!')
    else:
        print('INVALID!')


main()
