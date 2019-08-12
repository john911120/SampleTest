"""
num = 0

def main():
    counter(num)

def counter(num):
    print(num)
    num += 1
    counter(num)

    main()
"""


def main():
    loopnum = int(input("How Many times would you like to loop?\n"))
    counter = 1
    recurr(loopnum,counter)
#루프를 도는 회수를 지정해준다.

def recurr(loopnum, counter):
    if loopnum > 0:
        print("This is loop iteration",counter)
        recurr(loopnum - 1, counter + 1)
    else:
            print("loop complete")
    #루프가 진행중이라면 진행중인 회수를 표시해주고 끝나면 완료 메시지를 출력을 해준다.
main()