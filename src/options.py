from flask import Flask, request, Markup

app = Flask(__name__)


@app.route('/')
def index():
    html = '''
    <form action="/test">
        <p><label>test: </label>
        <input type="text" name="test" value="default">
        <button type="submit" formmethod="get">GET</button>
        <button type="submit" formmethod="post">POST</button></p>
    </form>
    '''
    return Markup(html)


@app.route('/test', methods=['GET', 'POST'])
def test():
    try:
        if request.method == 'POST':
            return request.form['test']
        else:
            return request.args.get('test', '')
    except Exception as e:
        return str(e)


if __name__ == '__main__':
    app.run()
