import logging
import os
import re
from uuid import uuid4

import boto3
from botocore.exceptions import ClientError


class AWS_S3:
    bucket = "follow-events"
    url = "https://follow-events.s3.amazonaws.com/"

    @classmethod
    def upload_file(cls, file_name):
        s3_client = boto3.client("s3", aws_secret_access_key=os.environ["AWS_SECRET_ACCESS_KEY"] , aws_access_key_id=os.environ["AWS_ACCESS_KEY_ID"])
        try:
            id = uuid4()
            type_banner = file_name.content_type.split("/")
            name = str(id) + "." + type_banner[1]
            s3_client.upload_fileobj(file_name, cls.bucket, name)
        except ClientError as e:
            logging.error(e)
            return False
        return f"{cls.url}{name}", type_banner[0]
