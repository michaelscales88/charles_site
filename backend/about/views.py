import os
import os.path as op
from flask import Markup, url_for
from flask_admin import form
from wtforms import StringField
from backend.base_view import BaseView
from .. import server

# Create directory for file fields to use
file_path = op.join(server.config['BASE_DIR'], 'static/img')
try:
    os.mkdir(file_path)
except OSError:
    pass


class AboutImageView(BaseView):

    form_excluded_columns = ("about_info",)

    def _list_thumbnail(view, context, model, name):
        if not model.path:
            return ''

        return Markup(
            '<img src="{}">'.format(
                url_for(
                    'static',
                    filename='img/' + form.thumbgen_filename(model.path)
                )
            )
        )

    column_formatters = {
        'path': _list_thumbnail
    }

    form_extra_fields = {
        'file_path': StringField(
            'Directory',
            default=file_path,
            render_kw={'readonly': True}
        ),
        'path': form.ImageUploadField(
            'Image',
            base_path=file_path,
            url_relative_path='img/',
            thumbnail_size=(100, 100, True)
        )
    }


class AboutView(BaseView):
    form_columns = ("title", "description", "image")
