# create a SQLite3 table and populate it with data

import sqlite3

# create a new database if the database doesn't already exist
with sqlite3.connect("blog.db") as connection:

	# get a cursor object used to execute SQL commands
	c = connection.cursor()

	# create the table
	c.execute("""create table posts
			(title text, post text)
			""")

	# insert dummy data into the table
	c.execute('insert into posts values("Good", "I\'m good.")')
	c.execute('insert into posts values("Well", "I\'m well.")')
	c.execute('insert into posts values("Excellent", "I\'m excellent.")')
	c.execute('insert into posts values("Okay", "I\'m okay.")')

	