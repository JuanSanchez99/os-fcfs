from flask import Flask

# blueprint import
from app.api import bp_api

def create_app():
    app = Flask(__name__)
    # setup with the configuration provided
    app.config.from_object('config.DevelopmentConfig')
    
    # register blueprint
    app.register_blueprint(bp_api)
    
    return app

if __name__ == "__main__":
    create_app().run()