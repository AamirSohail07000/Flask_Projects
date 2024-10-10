from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello_world():
  return "Hello World"

@app.route('/aamir')
def heelo_aamir():
  return "Hi Aamir"

if __name__ == '__main__':
  app.run(port=5000, debug=True)