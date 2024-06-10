import logging
from os import getenv

from boto3 import Session
from botocore.exceptions import (
    EndpointConnectionError,
    NoCredentialsError,
    PartialCredentialsError,
)
from dotenv import load_dotenv

logging.basicConfig(
    level=logging.ERROR, format="%(asctime)s - %(levelname)s - %(message)s"
)


def create_session():
    load_dotenv(".env")

    access_key = getenv("AWS_ACCESS_KEY")
    secret_key = getenv("AWS_SECRET_KEY")
    region = getenv("AWS_REGION")

    if not all([access_key, secret_key, region]):
        logging.error("Please set credential on .env file!")
        return None

    try:
        session = Session(
            aws_access_key_id=access_key,
            aws_secret_access_key=secret_key,
            region_name=region,
        )
        return session

    except NoCredentialsError as no_cred:
        logging.error(no_cred)
        print("Please set the credential!")
    except PartialCredentialsError as partial_cred_err:
        logging.error(partial_cred_err)
        print("Partial credential is not valid!")
    except EndpointConnectionError as endpoint_err:
        logging.error(endpoint_err)
        print("Cannot connect to AWS!")
    except Exception as err:
        logging.error(err)
        print(f"Something happened!: {err}")
