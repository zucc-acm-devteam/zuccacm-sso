from app.libs.error_code import AuthFailed, DeleteSuccess, CreateSuccess
from app.libs.red_print import RedPrint
from app.validators.user import RegisterForm
from app.models.user import User

api = RedPrint('user')


@api.route('', methods=['POST'])
def create_user_api():
    form = RegisterForm().validate_for_api().data_
    User.create(**form)
    return CreateSuccess('注册成功')
