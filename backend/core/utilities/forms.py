# security/forms.py
from flask_security.forms import LoginForm
from wtforms import StringField, SelectMultipleField
from wtforms.validators import InputRequired


class ExtendedLoginForm(LoginForm):
    email = StringField('Username or email', [InputRequired()])


class Select2MultipleField(SelectMultipleField):

    def pre_validate(self, form):
        # Prevent "not a valid choice" error
        pass

    def process_formdata(self, valuelist):
        if valuelist:
            self.data = ",".join(valuelist)
        else:
            self.data = ""
