
import imp
import json
from django.shortcuts import render
from django.http import HttpResponse
# from django.shortcuts import HttpResponse

# import shared info modules that provides common data for all aws services
from .shared_info.resources import *
from .shared_info.variables import *

# Create your views here.
x="Hello from AWS!"

def s3_public_check(request):
    s3_info = []
    try:
        s3 = boto3.resource('s3')
        s3_client = boto3.client('s3')
        # list all the buckets
        buckets = s3.buckets.all()
        # print(buckets)
        if not buckets:
            Bucket_info = ''
            visibility_info = ''
            print('No buckets as of now')
            s3_info.append(
                {
                    'bucket': Bucket_info,
                    'visibility': visibility_info
                }
            )
        else:
            # [print(bucket.name) for bucket in buckets]
            for bucket in buckets:
                BucketName = bucket.name
                # print(BucketName, '->', BucketName)
                try:
                    # print('Enter 1-try')
                    response_policy = s3_client.get_bucket_policy(Bucket=BucketName)
                    # print(BucketName, '->', response_policy)
                    try:
                        response_status = s3_client.get_bucket_policy_status(Bucket=BucketName)
                        # print(BucketName, '->', response_status)
                        PublicPolicyCheck = str(response_status["PolicyStatus"]["IsPublic"])
                        if PublicPolicyCheck != 'False':
                            print('*| Bucket is Public. |*')
                            visibility_info = 'Public'
                            s3_info.append(
                                {
                                    'bucket': BucketName,
                                    'visibility': visibility_info
                                }
                            )
                
                        # else:
                        #     print('*| Bucket is Not Public. |*')
                    except Exception as ex:
                        print(ex)

                except Exception as ex:
                    # print('\nBucket Policy does not exists for %s! - \n%s\n'% (bucket.name,ex))
                    s3_policy_info = 'Bucket Policy does not exists for {}! \n'.format(BucketName)
                    print(s3_policy_info)
                    s3_info.append(
                        {
                            'bucket': BucketName,
                            'visibility': s3_policy_info
                        }
                    )

                context = {
                    'data': s3_info
                }
                return render(request, 's3.html', context)

    except Exception as error:
        logging.error("Error Message: ", error)

