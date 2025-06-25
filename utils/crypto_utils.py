from cryptography.fernet import Fernet

# Change using your generate key
fernet_key = b'vC4Tl-6pxpXy5tVMMn2mTEIzSioMCydKAZdzQvFy2nk='
cipher = Fernet(fernet_key)

def encrypt(text: str) -> str:
    return cipher.encrypt(text.encode()).decode()

def decrypt(token: str) -> str:
    return cipher.decrypt(token.encode()).decode()
