import os

SITE_NAME = os.getenv("SITE_NAME", "DEFAULT")

# Flask-Bootstrap Settings
BOOTSTRAP_SERVE_LOCAL = True
BOOTSTRAP_USE_MINIFIED = False

# Flask-Mail settings
MAIL_USERNAME = os.getenv('MAIL_USERNAME', 'youremail@example.com')
MAIL_PASSWORD = os.getenv('MAIL_PASSWORD', 'yourpassword')
MAIL_DEFAULT_SENDER = os.getenv('MAIL_DEFAULT_SENDER', '"Default" <{email}>'.format(email=MAIL_USERNAME))
MAIL_SERVER = os.getenv('MAIL_SERVER', 'smtp.gmail.com')
MAIL_PORT = int(os.getenv('MAIL_PORT', '465'))
MAIL_USE_SSL = int(os.getenv('MAIL_USE_SSL', True))

# administrator list
ADMINS = [MAIL_DEFAULT_SENDER, '"Mike Scales" michael.scales88@gmail.com']
