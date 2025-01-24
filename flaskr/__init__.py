from flask import Flask, redirect, url_for, render_template, session

def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'clave-secreta'

    # Registrar el Blueprint
    from .auth import auth_bp
    app.register_blueprint(auth_bp, url_prefix='/auth')

    # Página principal
    @app.route('/')
    def index():
        if 'user' in session:
            return render_template('blog/index.html', user=session['user'])
        return redirect(url_for('auth.login'))

    return app
