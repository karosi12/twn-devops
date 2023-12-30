terraform {
  backend "s3" {
    bucket = "demo-twn"
    key    = "myapp/state.tfstate"
    region = "eu-central-1"
  }
}

module "eks" {
  source  = "terraform-aws-modules/eks/aws"
  version = "19.20.0"

  cluster_name = "myapp-eks-cluster"
  cluster_version = "1.27"

  subnet_ids = module.myapp-vpc.private_subnets
  vpc_id = module.myapp-vpc.vpc_id
  cluster_endpoint_public_access = true
  eks_managed_node_groups = {
    dev = {
      min_size     = 1
      max_size     = 3
      desired_size = 3

      instance_types = ["t2.small"]
    }
  }

  fargate_profiles = {
    default = {
      name = "default"
      selectors = [
        {
          namespace = "default"
        }
      ]
    }
  }

  tags = {
    environment = "development"
    application = "myapp"
  }
}