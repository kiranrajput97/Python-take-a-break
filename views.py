import webbrowser
import time
import os

total_breaks=1000
break_count=0
delay = 15

print("This started on" +time.ctime())
while(break_count < total_breaks):    
    webbrowser.open("https://www.youtube.com/watch?v=iVsiU5j-fQY&list=UUxtYZuJEs2-zwUKxRKATe2w")
    time.sleep(delay)
    os.system("taskkill /im chrome.exe")
    # break_count = break_count + 1
