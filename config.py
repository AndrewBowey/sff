import os

class Config:
    THREADS_PER_PAGE = 2
    CSRF_ENABLED = True
    CSRF_SESSION_KEY = "PDUhr8bFz7RWuTdgjVLBSq"
    SECRET_KEY = "NpnJzjFeDhux8BE5TC6PgY"

    basedir = os.path.abspath(os.path.dirname(__file__))
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'app.db')

    DEBUG = True
    TEMPLATES_AUTO_RELOAD = True
