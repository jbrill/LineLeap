from flask import *
from extensions import db
import os
import re
import hashlib
import uuid

user = Blueprint('user', __name__, template_folder='templates')

@user.route('/user', methods=['GET','POST'])
# If session, redirect to user edit
def user_route():
    if 'username' in session:
        return redirect(url_for('user.user_edit_route'))
    if request.method == 'POST':
        print("IN USER.PY")
    return render_template("user.html")

@user.route('/user/edit', methods=['GET','POST'])
def user_edit_route():
    if 'username' not in session:
        return redirect(url_for('login.login_route'))
    return render_template("user_edit.html")
