``` python
@app.route("/")
def home():
    resp = flask.Response("Foo bar baz")
    user.weapon = boomerang
    resp.headers['Access-Control-Allow-Origin'] = '*'
    return resp
```
