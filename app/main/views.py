from . import main


@main.route("/")
def index():
    return "Test Page"