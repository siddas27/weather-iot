from temps.py import read_temp
from flask import Flask, render_template, url_for
from flask import jsonify, request

app = Flask(__name__)


temp1 = read_temp()

@app.route('/')
def server():
	
	return render_template('index.html')
	
@app.route('/rtemp', methods=['GET'])
def rtemp():
	global temp1
	temp1 = read_temp()
	return jsonify(temp=temp1)

if __name__ =='__main__':
	app.run(debug=True)


