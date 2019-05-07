# cloudConfigChecker

Usage:

POST a completed deployment to the API:

curl -H "Content-Type: application/json" -X POST -d '{"DeploymentName":"Deploy-2","Status":"Done"}' http://servername/deploymentpush

GET Status of Deployment:

http://servername/deployments/<deployment name>
  

Returns:

If a deployment recoord does not exist you will receive:
  {"status": "Not Done"} with a return code of 210 UNKNOWN
  
If a deployment record exists you will receive:
  {"status": "Done"} with a return code of 200 OK
  
On successful POST you will receive:
  {"status": "success"} with a return code of 201 CREATED
