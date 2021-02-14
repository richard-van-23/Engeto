import random

def getnum(num):
    return [int(x) for x in str(num)]

def notsame(num):
    num_li = getnum(num)
    if len(num_li) == len(set(num_li)):
        return True
    else:
        return False

def createnum():
    while True:
        num = random.randint(1000, 9999)
        if notsame(num):
            return num

def numbullcows(num, guess):
    count = [0, 0]
    num = getnum(num)
    guess_li = getnum(guess)

    for x, y in zip(num, guess_li):
        if y in num:
            if y == x:
                count[0] += 1
            else:
                count[1] += 1
    return count


num = createnum()
tries = int(input('Enter number of tries: '))

while tries > 0:
    guess = int(input("Enter your guess: "))

    if not notsame(guess):
        print("Digits can't repeat")
        continue
    if guess < 1000 or guess > 9999:
        print("Input only 4 digit number")
        continue

    count = numbullcows(num, guess)
    print(f"{count[0]} bulls, {count[1]} cows")
    tries -= 1

    if count[0] == 4:
        print("You guessed right!")
        break
else:
    print(f"You ran out of tries. Number was {num}")