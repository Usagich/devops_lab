fileInput = open('/home/student/input6')
text = fileInput.read()

flag = False
operationsList = ['+', '-', '/', '*', '=']
result = 0

def split(txt, seps):
    default_sep = seps[0]
    for sep in seps[1:]:
        txt = txt.replace(sep, default_sep)
    return [i.strip() for i in txt.split(default_sep)]

numbers = split(text, operationsList)
chars = split(text, str(range(0, 30)))
for i in chars:
    chars.remove('')

if numbers.__len__() != 3 and chars.__len__() != 2:
    print("Oops!  That was no valid number.  Try again...")
else:
    try:
        if chars[0] == operationsList[0]:
            result = int(numbers[0]) + int(numbers[1])
        elif chars[0] == operationsList[1]:
            result = int(numbers[0]) - int(numbers[1])
        elif chars[0] == operationsList[2]:
            result = int(numbers[0]) / int(numbers[1])
        elif chars[0] == operationsList[3]:
            result = int(numbers[0]) * int(numbers[1])
    except ValueError:
        print("Oops!  That was no valid string.  Try again...")


    if result == int(numbers[-1]):
        flag = True
        with open("/home/student/output6", "a") as output:
            output.write("%s" % flag)
    else:
        with open("/home/student/output6", "a") as output:
            output.write("%s" % flag)
        print("Oops!  That was no valid string.  Try again...")

