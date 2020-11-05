import logging
import boto3
import json
from botocore.exceptions import ClientError

def detect(bucket_name, file_name):
    client = boto3.client('rekognition')
    response = client.detect_labels(
        Image={
            'S3Object': {
                'Bucket': bucket_name,
                'Name': file_name,
            },
        },
        MaxLabels=123,
        MinConfidence=90,
    )

    print(response)


def main():
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument('bucket_name', help='The name of the bucket.')
    parser.add_argument('--file_name', help='The name of the file to upload.')
    
    region = 'us-east-1'
  
    args = parser.parse_args()
    # list_objects_v2(args.bucket_name, args.file_name)
    detect(args.bucket_name, args.file_name)
  

if __name__ == '__main__':
 main()
 
 
