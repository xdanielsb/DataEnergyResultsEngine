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

from launcher import getLabels, getSpecificData, getSessionInfo

UPLOAD_FOLDER = './data/'
ALLOWED_EXTENSIONS = set(['csv'])

app = Flask(__name__)
app.config['SECRET_KEY'] = 'mys3cr31'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

PATH_FILE = ""


def allowed_file(filename):
  return '.' in filename and \
  filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


@app.route('/', methods=['GET', 'POST'])
def browser ():
  global PATH_FILE
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
        PATH_FILE = npath
        data = pa.read_csv(npath)
        infoExperiments = getLabels(data)
        return render_template('index.html', name_file=npath, headers=infoExperiments)
      #for testing purposes 
      """
        put the code here to test with a default file
      """
    return render_template('index.html')
  except Exception as e:
    print(e)
    return render_template('500.html',error=e)

@app.route('/results/<labelid>')
def results(labelid):
  global PATH_FILE
  try:
    PATH_FILE = "./data/data.csv"
    if(len(labelid) == 0 ):
      return render_template('results.html', path=PATH_FILE)
    else: 
      headers, values = getSpecificData(PATH_FILE, labelid)
      h, v  = getSessionInfo(PATH_FILE, labelid)
      return render_template('results.html', headers=headers, values=values, header_session=h, values_session=v)
  except Exception as e:
    print(e)
    return render_template("500.html", error=e)

if __name__ =="__main__":
    print(__doc__)
    app.run(debug=True)