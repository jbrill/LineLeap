from flask import *
from extensions import db

main = Blueprint('main', __name__, template_folder='templates')

@main.route('/')
def main_route():
	cur = db.cursor()
	cur.execute("SELECT * FROM User")
	users = cur.fetchall()
	cur.execute("SELECT albumid FROM Album WHERE access=\"" + ('public') + "\"")
	albums = cur.fetchall()
	# print(albums)
	if 'username' in session:
		cur.execute("SELECT albumid FROM AlbumAccess WHERE username=\"" + session['username'] + "\"")
		newids = cur.fetchall()

		albums += newids

		cur.execute("SELECT albumid FROM Album WHERE username=\"" + session['username'] + "\" AND access =\"" + 'private' + "\"")
		newids = cur.fetchall()
		albums += newids

	counter = 0
	myalbums = []
	for album_id in albums:
		cur.execute("SELECT * FROM Album WHERE albumid=\"" + str(album_id['albumid']) + "\"")
		newalbum = cur.fetchall()
		myalbums.extend(newalbum)

	return render_template("index.html", users=users, albums=myalbums)
