from flask import Flask
import logging
import logging.handlers

app = Flask(__name__)

FILENAME = "/var/log/app.log"

handler = logging.handlers.RotatingFileHandler(FILENAME, "a+", maxBytes=3000, backupCount=5)
handler.setFormatter(
  logging.Formatter("[%(asctime)s] %(levelname)s in %(module)s: %(message)s")
)
app.logger.addHandler(handler)

@app.route("/")
def index():
    app.logger.debug("A value for debugging")
    return "success"
