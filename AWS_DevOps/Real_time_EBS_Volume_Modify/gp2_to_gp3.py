import json
import boto3

def get_volume_id(ebs_arn):
    arn_parts = ebs_arn.split(':')
    volume_id = arn_parts[-1].split('/')[-1]
    return volume_id
    

def lambda_handler(event, context):
   
    print("volume created")
    
    ebs_arn= event['resources'][0]
    volume_id=get_volume_id(ebs_arn)
    
    
    client=boto3.client('ec2')
    
    response = client.modify_volume(
    VolumeId=volume_id,
    VolumeType='gp3',