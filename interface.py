import os
from flask import Blueprint
from flask import render_template, send_from_directory, request
import docker_client as dc

interface = Blueprint('interface', __name__)


@interface.route('/')
@interface.route('/index')
def index():
    return render_template(
        'index.html',
        title=__name__,
        containers=dc.get_containers(filters=request.args)
    )


@interface.route('/containers')
def containers_page():
    return render_template(
        'containers.html',
        title=__name__,
        containers=dc.get_containers(filters=request.args)
    )


@interface.route('/images')
def images_page():
    return render_template(
        'images.html',
        title=__name__,
        images=dc.get_images(filters=request.args)
    )


# favicon
@interface.route('/favicon.ico')
def favicon():
    return send_from_directory(
        os.path.join(interface.root_path, 'static'), 'favicon.ico')
