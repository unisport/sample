# -*- coding: utf-8 -*-
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.template.defaultfilters import slugify
import os
import time
from django.conf import settings


def render_to(template, content_type='text/html'):
    """
    Decorator for Django views that sends returned dict to render_to_response function
    with given template and RequestContext as context instance.

    If view doesn't return dict then decorator simply returns output.
    Additionally view can return two-tuple, which must contain dict as first
    element and string with template name as second. This string will
    override template name, given as parameter

    Parameters:

     — template: template name to use
    """

    def renderer(func):
        def wrapper(request, *args, **kw):
            output = func(request, *args, **kw)
            if isinstance(output, (list, tuple)):
                return render_to_response(output[1], output[0], RequestContext(request), content_type=content_type)
            elif isinstance(output, dict):
                return render_to_response(template, output, RequestContext(request), content_type=content_type)
            return output
        return wrapper
    return renderer


def upload_file(request, name, path=None):
    """
    Handle uploaded file - dowcode and slugify filename, add timestamp to filename and write file under MEDIA_ROOT.
    Returns relative path to uploaded file from MEDIA_ROOT.
    Arguments:
    - request - HttpRequest object
    - name - name of file in POST-request
    - path - suffix for upload path (optional). Example: path = "images/"
    """
    if request.method == 'POST':
        if request.FILES.__contains__(name):
            timestamp = int(time.time())
            filename, ext = os.path.splitext(request.FILES[name].name)
            filename = slugify(downcode(filename))
            filename = "%s%d%s" % (filename, timestamp, ext)
            rel_path = path + filename if path else filename
            if not os.path.exists(os.path.join(settings.MEDIA_ROOT, path)):
                os.mkdir(os.path.join(settings.MEDIA_ROOT, path))
            destination = open(settings.MEDIA_ROOT + rel_path, 'wb+')
            for chunk in request.FILES[name].chunks():
                destination.write(chunk)
            destination.close()
            return rel_path
    return None