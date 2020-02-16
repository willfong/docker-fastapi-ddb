# Docker // FastAPI // Vue // DynamoDB

This is a template repository for an opinionated proof-of-concept architecture.

## Guiding Principles

- Local development - The entire infrastrucutre must easily run locally for end-to-end testing
- Cloud deployment - We're focused on AWS-specifics here

## Getting Started

1. https://github.com/willfong/docker-fastapi-ddb/generate to create your own copy of this template




## Vue

Start with: `npm install`
Build with: `npm run build; cp -r dist/* ../static`


## DynamoDB Notes

There is no need to specify AWS credentials. dynamodb-local just needs to have a non-empty string.

Use Terraform to provision the DDB schema: `terraform apply -auto-approve`

Manually check tables: `aws dynamodb scan --table-name Users --endpoint-url http://localhost:8000`

## Google Auth
What all the keys mean
https://developers.google.com/identity/protocols/OpenIDConnect


## Production Deployment Notes
```
docker run -it --rm --name certbot \
    -p 80:80 \
    -v "${PWD}/data/certbot/conf/:/etc/letsencrypt" \
    -v "${PWD}/data/certbot/lib/:/var/lib/letsencrypt" \
    -v "${PWD}/data/certbot/www/:/www" \
    --name initcert \
    certbot/certbot certonly
```