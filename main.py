from bottle import route, run
from helpers import somme
import sys


@route("/add/<a>/<b>")
def addition_test(a="0", b="0"):
    return {"result": somme(a, b)}


run(host="0.0.0.0", port=sys.argv[1], reloader=True)
