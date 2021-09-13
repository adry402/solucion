
from flask import Flask, request, jsonify
from utils.do_queries_api import ret_response
from utils.api_errors import APIBadRequestError, APIError, APIConnectException
import config
import os

app = Flask(__name__)
app.config["DEBUG"] = config.dev

basedir = os.path.abspath(os.path.dirname(__file__))
data_file = os.path.join(basedir, 'static/'+ config.file_name)
write_file = os.path.join(basedir, 'static/'+ 'salida_temp.txt') 


def work_file(data_file):
    with open(data_file, encoding= config.encoding) as infile:
        next(infile)
        for line in infile:
            new_line = applyStrategy(line)
            with open(write_file, 'a') as the_file:
                the_file.write(config.separator.join(map(str, new_line)))
            

def applyStrategy(line):
    # Se llama a cada API
    register = line.replace(config.separator, "")
    response = ret_response(register)
    return response


@app.route('/', methods=['GET'])
def home():
    return jsonify({
        'success': True,
        'message': 'Server online'
    })


@app.route('/api', methods=['GET'])
def api():
    return jsonify({
        'success': True,
        'message': 'API working'
    })



@app.route('/api/<version>', methods=['GET'])
def byStrategy(version):
    work_file(data_file)
    return "Tarea terminada"


@app.errorhandler(APIBadRequestError)
def handle_exception(err):
    """Return custom JSON when APIError or its children are raised"""
    response = {"error": err.description, "message": ""}
    if len(err.args) > 0:
        response["message"] = err.args[0]
    # TODO: Add some logging so that we can monitor different types of errors
    return jsonify(response), err.code


@app.errorhandler(APIConnectException)
def handle_exception(err):
    """Return custom JSON when APIError or its children are raised"""
    response = {"error": err.description,
                "url": err.args[0], "message": err.args[1]}
    # TODO: Add some logging so that we can monitor different types of errors
    return jsonify(response), err.code


@app.errorhandler(500)
def handle_exception(err):
    """Return JSON instead of HTML for any other server error"""
    # TODO: Add some logging so that we can monitor different types of errors
    response = {
        "error": "Sorry, that error is on us, please contact support if this wasn't an accident"}
    return jsonify(response), 500


if __name__ == '__main__':
    app.run(port=config.port)

