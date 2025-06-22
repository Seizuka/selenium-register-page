from cryptography.fernet import Fernet

fernet_key= b'YdR2k8-2zJlbdnkDRyaX8NhcHowEmdna_jYZqWcdsRo='
cipher = Fernet(fernet_key)

def encrypt(text: str) -> str:
    return cipher.encrypt(text.encode()).decode()

def decrypt(token: str) -> str:
    return cipher.decrypt(token.encode()).decode()