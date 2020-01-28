resource "aws_dynamodb_table" "users" {
  name           = "users"
  billing_mode   = "PROVISIONED"
  read_capacity  = 20
  write_capacity = 20
  hash_key       = "id"

  attribute {
    name = "id"
    type = "S"
  }

  attribute {
    name = "oauth_source"
    type = "S"
  }

  attribute {
    name = "oauth_payload"
    type = "S"
  }

  attribute {
    name = "full_name"
    type = "S"
  }

  attribute {
    name = "picture_url"
    type = "S"
  }

  attribute {
    name = "email"
    type = "S"
  }

}



resource "aws_dynamodb_table" "basic-dynamodb-table" {
  name           = "GameScores"
  billing_mode   = "PROVISIONED"
  read_capacity  = 20
  write_capacity = 20
  hash_key       = "UserID"
  range_key      = "GameTitle"

  attribute {
    name = "UserID"
    type = "S"
  }

  attribute {
    name = "GameTitle"
    type = "S"
  }

  ttl {
    attribute_name = "TimeToExist"
    enabled        = false
  }

  tags = {
    Name        = "dynamodb-table-1"
    Environment = "production"
  }
}
