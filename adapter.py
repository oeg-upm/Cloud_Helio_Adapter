import os
from flask import Flask, json, send_file, request, make_response, jsonify, after_this_request, Response
from Config_Manager import Config_Manager
from controller.Helio_Controller import Helio_Controller
from service.Map_Generator_Service import Map_Generator_Service
import sys
sys.stdout.flush()

app = Flask(__name__)

@app.route("/data/<id>", methods=['POST'])
def retrieve_data(id):
    """
    POST JSON DATA
    """
    generator = Map_Generator_Service(request.json)
    mapping = generator.render_template()
    controller = Helio_Controller(manager.helio_host, id, mapping)
    controller.create_task()
    controller.retrieve_file()
    return controller.ttl




if __name__ == '__main__':
    
    manager = Config_Manager()
    manager.save_config()

    app.run(debug=True, host=manager.adapter_host, port=manager.adapter_port)