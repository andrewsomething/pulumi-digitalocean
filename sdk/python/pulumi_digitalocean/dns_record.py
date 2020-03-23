# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import json
import warnings
import pulumi
import pulumi.runtime
from typing import Union
from . import utilities, tables

class DnsRecord(pulumi.CustomResource):
    domain: pulumi.Output[str]
    """
    The domain to add the record to.
    """
    flags: pulumi.Output[float]
    """
    The flags of the record. Only valid when type is `CAA`. Must be between 0 and 255.
    """
    fqdn: pulumi.Output[str]
    """
    The FQDN of the record
    """
    name: pulumi.Output[str]
    """
    The name of the record. Use `@` for records on domain's name itself.
    """
    port: pulumi.Output[float]
    """
    The port of the record. Only valid when type is `SRV`.  Must be between 1 and 65535.
    """
    priority: pulumi.Output[float]
    """
    The priority of the record. Only valid when type is `MX` or `SRV`. Must be between 0 and 65535.
    """
    tag: pulumi.Output[str]
    """
    The tag of the record. Only valid when type is `CAA`. Must be one of `issue`, `issuewild`, or `iodef`.
    """
    ttl: pulumi.Output[float]
    """
    The time to live for the record, in seconds. Must be at least 0.
    """
    type: pulumi.Output[str]
    """
    The type of record. Must be one of `A`, `AAAA`, `CAA`, `CNAME`, `MX`, `NS`, `TXT`, or `SRV`.
    """
    value: pulumi.Output[str]
    """
    The value of the record.
    """
    weight: pulumi.Output[float]
    """
    The weight of the record. Only valid when type is `SRV`.  Must be between 0 and 65535.
    """
    def __init__(__self__, resource_name, opts=None, domain=None, flags=None, name=None, port=None, priority=None, tag=None, ttl=None, type=None, value=None, weight=None, __props__=None, __name__=None, __opts__=None):
        """
        Provides a DigitalOcean DNS record resource.

        > This content is derived from https://github.com/terraform-providers/terraform-provider-digitalocean/blob/master/website/docs/r/record.html.markdown.

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] domain: The domain to add the record to.
        :param pulumi.Input[float] flags: The flags of the record. Only valid when type is `CAA`. Must be between 0 and 255.
        :param pulumi.Input[str] name: The name of the record. Use `@` for records on domain's name itself.
        :param pulumi.Input[float] port: The port of the record. Only valid when type is `SRV`.  Must be between 1 and 65535.
        :param pulumi.Input[float] priority: The priority of the record. Only valid when type is `MX` or `SRV`. Must be between 0 and 65535.
        :param pulumi.Input[str] tag: The tag of the record. Only valid when type is `CAA`. Must be one of `issue`, `issuewild`, or `iodef`.
        :param pulumi.Input[float] ttl: The time to live for the record, in seconds. Must be at least 0.
        :param pulumi.Input[str] type: The type of record. Must be one of `A`, `AAAA`, `CAA`, `CNAME`, `MX`, `NS`, `TXT`, or `SRV`.
        :param pulumi.Input[str] value: The value of the record.
        :param pulumi.Input[float] weight: The weight of the record. Only valid when type is `SRV`.  Must be between 0 and 65535.
        """
        if __name__ is not None:
            warnings.warn("explicit use of __name__ is deprecated", DeprecationWarning)
            resource_name = __name__
        if __opts__ is not None:
            warnings.warn("explicit use of __opts__ is deprecated, use 'opts' instead", DeprecationWarning)
            opts = __opts__
        if opts is None:
            opts = pulumi.ResourceOptions()
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.version is None:
            opts.version = utilities.get_version()
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = dict()

            if domain is None:
                raise TypeError("Missing required property 'domain'")
            __props__['domain'] = domain
            __props__['flags'] = flags
            __props__['name'] = name
            __props__['port'] = port
            __props__['priority'] = priority
            __props__['tag'] = tag
            __props__['ttl'] = ttl
            if type is None:
                raise TypeError("Missing required property 'type'")
            __props__['type'] = type
            if value is None:
                raise TypeError("Missing required property 'value'")
            __props__['value'] = value
            __props__['weight'] = weight
            __props__['fqdn'] = None
        super(DnsRecord, __self__).__init__(
            'digitalocean:index/dnsRecord:DnsRecord',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name, id, opts=None, domain=None, flags=None, fqdn=None, name=None, port=None, priority=None, tag=None, ttl=None, type=None, value=None, weight=None):
        """
        Get an existing DnsRecord resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param str id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] domain: The domain to add the record to.
        :param pulumi.Input[float] flags: The flags of the record. Only valid when type is `CAA`. Must be between 0 and 255.
        :param pulumi.Input[str] fqdn: The FQDN of the record
        :param pulumi.Input[str] name: The name of the record. Use `@` for records on domain's name itself.
        :param pulumi.Input[float] port: The port of the record. Only valid when type is `SRV`.  Must be between 1 and 65535.
        :param pulumi.Input[float] priority: The priority of the record. Only valid when type is `MX` or `SRV`. Must be between 0 and 65535.
        :param pulumi.Input[str] tag: The tag of the record. Only valid when type is `CAA`. Must be one of `issue`, `issuewild`, or `iodef`.
        :param pulumi.Input[float] ttl: The time to live for the record, in seconds. Must be at least 0.
        :param pulumi.Input[str] type: The type of record. Must be one of `A`, `AAAA`, `CAA`, `CNAME`, `MX`, `NS`, `TXT`, or `SRV`.
        :param pulumi.Input[str] value: The value of the record.
        :param pulumi.Input[float] weight: The weight of the record. Only valid when type is `SRV`.  Must be between 0 and 65535.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = dict()

        __props__["domain"] = domain
        __props__["flags"] = flags
        __props__["fqdn"] = fqdn
        __props__["name"] = name
        __props__["port"] = port
        __props__["priority"] = priority
        __props__["tag"] = tag
        __props__["ttl"] = ttl
        __props__["type"] = type
        __props__["value"] = value
        __props__["weight"] = weight
        return DnsRecord(resource_name, opts=opts, __props__=__props__)
    def translate_output_property(self, prop):
        return tables._CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop

    def translate_input_property(self, prop):
        return tables._SNAKE_TO_CAMEL_CASE_TABLE.get(prop) or prop

