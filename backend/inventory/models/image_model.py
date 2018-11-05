import os
import os.path as op
from sqlalchemy.event import listens_for
from flask_admin import form

from ...extensions import db
from ... import server


# Create directory for file fields to use
file_path = op.join(server.config['BASE_DIR'], 'static/img')
try:
    os.mkdir(file_path)
except OSError:
    pass


class ImageModel(db.Model):

    __tablename__ = "image"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.Unicode(64))
    path = db.Column(db.Unicode(128))

    inventory = db.relationship("InventoryModel", back_populates="image")

    def __str__(self):
        return self.name


@listens_for(ImageModel, 'after_delete')
def del_image(mapper, connection, target):
    if target.path:
        # Delete image
        try:
            os.remove(op.join(file_path, target.path))
        except OSError:
            pass

        # Delete thumbnail
        try:
            os.remove(
                op.join(
                    file_path,
                    form.thumbgen_filename(target.path)
                )
            )
        except OSError:
            pass
