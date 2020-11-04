import logging
import boto3
from botocore.exceptions import ClientError

def list_objects_v2(bucket_name):
    s3_client = boto3.client('s3')
    response = s3_client.list_objects_v2(
        Bucket = bucket_name
    )
    
    if response['KeyCount'] != 0:
          for content in response['Contents']:
            object_key = content['Key']
            object_size = content['Size']
            object_last_modified = content['LastModified']
            print(object_key, " ", object_size, " ", object_last_modified)

def main():
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument('bucket_name', help='The name of the bucket.')
  
    region = 'us-east-1'
  
    args = parser.parse_args()
    list_objects_v2(args.bucket_name)
  

if __name__ == '__main__':
 main()
 
 
