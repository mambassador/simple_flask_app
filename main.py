from flask import Flask

from views import get_average_measurement, get_requirements, generate_users, count_astros


app = Flask(__name__)


@app.route('/requirements/')
def get_requirements_route():
    return get_requirements()


@app.route('/generate-users/')
def generate_users_route():
    return generate_users()


@app.route('/mean/')
def get_average_measurement_route():
    return get_average_measurement()


@app.route('/space')
def count_astros_route():
    return count_astros()


if __name__ == "__main__":
    app.run()
