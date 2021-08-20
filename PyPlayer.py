from subprocess import check_output as exe
from playsound import playsound
from random import randint
list = exe(['ls', '-ha'], text=True)
file = open('.temp', "w")
file.write(list)
file.close()
file = open('.temp', 'r')
exeList = []
print('\n Executable list: \n')
lineNum = 0
for line in file.readlines():
    if ".mp3" in line.strip() :
        exeList.append(line)
        lineNum += 1
        print("{} : {}".format(lineNum, line.strip()))
    if '.flac' in line.strip():
        lineNum += 1
        print("{} : {}".format(lineNum, line.strip()))
        exeList.append(line)
l = len(exeList)
l = l-1

played = []
checkFlag = True
for i in range(l):
    musicNum = randint(0,l)
    while checkFlag:
        if musicNum in played:
            musicNum = randint(0,l)
        else:
            checkFalg = False
            break
    played.append(musicNum)
    print('\nplaying : {}'.format(exeList[musicNum]))
    name = exeList[musicNum].split('\n')
    print("\n\n name : {}".format(name))
    playsound(name[0])
    

