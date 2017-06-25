#magic8ball
import random

def getAnswer(r):
    if r == 1:
        return 'It is uncertain'
    elif r == 2:
        return 'It is decidedly so'
    elif r == 3:
        return 'Yes'
    elif r == 4:
        return 'Reply hazy try again'
    elif r == 5:
        return 'Ask again later'
    elif r == 6:
        return 'Concentrate and ask'
    elif r == 7:
        return 'My reply is No'
    elif r == 8:
        return 'Outlook not so good'
    elif r == 9:
        return 'Very doubtful'
r = random.randint(1,9)
print (getAnswer(r))


