from app import app

if __name__ == '__main__':
	debug = False
	host = "0.0.0.0"
	app.run(host, debug = debug)
	
	#flask_app.config['DEBUG'] = True
	#flask_app.run(host='0.0.0.0', port = '5000')

