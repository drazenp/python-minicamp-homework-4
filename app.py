from flask import Flask, request, render_template, jsonify
import sqlite3

app = Flask(__name__)

@app.route('/')
def index():
	return render_template('home.html')
	
@app.route('/addmovie', methods = {'POST'})
def addMovie():
	connection = sqlite3.connect('database.db')
	
	message = ''
	try:
		cursor = connection.cursor()
		
		title = request.form['title']
		description = request.form['description']
		
		cursor.execute('INSERT INTO movies (title, description) VALUES (?, ?)', (title, description))
		connection.commit()
		message = 'Movie successfully added'
	except Exception as e:
		print(str(e))
		connection.rollback()
		message = 'Error in insert operation'
	finally:
		connection.close()
		return message
		
@app.route('/movies')
def movies():
	connection = sqlite3.connect('database.db')
	
	movies = ''
	try:
		cursor = connection.cursor()
		
		cursor.execute('SELECT * FROM movies')
		movies = cursor.fetchall()
	except Exception as e:
		print(str(e))
	finally:
		connection.close()
		return jsonify(movies)