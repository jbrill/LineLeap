from flask import *
from extensions import db
import os

albums = Blueprint('albums', __name__, template_folder='templates')

@albums.route('/albums/edit', methods=['POST', 'GET'])
def albums_edit_route():

	if 'username' not in session:
		return redirect(url_for('login.login_route'))
	else:
		username = session['username']


	# username = str(request.args.get('username'))

	cur = db.cursor()
	# query = "SELECT 1 FROM User WHERE username=\"" + (username) + "\""
	# cur.execute(query)
	# user = cur.fetchall()
	# if (not user):
	# 	abort(404)
	

	#check if delete or add
	if request.method == 'POST':
		if request.form['op'] == "add":
			mytitle = str(request.form["title"])

			query = "INSERT INTO Album (title, created, lastupdated, username, access) VALUES (\"" + mytitle + "\", CURRENT_TIMESTAMP, CURRENT_TIMESTAMP, \"" + username + "\", 'private');"
			cur.execute(query)
		else:
			albumid = str(request.form["albumid"])

			query = "SELECT picid FROM Contain WHERE albumid = \"" + albumid + "\";"
			cur.execute(query)
			mypics = cur.fetchall() #grabbing pics

			#DELETE ORDER: contain, album, photo
			query = "DELETE FROM AlbumAccess WHERE albumid = \"" + albumid + "\";"
			cur.execute(query)
			query = "DELETE FROM Contain WHERE albumid =\"" + albumid + "\";"
			cur.execute(query)
			query = "DELETE FROM Album WHERE albumid =\"" + albumid + "\";"
			cur.execute(query)

			for pic in mypics:
				query = "SELECT format FROM Photo WHERE picid =\"" + pic['picid'] + "\";"
				cur.execute(query)
				myform = cur.fetchone()
				# print(myform)
				# os.remove
				os.remove((os.path.dirname(os.path.dirname(os.path.realpath(__file__))) + '/static/images/' + pic['picid'] + "." + str(myform['format'])))

				query = "DELETE FROM Photo WHERE picid =\"" + pic['picid'] + "\";"
				cur.execute(query)


	query = "SELECT * FROM Album WHERE username=\"" + (username) + "\";"
	cur.execute(query)
	albums = cur.fetchall()

	options = {
		"edit": True
	}
	return render_template("albums.html", albums=albums, username=username, **options)


@albums.route('/albums')
def albums_route():
	username = str(request.args.get('username'))
	# print("Username: " + username)
	if username == "None":
		if 'username' in session:
			username = session['username']
			query = "SELECT * FROM Album WHERE username=\"" + (username) + "\";"
			cur = db.cursor()
			cur.execute(query)
			albums = cur.fetchall()
			options = {
				"edit": False,
				"owner": True
			}

			return render_template("albums.html", albums=albums, username=username, **options)
		else:
			return redirect(url_for('login.login_route'))
	else:
		cur = db.cursor()
		query = "SELECT 1 FROM User WHERE username=\"" + (username) + "\""
		cur.execute(query)
		user = cur.fetchall()
		if (not user):
			abort(404)

		query = "SELECT * FROM Album WHERE username=\"" + (username) + "\" AND access = 'public';"
		#print(query)
		cur.execute(query)
		albums = cur.fetchall()
		#print albums
		options = {
			"edit": False,
			"owner": False
		}

		return render_template("albums.html", albums=albums, username=username, **options)
