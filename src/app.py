from pathlib import Path

from flask import Flask, Blueprint

from flask_cors import CORS

import logging

from src import app_config

from src.simple_app.endpoints import api_routes

logger= logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)
formatter = logging. Formatter('%(asctime)s:%(levelname)s%:%(message)')
stream_handler = logging.StreamHandler()
stream_handler.setFormatter(formatter)
logger.addHandler(stream_handler)

def create_app():

    web_app = Flask(__name__, root_path=Path(__file__).parent)
    # web_app.config.from_object(app_config) # Load Flask Configuration ()
    CORS(web_app)

    api_blueprint = Blueprint('api_blueprint', __name__)
    api_blueprint = api_routes(api_blueprint)

    web_app.register_blueprint(api_blueprint, url_prefix='/api')

    return web_app

app= create_app()

if __name__ == "__main__":
    app.run(host="0.0.0.0")