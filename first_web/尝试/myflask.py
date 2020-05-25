from flask import Flask

app = Flask(__name__)



@app.route('/index')
def func1():
    print('我是一个破烂函数')
    return "<div style='color:red'>你真厉害</div>"


@app.route('/login')
def func2():
    print('我是一个牛逼函数')

if __name__ == '__main__':
    app.run()
# http://127.0.0.1:5000/