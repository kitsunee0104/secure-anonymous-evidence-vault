import hashlib
from cryptography.fernet import Fernet

def generate_key():
    return Fernet.generate_key()

def encrypt_data(data: bytes, key: bytes) -> bytes:
    f = Fernet(key)
    return f.encrypt(data)

def decrypt_data(data: bytes, key: bytes) -> bytes:
    f = Fernet(key)
    return f.decrypt(data)

def generate_hash(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()
