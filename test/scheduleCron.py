from crontab import CronTab

my_cron = CronTab(user='your username')

for job in my_cron:
    print(job)

