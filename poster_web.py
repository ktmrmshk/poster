from flask import *
app = Flask(__name__)

@app.route('/', methods=['GET'])
def poster_get():
    return 'hello! -GET'

@app.route('/', methods=['POST'])
def poster_post():
    print('HEADERS:\n====>\n{}<====\n'.format(request.headers))
    print('BODY:\n====>\n {}\n<===='.format(request.get_data()))
    return 'ok'




if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=6636)

