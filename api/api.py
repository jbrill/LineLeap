from flask import *
from extensions import db
import os
import re
import hashlib
import uuid

api = Blueprint('api', __name__, template_folder='templates')

def fieldCheck(jsonVals):
	if 'username' not in jsonVals or 'firstname' not in jsonVals or 'lastname' not in jsonVals or 'password1' not in jsonVals or 'password2' not in jsonVals or 'email' not in jsonVals:
		return True
	return False

def uniqueCheck(jsonVals):
	print(jsonVals)
	cur = db.cursor()
	cur.execute("SELECT username FROM User")
	userlist = cur.fetchall()
	for user in userlist:
		newuser = user['username'].lower()
		print(jsonVals['username'])
		if newuser == jsonVals['username'].lower():
			return True
	return False

@api.route('/api/v1/user', methods=['POST', 'GET', 'PUT'])
def userApi():
	if request.method == "GET":
		if 'username' in session:
			#query that user in db, return in dictionary form
			cur = db.cursor()
			cur.execute("SELECT username, firstname, lastname, email FROM User WHERE username=\"" + (session['username']) + "\"")
			userdata = cur.fetchone()
			return jsonify(userdata)
		else:
			errors = {}
			message = "You do not have the necessary credentials for the resource"
			messages = {}
			messages["message"] = message
			errors["errors"] = [messages]
			return jsonify(errors), 401

	elif request.method == "POST":
		#dealWithPostData(request.get_json())
		# print("user " + request.json['username'])

		myvals = request.get_json()
		print(myvals)

		errors = {}
		errors["errors"] = []
		error = False

		if fieldCheck(myvals):
			messages = {}
			messages["message"] = "You did not provide the necessary fields"
			errors["errors"].append(messages)
			return jsonify(errors), 422
		if uniqueCheck(myvals):
			messages = {}
			messages["message"] = "This username is taken"
			errors["errors"].append(messages)
			error = True
		if not len(myvals['username']) > 2:
			messages = {}
			messages["message"] = "Usernames must be at least 3 characters long"
			errors["errors"].append(messages)
			error = True
		if not re.match("^[A-Za-z0-9_-]*$", myvals['username']):
			messages = {}
			messages["message"] = "Usernames may only contain letters, digits, and underscores"
			errors["errors"].append(messages)
			error = True
		if len(myvals['password1']) < 8:
			messages = {}
			messages["message"] = "Passwords must be at least 8 characters long"
			errors["errors"].append(messages)
			error = True
		if not re.match('[a-zA-Z]', myvals['password1']) or not any(char.isdigit() for char in myvals['password1']):
			messages = {}
			messages["message"] = "Passwords must contain at least one letter and one number"
			errors["errors"].append(messages)
			error = True
		if not re.match("^[A-Za-z0-9_-]*$", myvals['password1']):
			messages = {}
			messages["message"] = "Passwords may only contain letters, digits, and underscores"
			errors["errors"].append(messages)
			error = True
		if myvals['password1'] != myvals['password2']:
			messages = {}
			messages["message"] = "Passwords do not match"
			errors["errors"].append(messages)
			error = True
		if not re.match(r"[^@]+@[^@]+\.[^@]+", myvals['email']):
			messages = {}
			messages["message"] = "Email address must be valid"
			errors["errors"].append(messages)
			error = True
		if len(myvals['email']) > 40:
			messages = {}
			messages["message"] = "Email must be no longer than 20 characters"
			errors["errors"].append(messages)
			error = True
		if len(myvals['username']) > 20:
			messages = {}
			messages["message"] = "Username must be no longer than 20 characters"
			errors["errors"].append(messages)
			error = True
		if len(myvals['firstname']) > 20:
			messages = {}
			messages["message"] = "Firstname must be no longer than 20 characters"
			errors["errors"].append(messages)
			error = True
		if len(myvals['lastname']) > 20:
			messages = {}
			messages["message"] = "Lastname must be no longer than 20 characters"
			errors["errors"].append(messages)
			error = True
		if error:
			print(errors)
			return jsonify(errors), 422

		username = myvals['username']
		firstname = myvals['firstname']
		lastname = myvals['lastname']
		email = myvals['email']
		password1 = myvals['password1']
		password2 = myvals['password1']

		cur = db.cursor()

		algorithm = 'sha512' # name of the algorithm to use for encryption
		salt = uuid.uuid4().hex # salt as a hex string for storage in db
		m = hashlib.new(algorithm)
		m.update(salt + password1)
		password_hash = m.hexdigest()
		dbpass = "$".join([algorithm,salt,password_hash])
		cur.execute("INSERT INTO User (username, firstname, lastname, password, email) VALUES (\"" + username + "\", \"" + firstname + "\", \"" + lastname + "\", \"" + dbpass + "\", \"" + email + "\")")
		cur.execute("SELECT username, firstname, lastname, email FROM User WHERE username=\"" + username + "\"")

		userdata = cur.fetchone()

		return jsonify(userdata), 201
	elif request.method == "PUT":
		print("HERE")
		if 'username' not in session:
			errors = {}
			message = "You do not have the necessary credentials for the resource"
			messages = {}
			messages["message"] = message
			errors["errors"] = [messages]
			return jsonify(errors), 401


		myvals = request.get_json()

		print(myvals)
		#make validation check
		if session['username'] != myvals['username']:
			errors = {}
			message = "You do not have the necessary permissions for the resource"
			messages = {}
			messages["message"] = message
			errors["errors"] = [messages]
			return jsonify(errors), 403

		username = myvals['username']
		firstname = myvals['firstname']
		lastname = myvals['lastname']
		email = myvals['email']
		password1 = myvals['password1']
		password2 = myvals['password2']
		passcheck = True

		if password1 == "" and password2 == "":
			#they are not being modified
			passcheck = False

		cur = db.cursor()
		errors = {}
		errors["errors"] = []
		error = False

		if fieldCheck(myvals):
			messages = {}
			messages["message"] = "You did not provide the necessary fields"
			errors["errors"].append(messages)
			return jsonify(errors), 422
		if not len(myvals['username']) > 2:
			messages = {}
			messages["message"] = "Usernames must be at least 3 characters long"
			errors["errors"].append(messages)
			error = True
		if not re.match("^[A-Za-z0-9_-]*$", myvals['username']):
			messages = {}
			messages["message"] = "Usernames may only contain letters, digits, and underscores"
			errors["errors"].append(messages)
			error = True
		if len(myvals['password1']) < 8 and passcheck:
			messages = {}
			messages["message"] = "Passwords must be at least 8 characters long"
			errors["errors"].append(messages)
			error = True
		if passcheck and (not re.match('[a-zA-Z]', myvals['password1']) or not any(char.isdigit() for char in myvals['password1'])):
			messages = {}
			messages["message"] = "Passwords must contain at least one letter and one number"
			errors["errors"].append(messages)
			error = True
		if not re.match("^[A-Za-z0-9_-]*$", myvals['password1']) and passcheck:
			messages = {}
			messages["message"] = "Passwords may only contain letters, digits, and underscores"
			errors["errors"].append(messages)
			error = True
		if myvals['password1'] != myvals['password2'] and passcheck:
			messages = {}
			messages["message"] = "Passwords do not match"
			errors["errors"].append(messages)
			error = True
		if not re.match(r"[^@]+@[^@]+\.[^@]+", myvals['email']):
			messages = {}
			messages["message"] = "Email address must be valid"
			errors["errors"].append(messages)
			error = True
		if len(myvals['email']) > 40:
			messages = {}
			messages["message"] = "Email must be no longer than 40 characters"
			errors["errors"].append(messages)
			error = True
		if len(myvals['username']) > 20:
			messages = {}
			messages["message"] = "Username must be no longer than 20 characters"
			errors["errors"].append(messages)
			error = True
		if len(myvals['firstname']) > 20:
			messages = {}
			messages["message"] = "Firstname must be no longer than 20 characters"
			errors["errors"].append(messages)
			error = True
		if len(myvals['lastname']) > 20:
			messages = {}
			messages["message"] = "Lastname must be no longer than 20 characters"
			errors["errors"].append(messages)
			error = True
		if error:
			return jsonify(errors), 422

		if passcheck:
			algorithm = 'sha512' # name of the algorithm to use for encryption
			salt = uuid.uuid4().hex # salt as a hex string for storage in db
			m = hashlib.new(algorithm)
			m.update(salt + password1)
			password_hash = m.hexdigest()
			dbpass = "$".join([algorithm,salt,password_hash])


			query = "UPDATE User SET firstname = \"" + firstname + "\", lastname = \"" + lastname + "\", password = \"" + dbpass + "\", email = \"" + email + "\" WHERE username = \"" + username + "\";"
		else:
			query = "UPDATE User SET firstname = \"" + firstname + "\", lastname = \"" + lastname + "\", email = \"" + email + "\" WHERE username = \"" + username + "\";"

		print(query)
		cur.execute(query)
		cur.execute("SELECT username, firstname, lastname, email FROM User WHERE username=\"" + username + "\"")
		userdata = cur.fetchone()
		session['firstname'] = firstname
		session['lastname'] = lastname

		return jsonify(userdata), 200
	return 404

