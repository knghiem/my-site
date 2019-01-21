from flask import Flask, render_template

app = Flask(__name__)

@app.route('/', methods=['GET'])
def main():
    return render_template('index.html')

@app.route('/kvn2112', methods=['GET'])
def mypage():
    return render_template('khanh.html')

