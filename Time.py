import time,datetime,random

messages=["안녕하세요 만나서 반갑습니다"]
print("Typing speed test.")

time.sleep(2)
print("Ready...")
time.sleep(1)
print("Set...")
time.sleep(1)
print("Go!")

message=random.choice(messages)
print("enter:",message)
start_time=datetime.datetime.now()
typing=input(">")
end_time=datetime.datetime.now()
diff=end_time-start_time
typing_time=diff.seconds+diff.microseconds/float(1000000)
cps=len(message)/typing_time
typ=cps*60
print("Speed(per second):%.1f" %cps)

print("%.1f Typing(per minute" %typ)

if typing==message:
    print("No mistake!")
else:
    print("Hmmm..not bad")

