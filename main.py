from flask import request, Flask, url_for, render_template
from randm import read_temp
app = Flask(__name__)

temp = read_temp()


@app.route('/')
def server():
	return render_template('index.html', temp=temp)
	
if __name__ =='__main__':
	app.run(debug=True)


