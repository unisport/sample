import json
from django.http import HttpResponse


class StatusResponse(object):
    OK = 'OK'
    FAIL = 'FAIL'

    @classmethod
    def ok(cls, text=None, **additional_params):
        return cls._get_json_response(cls.OK, text, **additional_params)

    @classmethod
    def fail(cls, text=None, **additional_params):
        return cls._get_json_response(cls.FAIL, text, **additional_params)

    @classmethod
    def _get_json_response(cls, status, text, **additional_params):
        response_dict = {
            'status': status,
        }

        if text:
            response_dict['responseText'] = text

        response_dict.update(additional_params)

        return HttpResponse(
            json.dumps(response_dict),
            content_type="application/json"
        )
