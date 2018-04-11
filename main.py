#!/usr/bin/python
__author__ = "Daniel Fernando Santos Bustos"
__license__ = "GPL V3"
__version__ = "1.0"
__maintainer__ = "Daniel Santos"
__email__ = "dfsantosbu@unal.edu.co"

import os
import pandas as pa
import numpy as nu
import datetime as dt
from flask import Flask, render_template, request, redirect, url_for
from werkzeug.utils import secure_filename

from launcher import getLabels

UPLOAD_FOLDER = './data/'
ALLOWED_EXTENSIONS = set(['csv'])

app = Flask(__name__)
app.config['SECRET_KEY'] = 'mys3cr31'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

def allowed_file(filename):
  return '.' in filename and \
  filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


@app.route('/', methods=['GET', 'POST'])
def browser ():
  try:
    if request.method == 'POST':
      print(request.files)
      if 'file' not in request.files:
        return render_template('index.html')
      file = request.files['file']
      if file.filename == '':
        return render_template('index.html')
      if file:# and allowed_file(file.filename):
        filename = secure_filename(file.filename)
        npath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        file.save(npath)
        data = pa.read_csv(npath)
        infoExperiments = getLabels(data)
        return render_template('index.html', name_file=npath, headers=infoExperiments)
    return render_template('index.html')
  except Exception as e:
    return render_template('500.html',error=e)

@app.route('/results/')
def results():
  try:
    npath = "./data/data.csv"
    data = pa.read_csv(npath)
    infoExperiments = getLabels(data)
    return render_template('index.html', name_file=npath, headers=infoExperiments)
  except Exception as e:
    return render_template("500.html", error=e)

if __name__ =="__main__":
    print(__doc__)
    app.run(debug=True)