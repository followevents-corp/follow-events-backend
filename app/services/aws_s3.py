import boto3
import os
import logging
from botocore.exceptions import ClientError


class AWS_S3:
    bucket = 'follow-events'
    url = 'https://follow-events.s3.amazonaws.com/'

    @classmethod
    def upload_file(cls, file_name, object_name=None):
        if object_name is None:
            object_name = os.path.basename(file_name)

        s3_client = boto3.client('s3')
        try:
            type_banner = "".join(file_name.filename).replace(" ","") # pegar o tipo de um arquivo!
            name = object_name + "." + type_banner 
            s3_client.upload_fileobj(file_name, cls.bucket, name)
        except ClientError as e:
            logging.error(e)
            return False
        return f'{cls.url}{name}'