#public
@api.route('/api/v1/login', methods=['POST'])
def loginApi():
	#login using post params

	if request.method == 'POST':
		myvals = request.get_json()
		errors = {}
		if 'username' not in myvals or 'password' not in myvals:

			messages = {}
			messages["message"] = "You did not provide the necessary fields"
			errors["errors"] = [messages]
			return jsonify(errors), 422

		#checks
		username = myvals['username']
		password = myvals['password']

		cur = db.cursor()
		query = "SELECT * FROM User WHERE username=\"" + (username) + "\""
		cur.execute(query)
		user = cur.fetchone()
		if (not user):
			#user does not exist
			errors = {}
			message = "Username does not exist"
			messages = {}
			messages["message"] = message
			errors["errors"] = [messages]
			return jsonify(errors), 404

		dbpass = user["password"]
		passvals = dbpass.split("$")
		algorithm = passvals[0]
		salt = passvals[1]
		originalpass = passvals[2]

		m = hashlib.new(algorithm)
		m.update(salt + password)
		password_hash = m.hexdigest()

		if password_hash == originalpass:
		    session['username'] = username
		    session['firstname'] = user["firstname"]
		    session['lastname'] = user["lastname"]
		else:
			#incorrect password
			errors = {}
			message = "Password is incorrect for the specified username"
			messages = {}
			messages["message"] = message
			errors["errors"] = [messages]
			return jsonify(errors), 422

		userdata = {}
		userdata["username"] = username

		return jsonify(userdata)

