from app.libs.error import APIException


class Success(APIException):
    code = 200
    msg = 'ok'
    error_code = 0


class CreateSuccess(APIException):
    code = 201
    error_code = 0


class DeleteSuccess(Success):
    code = 202
    error_code = 0


class SearchSuccess(Success):
    def get_body(self, environ=None, scope=None):
        from flask import json, request
        body = {
            'msg': self.msg,
            'code': self.error_code,
            'request': request.method + ' ' + self.get_url_no_param()
        }
        body.update(self.data)
        text = json.dumps(body)
        return text


class ServerError(APIException):
    code = 500
    msg = 'sorry, we made a mistake (*￣︶￣)!'
    error_code = 999


class ParameterException(APIException):
    code = 400
    msg = 'invalid parameter'
    error_code = 1000


class NotFound(APIException):
    code = 404
    msg = 'the resource are not found O__O...'
    error_code = 1001


class AuthFailed(APIException):
    code = 401
    error_code = 1005
    msg = '请先登录'


class Forbidden(APIException):
    code = 403
    error_code = 1004
    msg = 'forbidden'


class NotAchieved(APIException):
    code = 405
    error_code = -1
    msg = '施工中∑(っ°Д°;)っ'
