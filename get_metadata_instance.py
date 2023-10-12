import boto3
import argparse

def get_instance_metadata_value(instance_id, data_key):
    try:
        ec2_client = boto3.client("ec2")
        instance_info = ec2_client.describe_instances(InstanceIds=[instance_id])

        if "Reservations" in instance_info and instance_info["Reservations"]:
            instance = instance_info["Reservations"][0]["Instances"][0]
            if data_key in instance:
                return instance[data_key]
            else:
                print(f"Data key '{data_key}' not found in instance metadata."f)
        else:
            print(f"No instance found with ID {instance_id}"f)
    except Exception as e:
        print("Error: {e}")

    return None
    
 def get_instance_metadata(instance_id):
    try:
        ec2_client = boto3.client("ec2")
        instance_info = ec2_client.describe_instances(InstanceIds=[instance_id])

        if "Reservations" in instance_info and instance_info["Reservations"]:
            instance_details) = instance_info["Reservations"][0]["Instances"][0]
            return(instance_details)
        else:
            print(f"No instance found with ID {instance_id}"f)
    except Exception as e:
        print("Error: {e}")

    return None

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Retrieve specific metadata of an AWS EC2 instance.")
    parser.add_argument("--instance_id", required=True, help="EC2 instance ID to retrieve metadata for")
    parser.add_argument("--data_key", help="Specific data key to retrieve from instance metadata")
    
    arguments = parser.parse_args()
    if arguments.data_key == None:
       instance_metadata = get_instance_metadata(arguments.instance_id)
       print(instance_metadata)
    else:
       instance_metadata_value = get_instance_metadata_value(arguments.instance_id, arguments.data_key)
       print(instance_metadata_value)