@api.route('/api/v1/logout', methods=['POST'])
def logoutApi():
	if 'username' not in session:
			errors = {}
			message = "You do not have the necessary credentials for the resource"
			messages = {}
			messages["message"] = message
			errors["errors"] = [messages]
			return jsonify(errors), 401
	session.pop('username', None)
	session.pop('firstname', None)
	session.pop('lastname', None)
	return jsonify(), 204

@api.route('/api/v1/album/<albumid>', methods=['GET'])
def albumApi(albumid):
	cur = db.cursor()
	cur.execute("SELECT * FROM Album WHERE albumid = \"" + albumid + "\"")
	myres = cur.fetchone()

	if (not myres):
		errors = {}
		message = "The requested resource could not be found"
		messages = {}
		messages["message"] = message
		errors["errors"] = [messages]
		return jsonify(errors), 404


	query = "SELECT access FROM Album WHERE albumid=\"" + (albumid) + "\""
	cur.execute(query)
	ac = cur.fetchone()['access']

	owner = False;


	if 'username' in session:
		query = "SELECT username FROM Album WHERE username=\"" + session['username'] + "\" AND albumid =" + str(albumid)
		cur.execute(query)
		person = cur.fetchall()
		if session['username'] in str(person):
			owner = True;
		else:
			if ac == 'private':
				query = "SELECT username FROM AlbumAccess where albumid =" + str(albumid)
				cur.execute(query)
				names = cur.fetchall()
				if session['username'] not in str(names):
					errors = {}
					message = "You do not have the necessary permissions for the resource"
					messages = {}
					messages["message"] = message
					errors["errors"] = [messages]
					return jsonify(errors), 403
	else:
		if ac == 'private':
			errors = {}
			message = "You do not have the necessary credentials for the resource"
			messages = {}
			messages["message"] = message
			errors["errors"] = [messages]
			return jsonify(errors), 401

	picsholder = {}

	cur.execute("SELECT * FROM Contain WHERE albumid = \"" + albumid + "\"")
	containdata = cur.fetchall()

	# mypics = {}
	# mypics["pics"] = []
	album = {}
	album['pics'] = []
	# pics["pics"] = []
	for snippet in containdata:
		pic = {}

		pic["albumid"] = snippet['albumid']
		pic["caption"] = (snippet['caption'])
		pic["picid"] = (snippet['picid'])
		pic["sequencenum"] = (snippet['sequencenum'])
		cur.execute("SELECT date, format FROM Photo WHERE picid = \"" + snippet['picid'] + "\"")
		photodata = cur.fetchone()
		pic["date"] = photodata['date']
		pic["format"] = photodata['format']

		album['pics'].append(pic)

	#print(album['pics'])
	album["access"] = myres["access"]
	album["albumid"] = myres["albumid"]
	album["created"] = myres["created"]
	album["lastupdated"] = myres["lastupdated"]
	album["title"] = myres["title"]
	album["username"] = myres["username"]

	return jsonify(album)

