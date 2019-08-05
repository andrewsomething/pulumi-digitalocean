# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import json
import warnings
import pulumi
import pulumi.runtime
from . import utilities, tables

class Firewall(pulumi.CustomResource):
    created_at: pulumi.Output[str]
    """
    A time value given in ISO8601 combined date and time format
    that represents when the Firewall was created.
    """
    droplet_ids: pulumi.Output[list]
    """
    The list of the IDs of the Droplets assigned
    to the Firewall.
    """
    inbound_rules: pulumi.Output[list]
    """
    The inbound access rule block for the Firewall.
    The `inbound_rule` block is documented below.
    """
    name: pulumi.Output[str]
    """
    The Firewall name
    """
    outbound_rules: pulumi.Output[list]
    """
    The outbound access rule block for the Firewall.
    The `outbound_rule` block is documented below.
    """
    pending_changes: pulumi.Output[list]
    """
    An list of object containing the fields, "droplet_id",
    "removing", and "status".  It is provided to detail exactly which Droplets
    are having their security policies updated.  When empty, all changes
    have been successfully applied.
    """
    status: pulumi.Output[str]
    """
    A status string indicating the current state of the Firewall.
    This can be "waiting", "succeeded", or "failed".
    """
    tags: pulumi.Output[list]
    """
    The names of the Tags assigned to the Firewall.
    """
    def __init__(__self__, resource_name, opts=None, droplet_ids=None, inbound_rules=None, name=None, outbound_rules=None, tags=None, __name__=None, __opts__=None):
        """
        Provides a DigitalOcean Cloud Firewall resource. This can be used to create,
        modify, and delete Firewalls.
        
        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[list] droplet_ids: The list of the IDs of the Droplets assigned
               to the Firewall.
        :param pulumi.Input[list] inbound_rules: The inbound access rule block for the Firewall.
               The `inbound_rule` block is documented below.
        :param pulumi.Input[str] name: The Firewall name
        :param pulumi.Input[list] outbound_rules: The outbound access rule block for the Firewall.
               The `outbound_rule` block is documented below.
        :param pulumi.Input[list] tags: The names of the Tags assigned to the Firewall.

        > This content is derived from https://github.com/terraform-providers/terraform-provider-digitalocean/blob/master/website/docs/r/firewall.html.markdown.
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

        __props__['droplet_ids'] = droplet_ids

        __props__['inbound_rules'] = inbound_rules

        __props__['name'] = name

        __props__['outbound_rules'] = outbound_rules

        __props__['tags'] = tags

        __props__['created_at'] = None
        __props__['pending_changes'] = None
        __props__['status'] = None

        if opts is None:
            opts = pulumi.ResourceOptions()
        if opts.version is None:
            opts.version = utilities.get_version()
        super(Firewall, __self__).__init__(
            'digitalocean:index/firewall:Firewall',
            resource_name,
            __props__,
            opts)


    def translate_output_property(self, prop):
        return tables._CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop

    def translate_input_property(self, prop):
        return tables._SNAKE_TO_CAMEL_CASE_TABLE.get(prop) or prop

