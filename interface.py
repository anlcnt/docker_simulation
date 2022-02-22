import os
from flask import Blueprint
from flask import render_template, send_from_directory, request
import docker_client as dc

interface = Blueprint('interface', __name__,)


@interface.route('/')
@interface.route('/index')
def index():
    return render_template(
        'index.html',
        title=__name__,
        containers=dc.get_containers(filters=request.args)
    )


# favicon
@interface.route('/favicon.ico')
def favicon():
    return send_from_directory(os.path.join(interface.root_path, 'static'),
                               'favicon.ico')
