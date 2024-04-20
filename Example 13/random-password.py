import random
a = "ABCDEFGHIJKLMNOPRSTUVYZ"
b = "abcdefghijklmnoprstuvyz"
randomLetterA = []
randomLetterB = []
randomNumber =[]
while True:
    x = random.choice(a)
    randomLetterA.append(x)
    i = random.choice(b)
    randomLetterB.append(i)
    y = random.randint(10,100)
    randomNumber.append(y)
    if len(randomLetterA) == 10 and len(randomLetterB) == 10 and len(randomNumber) == 10:
        break
    else:
        pass
randomPasswordElement00 = [randomLetterA, randomLetterB, randomNumber]
passwordElement = []
for p in range(20):
    randomPasswordElement0 = random.choice(randomPasswordElement00)
    randomPasswordElement = random.choice(randomPasswordElement0)
    passwordElement.append(randomPasswordElement)
passwordElement = random.sample(passwordElement, len(passwordElement))
password = "".join([str(passwordElement) for passwordElement in passwordElement])
print(password)

