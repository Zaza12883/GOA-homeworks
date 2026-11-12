#4) for ციკლისა და range-ის საშვალებით გამოიტანეთ რიცხვები
#80-დან 90-მდე
#90-იდან 80-მდე
#78-იდან 94-მდე მხოლოდ ლუწი
for i in range(80, 91):
    print(i)
for i in range(90, 79, -1):
    print(i)
for i in range(78, 95, 2):
    print(i)
for i in range(31):
    print(i)
for i in range(15, 81):
    print(i)
for i in range(89):
    print(i)
for i in range(0, 51, 3):
    print(i)
num1 = int(input("Enter First Number: "))
num2 = int(input("Enter Second Number: "))

for i in range(num1, num2 + 1):
    print(i)