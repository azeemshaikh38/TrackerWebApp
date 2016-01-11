from django.http import HttpResponse
import json

def HttpResponseError(e=None, status=None):
    ret = {"success": False}
    if e is not None:
        ret['detail'] = e
    status_int = 400
    if status is not None:
        status_int = status
    return HttpResponse(json.dumps(ret), status=status_int)

def HttpResponseSuccess(m=None, status=None):
    ret = {"success": True}
    if m is not None:
        ret['detail'] = m
    status_int = 200
    if status is not None:
        status_int = status
    return HttpResponse(json.dumps(ret), status=status_int)
