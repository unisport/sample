import collections
from flask import jsonify

# helper function for normalizing sqlalchemy data
# input: wrapper - string
# input: data - sqlalchemy data
# return: json_object
def alchemy_to_json(wraper, data):
    if isinstance(data, collections.Iterable): 
        data = [item.as_dict() for item in data]
        return jsonify({wraper: data})
    return jsonify({wraper: data.as_dict()})