threshold = 100
product = 1
currentNumber = 1


while product < threshold:
    product *= currentNumber
    currentNumber += 1

print(product, (currentNumber-1))
 # your loop logic here