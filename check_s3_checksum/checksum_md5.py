import hashlib
import base64
import logging

logging.basicConfig(level=logging.INFO,
                    format='%(asctime)s - %(name)s - %(level)s - %(message)s',
                    handlers=[logging.FileHandler('output.log'),
                              logging.StreamHandler])

logger = logging.getLogger(__name__)


def calculate_md5(file_path: str) -> str|None:
    md5 = hashlib.md5()
    
    try:
        logger.info("Getting the MD5 checksum from file...")
        with open(file=file_path, mode='rb') as f:
            while chunk := f.read(4096):
                md5.update(chunk)
    
        digest = md5.digest()
    
        md5_base64 = base64.b64encode(digest).decode('utf-8')
    
        logger.info("MD5 has been received!")
        return md5_base64
    except IOError as io_err:
        logger.error(io_err)
        return None
