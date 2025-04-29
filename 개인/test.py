f = open('d:/대학/University/개인/temp.txt', 'r')

rfs = f.readlines()

for i in range(0, len(rfs)):
    print(rfs[i].strip())

f.close()

f = open('d:/대학/University/개인/temp.txt')