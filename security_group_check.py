import boto3

def check_security_groups():

    ec2 = boto3.client('ec2')

    print("\nChecking Security Groups...\n")

    response = ec2.describe_security_groups()

    issue_count = 0

    for group in response['SecurityGroups']:

        group_name = group['GroupName']

        for permission in group['IpPermissions']:

            ip_ranges = permission.get('IpRanges', [])

            for ip in ip_ranges:

                if ip.get('CidrIp') == "0.0.0.0/0":

                    port = permission.get('FromPort')

                    print(f"[MEDIUM] Security Group '{group_name}' allows public access on port {port}")

                    issue_count += 1

    return issue_count