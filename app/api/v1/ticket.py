from flask_login import current_user, login_required
from app.libs.red_print import RedPrint
from app.libs.error_code import Success, NotFound, Forbidden
from app.validators.ticket import CheckTicketForm
from app.models.user import User
from app.libs.helper import get_ticket, renew_ticket

api = RedPrint('ticket')


@api.route('', methods=['GET'])
@login_required
def get_ticket_api():
    ticket = get_ticket(current_user)
    if ticket is None:
        return NotFound()
    return Success(data={
        'username': current_user.username,
        'ticket': ticket
    })


@api.route('/renew', methods=['POST'])
@login_required
def renew_ticket_api():
    ticket = renew_ticket(current_user)
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
    ticket = get_ticket(user)
    if ticket is None or ticket != form['ticket']:
        return Forbidden(msg='校验失败')
    return Success(msg='校验成功')
