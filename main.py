import uuid
import json
import flask
from flask import Flask, request, Response, send_file

from Domain.Models.Music import Music
from Domain.Models.User import User
from Services.DI import users, musics

app = Flask(__name__)



@app.route("/users", methods=("GET",))
def get_user():
    try:
        id = request.args.get("id")
        return Response(json.dumps(users.get_by_id(id).__dict__), status=200)
    except Exception as e:
        print(e)
        return Response("Not Found", status=404)

@app.route("/users", methods=("POST",))
def add_user():
    try:
        data = request.get_json(force=True)
        user = User(data['id'], data['email'], data['password'], data['name'], data['additional_info'], data['phone'])
        users.add(user)
        return Response("OK", status=200)
    except Exception as e:
        print(e)
        return Response("BadRequest", status=400)

@app.route("/users/<string:user_id>", methods=("PUT",))
def update_user(user_id):
    try:
        data = request.get_json(force=True)
        user = User(user_id, data['email'], data['password'], data['name'], data['additional_info'], data['phone'])
        users.update(user)
        return Response("OK", status=200)
    except Exception as e:
        print(e)
        return Response("BadRequest", status=400)

@app.route("/users/<string:user_id>", methods=("DELETE",))
def delete_user(user_id):
    users.delete(user_id)
    return Response("OK", status=200)

@app.route("/music", methods=("GET",))
def get_music():
    try:
        id = request.args.get("id")
        return send_file("music/" + id, mimetype="audio/basic")
    except Exception as e:
        print(e)
        return Response("Not Found", status=404)

@app.route("/music/<string:file_id>", methods=("POST",))
def add_music(file_id):
    try:
        f = request.files['file']
        f.save("music/{0}.{1}".format(file_id, f.filename.split(".")[-1]))
        musics.add(Music(file_id, f))
        return Response("OK", status=200)
    except Exception as e:
        print(e)
        return Response("BadRequest", status=400)

@app.route("/music/<string:file_id>", methods=("PUT",))
def update_music(file_id):
    try:
        f = request.files['file']
        musics.update(Music(file_id, f))
        return Response("OK", status=200)
    except Exception as e:
        print(e)
        return Response("BadRequest", status=400)

@app.route("/music/<string:music_id>", methods=("DELETE",))
def delete_music(music_id):
    musics.delete(music_id)
    return Response("OK", status=200)

if __name__ == '__main__':
      app.run(port=3005)