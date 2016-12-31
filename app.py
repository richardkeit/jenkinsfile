#### Richard Keit <rajkeit@gmail.com> ######

import os
import socket
import string
from flask import Flask, render_template, request, redirect, url_for, abort, session
import html
import datetime
from time import gmtime, strftime
import time
app = Flask(__name__)

time=(strftime("%Y-%m-%d %H:%M:%S") + "\n")


####################################################

@app.route('/')
def index():
 return 'Your app is working - application started at '+ time


if __name__ == '__main__':
    app.run(debug=False, host='0.0.0.0')

