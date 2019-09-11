import time
import datetime
import os

def daily(letter,name,x):
# check if its Saturday
    print(r"""
     _______       ___       __   __      ____    ____     _______   ______     _______  _______ 
    |       \     /   \     |  | |  |     \   \  /   /    |       \ /  __  \   /  _____||   ____|
    |  .--.  |   /  ^  \    |  | |  |      \   \/   /     |  .--.  |  |  |  | |  |  __  |  |__   
    |  |  |  |  /  /_\  \   |  | |  |       \_    _/      |  |  |  |  |  |  | |  | |_ | |   __|  
    |  '--'  | /  _____  \  |  | |  `----.    |  |        |  '--'  |  `--'  | |  |__| | |  |____ 
    |_______/ /__/     \__\ |__| |_______|    |__|        |_______/ \______/   \______| |_______|                                                                                            
                .--~~,__
   :-....,-------`~~'._.'
    `-,,,  ,_      ;'~U'
     _,-' ,'`-__; '--.
    (_/'~~      ''''(;
    """)
    print(name)
    a = datetime.datetime.now()
    if a.isoweekday() == 6:
        a += datetime.timedelta(days=2)
        a = a.replace(hour=9,minute=0,second=0,microsecond=0)
        now = datetime.datetime.now()
        c = a - now
        wait_time = c.seconds
        print('Its Saturday... sleeping',wait_time,"seconds...")
        time.sleep(wait_time)
#check if its Sunday
    elif a.isoweekday() == 7:
        a += datetime.timedelta(days=1)
        a = a.replace(hour=9,minute=0,second=0,microsecond=0)
        now = datetime.datetime.now()
        c = a - now
        wait_time = c.seconds
        print('Its Sunday... sleeping',wait_time,"seconds...")
        time.sleep(wait_time)
#check if its work hours
    now = datetime.datetime.today().time()
    work_hours = [9,10,11,12,13,14,15,16,17]
    if now.hour not in work_hours:
        a = datetime.datetime.now()
        a += datetime.timedelta(days=1)
        a = a.replace(hour=9,minute=0,second=0,microsecond=0)
        now = datetime.datetime.now()
        c = a - now
        wait_time = c.seconds
        print(datetime.datetime.now())
        print("Its not time to work... sleeping",wait_time,"seconds...")
        time.sleep(wait_time)
#check for changes in file modification timestamps
    else:
        print(datetime.datetime.now())
        print("****Running DAILY TASK...")
        os.system(x)
        with open("test_"+str(letter)+".txt", "a") as f:
            f.write("\n")
            f.write(str(name)+"****Running DAILY TASK... "+str(datetime.datetime.now()))
            f.write("\n")
            f.write(str(datetime.datetime.now()))
        a = datetime.datetime.now()
        a += datetime.timedelta(days=1)
        a = a.replace(hour=9,minute=0,second=0,microsecond=0)
        now = datetime.datetime.now()
        c = a - now
        wait_time = c.seconds
        print(datetime.datetime.now())
        print("RAN AACF, sleeping",wait_time,"seconds...")
        time.sleep(wait_time)
while True:
    daily('c','daily taskname','python daily_report.py')
