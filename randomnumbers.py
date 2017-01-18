import random
import string
for i in range(501):
    print(str(random.randint(1,1000000)) + random.choice(string.ascii_letters),end=' ')
    if i == 500:
        print('\n Successfully Hacked!')




