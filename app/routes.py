from app import app

@app.route('/')
@app.route('/index')
def index():
	return "Our sample app"
