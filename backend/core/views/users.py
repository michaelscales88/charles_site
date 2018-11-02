from backend.base_view import BaseView
from ..models import UserModel


class UsersView(BaseView):
    column_exclude_list = ['password']
    form_columns = ('email', 'username', 'password', 'roles', 'active')
    form_widget_args = {
        'password': {
            'style': 'color: red',
            'minlength': '8'
        }
    }
