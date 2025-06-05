from flask import Flask, request, jsonify, abort
from uuid import uuid4

from .config import Config
from .models import db, User, Activity, Payment, Post
from .payments import PaymentGateway


def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    db.init_app(app)

    payment_gateway = PaymentGateway()

    def require_auth(f):
        def wrapper(*args, **kwargs):
            token = request.headers.get('Authorization')
            if not token:
                abort(401)
            user = User.query.filter_by(token=token).first()
            if not user:
                abort(401)
            return f(user, *args, **kwargs)
        wrapper.__name__ = f.__name__
        return wrapper

    @app.before_first_request
    def create_tables():
        db.create_all()

    @app.route('/register', methods=['POST'])
    def register():
        data = request.json
        username = data.get('username')
        password = data.get('password')
        if not username or not password:
            return jsonify({'error': 'username and password required'}), 400
        if User.query.filter_by(username=username).first():
            return jsonify({'error': 'username exists'}), 400
        token = str(uuid4())
        user = User(username=username, password=password, token=token)
        db.session.add(user)
        db.session.commit()
        return jsonify({'token': token})

    @app.route('/activities', methods=['POST'])
    @require_auth
    def create_activity(user):
        data = request.json
        title = data.get('title')
        description = data.get('description')
        activity = Activity(title=title, description=description, creator_id=user.id)
        db.session.add(activity)
        db.session.commit()
        return jsonify({'id': activity.id, 'title': activity.title})

    @app.route('/activities', methods=['GET'])
    def list_activities():
        activities = Activity.query.all()
        return jsonify([
            {'id': a.id, 'title': a.title, 'description': a.description, 'date': a.date.isoformat()}
            for a in activities
        ])

    @app.route('/activities/<int:activity_id>/pay', methods=['POST'])
    @require_auth
    def pay(user, activity_id):
        data = request.json
        amount = data.get('amount')
        provider = data.get('provider')
        activity = Activity.query.get_or_404(activity_id)
        result = payment_gateway.pay(provider, amount)
        payment = Payment(user_id=user.id, activity_id=activity.id, amount=amount,
                          status=result['status'], provider=provider)
        db.session.add(payment)
        db.session.commit()
        return jsonify(result)

    return app

if __name__ == '__main__':
    app = create_app()
    app.run(debug=True)
