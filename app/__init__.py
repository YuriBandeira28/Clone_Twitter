# configurações principais do flask
from flask import Flask

app = Flask(__name__)

from app.controllers import default