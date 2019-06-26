from rest_framework.views import exception_handler

from utils import restful_status


def custom_exception_handler(exc, context):
    response = exception_handler(exc, context)
    response.status_code = 200
    response.data['status'] = restful_status.STATUS_ERROR
    response.data['msg'] = response.data['detail']
    del response.data['detail']
    return response
