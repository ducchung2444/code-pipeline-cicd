from aws_cdk import Stack, aws_ec2
from constructs import Construct
from ..configs import ASSET_DIR


class WebServerStack(Stack):
    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)
        # VPC
        my_vpc = aws_ec2.Vpc(
            self,
            "my_vpc",
            vpc_name="my-vpc",
            ip_addresses=aws_ec2.IpAddresses.cidr("10.0.0.0/16"),
            nat_gateways=0,
            max_azs=1,
        )
        # security group
        my_sg = aws_ec2.SecurityGroup(
            self,
            "my-sg",
            vpc=my_vpc,
            security_group_name="allow http traffic",
            allow_all_outbound=True,
        )
        # allow http traffic
        my_sg.add_ingress_rule(
            peer=aws_ec2.Peer.any_ipv4(),
            connection=aws_ec2.Port.tcp(80),
            description="allow http traffic",
        )
        # allow ssh access
        my_sg.add_ingress_rule(
            peer=aws_ec2.Peer.any_ipv4(),
            connection=aws_ec2.Port.tcp(22),
            description="allow ssh access",
        )
        # ec2 instance
        my_ec2 = aws_ec2.Instance(
            self,
            "my-ec2-instance",
            vpc=my_vpc,
            vpc_subnets=aws_ec2.SubnetSelection(subnet_type=aws_ec2.SubnetType.PUBLIC),
            instance_type=aws_ec2.InstanceType.of(aws_ec2.InstanceClass.T3, aws_ec2.InstanceSize.MICRO),
            machine_image=aws_ec2.AmazonLinuxImage(generation=aws_ec2.AmazonLinuxGeneration.AMAZON_LINUX_2),
            security_group=my_sg,
            key_name="my-ki-hehe", # create at `https://ap-east-1.console.aws.amazon.com/ec2/home?region=ap-east-1#KeyPairs:` if ssh is needed
        )
        my_ec2.add_user_data((ASSET_DIR / "userdata.sh").read_text())
