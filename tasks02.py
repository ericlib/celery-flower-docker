from main import app

@app.task
def hello(x, y):
    return 'hello '*x*y