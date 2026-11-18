
import secrets
import string
import hashlib
import hmac


def generate_password(length=12, include_symbols=True):
    if not isinstance(length, int) or isinstance(length, bool):
        raise TypeError("Length must be an integer")

    if length < 1:
        raise ValueError("Length must be positive")

    characters = string.ascii_letters + string.digits

    if include_symbols:
        characters += "!@#$%^&*()_+-="

    return "".join(secrets.choice(characters) for _ in range(length))


def password_strength(password):
    if not isinstance(password, str):
        raise TypeError("Password must be a string")

    score = 0

    if len(password) >= 8:
        score += 1
    if len(password) >= 12:
        score += 1
    if any(c.islower() for c in password):
        score += 1
    if any(c.isupper() for c in password):
        score += 1
    if any(c.isdigit() for c in password):
        score += 1
    if any(c in string.punctuation for c in password):
        score += 1

    if score <= 2:
        return "Weak"
    elif score <= 4:
        return "Medium"
    return "Strong"


def hash_text(text):
    if not isinstance(text, str):
        raise TypeError("Input must be a string")

    return hashlib.sha256(text.encode()).hexdigest()


def verify_hash(text, hashed):
    if not isinstance(text, str) or not isinstance(hashed, str):
        raise TypeError("Both inputs must be strings")

    return hmac.compare_digest(hash_text(text), hashed)
