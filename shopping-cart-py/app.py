"""
Used for running through uwsgi

I'm still tweaking it as I fumble my way through this world
The command line I used to spawn uwsgi is:

uwsgi --http :8080 --wsgi-file app.py --callable app --master --processes 8 --threads 5

So far, this has barely handled 80 concurrent users with any kind of acceptable
response times (quite a few timed out and were retried much much later).
"""
import connexion
from swagger_server.encoder import JSONEncoder
from swagger_server.models import db
import swagger_server.config


config = swagger_server.config
app = connexion.App(__name__, specification_dir='swagger_server/swagger/')
app.app.json_encoder = JSONEncoder
app.add_api('swagger.yaml', arguments={'title': 'Shopping Cart Service with Spring REST and Swagger'})
app.app.config.from_object(config)
db.app = app.app
db.init_app(app.app)
# app.run(port=8080)
app = app.app