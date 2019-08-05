# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import json
import warnings
import pulumi
import pulumi.runtime
from . import utilities, tables

class KubernetesCluster(pulumi.CustomResource):
    cluster_subnet: pulumi.Output[str]
    """
    The range of IP addresses in the overlay network of the Kubernetes cluster.
    """
    created_at: pulumi.Output[str]
    """
    The date and time when the Kubernetes cluster was created.
    """
    endpoint: pulumi.Output[str]
    """
    The base URL of the API server on the Kubernetes master node.
    """
    ipv4_address: pulumi.Output[str]
    """
    The public IPv4 address of the Kubernetes master node.
    """
    kube_configs: pulumi.Output[list]
    name: pulumi.Output[str]
    """
    A name for the Kubernetes cluster.
    """
    node_pool: pulumi.Output[dict]
    """
    A block representing the cluster's default node pool. Additional node pools may be added to the cluster using the `digitalocean_kubernetes_node_pool` resource. The following arguments may be specified:
    - `name` - (Required) A name for the node pool.
    - `size` - (Required) The slug identifier for the type of Droplet to be used as workers in the node pool.
    - `node_count` - (Required) The number of Droplet instances in the node pool.
    - `tags` - (Optional) A list of tag names to be applied to the Kubernetes cluster.
    """
    region: pulumi.Output[str]
    """
    The slug identifier for the region where the Kubernetes cluster will be created.
    """
    service_subnet: pulumi.Output[str]
    """
    The range of assignable IP addresses for services running in the Kubernetes cluster.
    """
    status: pulumi.Output[str]
    """
    A string indicating the current status of the cluster. Potential values include running, provisioning, and errored.
    """
    tags: pulumi.Output[list]
    """
    A list of tag names to be applied to the Kubernetes cluster.
    """
    updated_at: pulumi.Output[str]
    """
    The date and time when the Kubernetes cluster was last updated.
    * `kube_config.0` - A representation of the Kubernetes cluster's kubeconfig with the following attributes:
    - `raw_config` - The full contents of the Kubernetes cluster's kubeconfig file.
    - `host` - The URL of the API server on the Kubernetes master node.
    - `client_key` - The base64 encoded private key used by clients to access the cluster.
    - `client_certificate` - The base64 encoded public certificate used by clients to access the cluster.
    - `cluster_ca_certificate` - The base64 encoded public certificate for the cluster's certificate authority.
    """
    version: pulumi.Output[str]
    """
    The slug identifier for the version of Kubernetes used for the cluster.
    """
    def __init__(__self__, resource_name, opts=None, name=None, node_pool=None, region=None, tags=None, version=None, __name__=None, __opts__=None):
        """
        Provides a DigitalOcean Kubernetes cluster resource. This can be used to create, delete, and modify clusters. For more information see the [official documentation](https://www.digitalocean.com/docs/kubernetes/).
        
        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] name: A name for the Kubernetes cluster.
        :param pulumi.Input[dict] node_pool: A block representing the cluster's default node pool. Additional node pools may be added to the cluster using the `digitalocean_kubernetes_node_pool` resource. The following arguments may be specified:
               - `name` - (Required) A name for the node pool.
               - `size` - (Required) The slug identifier for the type of Droplet to be used as workers in the node pool.
               - `node_count` - (Required) The number of Droplet instances in the node pool.
               - `tags` - (Optional) A list of tag names to be applied to the Kubernetes cluster.
        :param pulumi.Input[str] region: The slug identifier for the region where the Kubernetes cluster will be created.
        :param pulumi.Input[list] tags: A list of tag names to be applied to the Kubernetes cluster.
        :param pulumi.Input[str] version: The slug identifier for the version of Kubernetes used for the cluster.

        > This content is derived from https://github.com/terraform-providers/terraform-provider-digitalocean/blob/master/website/docs/r/kubernetes_cluster.html.markdown.
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

        __props__['name'] = name

        if node_pool is None:
            raise TypeError("Missing required property 'node_pool'")
        __props__['node_pool'] = node_pool

        if region is None:
            raise TypeError("Missing required property 'region'")
        __props__['region'] = region

        __props__['tags'] = tags

        if version is None:
            raise TypeError("Missing required property 'version'")
        __props__['version'] = version

        __props__['cluster_subnet'] = None
        __props__['created_at'] = None
        __props__['endpoint'] = None
        __props__['ipv4_address'] = None
        __props__['kube_configs'] = None
        __props__['service_subnet'] = None
        __props__['status'] = None
        __props__['updated_at'] = None

        if opts is None:
            opts = pulumi.ResourceOptions()
        if opts.version is None:
            opts.version = utilities.get_version()
        super(KubernetesCluster, __self__).__init__(
            'digitalocean:index/kubernetesCluster:KubernetesCluster',
            resource_name,
            __props__,
            opts)


    def translate_output_property(self, prop):
        return tables._CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop

    def translate_input_property(self, prop):
        return tables._SNAKE_TO_CAMEL_CASE_TABLE.get(prop) or prop

