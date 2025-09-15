from datetime import UTC, datetime, timedelta

import jwt
from django.conf import settings


def generate_confirmation_token(user_id):
    """Generate JWT token"""
    payload = {
        "user_id": user_id,
        "exp": datetime.now(UTC) + timedelta(hours=1),
    }
    print(">>> Generate token")
    return jwt.encode(payload, settings.SECRET_KEY, algorithm="HS256")
