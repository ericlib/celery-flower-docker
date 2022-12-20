from main import app

@app.task
def add(x, y):
    return x + y

@app.task
def send_email(s):
    return '发送邮件给：' + s