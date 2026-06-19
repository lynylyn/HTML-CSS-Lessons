from app import app

@app.route('/')
@app.route('/index')
def index():
    user = {'username': 'Juliet'}
    return '''
<html>
    <head>
        <title>Home Page - Evil Pals</title>
    </head>
    <body>
        <h1>Hello, ''' + user['username'] + '''!</h1>
    </body>
</html>'''