from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
# def hello():
#     return 'Hello world'


def content():
    return '<h1>This is our first flask app</h1>'

@app.route('/about')
def about():
    return 'We are new to flask and we are trying things out'

@app.route('/index')
def table():
    return  render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)


#%%
