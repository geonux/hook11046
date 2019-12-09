from pywps import UOM

conf = {
    "handler": "say_hello",
    "inputs": [
    {
        "type": "string",
        "identifier": "name",
        "title": "Input name"
    },
    {
        "type": "float",
        "identifier": "count",
        "title": "Allowed values",
        "allowed_values": [[0, 0.1, 1]]
    },
    {
        "type": "string",
        "identifier": "with_enum",
        "title": "Enums",
        "allowed_values": ["one","two","three"]
    },
    {
        "type": "bbox",
        "identifier": "thebbox",
        "title": "Extend",
        "crss": ['EPSG:3857', 'EPSG:4326'],
        "min_occurs": 0
    }],
    "outputs": [
    {
        "type": "string",
        "identifier": "response",
        "title": "Output response"
    }],
    "store_supported": "True",
    "status_supported": "True"
}


def say_hello(request, response):
    '''
    This is a docstring

    Thios
    :param request:
    :param response:
    '''
    response.outputs['response'].data = 'Hello from France  ' + \
        request.inputs['name'][0].data
    response.outputs['response'].uom = UOM('unity')
    return response
