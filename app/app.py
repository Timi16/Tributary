from flask import Flask
import redis

app = Flask(__name__)
app.config.from_object('app.config')

# Initialize Redis
r = redis.Redis(host='redis', port=6379, db=0)

from app import routes
