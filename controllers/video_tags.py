from ast import Return
from re import X
from urllib import request
from flask import jsonify, request
from flask_sqlalchemy import SQLAlchemy
import os
from urllib.parse import quote
import models


def video_tags():
    if request.method == 'GET':
        video_tags = models.VideoTags.query.all()
        result = [video_tag.serialize for video_tag in video_tags]
        data = jsonify({"status": 200,
                       "message": "Data Fetched Successfully", "data": result})

        return data
    else:
        return {"message": "Request Failed"}


def tag_durations():
    if request.method == 'GET':
        tag_durations = models.TagAvgDuration.query.all()

        result = [tag_duration.serialize for tag_duration in tag_durations]
        max_tags_avg_duration = max(result, key=lambda x: x['video_duration'])
        min_tags_avg_duration = min(result, key=lambda x: x['video_duration'])

        dataReturn = {"data": result, "max_tags_avg_duration": max_tags_avg_duration,
                      "min_tags_avg_duration": min_tags_avg_duration,
                      }

        # data = jsonify(
        #     [tag_duration.serialize for tag_duration in tag_durations])

        data = jsonify({"status": 200,
                       "message": "Data Fetched Successfully", "data": dataReturn})

        return data
    else:
        return {"message": "Request Failed"}
