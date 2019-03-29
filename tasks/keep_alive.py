from apscheduler.schedulers.blocking import BlockingScheduler
import requests

sched = BlockingScheduler({
    'apscheduler.timezone': 'America/Los_Angeles'
})

@sched.scheduled_job('interval', minutes=29)
def keep_alive():
    response = requests.get('http://beatnikapp.com/')
    print(response)

sched.start()
