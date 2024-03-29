from distutils.log import debug
from traceback import print_tb
# import imp
from urllib import request
from flask import Flask, render_template, jsonify, request
from flask_sqlalchemy import SQLAlchemy
import os
from urllib.parse import quote
from sqlalchemy.engine import create_engine
from flask_migrate import Migrate
from flask_migrate import MigrateCommand
import models
from controller import read_table_data


from routes.videos import video_tag

app = Flask(__name__)


app.config[
    "SQLALCHEMY_DATABASE_URI"
] = f"postgresql://postgres:123Ht@localhost/aviyel"

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
migrate = Migrate(app, db)


db = SQLAlchemy()
migrate = Migrate()


def create_app():
    app = Flask(__name__)
    db.init_app(app)
    migrate.init_app(app, db)
    return app


app.register_blueprint(video_tag, url_prefix='/videos')


@app.route('/')
def index():
    if request.method == 'GET':
        return {"message": "Welcome to Python Data Etl, explore the tool"}
    else:
        return {"message": "Invalid Request"}


# @app.route('/video-tags')
# def video_tags():
#     if request.method == 'GET':
#         video_tags = models.VideoTags.query.all()
#         return jsonify([video_tag.serialize for video_tag in video_tags])
#     else:
#         return {"message": "Request Failed"}


@app.route('/data-to-loaded')
def read_table():
    if request.method == 'GET':
        videos = read_table_data()
        return videos
    else:
        return {"message": "Request Failed"}


if __name__ == "__main__":
    app.run(debug=True)
