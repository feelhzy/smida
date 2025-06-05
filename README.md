# smida

A simple Flask-based community API with activities and payments.

## Setup

Install dependencies:

```bash
pip install Flask Flask-SQLAlchemy
```

Run the application:

```bash
python -m smidapi.app
```

## API Endpoints

- `POST /register` – register new user and receive auth token.
- `POST /activities` – create activity (requires `Authorization` header).
- `GET /activities` – list activities.
- `POST /activities/<id>/pay` – pay for an activity using Alipay, WeChat Pay or KakaoPay.
