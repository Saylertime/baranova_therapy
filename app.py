from pathlib import Path
from flask import Flask, send_file

BASE_DIR = Path(__file__).resolve().parent

app = Flask(
    __name__,
    static_folder=str(BASE_DIR / "assets"),
    static_url_path="/assets"
)


@app.route("/")
def index():
    return send_file(BASE_DIR / "index.html")


if __name__ == "__main__":
    app.run(
        host="0.0.0.0",
        port=5021,
        debug=False
    )