import webbrowser
import time

total_breaks=3
break_count=0

print("This started on" +time.ctime())
while(break_count < total_breaks):
    time.sleep(10)
    webbrowser.open("https://www.youtube.com/watch?v=UouO-XBlEwM&ab_channel=stuffhai")
    break_count = break_count + 1
