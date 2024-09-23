import base64
from flask import jsonify, make_response, request, send_from_directory
import os.path
from urllib.parse import urlparse
import random
from PIL import Image
from io import BytesIO


def make_link(localhost, path):
    url = f"{localhost}{path}"
    return url


def split_join(url):
    url = url.split("/")
    url = "/".join(url[:3])
    return url


def make_image_local_path(PATH, url):
    parsed_url = urlparse(url)

    path = parsed_url.path

    path_segments = path.split("/")
    new_path = "/".join(path_segments[2:])
    pathFull = os.path.join(PATH, new_path)
    print("________" + str(pathFull) + "_____" + str(url))
    return pathFull


def make_url_nginx_image(id_user, path, imageSaved, typeof):
    local_host = split_join(request.base_url)
    random_name = f"{id_user}_{typeof}_{random.randint(100000, 999999)}.jpg"
    image_link = f"https://samsungnote.store/image/{id_user}/{random_name}"

    if not os.path.isdir(path):
        os.makedirs(path)
    else:
        user_path = os.path.join(path, str(id_user))
        if not os.path.isdir(user_path):
            os.makedirs(user_path)
            print(user_path)
            imageSaved = Image.open(BytesIO(imageSaved))
            imageSaved.save(optimize=True, quality=40)
            # imageSaved.save(os.path.join(user_path, random_name))
        else:
            imageSaved.save(os.path.join(user_path, random_name))
    print(image_link)
    return image_link


def make_url_apache_image(id_user, path, imageSaved, typeof):
    local_host = split_join(request.base_url)
    random_name = f"{id_user}_{typeof}_{random.randint(100000, 999999)}.jpg"
    image_link = f"https://samsungnote.store/image/{id_user}/{random_name}"

    if not os.path.isdir(path):
        os.makedirs(path)
    else:
        print("____path___make_url_apache_image_" + str(path))
        user_path = os.path.join(path, str(id_user))
        if not os.path.isdir(user_path):
            os.makedirs(user_path)
            print(user_path)
            imageSaved = Image.open(BytesIO(imageSaved))
            imageSaved.save(optimize=True, quality=40)
            # imageSaved.save(os.path.join(user_path, random_name))
        else:
            imageSaved.save(os.path.join(user_path, random_name))
    print("____________PRO____")
    print(id_user)
    print(random_name)
    print(image_link)
    return image_link


def make_url_image(id_user, path, imageSaved, typeof):
    local_host = split_join(request.base_url)
    random_name = f"{id_user}_{typeof}_{random.randint(100000, 999999)}.jpg"
    image_link = f"/get-image/{id_user}/{random_name}"

    if not os.path.isdir(path):
        os.makedirs(path)
    else:
        user_path = os.path.join(path, str(id_user))
        if not os.path.isdir(user_path):
            os.makedirs(user_path)
            print(user_path)
            imageSaved = Image.open(BytesIO(imageSaved))
            imageSaved.save(optimize=True, quality=40)
            # imageSaved.save(os.path.join(user_path, random_name))
        else:
            imageSaved.save(os.path.join(user_path, random_name))
    print("____________PRO____")
    print(id_user)
    print(random_name)
    print(image_link)
    return make_link(local_host, image_link)


def make_url_image_base64(id_user, path, imageSaved, typeof):
    local_host = split_join(request.base_url)
    random_name = f"{id_user}_{typeof}_{random.randint(100000, 999999)}.jpg"
    image_link = f"/get-image-chat/{id_user}/{random_name}"
    print(image_link)
    if not os.path.isdir(path):
        os.makedirs(path)
    else:
        user_path = os.path.join(path, str(id_user))
        if not os.path.isdir(user_path):
            os.makedirs(user_path)
            img_name = f"{user_path}/{random_name}"
            with open(img_name, "wb") as f:
                f.write(imageSaved)
        else:
            img_name = f"{user_path}/{random_name}"
            with open(img_name, "wb") as f:
                f.write(imageSaved)
    return make_link(local_host, image_link)


def make_link_share(id_note):
    local_host = split_join(request.base_url)
    return make_link(local_host, f"/share-note/{id_note}")


def byteToString(byte):
    if byte:
        base64_string = base64.b64encode(byte).decode("utf-8")
        return str(base64_string)
    return None


def view_image_chat(id_user, file_name):
    PATH_IMAGE = "/var/www/samnote-build/image"
    try:
        user_path = os.path.join(PATH_IMAGE, str(id_user))
        # print(f"{user_path}/{file_name}")
        # print(os.path.exists(f"{user_path}/{file_name}"))
        if os.path.exists(f"{user_path}/{file_name}"):
            response = send_from_directory(user_path, file_name)
        return response
    except Exception as e:
        return make_response(jsonify("Something went wrong: ", str(e)), 500)
