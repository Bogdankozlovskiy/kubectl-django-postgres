from os import system, environ
from sys import argv
import psycopg2


while True:
	try:
		psycopg2.connect(
			database=environ.get('DATABASE_NAME'),
			user=environ.get('DATABASE_USER'),
			password=environ.get('DATABASE_PASSWORD'),
			host=environ.get('DATABASE_HOST'),
			port=environ.get('DATABASE_PORT')
		)
	except psycopg2.OperationalError:
		print("there isn't connect to database, I Am trying again")
	else:
		break
command = " ".join(argv[1:])
system(command)
