"""An AliCloud Python Pulumi program"""

import pulumi
import pulumi_alicloud as alicloud

stack = pulumi.get_stack()
# Create an RAM Role to run auto cert serverless functions.
role = alicloud.ram.Role(f"{stack}-fc-auto-cert",
                        document="""
                        {
                            "Statement": [
                                {
                                "Action": "sts:AssumeRole",
                                "Effect": "Allow",
                                "Principal": {
                                    "Service": [
                                    "fc.aliyuncs.com"
                                    ]
                                }
                                }
                            ],
                            "Version": "1"
                            }
                        """, force=True)


# Export the name of the bucket
pulumi.export('role_arn: ', role.arn)
