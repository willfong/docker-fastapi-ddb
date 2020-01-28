# docker-fastapi-ddb

## DDB

There is no need to specify AWS credentials. dynamodb-local just needs to have a non-empty string.

Use Terraform to provision the DDB schema: `terraform apply`

Manually check tables: `aws dynamodb scan --table-name GameScores --endpoint-url http://localhost:8000`

## Google Auth
What all the keys mean
https://developers.google.com/identity/protocols/OpenIDConnect
