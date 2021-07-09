#1. multiply every 2nd digit by 2 starting from the 2nd to the last
#and then ADD those DIGITS (not results, but DIGITS OF THE RESULTS) together!
#2. add that sum to the sum of the DIGITS that were NOT multiplied by 2
#3. find the remainder when that is divided by 10
#4. if remainder is 0, the credit card number is valid!

def luhn_algorithm(card):
    # 1 - - - - - - -
    lista1 = [x for x in card]
    lista1.reverse()
    # print(lista1)

    digits1 = []
    digits4 = []
    for count, i in enumerate(lista1, start=-1):
        if count % 2 == 0:
            digits1.append(i)
        else:
            digits4.append(i)

    digits2 = [str(int(j) * 2) for j in digits1]
    digits3 = []
    for i in digits2:
        for j in i:
            digits3.append(j)
    # print(digits2)
    # print(digits3)

    sum1 = 0
    for i in digits3:
        sum1 += int(i)

    sum2 = 0
    for i in digits4:
        sum2 += int(i)

    sum3 = sum1 + sum2
    # print(sum1)
    # print(sum2)
    # print(sum3)

    if sum3 % 10 == 0:
        print("Your card number is valid!")
    else:
        print("Sorry, your card number is not valid!")


card = "371449635398431"
luhn_algorithm(card)

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    pass