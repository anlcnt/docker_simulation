# Docker client
import docker
from werkzeug.datastructures import MultiDict

client = docker.from_env()


def get_containers(filters: MultiDict):
    return client.containers.list(all=True, filters=filters.to_dict())


def get_container(container_id: str):
    return client.containers.get(container_id)


def get_images(filters: MultiDict):
    return client.images.list(filters=filters.to_dict())


def get_image(image_id: str):
    return client.images.get(image_id)


def create_containers(image=None, count=1):
    return tuple(
        map(lambda _: client.containers.create(image), range(count))
    )
