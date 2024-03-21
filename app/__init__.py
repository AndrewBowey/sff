from flask import Flask

import app.views as views
from app.extensions import db

app = Flask(__name__, template_folder='templates')

app.config.from_object('config.Config')

db.init_app(app)

from app.models import User

app.add_url_rule('/', view_func=views.home)
app.add_url_rule('/account', view_func=views.account)
app.add_url_rule('/visualiser', view_func=views.calculator)
app.add_url_rule('/calc-fv', view_func=views.calc_fv)

@app.context_processor
def inject_user():
    return dict(user=User.query.first())