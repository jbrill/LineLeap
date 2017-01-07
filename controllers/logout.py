from flask import *
from extensions import db
import os

logout = Blueprint('logout', __name__, template_folder='templates')

@logout.route('/logout', methods=['GET', 'POST'])
def logout_route():
    if request.method == 'POST':
        session.pop('username', None)
        session.pop('firstname', None)
        session.pop('lastname', None)
        return redirect(url_for('main.main_route'))
    return redirect(url_for('main.main_route'))
