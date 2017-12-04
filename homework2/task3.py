fileInput = open('/home/student/input')
number = int(fileInput.read())

def primfacs(number):
    print number
    i = 2
    primfac = []
    res = []
    check = 0
    while i * i <= number:
        while number % i == 0:
            primfac.append(i)
            number = number / i
        i = i + 1
    if number > 1:
        primfac.append(number)

    for i in primfac:
        if i > 9:
            return -1
    i = primfac.count(2)
    if i > 3:
        while i < (primfac.count(2) // 3) and i!=0:
            res.append(8)
            i-=3
        while i < primfac.count(2) % 3 and i!=0:
            if i == 2:
                res.append(4)
            res.append(2)
    elif i==2:
        res.append(4)
    elif i==1:
        res.append(2)
    i = primfac.count(3)
    while i >= (primfac.count(3) // 2) and i!=0:
        res.append(9)
        i-=2
    if i == 1:
        res.append(3)
    if 2 in res and 3 in res:
        res.remove(2)
        res.remove(3)
        res.append(6)
    for i in primfac:
        if i not in res and i !=2 and i!=3:
            res.append(i)
    res.sort()
    for i in res:
        check*=i
    if i != number:
        return -1
    else:
        return res
print primfacs(number)

with open("/home/student/output", "a") as output:
    output.write("%d" % primfacs(number))

