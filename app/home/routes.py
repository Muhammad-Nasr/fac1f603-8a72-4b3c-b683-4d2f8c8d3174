
from app.home import bp
from flask import render_template
from flask_login import login_required


@bp.route('/index')
@login_required
def index():

    return render_template('home/index.html', segment='index')


# Helper - Extract current page name from request
def get_segment(request):

    try:

        segment = request.path.split('/')[-1]

        if segment == '':
            segment = 'index'

        return segment

    except:
        return None
