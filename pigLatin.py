text = input()
if len(text) > 0:
    arr = text[1:len(text)-1] + text[0] + "ay"
    print (arr)
else:
    print("enter a valid word")
