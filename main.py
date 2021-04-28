from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():

    return 

if __name__ == '__main__':
    print('程式成功啟動')
    app.run()