import docker.errors
from flask import Blueprint
from flask import jsonify, abort, redirect
from client import client
from functools import wraps

api = Blueprint('api', __name__,)


def json_list(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        input_list = tuple(map(lambda c: c.attrs, func(*args, **kwargs)))
        return jsonify(input_list)
    return wrapper


def docker_error_handling(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except docker.errors.NotFound:
            abort(404)
        except docker.errors.APIError as e:
            return e.explanation, e.response.status_code

    return wrapper


@api.route('/')
def index():
    return "Docker webAPI"


@api.route('/containers')
@json_list
def get_containers():
    return client.containers.list()


@api.route('/containers/<container_id>')
@docker_error_handling
def get_container(container_id):
    container = client.containers.get(container_id)
    return jsonify(container.attrs)


@api.route('/images')
@json_list
def get_images():
    return client.images.list()


@api.route('/images/<image_id>')
@docker_error_handling
def get_image(image_id):
    image = client.containers.get(image_id)
    return jsonify(image.attrs)
