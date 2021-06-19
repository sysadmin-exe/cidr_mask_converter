# Application Overview

This is an api that converts CIDR to Subnet mask values and vice versa as well as validating IP address values.

The Dockerfile will deploy the python code to an image.

The image can be run locally and tested like below

e.g.

```
curl localhost:8000/cidr-to-mask?value=24
{
  "function": "cidrToMask",
  "input": "24",
  "output": "255.255.255.0"
}
```

```
curl localhost:8000/mask-to-cidr?value=255.255.0.0
{
  "function": "maskToCidr",
  "input": "255.255.0.0",
  "output": "16"
}

```

```
curl localhost:8000/ip-validation?value=255.255.0.0
{
  "function": "ipv4Validation",
  "input": "255.255.0.0",
  "output": true
}

```
## Code test
To test the code run the test file with Python3.

## CI/CD
Jenkins will be used for the pipeline and can be changed to learn other tools. Pipeline should only work on the MASTER branch and pull requests to the master branch. 

## Branching and GitOps
Production/Deployment branch is the MASTER branch. Changes to code should be done on a different branch and the branch to be merged master branch via a Pull Requests.

## Deployment
The image will be deployed into a server and the port exposed to allow the app accessible over server IP address.