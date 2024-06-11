import hashlib
import base64


def calculate_md5(file_path: str) -> str:
    md5 = hashlib.md5()
    
    with open(file=file_path, mode='rb') as f:
        while chunk := f.read(4096):
            md5.update(chunk)
    
    digest = md5.digest()
    
    md5_base64 = base64.b64encode(digest).decode('utf-8')
    
    return md5_base64
