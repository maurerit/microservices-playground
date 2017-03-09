#!/usr/bin/env python3

import connexion
from .encoder import JSONEncoder
from swagger_server.models import db
import swagger_server.config


if __name__ == '__main__':
    config = swagger_server.config
    app = connexion.App(__name__, specification_dir='./swagger/')
    app.app.json_encoder = JSONEncoder
    app.add_api('swagger.yaml', arguments={'title': 'Shopping Cart Service with Spring REST and Swagger'})
    app.app.config.from_object(config)
    db.app = app.app
    db.init_app(app.app)
    app.run(port=8080)
    # application = app.app