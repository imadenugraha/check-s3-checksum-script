import logging
from os import getenv

from boto3 import Session
from dotenv import load_dotenv

logging.basicConfig(level=logging.INFO, 
                    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
                    handlers=[logging.FileHandler('output.log'),
                              logging.StreamHandler()]
)

logger = logging.getLogger(__name__)


def create_session() -> Session:
    load_dotenv(".env")

    access_key = getenv("AWS_ACCESS_KEY")
    secret_key = getenv("AWS_SECRET_KEY")
    region = getenv("AWS_REGION")

    if not all([access_key, secret_key, region]):
        logger.error("Please set credential on .env file!")
        return None

    try:
        logger.info('Creating session...')
        session = Session(
            aws_access_key_id=access_key,
            aws_secret_access_key=secret_key,
            region_name=region,
        )
        
        logger.info('Session has been created!')
        return session

    except Exception as err:
        logger.error(err)
        return None
