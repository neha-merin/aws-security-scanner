from s3_check import check_public_buckets
from security_group_check import check_security_groups

print("AWS Security Misconfiguration Scanner")
print("--------------------------------------")

s3_issues = check_public_buckets()

sg_issues = check_security_groups()

print("\nScan Summary")
print("-------------")

print(f"S3 Issues: {s3_issues}")
print(f"Security Group Issues: {sg_issues}")