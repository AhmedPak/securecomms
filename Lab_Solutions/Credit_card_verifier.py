import random

if __name__ == '__main':
    print("credit card verifier")

counter = 0
# ask user for digits
cardDigits = []
while counter < 6:
    digits = int(input("enter 5 digits: "))
    cardDigits.append(digits)
    counter += 1

for x in range(4):
    checkdigit = random.randint(1, 9)
    cardDigits.append(checkdigit)

print(cardDigits)


# create a function to double every second digit
def cardverifier():
    for i in range(1, len(cardDigits), 2):
        cardDigits[i] = cardDigits[i] * 2
        if cardDigits[i] >= 10:
            cardDigits[i] = cardDigits[i] % 10 + (cardDigits[i] // 10)
    print(cardDigits)
    total = sum(cardDigits)
    print(total)

    if total % 10 != 0:
        print("This is not a valid card. Please a valid card")
    else:
        print('Your card has been verified. Payment approved :)')


cardverifier()

# check digit calculation
def check_digit():
    carddigitstotal = sum(cardDigits) * 9
    check_sum = int(carddigitstotal) % 10
    print("Check digit is : ", check_sum)


check_digit()


def vender_identity():
    global card_num2
    vendor_dict = {"34|37": "American Express", "62": "China UnionPay", "3528": "JCB",
                   "6304": "Laser", "6759": "Master UK", "50": "Maestro", "5019": "Dankort",
                   "4571": "Dankort Co-branded", "2200": "MIR", "2221": "Mastercard", "51": "Mastercard",
                   "6334": "Solo", "4903": "Switch", "4": "Visa", "1": "UATP"}

    card_num = input("enter first two digits of your card number: ")
    if card_num in vendor_dict:
        print(vendor_dict.get(card_num))
    else:
        print('enter a valid card number')
    print()
    vendor_list = ["American Express", "Master Card", "Visa Debit", " China UnionPay", " Switch", " Solo"]
    print("Vendors are: ", vendor_list)
    select = input("select your vendor: ")
    if select in vendor_list:
        print ("your vendor card number is : ")
        for i in range(9):
            card_num2 = random.randint(1, 9)
            print(card_num2)
    else:
        print("Enter a valid vendor")


vender_identity()