import pymysql
from app import app
from config import mysql
from flask import jsonify
from flask import flash, request

#Get all Breed
@app.route('/breeds')
def breeds():
	try:
		conn = mysql.connect()
		cursor = conn.cursor(pymysql.cursors.DictCursor)
		cursor.execute("SELECT * FROM cats")
		empRows = cursor.fetchall()
		respone = jsonify(empRows)
		respone.status_code = 200
		return respone
	except Exception as e:
		print(e)
	finally:
		cursor.close() 
		conn.close()

#Get a specify Breed
@app.route('/breeds/<name>')
def breed(name):
	try:
		conn = mysql.connect()
		cursor = conn.cursor(pymysql.cursors.DictCursor)
		cursor.execute("SELECT * FROM cats WHERE name = %s", name)
		empRow = cursor.fetchone()
		respone = jsonify(empRow)
		respone.status_code = 200
		return respone
	except Exception as e:
		print(e)
	finally:
		cursor.close() 
		conn.close()

#Get Breed with temperament equals <temperament>
@app.route('/temperament/<temperament>')
def temperament(temperament):
	try:
		conn = mysql.connect()
		cursor = conn.cursor(pymysql.cursors.DictCursor)
		cursor.execute("SELECT name FROM cats WHERE temperament LIKE %s", ('%' + temperament + '%'))
		empRow = cursor.fetchall()
		respone = jsonify(empRow)
		respone.status_code = 200
		return respone
	except Exception as e:
		print(e)
	finally:
		cursor.close() 
		conn.close()

#Get Breed with origin equals <origin>
@app.route('/origin/<origin>')
def origin(origin):
	try:
		conn = mysql.connect()
		cursor = conn.cursor(pymysql.cursors.DictCursor)
		cursor.execute("SELECT name FROM cats WHERE origin LIKE %s", ("%" + origin + "%"))
		empRow = cursor.fetchall()
		respone = jsonify(empRow)
		respone.status_code = 200
		return respone
	except Exception as e:
		print(e)
	finally:
		cursor.close() 
		conn.close()
		
@app.errorhandler(404)
def not_found(error=None):
    message = {
        'status': 404,
        'message': 'Record not found: ' + request.url,
    }
    respone = jsonify(message)
    respone.status_code = 404
    return respone
		
if __name__ == "__main__":
    app.run()