# Joshua Hinojoas
# 8/25/16
# Mr. Davis
# Basic Python Review
import random
def randomnum():
    counter = 0
    numlist = []
    while counter < 10:
        randnum = random.randint(1, 50)
        if str(randnum) not in numlist:
            numlist.append(str(randnum))
            counter += 1

    nums = " ".join(numlist)
    print(nums)

randomnum()