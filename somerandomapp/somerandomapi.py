from sanic import Sanic
from sanic.response import json

from sanic_openapi import openapi3_blueprint

app = Sanic("HelloWorld")
app.blueprint(openapi3_blueprint)


@app.route("/")
async def test(request):
    return json({"hello": "world"})


def run(host="0.0.0.0", port=8000):
    app.run(host=host, port=port)
