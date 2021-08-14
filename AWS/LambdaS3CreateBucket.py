# Lambda Function for Create S3 buckets

import boto3, os, time

AWS_DEFAULT_REGION = "us-east-2" #Region where Lambda Running
os.environ['AWS_DEFAULT_REGION'] = AWS_DEFAULT_REGION

bucketname = "lambda.created.me.on-" + str(time.time())

mys3 = boto3.client('s3')
try:
    results = mys3.create_bucket(
                            Bucket = bucketname,
                            CreateBucketConfiguration = {'LocationConstraint': AWS_DEFAULT_REGION}
    )
    print("<h1><font color=green>S3 Bucket Created Successfully:</font><h1><br><br>" + str(results))
except:
    print("<h1><font color=green>Error!</font><h1><br><br>")
