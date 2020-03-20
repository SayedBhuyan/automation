from main import send_msg
from apscheduler.schedulers.background import BackgroundScheduler
import time


scheduler = BackgroundScheduler()

arg1 = 0
arg2 = ''
job = scheduler.add_job(send_msg, 'interval',args=['arg1','arg2'], seconds=0.7)
scheduler.start()
print((job))

while True:
    time.sleep(10)
scheduler.shutdown()
