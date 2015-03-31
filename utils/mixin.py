# -*- coding: utf-8 -*-
from __future__ import division, print_function, unicode_literals

import json

from django.http import HttpResponse

from utils.encoders import encoder


class JSONResponseMixin(object):
    def __init__(self):
        self.context = {
            'status': True,
            'errors': {},
            'data': {}
        }

    def render_to_response(self, context):
        """
        Returns a JSON response containing 'context' as payload
        """
        return self.get_json_response(self.convert_context_to_json(context))

    def get_json_response(self, content, **httpresponse_kwargs):
        """
        Construct an `HttpResponse` object.
        """
        return HttpResponse(content,
                            content_type='application/json',
                            **httpresponse_kwargs)

    def convert_context_to_json(self, context):
        """
        Convert the context dictionary into a JSON object
        """
        return json.dumps(context, default=encoder, encoding='utf-8')