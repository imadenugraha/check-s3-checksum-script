import logging
import os

from check_s3_checksum.create_session import create_session
from check_s3_checksum.checksum_md5 import calculate_md5
from dotenv import load_dotenv

logging.basicConfig(level=logging.INFO,
                    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    handlers=[logging.FileHandler('output.log'),
                              logging.StreamHandler()])

logger = logging.getLogger(__name__)


def upload_object(file_path: str, object_key: str):
    load_dotenv()
    bucket = os.getenv('AWS_BUCKET_NAME')

    s3 = create_session().resource('s3')

    md5_file = calculate_md5(file_path)

    try:
        logger.info(f"Upload {file_path} to bucket {bucket} starting...")
        with open(file_path, 'rb') as f_data:
            response = s3.Object(bucket_name=bucket, key=object_key).put(Body=f_data, ContentMD5=md5_file)

        logger.info(f"Upload {file_path} to bucket {bucket} finished!")
        return response
    except Exception as e:
        logger.error(e)
        return None
