# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import json
import warnings
import pulumi
import pulumi.runtime
from . import utilities, tables

class SpacesBucket(pulumi.CustomResource):
    acl: pulumi.Output[str]
    """
    Canned ACL applied on bucket creation (`private` or `public-read`)
    """
    bucket_domain_name: pulumi.Output[str]
    """
    The FQDN of the bucket (e.g. bucket-name.nyc3.digitaloceanspaces.com)
    """
    force_destroy: pulumi.Output[bool]
    """
    Unless `true`, the bucket will only be destroyed if empty (Defaults to `false`)
    """
    name: pulumi.Output[str]
    """
    The name of the bucket
    """
    region: pulumi.Output[str]
    """
    The region where the bucket resides (Defaults to `nyc3`)
    """
    urn: pulumi.Output[str]
    """
    The uniform resource name for the bucket
    """
    def __init__(__self__, resource_name, opts=None, acl=None, force_destroy=None, name=None, region=None, __name__=None, __opts__=None):
        """
        Provides a bucket resource for Spaces, DigitalOcean's object storage product.
        
        The [Spaces API](https://developers.digitalocean.com/documentation/spaces/) was
        designed to be interoperable with Amazon's AWS S3 API. This allows users to
        interact with the service while using the tools they already know. Spaces
        mirrors S3's authentication framework and requests to Spaces require a key pair
        similar to Amazon's Access ID and Secret Key.
        
        The authentication requirement can be met by either setting the
        `SPACES_ACCESS_KEY_ID` and `SPACES_SECRET_ACCESS_KEY` environment variables or
        the provider's `spaces_access_id` and `spaces_secret_key` arguments to the
        access ID and secret you generate via the DigitalOcean control panel. For
        example:
        
        
        For more information, See [An Introduction to DigitalOcean Spaces](https://www.digitalocean.com/community/tutorials/an-introduction-to-digitalocean-spaces)
        
        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] acl: Canned ACL applied on bucket creation (`private` or `public-read`)
        :param pulumi.Input[bool] force_destroy: Unless `true`, the bucket will only be destroyed if empty (Defaults to `false`)
        :param pulumi.Input[str] name: The name of the bucket
        :param pulumi.Input[str] region: The region where the bucket resides (Defaults to `nyc3`)
        """
        if __name__ is not None:
            warnings.warn("explicit use of __name__ is deprecated", DeprecationWarning)
            resource_name = __name__
        if __opts__ is not None:
            warnings.warn("explicit use of __opts__ is deprecated, use 'opts' instead", DeprecationWarning)
            opts = __opts__
        if not resource_name:
            raise TypeError('Missing resource name argument (for URN creation)')
        if not isinstance(resource_name, str):
            raise TypeError('Expected resource name to be a string')
        if opts and not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')

        __props__ = dict()

        __props__['acl'] = acl

        __props__['force_destroy'] = force_destroy

        __props__['name'] = name

        __props__['region'] = region

        __props__['bucket_domain_name'] = None
        __props__['urn'] = None

        super(SpacesBucket, __self__).__init__(
            'digitalocean:index/spacesBucket:SpacesBucket',
            resource_name,
            __props__,
            opts)


    def translate_output_property(self, prop):
        return tables._CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop

    def translate_input_property(self, prop):
        return tables._SNAKE_TO_CAMEL_CASE_TABLE.get(prop) or prop

