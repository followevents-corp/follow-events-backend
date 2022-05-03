import logging
import os
from uuid import uuid4

import boto3
import dotenv
from botocore.exceptions import ClientError

dotenv.load_dotenv()


class AWS_S3:
    bucket = "follow-events"
    url = "https://follow-events.s3.amazonaws.com/"
    s3_client = boto3.client(
        "s3",
        aws_secret_access_key=os.getenv("AWS_SECRET_ACCESS_KEY"),
        aws_access_key_id=os.getenv("AWS_ACCESS_KEY_ID"),
    )

    @classmethod
    def upload_file(cls, file):

        try:
            id = uuid4()
            type_banner = file.content_type.split("/")
            name = str(id) + "." + type_banner[1]
            cls.s3_client.upload_fileobj(file, cls.bucket, name)
        except ClientError as e:
            logging.error(e)
            return False
        return f"{cls.url}{name}", type_banner[0]

    @classmethod
    def delete_file(cls, key):
        cls.s3_client.delete_object(Bucket=cls.bucket, Key=key)
