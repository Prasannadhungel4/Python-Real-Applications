import time, subprocess

timeLeft = int(input("Enter the countdown time in seconds: "))
while timeLeft>0:
    print(timeLeft, end='')
    time.sleep(1)
    timeLeft = timeLeft-1

subprocess.Popen(['start', "alarm.mp3"], shell=True)
