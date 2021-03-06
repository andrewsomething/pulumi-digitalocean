# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import json
import warnings
import pulumi
import pulumi.runtime
from typing import Union
from . import utilities, tables

class GetKubernetesVersionsResult:
    """
    A collection of values returned by getKubernetesVersions.
    """
    def __init__(__self__, id=None, latest_version=None, valid_versions=None, version_prefix=None):
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        __self__.id = id
        """
        The provider-assigned unique ID for this managed resource.
        """
        if latest_version and not isinstance(latest_version, str):
            raise TypeError("Expected argument 'latest_version' to be a str")
        __self__.latest_version = latest_version
        """
        The most recent version available.
        """
        if valid_versions and not isinstance(valid_versions, list):
            raise TypeError("Expected argument 'valid_versions' to be a list")
        __self__.valid_versions = valid_versions
        """
        A list of available versions.
        """
        if version_prefix and not isinstance(version_prefix, str):
            raise TypeError("Expected argument 'version_prefix' to be a str")
        __self__.version_prefix = version_prefix
class AwaitableGetKubernetesVersionsResult(GetKubernetesVersionsResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetKubernetesVersionsResult(
            id=self.id,
            latest_version=self.latest_version,
            valid_versions=self.valid_versions,
            version_prefix=self.version_prefix)

def get_kubernetes_versions(version_prefix=None,opts=None):
    """
    Provides access to the available DigitalOcean Kubernetes Service versions.

    ## Example Usage

    ### Output a list of all available versions

    ```python
    import pulumi
    import pulumi_digitalocean as digitalocean

    example = digitalocean.get_kubernetes_versions()
    pulumi.export("k8s-versions", example.valid_versions)
    ```

    ### Create a Kubernetes cluster using the most recent version available

    ```python
    import pulumi
    import pulumi_digitalocean as digitalocean

    example = digitalocean.get_kubernetes_versions()
    example_cluster = digitalocean.KubernetesCluster("example-cluster",
        region="lon1",
        version=example.latest_version,
        node_pool={
            "name": "default",
            "size": "s-1vcpu-2gb",
            "nodeCount": 3,
        })
    ```

    ### Pin a Kubernetes cluster to a specific minor version

    ```python
    import pulumi
    import pulumi_digitalocean as digitalocean

    example = digitalocean.get_kubernetes_versions(version_prefix="1.16.")
    example_cluster = digitalocean.KubernetesCluster("example-cluster",
        region="lon1",
        version=example.latest_version,
        node_pool={
            "name": "default",
            "size": "s-1vcpu-2gb",
            "nodeCount": 3,
        })
    ```
    """
    __args__ = dict()


    __args__['versionPrefix'] = version_prefix
    if opts is None:
        opts = pulumi.InvokeOptions()
    if opts.version is None:
        opts.version = utilities.get_version()
    __ret__ = pulumi.runtime.invoke('digitalocean:index/getKubernetesVersions:getKubernetesVersions', __args__, opts=opts).value

    return AwaitableGetKubernetesVersionsResult(
        id=__ret__.get('id'),
        latest_version=__ret__.get('latestVersion'),
        valid_versions=__ret__.get('validVersions'),
        version_prefix=__ret__.get('versionPrefix'))
