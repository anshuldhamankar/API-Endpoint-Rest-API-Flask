from flask import Blueprint, request, jsonify
from .utils import load_wimbledon_data

bp = Blueprint('routes', __name__)
wimbledon_data = load_wimbledon_data()

@bp.route('/wimbledon', methods=['GET'])
def get_wimbledon_result():
    year = request.args.get('year')

    if not year:
        return jsonify({"error": "Missing 'year' query parameter"}), 400

    if not year.isdigit():
        return jsonify({"error": "Year must be a valid number"}), 400

    if year not in wimbledon_data:
        return jsonify({"error": f"No data found for year {year}"}), 404

    data = wimbledon_data[year]
    return jsonify({
        "year": int(year),
        "champion": data["champion"],
        "runner_up": data["runner_up"],
        "score": data["score"],
        "sets": data["sets"],
        "tiebreak": data["tiebreak"]
    })
@bp.route('/')
def index():
    return jsonify({
        "message": "Welcome to the Wimbledon Finals API. Use /wimbledon?year=YYYY"
    })