import mysql.connector

cred = {
 	'HOST': 'bmnjrjw8fttrvk80m4cp-mysql.services.clever-cloud.com',
	'DB':'bmnjrjw8fttrvk80m4cp',
	'USER':'ux5kkgzfupavbhwi',
	'PORT':'3306',
	'PASSWORD':'esjMYCcpSdyg0qPvMYtj'
	
}

print('Checking Credentials...\n')
for i in list(cred.keys()):
	print(f'{i}:{cred[i]}')

try:
	db = mysql.connector.connect(
		host=cred['HOST'],
		user=cred['USER'],
		password=cred['PASSWORD'],
		port=cred['PORT'])
	
	cursor = db.cursor()
	execute = cursor.execute
	print('\nConnected!')
except mysql.connector.errors.InterfaceError as e:
	cred['HOST'] = 'unresolved'
	cred['DB']=None
	print('\nError: Host unresolved.')
	print(e)
	
if(cred['DB']):
	try:
		execute(f'use {cred["DB"]};')
		print(f'Database `{cred["DB"]}` connected successfully!')
	except mysql.connector.errors.ProgrammingError as e:
		print(f'Error: {e}')

while(True):
	comm = input(f'\n{cred["USER"]}@{cred["HOST"]}:{cred["PORT"]} > MariaDB: ')
	try:
		execute(comm)
		for x in cursor:
			print(x)
		db.commit()
	except NameError:
		print('\nError: Host unresolved.')
	except mysql.connector.errors.ProgrammingError as e:
		print(f'\nError: {e}')