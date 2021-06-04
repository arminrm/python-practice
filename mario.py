def check_if_number():
    user = input("Height: ")
    while user.isnumeric() == False:
        user = input("Height: ")
    return int(user)

def main():

    height = 0
    while height < 1 or height > 8:
        height = check_if_number()
    for i in range(1, height + 1):
        print(" " * (height - i), end= "")
        print("#" * i, "#" * i, sep= "  ")

main()
