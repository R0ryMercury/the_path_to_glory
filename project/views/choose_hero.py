from flask_restx import Namespace, Resource
from flask import request, render_template, redirect, make_response
from project.container import heroes
from project.logic.unit import PlayerUnit
from project.logic.data_for_front import create_unit, get_unit_params

choose_hero_ns = Namespace("choose-hero")


@choose_hero_ns.route("/")
class ChooseHeroView(Resource):
    def get(self):
        unit_params = get_unit_params()
        unit_params["header"] = "героя"
        headers = {"Content-Type": "text/html"}
        return make_response(
            render_template("hero_choosing.html", result=unit_params), 200, headers
        )

    def post(self):
        player_data = request.form.to_dict()
        heroes["player"] = create_unit(player_data, PlayerUnit)
        return redirect("/choose-enemy/")
