from celery import Celery
from celery.schedules import crontab


app = Celery('tasks', broker='redis://redis:6379/0', backend='redis://redis:6379/1' )

# 导入任务模块
app.conf.imports = (
    'tasks01',
    'tasks02',
    )

# 指定时区，默认是 UTC
app.conf.timezone = 'Asia/Shanghai'

# 设置定时
app.conf.beat_schedule = {
    'add-every-30-seconds': {
        'task': 'tasks01.add',
        'schedule': 30,
        'args': (20, 20)
    },
    '每天8点半': {
        'task': 'tasks02.hello',
        'schedule': crontab(hour=8, minute=30),
        'args': (2, 2)
    },
}



