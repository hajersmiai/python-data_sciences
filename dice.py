from random import randint
def dice (amount):
    result=0
    for _ in range(amount):
        result+= randint(1,6)
    return result

print (dice(5))

# from random import randint
def dice2(faces=6):
    result = randint(1,faces)
    return result
print (dice2())

