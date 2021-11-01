from app.validators.base import BaseForm
from wtforms.fields import StringField
from wtforms.validators import DataRequired, ValidationError

from app.models.user import User


class RegisterForm(BaseForm):
    username = StringField(validators=[DataRequired(message='用户名不能为空')])
    password = StringField(validators=[DataRequired(message='密码不能为空')])
    nickname = StringField(validators=[DataRequired(message='姓名不能为空')])

    def validate_username(self, value):
        if User.get_by_id(self.username.data):
            raise ValidationError('用户已存在')


class LoginForm(BaseForm):
    username = StringField(validators=[DataRequired(message='Username cannot be empty')])
    password = StringField(validators=[DataRequired(message='Password cannot be empty')])
