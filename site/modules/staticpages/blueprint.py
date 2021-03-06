from flask import Blueprint, render_template, make_response
from jinja2 import TemplateNotFound

staticpages = Blueprint("staticpages", __name__, template_folder="templates", url_prefix="")

@staticpages.route("/", defaults={"page": "index"})
@staticpages.route("/<page>/")
def show_staticpage(page):
    try:
        return render_template("staticpages/{}.html".format(page))
    except TemplateNotFound:
        return make_response(render_template("not_found.html"), 404)
