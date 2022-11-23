import mysql.connector
# Guardar las credenciales de la base de datos a usar
cred = {
 	'HOST': 'bmnjrjw8fttrvk80m4cp-mysql.services.clever-cloud.com',
	'DB':'bmnjrjw8fttrvk80m4cp',
	'USER':'ux5kkgzfupavbhwi',
	'PORT':'3306',
	'PASSWORD':'esjMYCcpSdyg0qPvMYtj'
	
}

print('Checking Credentials...\n')
for i in list(cred.keys()):
	print(f'{i}:{cred[i]}')		# Mostrar al usuario

try:
	#Crear la base de datos por medio del msql.connector
	db = mysql.connector.connect(
		host=cred['HOST'],
		user=cred['USER'],
		password=cred['PASSWORD'],
		port=cred['PORT'])
	
	cursor = db.cursor()		#Linea de comando para mandar instrucciones a la base de datos
	execute = cursor.execute	#Ejecutador de instrucciones
	print('\nConnected!')
# Si no se puede conectar se hace una excepción mandando un aviso de error
except mysql.connector.errors.InterfaceError as e: 
	cred['HOST'] = 'unresolved'
	cred['DB']=None
	print('\nError: Host unresolved.')
	print(e)
# Si existe una base de datos, conectate a ella.
if(cred['DB']):
	try:
		execute(f'use {cred["DB"]};')  #Indica la base de datos a utilizar
		print(f'Database `{cred["DB"]}` connected successfully!')
    # Si hay un error de sintaxis:     
	except mysql.connector.errors.ProgrammingError as e:
		print(f'Error: {e}')

	
execute('insert into signalmari(CH1) values (153);')
db.commit()

print('Sisepudoburrooooo')