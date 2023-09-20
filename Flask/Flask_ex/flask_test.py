from flask import Flask
app = Flask(__name__)

@app.route('/') # 데코레이터 => 함수 앞뒤에 부가적 구문 추가해 반복작업 용이
def hello():
    return '<h1>Hello World!</h1>'

if __name__ == '__main__':
    app.run()