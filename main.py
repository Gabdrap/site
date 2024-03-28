from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/info')
def page1():
    return render_template('info.html')

@app.route('/conseq')
def page2():
    return render_template('conseq.html')

@app.route('/defence')
def page3():
    return render_template('defence.html')

if __name__ == '__main__':
    app.run(debug=True)