from app import app

if __name__ == '__main__':
    app.jinja_env.auto_reload = True
    app.run(host="0.0.0.0", port=5555)