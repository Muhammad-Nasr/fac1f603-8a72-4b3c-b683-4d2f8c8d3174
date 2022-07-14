
from flask_minify import Minify
from sys import exit
import os
from app.config import config_dict
from app import create_app, db
from app.authentication.models import User

# WARNING: Don't run with debug turned on in production!
DEBUG = (config_dict['default'])

# The configuration
get_config_mode = 'Debug' if DEBUG else 'Production'


app = create_app(os.getenv('FLASK_CONFIG') or 'default')
@app.shell_context_processor
def make_shell_context():
    return dict(db=db, User=User)


if not DEBUG:
    Minify(app=app, html=True, js=False, cssless=False)


if __name__ == "__main__":
    app.run()
