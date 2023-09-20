from flask import Flask, request

app = Flask(__name__)

@app.route('/')
def user_juso():
    temp1 = request.args.get('name','user01')
    temp2 = request.args.get('juso','busan')
    
    return temp1 + '-' + temp2

if __name__ =='__main__':
    app.run()