@api.route('/api/v1/pic/<picid>', methods=['GET', 'PUT'])
def picApi(picid):
	cur = db.cursor()
	if request.method == 'GET':
		cur.execute("SELECT * FROM Contain WHERE picid = \"" + picid + "\"")
		picdata = cur.fetchone()

		if(not picdata):
			errors = {}
			message = "The requested resource could not be found"
			messages = {}
			messages["message"] = message
			errors["errors"] = [messages]
			return jsonify(errors), 404

		query = "SELECT access FROM Album WHERE albumid=\"" + str(picdata['albumid']) + "\""
		cur.execute(query)
		ac = cur.fetchone()['access']

		owner = False;
		if 'username' in session:
			query = "SELECT username FROM Album WHERE username=\"" + session['username'] + "\" AND albumid =" + str(picdata['albumid'])
			cur.execute(query)
			person = cur.fetchall()
			if session['username'] in str(person):
				owner = True;
			else:
				if ac == 'private':
					query = "SELECT username FROM AlbumAccess where albumid =" + str(picdata['albumid'])
					cur.execute(query)
					names = cur.fetchall()
					if session['username'] not in str(names):
						errors = {}
						message = "You do not have the necessary permissions for the resource"
						messages = {}
						messages["message"] = message
						errors["errors"] = [messages]
						return jsonify(errors), 403
		else:
			if ac == 'private':
				errors = {}
				message = "You do not have the necessary credentials for the resource"
				messages = {}
				messages["message"] = message
				errors["errors"] = [messages]
				return jsonify(errors), 401

		cur.execute("SELECT format FROM Photo WHERE picid = \"" + picid + "\"")
		formatdata = cur.fetchone()

		pic = {}

		pic["albumid"] = picdata["albumid"]
		pic["caption"] = picdata["caption"]
		pic["picid"] = picdata["picid"]
		pic["format"] = formatdata["format"]

		sequencenum = picdata["sequencenum"]

		# get next id
		query = "SELECT picid FROM Contain WHERE albumid = " + str(pic["albumid"]) + " AND sequencenum > " + str(sequencenum) + " ORDER BY sequencenum ASC LIMIT 1"
		cur.execute(query)
		nextid = cur.fetchone()
		#print (nextid)

		# get previd
		query = "SELECT picid FROM Contain WHERE albumid = " + str(pic["albumid"]) + " AND sequencenum < " + str(sequencenum) + " ORDER BY sequencenum DESC LIMIT 1"
		cur.execute(query)
		previd = cur.fetchone()
		#print (previd)

		if nextid is None:
			pic["next"] = ""
		else:
			pic["next"] = nextid['picid']

		if previd is None:
			pic["prev"] = ""
		else:
			pic["prev"] = previd['picid']

		return jsonify(pic)

	elif request.method == 'PUT':
		myvals = request.get_json()
		if 'albumid' not in myvals or 'caption' not in myvals or 'format' not in myvals or 'next' not in myvals or'picid' not in myvals or'prev' not in myvals:
			errors = {}
			message = "You did not provide the necessary fields"
			messages = {}
			messages["message"] = message
			errors["errors"] = [messages]
			return jsonify(errors), 422

		cur = db.cursor()
		cur.execute("SELECT * FROM Contain WHERE picid = \"" + picid + "\"")
		picdata = cur.fetchone()

		if(not picdata):
			errors = {}
			message = "The requested resource could not be found"
			messages = {}
			messages["message"] = message
			errors["errors"] = [messages]
			return jsonify(errors), 404


		query = "SELECT access FROM Album WHERE albumid=\"" + str(picdata['albumid']) + "\""
		cur.execute(query)
		ac = cur.fetchone()['access']

		owner = False;
		if 'username' in session:
			query = "SELECT username FROM Album WHERE username=\"" + session['username'] + "\" AND albumid =" + str(picdata['albumid'])
			cur.execute(query)
			person = cur.fetchall()
			if session['username'] in str(person):
				owner = True;
			else:
				if ac == 'private':
					query = "SELECT username FROM AlbumAccess where albumid =" + str(picdata['albumid'])
					cur.execute(query)
					names = cur.fetchall()
					if session['username'] not in str(names):
						errors = {}
						message = "You do not have the necessary permissions for the resource"
						messages = {}
						messages["message"] = message
						errors["errors"] = [messages]
						return jsonify(errors), 401
		else:
			if ac == 'private':
				errors = {}
				message = "You do not have the necessary credentials for the resource"
				messages = {}
				messages["message"] = message
				errors["errors"] = [messages]
				return jsonify(errors), 401

		cur.execute("SELECT format FROM Photo WHERE picid = \"" + picid + "\"")
		formatdata = cur.fetchone()

		# get next id
		query = "SELECT picid FROM Contain WHERE albumid = " + str(picdata["albumid"]) + " AND sequencenum > " + str(picdata['sequencenum']) + " ORDER BY sequencenum ASC LIMIT 1"
		# print (query)
		cur.execute(query)
		nextid = cur.fetchone()


		# get previd
		query = "SELECT picid FROM Contain WHERE albumid = " + str(picdata["albumid"]) + " AND sequencenum < " + str(picdata['sequencenum']) + " ORDER BY sequencenum DESC LIMIT 1"
		# print (query)
		cur.execute(query)
		previd = cur.fetchone()

		picdata["next"] = nextid['picid']
		picdata["prev"] = previd['picid']

		if (myvals['albumid'] != picdata["albumid"]) or (myvals['format'] != formatdata["format"]) or (myvals['next'] != picdata["next"]) or (myvals['picid'] != picid) or (myvals['prev'] != picdata["prev"]):
			errors = {}
			message = "You can only update caption"
			messages = {}
			messages["message"] = message
			errors["errors"] = [messages]
			return jsonify(errors), 403

		newcap = myvals["caption"]

		cur = db.cursor()
		query = "UPDATE Contain SET caption = \"" + newcap + "\" WHERE picid = \"" + str(myvals['picid']) + "\";"
		cur.execute(query)
		query = "UPDATE Album SET lastupdated = CURRENT_TIMESTAMP where albumid =" + str(myvals['albumid']) + ";"
		cur.execute(query)
		return jsonify(myvals)