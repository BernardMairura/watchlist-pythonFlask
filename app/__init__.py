from flask import Flask
from .config import DevConfig

# Initializing application
app = Flask(instance_relative_config = True)


#setting up coonfiguration
app.config.from_object(DevConfig)
app.config.from_pyfile('config.py')


from app import views