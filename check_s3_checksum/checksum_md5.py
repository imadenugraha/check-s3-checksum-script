import hashlib


def calculate_md5(file_path: str) -> str:
    md5 = hashlib.md5()
    
    with open(file=file_path, mode='rb') as f:
        while chunk := f.read(8192):
            md5.update(chunk)
    
    return md5.hexdigest()
