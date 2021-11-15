from flask_login import current_user, login_required
from app.libs.red_print import RedPrint
from app import redis as rd
from app.config.config import redis_key_prefix
from app.libs.error_code import Success, NotFound, Forbidden
from app.validators.ticket import CheckTicketForm
from app.models.user import User

api = RedPrint('ticket')


@api.route('', methods=['GET'])
@login_required
def get_ticket_api():
    key = redis_key_prefix + 'session::' + current_user.username
    ticket = rd.get(key)
    if ticket is None:
        return NotFound()
    return Success(data={
        'username': current_user.username,
        'ticket': ticket
    })


@api.route('/check', methods=['POST'])
def check_ticket_api():
    form = CheckTicketForm().validate_for_api().data_
    user = User.get_by_id(form['username'])
    if not user:
        return NotFound(msg='用户不存在')
    key = redis_key_prefix + 'session::' + user.username
    ticket = rd.get(key)
    if ticket is None or ticket != form['ticket']:
        return Forbidden(msg='校验失败')
    return Success(msg='校验成功')
