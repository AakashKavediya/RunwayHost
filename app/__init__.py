from flask import Flask

def create_app():
    app = Flask(__name__)
    
    from .routes.api import api_bp
    from .routes.web import web

    # `api_bp` already declares url_prefix='/api' internally
    app.register_blueprint(api_bp)
    app.register_blueprint(web)

    return app

# Create the app instance for Vercel
app = create_app()
