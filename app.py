from flask import Flask, render_template, request,jsonify

app = Flask(__name__)

@app.route('/')
def index():
    return  render_template('index.html')

@app.route('/about')
def about():
    return  render_template('about.html')

@app.route('/home')
def about():
    return render_template('home.html')
    
if __name__ == '__main__':
    app.run(debug=True)