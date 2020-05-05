# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import json
import warnings
import pulumi
import pulumi.runtime
from typing import Union
from . import utilities, tables

class Provider(pulumi.ProviderResource):
    def __init__(__self__, resource_name, opts=None, api_endpoint=None, spaces_access_id=None, spaces_endpoint=None, spaces_secret_key=None, token=None, __props__=None, __name__=None, __opts__=None):
        """
        The provider type for the digitalocean package. By default, resources use package-wide configuration
        settings, however an explicit `Provider` instance may be created and passed during resource
        construction to achieve fine-grained programmatic control over provider settings. See the
        [documentation](https://www.pulumi.com/docs/reference/programming-model/#providers) for more information.

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] api_endpoint: The URL to use for the DigitalOcean API.
        :param pulumi.Input[str] spaces_access_id: The access key ID for Spaces API operations.
        :param pulumi.Input[str] spaces_endpoint: The URL to use for the DigitalOcean Spaces API.
        :param pulumi.Input[str] spaces_secret_key: The secret access key for Spaces API operations.
        :param pulumi.Input[str] token: The token key for API operations.
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

            if api_endpoint is None:
                api_endpoint = (utilities.get_env('DIGITALOCEAN_API_URL') or 'https://api.digitalocean.com')
            __props__['api_endpoint'] = api_endpoint
            if spaces_access_id is None:
                spaces_access_id = utilities.get_env('SPACES_ACCESS_KEY_ID')
            __props__['spaces_access_id'] = spaces_access_id
            if spaces_endpoint is None:
                spaces_endpoint = utilities.get_env('SPACES_ENDPOINT_URL')
            __props__['spaces_endpoint'] = spaces_endpoint
            if spaces_secret_key is None:
                spaces_secret_key = utilities.get_env('SPACES_SECRET_ACCESS_KEY')
            __props__['spaces_secret_key'] = spaces_secret_key
            if token is None:
                token = utilities.get_env('DIGITALOCEAN_TOKEN')
            __props__['token'] = token
        super(Provider, __self__).__init__(
            'digitalocean',
            resource_name,
            __props__,
            opts)

    def translate_output_property(self, prop):
        return tables._CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop

    def translate_input_property(self, prop):
        return tables._SNAKE_TO_CAMEL_CASE_TABLE.get(prop) or prop

