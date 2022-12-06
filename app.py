from flask import Flask, render_template
from flask_restx import Api
from project.views.choose_hero import choose_hero_ns
from project.views.choose_enemy import choose_enemy_ns
from project.config import Config


def create_app(config_object):
    app = Flask(__name__, template_folder="project/templates")
    app.config.from_object(config_object)
    register_extensions(app)
    return app


def register_extensions(app):
    api = Api(app, title="Flask Api", doc="/docs")
    api.add_namespace(choose_hero_ns)
    api.add_namespace(choose_enemy_ns)


app = create_app(Config())


@app.route("/")
def menu_page():
    return render_template("index.html")


if __name__ == "__main__":
    app.run()
