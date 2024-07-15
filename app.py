from flask import Flask
app = Flask(__name__)

@app.route('/')
def index():
    return '''
    <html>
        <head>
            <title>My Web App</title>
            <link rel="stylesheet" href="{{ url_for('static', filename='css/style.css') }}">
        </head>
        <body>
            <h1>Hello, World!</h1>
        </body>
    </html>
    '''

if __name__ == '__main__':
    app.run(debug=True)
