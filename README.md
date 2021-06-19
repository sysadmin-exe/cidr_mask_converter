## Application Overview

You need to complete a functionality in our API that provides some help to
the networking team.

The API has 3 missing endpoints, the first endpoint converts Subnet Mast to
CIDR format, the second endpoint return the CIDR value of a given Subnet Mask
and finally the third endpoint simply validates an IPv4.

e.g.

```
curl localhost/cidr-to-mask?value=24
{
  "function": "cidrToMask",
  "input": "24",
  "output": "255.255.255.0"
}
```

```
curl localhost/mask-to-cidr?value=255.255.0.0
{
  "function": "maskToCidr",
  "input": "255.255.0.0",
  "output": "16"
}

```

```
curl localhost/ip-validation?value=255.255.0.0
{
  "function": "ipv4Validation",
  "input": "255.255.0.0",
  "output": true
}

```# cidr_mask_converter
