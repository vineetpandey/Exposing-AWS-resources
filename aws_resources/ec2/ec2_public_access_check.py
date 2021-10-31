def paginate(cache):
    response = cache.get("paginate")
    if response:
        return response
    get_paginators = ec2.get_paginator("describe_instances")
    if get_paginators:
        cache["paginate"] = get_paginators.paginate(Filters=[{'Name': 'instance-state-name','Values': ['running','stopped']}])
        return cache["paginate"]
        
        
def ec2_public_facing_check(cache: dict, awsAccountId: str, awsRegion: str, awsPartition: str) -> dict:
    """EC2 Instances should not be internet-facing"""
    
    try:
        iterator = paginate(cache=cache)
        for page in iterator:
            for r in page["Reservations"]:
                for i in r["Instances"]:
                    instanceId = str(i["InstanceId"])
                    instanceArn = (f"arn:{awsPartition}:ec2:{awsRegion}:{awsAccountId}:instance/{instanceId}")
                    instanceType = str(i["InstanceType"])
                    instanceImage = str(i["ImageId"])
                    subnetId = str(i["SubnetId"])
                    vpcId = str(i["VpcId"])
                    instanceLaunchedAt = str(i["BlockDeviceMappings"][0]["Ebs"]["AttachTime"])
                    # If the Public DNS is not empty that means there is an entry, and that is is public facing
                    if str(i["PublicDnsName"]) != "":
						print("Instance: {} is public!".format(i))

	except Exception as e:
        print(e)