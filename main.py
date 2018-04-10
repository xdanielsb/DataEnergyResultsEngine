#!/usr/bin/python
__author__ = "Daniel Fernando Santos Bustos"
__license__ = "GPL V3"
__version__ = "1.0"
__maintainer__ = "Daniel Santos"
__email__ = "dfsantosbu@unal.edu.co"

from flask import Flask, render_template

app = Flask(__name__)
app.config['SECRET_KEY'] = 'mys3cr31'

@app.route('/')
def browser ():
    try:
        return render_template('browser.html')
    except Exception as e:
        return render_template('500.html',error=e)


if __name__ =="__main__":
    print(__doc__)
    app.run(host="0.0.0.0", threaded=True)