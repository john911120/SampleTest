import time

sleepNum = int ( input("How long will you sleep?"))

while sleepNum > 0:
    print(sleepNum)
    time.sleep(2)
    sleepNum = sleepNum - 2

print('Beep!\a')