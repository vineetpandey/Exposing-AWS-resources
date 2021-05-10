import sys
import os
# get the path from outside of directory
sys.path.append(os.path.abspath(os.path.join('..')))

from aws_resources.resources_var import *

try:
    s3 = boto3.resource('s3')
    s3_client = boto3.client('s3')
    # list all the buckets
    buckets = s3.buckets.all()
    if not buckets:
        print('No buckets as of now')
    else:
        # [print(bucket.name) for bucket in buckets]
        for bucket in buckets:
            BucketName = bucket.name
            try:
                response_policy = (s3_client.get_bucket_policy(Bucket=BucketName))
                try:
                    response_status = s3_client.get_bucket_policy_status(Bucket=BucketName)
                    #print(BucketName, '->', response_status)
                    PublicPolicyCheck = str(response_status["PolicyStatus"]["IsPublic"])
                    if PublicPolicyCheck != 'False':
                        print('*| Bucket is Public. |*')
                except Exception as ex:
                    print(ex)

            except Exception as ex:
                # print('\nBucket Policy does not exists for %s! - \n%s\n'% (bucket.name,ex))
                print('Bucket Policy does not exists for %s! \n'% (BucketName))
            
except Exception as error:
    logging.error("Error Message: ", error)

