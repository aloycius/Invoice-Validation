# main_app.py
from flask import Flask
from UploadComponent import upload_blueprint
from ValidationComponent import validation_blueprint
from VerificationComponent import verification_blueprint

app = Flask(__name__)

# Register blueprints
app.register_blueprint(upload_blueprint, url_prefix='/upload')
app.register_blueprint(validation_blueprint, url_prefix='/validate')
app.register_blueprint(verification_blueprint, url_prefix='/verify')

if __name__ == '__main__':
    app.run(debug=True)
