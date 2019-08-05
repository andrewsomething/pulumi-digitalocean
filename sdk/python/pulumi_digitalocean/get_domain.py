# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import json
import warnings
import pulumi
import pulumi.runtime
from . import utilities, tables

class GetDomainResult:
    """
    A collection of values returned by getDomain.
    """
    def __init__(__self__, name=None, ttl=None, urn=None, zone_file=None, id=None):
        if name and not isinstance(name, str):
            raise TypeError("Expected argument 'name' to be a str")
        __self__.name = name
        if ttl and not isinstance(ttl, float):
            raise TypeError("Expected argument 'ttl' to be a float")
        __self__.ttl = ttl
        if urn and not isinstance(urn, str):
            raise TypeError("Expected argument 'urn' to be a str")
        __self__.urn = urn
        """
        The uniform resource name of the domain
        * `zone_file`: The zone file of the domain.
        """
        if zone_file and not isinstance(zone_file, str):
            raise TypeError("Expected argument 'zone_file' to be a str")
        __self__.zone_file = zone_file
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        __self__.id = id
        """
        id is the provider-assigned unique ID for this managed resource.
        """

    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return self

    __iter__ = __await__

def get_domain(name=None,opts=None):
    """
    > This content is derived from https://github.com/terraform-providers/terraform-provider-digitalocean/blob/master/website/docs/d/domain.html.markdown.
    """
    __args__ = dict()

    __args__['name'] = name
    if opts is None:
        opts = pulumi.ResourceOptions()
    if opts.version is None:
        opts.version = utilities.get_version()
    __ret__ = pulumi.runtime.invoke('digitalocean:index/getDomain:getDomain', __args__, opts=opts).value

    return GetDomainResult(
        name=__ret__.get('name'),
        ttl=__ret__.get('ttl'),
        urn=__ret__.get('urn'),
        zone_file=__ret__.get('zoneFile'),
        id=__ret__.get('id'))
