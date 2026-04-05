import boto3

def check_public_buckets():

    s3 = boto3.client('s3')
    buckets = s3.list_buckets()

    print("\nChecking S3 buckets...\n")

    issue_count = 0

    for bucket in buckets['Buckets']:

        bucket_name = bucket['Name']

        try:
            acl = s3.get_bucket_acl(Bucket=bucket_name)

            for grant in acl['Grants']:

                grantee = grant.get('Grantee', {})

                if grantee.get('URI') == "http://acs.amazonaws.com/groups/global/AllUsers":

                    print(f"[HIGH] Public S3 Bucket Detected: {bucket_name}")
                    issue_count += 1

        except Exception as e:

            print(f"Could not check bucket {bucket_name}: {e}")

    return issue_count