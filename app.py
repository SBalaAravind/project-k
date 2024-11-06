instance = ec2.create_instances(
    ImageId='ami-xxxxxxxxxxxxxxxxx',  # Replace with a valid AMI ID
    MinCount=1,
    MaxCount=1,
    InstanceType='t2.micro',
    KeyName='my-key-pair'  # Replace with your EC2 key pair
)

