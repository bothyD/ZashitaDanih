import hashlib

def sha256_hash(input_string):
    sha256_hash = hashlib.sha256()
    sha256_hash.update(input_string.encode('utf-8'))
    hash_bytes = sha256_hash.digest()
    return hash_bytes