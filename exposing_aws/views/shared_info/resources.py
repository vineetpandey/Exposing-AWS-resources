from .variables import *


def get_regions(session):
    client = session.client('ec2')
    regions = client.describe_regions()
    return [
        region['RegionName']
        for region in regions['Regions']
    ]

def main():
    data = []
    parser = argparse.ArgumentParser(description="Analyse reserved instances")
    parser.add_argument("--profile", nargs="+", help="Specify AWS profile(s) (stored in ~/.aws/credentials) for the program to use")
    parser.add_argument("-o", nargs="?", help="Specify output csv file")
    parser.add_argument("--profiles-all", nargs="?", help="Run it on all profile")
    aws_access_key = os.environ.get('AWS_ACCESS_KEY_ID')
    aws_secret_key = os.environ.get('AWS_SECRET_ACCESS_KEY')
    aws_region = os.environ.get('AWS_DEFAULT_REGION')
    args = vars(parser.parse_args())
    if 'profiles-all' in args:
        keys = init()
    elif 'profile' in args and args['profile']:
        keys = args['profile']
    else:
        keys = init()
    
    for key in keys:
        print('Processing %s...' % key)
        try:
            if aws_secret_key and aws_access_key and aws_region:
                session = boto3.Session(aws_access_key_id = aws_access_key, aws_secret_key_id = aws_secret_key, region_name = aws_region)
            else:
                session = boto3.Session(profile_name = key)
            
            regions = get_regions(session)
            print(regions)

        except botocore.exceptions.ClientError as error:
            print(error)


# if __name__ == __main__:
#     main()
main()