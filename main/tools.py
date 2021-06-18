from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives.kdf.scrypt import Scrypt
from cryptography.hazmat.primitives.kdf.hkdf import HKDF
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
import json, os

def dumps(p, _return=True):
    for k, v in p.items():
        
        if k == 'accounts':
            for i in range(len(p[k])):
                p[k][i] = list(p[k][i])

        elif isinstance(v, bytes):
            p[k] = list(v)
        
        if isinstance(v, dict):
            p[k] = dumps(v, False)
    
    if _return: return json.dumps(p)
    
    else: return p

def loads(p, _load=True):
    if _load:
        p = json.loads(p)

    for k, v in p.items():
        if k == 'accounts':
            for i in range(len(p[k])):
                p[k][i] = bytes(p[k][i])

        elif isinstance(v, list):
            p[k] = bytes(v)
        
        if isinstance(v, dict):
            p[k] = loads(v, False)
    
    return p



derive_key = lambda password: HKDF(
    algorithm=hashes.SHA256(),
    length=32, salt=None, info=None,
    backend=default_backend()
    ).derive(password)



def encryptor(data, key):
    cipherdata = b''
    for chunk in range(0, len(data), 4096):
        # Derive key with a random 16-byte salt
        salt = os.urandom(16)
        kdf = Scrypt(
            salt=salt, length=32,
            n=2**14, r=8, p=1,
            backend=default_backend()
            )
        
        key = kdf.derive(key)

        # Generate a random 96-bit IV.
        iv = os.urandom(12)

        # Construct an AES-GCM Cipher object with the given key and IV.
        encryptor = Cipher(
            algorithms.AES(key),
            modes.GCM(iv),
            backend=default_backend()
            ).encryptor()

        associated_data = iv + salt

        # associated_data will be authenticated but not encrypted,
        # it must also be passed in on decryption.
        encryptor.authenticate_additional_data(associated_data)


        cipherchunk = encryptor.update(data[chunk: chunk + 4096]) + encryptor.finalize()
        header = associated_data + encryptor.tag
        cipherdata += header + cipherchunk
    
    return cipherdata

def decryptor(cipherdata, key):
    data = b''
    for chunk in range(0, len(cipherdata), 4096 + 44):
        cipherchunk =  cipherdata[chunk: chunk + 4096 + 44]
        header = cipherchunk[:44]
        cipher = cipherchunk[44:]
        associated_data = header[:28]

        iv = associated_data[:12]
        salt = associated_data[12:28]

        # derive the same key from the key + salt
        kdf = Scrypt(
            salt=salt, length=32,
            n=2**14, r=8, p=1,
            backend=default_backend()
            )
        
        key = kdf.derive(key)

        # get the tag. GCM tags are always 16 bytes
        tag = header[-16:]
        # Construct an AES-GCM Cipher object with the given key and IV
        # For decryption, the tag is passed in as a parameter
        decryptor = Cipher(
            algorithms.AES(key),
            modes.GCM(iv, tag),
            backend=default_backend()
            ).decryptor()
        
        decryptor.authenticate_additional_data(associated_data)
        data += decryptor.update(cipher)

    return data
