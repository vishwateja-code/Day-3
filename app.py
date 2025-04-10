import boto3

# Initialize EC2 resource
ec2 = boto3.resource('ec2')

# Define the parameters for the EC2 instance
instances = ec2.create_instances(
    ImageId='ami-076c6dbba59aa92e6', # Amazon Linux 2 AMI
    InstanceType='t2.micro',  # Instance type (t2.micro is free tier eligible)
    MinCount=1,
    MaxCount=1,
    KeyName='dev' # Your key pair name


)
