import os
import json
from flask import Flask, jsonify, request, send_from_directory, render_template_string

app = Flask(__name__)
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_FILE = os.path.join(BASE_DIR, "dashboard_data.json")

def load_data():
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, "r", encoding="utf-8") as f:
            return json.load(f)
    return {}

@app.route("/")
def index():
    html_file = os.path.join(BASE_DIR, "dashboard.html")
    if os.path.exists(html_file):
        with open(html_file, "r", encoding="utf-8") as f:
            return f.read()
    return "<h1>Rajasthan Royals SupeRR Selector Dashboard</h1><p>Please run build_dashboard.py first.</p>"

@app.route("/assets/<path:filename>")
def player_assets(filename):
    return send_from_directory(os.path.join(BASE_DIR, "assets"), filename)

@app.route("/api/data", methods=["GET"])
def get_all_data():
    data = load_data()
    return jsonify(data)

@app.route("/api/batters", methods=["GET"])
def get_batters():
    data = load_data()
    return jsonify({
        "top10": data.get("top10_batters", []),
        "all": data.get("all_batters", [])
    })

@app.route("/api/bowlers", methods=["GET"])
def get_bowlers():
    data = load_data()
    return jsonify({
        "top10": data.get("top10_bowlers", []),
        "all": data.get("all_bowlers", [])
    })

@app.route("/api/player/<name>", methods=["GET"])
def get_player(name):
    data = load_data()
    name_clean = name.strip().lower()
    for p in data.get("all_batters", []):
        if p.get("name", "").lower() == name_clean:
            return jsonify({"role": "bat", "player": p})
    for p in data.get("all_bowlers", []):
        if p.get("name", "").lower() == name_clean:
            return jsonify({"role": "bowl", "player": p})
    return jsonify({"error": "Player not found"}), 404

@app.route("/api/simulate", methods=["POST"])
def simulate():
    body = request.get_json() or {}
    bl = int(body.get("balls_left", 12))
    wk = int(body.get("wickets_lost", 5))
    need = int(body.get("runs_needed", 28))
    par = int(body.get("par", 175))
    elo = int(body.get("elo_diff", 0))
    inn = int(body.get("innings", 2))

    if inn == 2:
        rrr = (need / max(bl, 1)) * 6.0
        z = -0.55 * (rrr - 9.0) - 0.25 * (wk - 4) + 0.003 * elo - 0.01 * (need - bl * 1.5)
        wp = 1.0 / (1.0 + 2.71828 ** (-z))
        wp = max(0.01, min(0.99, wp))
        closeness = 1.0 - abs(wp - 0.5) * 2.0
        time_factor = (120 - bl) / 120.0
        li = (closeness * 2.8 + time_factor * 1.8 + (1.2 if rrr > 11 else 0.4)) * 0.75
    else:
        proj = par * (1.0 - wk * 0.06) + (120 - bl) * 1.4
        gap = proj - par
        wp = 1.0 / (1.0 + 2.71828 ** (-(gap / 20.0 + elo / 150.0)))
        li = 0.45 + (120 - bl) / 200.0 + (0.35 if wk >= 5 else 0.1)

    return jsonify({
        "win_probability": round(wp, 4),
        "leverage_index": round(li, 2),
        "is_pressure": bool(li >= 1.25)
    })

if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument("--port", type=int, default=5000, help="Port to run on")
    parser.add_argument("--host", type=str, default="127.0.0.1", help="Host interface")
    args = parser.parse_args()

    print(f"Starting Rajasthan Royals SupeRR Selector Dashboard on http://{args.host}:{args.port}")
    app.run(host=args.host, port=args.port, debug=False)
