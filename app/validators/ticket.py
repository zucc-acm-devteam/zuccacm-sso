from app.validators.base import BaseForm
from wtforms.fields import StringField
from wtforms.validators import DataRequired


class CheckTicketForm(BaseForm):
    username = StringField(validators=[DataRequired(message='用户名不能为空')])
    ticket = StringField(validators=[DataRequired(message='校验值不能为空')])
