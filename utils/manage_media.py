from PIL import Image
from io import BytesIO
from django.core.files.uploadedfile import InMemoryUploadedFile
import sys

import uuid, datetime

from utils.constants.constants import  MAX_TWO, CHAR_0
from utils.constants.media import (
    DEFAULT_EXTENSION_IMAGE, 
    MAX_SIZE, 
    MAX_QUALITY, 
    FIELD_NAME,
)

def get_path(type, app_name):
    return '{}{}/{}/{}'.format(
        datetime.datetime.now().year,
        str(datetime.datetime.now().month).rjust(MAX_TWO, CHAR_0),
        type,
        app_name,
    )

def get_name(prefix, extension):
    return '{}{}.{}'.format(
        prefix,
        uuid.uuid4(),
        extension
    )

def resizing(width, height):
    if width < MAX_SIZE and height < MAX_SIZE:
        return (width, height)

    if width > height:
        return (MAX_SIZE, int((height * MAX_SIZE) / width))
    return (int((width * MAX_SIZE) / height), MAX_SIZE)

def manage_image(image, prefix):
    image_temporary = Image.open(image)
    output_iostream = BytesIO()

    image_temporary_resized = image_temporary.resize(
        resizing(image_temporary.width ,image_temporary.height)
    )
    image_temporary.close()

    image_temporary_resized.save(
        output_iostream,
        format=DEFAULT_EXTENSION_IMAGE,
        quality=MAX_QUALITY
    )
    output_iostream.seek(0)

    return InMemoryUploadedFile(
        output_iostream,
        FIELD_NAME,
        get_name(prefix, DEFAULT_EXTENSION_IMAGE),
        DEFAULT_EXTENSION_IMAGE,
        sys.getsizeof(output_iostream),
        None
    )