import art

alphabet = [
    "a",
    "b",
    "c",
    "d",
    "e",
    "f",
    "g",
    "h",
    "i",
    "j",
    "k",
    "l",
    "m",
    "n",
    "o",
    "p",
    "q",
    "r",
    "s",
    "t",
    "u",
    "v",
    "w",
    "x",
    "y",
    "z",
]


def caesar(text, shift, direction):
    output_text = ""
    for letter in text:
        if letter.isalpha():
            index = alphabet.index(letter)
            total_shift = 0

            if direction == "encode":
                total_shift = shift + index
            elif direction == "decode":
                total_shift = index - shift

            if total_shift > 25 or total_shift < 0:
                total_shift %= 26
            output_text += alphabet[total_shift]
        else:
            output_text += letter

    print(f"The {direction}d text is {output_text}")


print(art.logo)


while True:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    if direction != 'encode' and direction != 'decode':
        print('Wrong Input!')
        break
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))

    caesar(text=text, shift=shift, direction=direction)
    user_input = input("Type 'yes' if you want to go again. Otherwise type 'no'.\n")
    if user_input == 'yes':
        print('\n')
        continue
    elif user_input == 'no':
        print("Goodbye")
        break
    else:
        print("Wrong Input!")
        break
