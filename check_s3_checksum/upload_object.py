import logging
import os
import hashlib

from check_s3_checksum.create_session import create_session
from dotenv import load_dotenv

logging.basicConfig(
    level=logging.ERROR, format="%(asctime)s - %(levelname)s - %(message)s"
)


def upload_object(file_path: str, object_key: str):
    load_dotenv('.env')

    bucket = os.getenv('AWS_BUCKET_NAME')

    s3 = create_session().resource('s3')

    md5 = hashlib.md5()

    with open(file_path, 'rb') as f:
        while chunk := f.read(8192):
            md5.update(chunk)
    
    md5_file = md5.hexdigest()

    try:
        with open(file_path, 'rb') as f_data:
            response = s3.Object(bucket_name=bucket, key=object_key).put(Body=f_data, ContentMD5=md5_file)

        return response
    except Exception as e:
        logging.error(e)
        return None
