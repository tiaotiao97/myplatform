#coding=utf-8

'''
@Time : 2019/5/20
@Author : hao
@File : main.py
@desc : 
'''
from csrftest import app
from flask import send_file,render_template,request
from csrftest.csrfpoc import split_csrf_params,save_html,create_form
from utils import fileutils

import os


@app.route("/csrf/index")
def index():
    return send_file('../static/csrf.html')
import json
@app.route("/csrf/createpoc",methods=['POST'])
def csrf_poc():
    test_url = request.form['test_url']
    params = request.form['params']
    csrf_method = request.form['csrf_method']
    csrf_poc_form = create_form(test_url,params,csrf_method)
    filename = save_html(test_url,csrf_poc_form)
    return send_file('../{}'.format(filename))

@app.route("/csrf/pocs/<filename>")
def show_poc(filename):
    return send_file('../pocs/csrfpocs/{}'.format(filename))

@app.route("/csrf/pocs/allpocs")
def go_to_poc():
    pocs_files = os.listdir('pocs/csrfpocs/')
    return render_template('csrfpocs.html',filenames=pocs_files)

@app.route("/csrf/renamepoc",methods=['get'])
def rename_file():
    old = request.args.get('old', '').replace(" ","")
    new = request.args.get('new', '').replace(" ","")
    if old and new:
        fileutils.rename_file("pocs/csrfpocs/{}".format(old),"pocs/csrfpocs/{}.html".format(new))
        return "rename success."
    else:
        return "rename faild."




if __name__ == '__main__':
    app.run(debug=True)