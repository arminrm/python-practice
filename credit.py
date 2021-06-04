def luhns_algorithm(number):

    products = []
    i = len(number) - 2

    while i >= 0:    #multiply each digit by two
        products.append(2 * int(number[i]))
        i -= 2

    total = 0  #add each digit
    for values in products:
        if values >= 10:
            total = total + int(str(values)[0]) + int(str(values)[1])
        else:
            total = total + values

    i = len(number) - 1 #add digits which were not multiplied by 2
    while i >= 0:
        total = total + int(number[i])
        i -= 2

    return total

def card(number):

    if len(number) == 15:
        if number[:2] == '34' or number[:2] == '37':
            return "AMEX"
        else:
            return "INVALID"
    elif len(number) == 13:
        if number[0] == '4':
            return "VISA"
        else:
            return "INVALID"
    elif len(number) == 16:
        if number[:2] == '51' or number[:2] == '52' or number[:2] == '53' or number[:2] == '54' or number[:2] == '55':
            return "MASTERCARD"
        elif number[:1] == '4':
            return "VISA"
        else:
            return "INVALID"

def main():

    number = input("Number: ")

    if luhns_algorithm(number) % 10 != 0:
        print("INVALID")
    else:
        print(card(number))


main()
