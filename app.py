from flask import Flask

app = Flask(__name__)

stores = [
	{
		'name': 'Store 1',
		'items': [
			{
				'name': 'Item 1',
				'price': 40
			}
		]
	}
]

@app.route('/')
def home():
	return "Hello World!"

@app.route('/store', method=['POST'])
def create_store():
	pass

@app.route('/store/<string:name>')
def get_store(name):
	pass

@app.route('/store/<string:name>/item', method=['POST'])
def create_item_in_store(name):
	pass

@app.route('/store/<string:name>/item')
def get_item_in_store(name):
	pass


app.run(port=5000)