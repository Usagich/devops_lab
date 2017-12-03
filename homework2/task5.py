inputNum = int(raw_input())
mask = bin(inputNum)
mask = mask[2:]
mask = mask.replace('0','1')
outputNum = inputNum ^ int('0b'+mask,2)
print outputNum