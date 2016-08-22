numberCounter = []
for i in range(5):
    number = int(input("Number: "))
    numberCounter.append(number)
print("The first number is", numberCounter[0])
print("The last number is", numberCounter[-1])
print("The smallest number is", min(numberCounter))
print("The largest number is", max(numberCounter))
print("The average of the numbers is", sum(numberCounter) / len(numberCounter))