from flask import *
from extensions import db
import os
import hashlib

login = Blueprint('login', __name__, template_folder='templates')

@login.route('/login', methods=['GET','POST'])
def login_route():
    if 'username' in session:
        return render_template("user_edit.html")
    return render_template("login.html")
