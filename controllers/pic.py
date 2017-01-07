from flask import *
from extensions import db

pic = Blueprint('pic', __name__, template_folder='templates')

@pic.route('/pic', methods=['GET', 'POST'])
def pic_route():
	picid = str(request.args.get('picid'))

	cur = db.cursor()

	query = "SELECT 1 FROM Photo WHERE picid=\"" + (picid) + "\""
	cur.execute(query)
	test = cur.fetchall()
	if (not test):
		abort(404)


	query = "SELECT albumid FROM Contain WHERE picid = \"" + picid + "\""
	cur.execute(query)
	albumid = cur.fetchone()
	# print albumid

	query = "SELECT access FROM Album WHERE albumid=\"" + str(albumid['albumid']) + "\""
	cur.execute(query)
	ac = cur.fetchone()['access']

	owner = False;
	if 'username' in session:
		query = "SELECT username FROM Album WHERE username=\"" + session['username'] + "\" AND albumid =" + str(albumid['albumid'])
		cur.execute(query)
		person = cur.fetchall()
		if session['username'] in str(person):
			owner = True;
		else:
			if ac == 'private':
				query = "SELECT username FROM AlbumAccess where albumid =" + str(albumid['albumid'])
				cur.execute(query)
				names = cur.fetchall()
				if session['username'] not in str(names):
					abort(403)
	else:
		if ac == 'private':
			return redirect(url_for('login.login_route'))

	if request.method == 'POST':
		if not owner:
			abort(403)
		new_cap = str(request.form["caption"])
		# print(new_cap)
		query = "UPDATE Contain SET caption = \"" + new_cap + "\" WHERE picid = \"" + str(picid) + "\";"

		# print(query)
		cur.execute(query)
		query = "UPDATE Album SET lastupdated = CURRENT_TIMESTAMP where albumid =" + str(albumid['albumid']) + ";"
		cur.execute(query)



		#edit album last updated



	query = "SELECT format FROM Photo WHERE picid = \"" + picid + "\""
	cur.execute(query)
	picformat = cur.fetchone()

	query = "SELECT sequencenum FROM Contain WHERE picid = \"" + picid + "\""
	cur.execute(query)
	startnum = cur.fetchone()
	# print (startnum)
	# print (albumid["albumid"])
	# print (startnum["sequencenum"])


	# get next id
	query = "SELECT picid FROM Contain WHERE albumid = " + str(albumid["albumid"]) + " AND sequencenum > " + str(startnum["sequencenum"]) + " ORDER BY sequencenum ASC LIMIT 1"
	# print (query)
	cur.execute(query)
	nextid = cur.fetchone()

	# get previd
	query = "SELECT picid FROM Contain WHERE albumid = " + str(albumid["albumid"]) + " AND sequencenum < " + str(startnum["sequencenum"]) + " ORDER BY sequencenum DESC LIMIT 1"
	# print (query)
	cur.execute(query)
	previd = cur.fetchone()
	# print(previd)

	query = "SELECT caption FROM Contain WHERE picid = \"" + picid + "\""
	cur.execute(query)
	caption = cur.fetchone()['caption']
	# print(caption)


	return render_template("pic.html", picid=picid, albumid=albumid, picformat=picformat, nextid=nextid, previd=previd, caption=caption, owner=owner)
