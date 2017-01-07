from flask import *
from extensions import db
import hashlib
import os

album = Blueprint('album', __name__, template_folder='templates')
ALLOWED_EXTENSIONS = set(['png', 'jpg', 'gif'])

@album.route('/album/edit', methods=['GET', 'POST'])
def album_edit_route():
	albumid = str(request.args.get('albumid'))
	cur = db.cursor()

	query = "SELECT username FROM Album WHERE albumid=\"" + (albumid) + "\""
	cur.execute(query)
	test = cur.fetchone()
	if (not test):
		abort(404)

	# print(test['username'])
	if 'username' not in session:
		return redirect(url_for('login.login_route'))
	elif test['username'] != session['username']:
		abort(403)


	if request.method == 'POST':
		if request.form["op"] == 'add':
			file = request.files['filename']
			filename = file.filename
			extension = filename.split('.')[-1]
			extension = extension.lower()
			# print (filename)
			# print (extension)
			# print ('.' in filename)
			# print (extension in ALLOWED_EXTENSIONS)
			if '.' in filename and extension in ALLOWED_EXTENSIONS:
				m = hashlib.md5(str(albumid) + filename)
				newname = m.hexdigest() + '.' + extension
				MYPATH = '/static/images'
				file.save(os.path.join(os.path.dirname(os.path.dirname(os.path.realpath(__file__))) + '/static/images', newname))
				query = "INSERT INTO Photo (picid, format) VALUES (\"" + m.hexdigest() + "\",\"" + extension + "\");"
				cur.execute(query)
				#
				query = "SELECT MAX(sequencenum) FROM Contain"
				cur.execute(query)
				seqnum = cur.fetchall()
				sequencenum = ((seqnum[0]['MAX(sequencenum)']))
				query = "INSERT INTO Contain (sequencenum, albumid, picid) VALUES (\"" + str(int(sequencenum) + 1) + "\",\"" + str(albumid) + "\", \"" + m.hexdigest() + "\");"
				cur.execute(query)

				query = "UPDATE Album SET lastupdated = CURRENT_TIMESTAMP WHERE albumid = \"" + str(albumid) + "\";"
				cur.execute(query)

		elif request.form["op"] == 'delete':
			query = "SELECT format FROM Photo WHERE picid =\"" + request.form['picid'] + "\";"
			cur.execute(query)
			myform = cur.fetchone()

			if (not myform):
				abort (404)

			query = "DELETE FROM Contain WHERE picid = \"" + request.form['picid'] + "\";"
			cur.execute(query)
			query = "DELETE FROM Photo WHERE picid = \"" + request.form['picid'] + "\";"
			cur.execute(query)

			os.remove((os.path.dirname(os.path.dirname(os.path.realpath(__file__))) + '/static/images/' + request.form['picid'] + "." + str(myform['format'])))

			query = "UPDATE Album SET lastupdated = CURRENT_TIMESTAMP WHERE albumid = \"" + str(albumid) + "\";"
			cur.execute(query)

		elif request.form["op"] == 'grant':
			query = "INSERT INTO AlbumAccess (albumid, username) VALUES (\"" + str(albumid) + "\", \"" + request.form['username'] + "\");"
			cur.execute(query)

		elif request.form["op"] == 'revoke':
			query = "DELETE FROM AlbumAccess WHERE albumid = \"" + str(albumid) + "\" AND username = \"" + request.form['username'] + "\";"
			cur.execute(query)
			#THIS NEEDS FIXING

		elif request.form["op"] == 'access':
			if request.form['access'] == 'public':
				query = "DELETE FROM AlbumAccess WHERE albumid = \"" + str(albumid) + "\";"
				cur.execute(query)

				query = "UPDATE Album SET access = 'public' WHERE albumid = \"" + str(albumid) + "\";"
				cur.execute(query)

			elif request.form['access'] == 'private':
				query = "UPDATE Album SET access = 'private' WHERE albumid = \"" + str(albumid) + "\";"
				cur.execute(query)

			query = "UPDATE Album SET lastupdated = CURRENT_TIMESTAMP WHERE albumid = \"" + str(albumid) + "\";"
			cur.execute(query)


	query = "SELECT picid FROM Contain WHERE albumid =" + str(albumid)
	cur.execute(query)
	picids = cur.fetchall()
	#print picids

	query = "SELECT username FROM AlbumAccess where albumid =" + str(albumid)
	cur.execute(query)
	names = cur.fetchall()

	formats = {}
	for pic in picids:
		query = "SELECT format FROM Photo WHERE picid = \"" + pic['picid'] + "\""
		cur.execute(query)
		formats[pic['picid']] = cur.fetchone()['format']

	options = {
		"edit": True
	}

	query = "SELECT title from Album WHERE albumid =" + str(albumid)
	cur.execute(query)
	titles = cur.fetchone()

	query = "SELECT username FROM Album WHERE albumid =" + str(albumid)
	cur.execute(query)
	creator = cur.fetchone()

	return render_template("album.html", albumid=albumid, picids=picids, formats=formats, names=names, titles=titles, creator=creator, **options)

@album.route('/album')
def album_route():
	return render_template("album.html")
