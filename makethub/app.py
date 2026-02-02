from flask import Flask
from auth.login import auth_bp
from marketplace.listings import listings_bp
from marketplace.uploads import uploads_bp
from marketplace.admin import admin_bp

app = Flask(__name__)
app.config["SECRET_KEY"] = "dev"

app.register_blueprint(auth_bp)
app.register_blueprint(listings_bp)
app.register_blueprint(uploads_bp)
app.register_blueprint(admin_bp)

app.run(debug=True)