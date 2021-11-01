from flask_login import current_user, login_required, login_user, logout_user

from app.libs.error_code import Success, NotFound, Forbidden, DeleteSuccess
from app.libs.red_print import RedPrint
from app.validators.user import LoginForm
from app.models.user import User
from app import redis as rd
from app.config.config import redis_key_prefix, ticket_expire_time
from app.libs.helper import generate_ticket

api = RedPrint('session')


@api.route('', methods=['GET'])
@login_required
def get_session_api():
    return Success(data=current_user)


@api.route('', methods=['POST'])
def create_session_api():
    form = LoginForm().validate_for_api().data_
    user = User.get_by_id(form['username'])
    if not user:
        raise NotFound(msg='用户不存在')
    if not user.check_password(form['password']):
        raise Forbidden(msg='密码错误')
    ticket = generate_ticket()
    key = redis_key_prefix + 'session::' + user.username
    rd.set(key, ticket)
    rd.expire(key, ticket_expire_time)
    login_user(user, remember=True)
    return Success(msg='登录成功')


@api.route('', methods=['DELETE'])
def delete_session_api():
    logout_user()
    return DeleteSuccess('登出成功')
