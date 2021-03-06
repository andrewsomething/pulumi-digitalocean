# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import json
import warnings
import pulumi
import pulumi.runtime
from typing import Union
from . import utilities, tables

class GetVpcResult:
    """
    A collection of values returned by getVpc.
    """
    def __init__(__self__, created_at=None, default=None, description=None, id=None, ip_range=None, name=None, region=None, urn=None):
        if created_at and not isinstance(created_at, str):
            raise TypeError("Expected argument 'created_at' to be a str")
        __self__.created_at = created_at
        """
        The date and time of when the VPC was created.
        """
        if default and not isinstance(default, bool):
            raise TypeError("Expected argument 'default' to be a bool")
        __self__.default = default
        """
        A boolean indicating whether or not the VPC is the default one for the region.
        """
        if description and not isinstance(description, str):
            raise TypeError("Expected argument 'description' to be a str")
        __self__.description = description
        """
        A free-form text field describing the VPC.
        """
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        __self__.id = id
        """
        The unique identifier for the VPC.
        """
        if ip_range and not isinstance(ip_range, str):
            raise TypeError("Expected argument 'ip_range' to be a str")
        __self__.ip_range = ip_range
        """
        The range of IP addresses for the VPC in CIDR notation.
        """
        if name and not isinstance(name, str):
            raise TypeError("Expected argument 'name' to be a str")
        __self__.name = name
        """
        The name of the VPC.
        """
        if region and not isinstance(region, str):
            raise TypeError("Expected argument 'region' to be a str")
        __self__.region = region
        """
        The DigitalOcean region slug for the VPC's location.
        """
        if urn and not isinstance(urn, str):
            raise TypeError("Expected argument 'urn' to be a str")
        __self__.urn = urn
        """
        The uniform resource name (URN) for the VPC.
        """
class AwaitableGetVpcResult(GetVpcResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetVpcResult(
            created_at=self.created_at,
            default=self.default,
            description=self.description,
            id=self.id,
            ip_range=self.ip_range,
            name=self.name,
            region=self.region,
            urn=self.urn)

def get_vpc(id=None,name=None,region=None,opts=None):
    """
    Use this data source to access information about an existing resource.

    :param str id: The unique identifier of an existing VPC.
    :param str name: The name of an existing VPC.
    :param str region: The DigitalOcean region slug for the VPC's location.
    """
    __args__ = dict()


    __args__['id'] = id
    __args__['name'] = name
    __args__['region'] = region
    if opts is None:
        opts = pulumi.InvokeOptions()
    if opts.version is None:
        opts.version = utilities.get_version()
    __ret__ = pulumi.runtime.invoke('digitalocean:index/getVpc:getVpc', __args__, opts=opts).value

    return AwaitableGetVpcResult(
        created_at=__ret__.get('createdAt'),
        default=__ret__.get('default'),
        description=__ret__.get('description'),
        id=__ret__.get('id'),
        ip_range=__ret__.get('ipRange'),
        name=__ret__.get('name'),
        region=__ret__.get('region'),
        urn=__ret__.get('urn'))
