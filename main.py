#!/usr/bin/python
__author__ = "Daniel Fernando Santos Bustos"
__license__ = "GPL V3"
__version__ = "1.0"
__maintainer__ = "Daniel Santos"
__email__ = "dfsantosbu@unal.edu.co"

import os
from flask import Flask, render_template, request, redirect, url_for
from werkzeug.utils import secure_filename

UPLOAD_FOLDER = '/data/'
ALLOWED_EXTENSIONS = set(['csv'])

app = Flask(__name__)
app.config['SECRET_KEY'] = 'mys3cr31'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER


def allowed_file(filename):
  return '.' in filename and \
  filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/')
def browser ():
    try:
      if request.method == 'POST':
        # check if the post request has the file part
        if 'file' not in request.files:
          return redirect(request.url)
        file = request.files['file']
        # if user does not select file, browser also
        # submit a empty part without filename
        if file.filename == '':
          return redirect(request.url)
        if file and allowed_file(file.filename):
          filename = secure_filename(file.filename)
          file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
          return redirect(url_for('uploaded_file',
                                    filename=filename))  
      return render_template('index.html')
    except Exception as e:
      return render_template('500.html',error=e)


if __name__ =="__main__":
    print(__doc__)
    app.run(host="0.0.0.0", threaded=True, debug=True)