from app import app
from flaskext.mysql import MySQL

mysql = MySQL()
app.config['MYSQL_DATABASE_USER'] = 'devops'
app.config['MYSQL_DATABASE_PASSWORD'] = 'mestre'
app.config['MYSQL_DATABASE_DB'] = 'cat'
app.config['MYSQL_DATABASE_HOST'] = 'localhost'
mysql.init_app(app)