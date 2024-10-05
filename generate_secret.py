import secrets

# Generate a 32-byte (256-bit) secure secret key
SECRET_KEY = secrets.token_urlsafe(32)
print(f"Your SECRET_KEY: {SECRET_KEY}")
