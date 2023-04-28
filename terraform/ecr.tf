provider "aws" {
  region = "eu-central-1"
}


resource "aws_ecr_repository" "my_repo" {
  name = "tf-training-dev-ecr-java"

# encryption_configuration {
#     encryption_type = "AES256"
#   }

  image_tag_mutability = "MUTABLE"

  image_scanning_configuration {
    scan_on_push = true
  }
}

resource "aws_ecr_repository" "my_repo_python" {
  name = "tf-training-dev-ecr-python"

# encryption_configuration {
#     encryption_type = "AES256"
#   }

  image_tag_mutability = "MUTABLE"

  image_scanning_configuration {
    scan_on_push = true
  }
}

# resource "aws_ecr_lifecycle_policy" "my_repo_lifecycle" {
#   repository = aws_ecr_repository.my_repo.name
# lifecycle_policy = jsonencode({
#   rules = [{
#     rulePriority = 1,
#     description = "Expire untagged images older than 14 days",
#     selection = {
#       tagStatus = "untagged",
#       countType = "sinceImagePushed",
#       countUnit = "days",
#       countNumber = 14
#     },
#     action = {
#       type = "expire"
#     }
#   }]
# })
# }
