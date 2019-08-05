# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import json
import warnings
import pulumi
import pulumi.runtime
from . import utilities, tables

class GetVolumeSnapshotResult:
    """
    A collection of values returned by getVolumeSnapshot.
    """
    def __init__(__self__, created_at=None, min_disk_size=None, most_recent=None, name=None, name_regex=None, region=None, regions=None, size=None, volume_id=None, id=None):
        if created_at and not isinstance(created_at, str):
            raise TypeError("Expected argument 'created_at' to be a str")
        __self__.created_at = created_at
        """
        The date and time the volume snapshot was created.
        """
        if min_disk_size and not isinstance(min_disk_size, float):
            raise TypeError("Expected argument 'min_disk_size' to be a float")
        __self__.min_disk_size = min_disk_size
        """
        The minimum size in gigabytes required for a volume to be created based on this volume snapshot.
        """
        if most_recent and not isinstance(most_recent, bool):
            raise TypeError("Expected argument 'most_recent' to be a bool")
        __self__.most_recent = most_recent
        if name and not isinstance(name, str):
            raise TypeError("Expected argument 'name' to be a str")
        __self__.name = name
        if name_regex and not isinstance(name_regex, str):
            raise TypeError("Expected argument 'name_regex' to be a str")
        __self__.name_regex = name_regex
        if region and not isinstance(region, str):
            raise TypeError("Expected argument 'region' to be a str")
        __self__.region = region
        if regions and not isinstance(regions, list):
            raise TypeError("Expected argument 'regions' to be a list")
        __self__.regions = regions
        """
        A list of DigitalOcean region "slugs" indicating where the volume snapshot is available.
        """
        if size and not isinstance(size, float):
            raise TypeError("Expected argument 'size' to be a float")
        __self__.size = size
        """
        The billable size of the volume snapshot in gigabytes.
        """
        if volume_id and not isinstance(volume_id, str):
            raise TypeError("Expected argument 'volume_id' to be a str")
        __self__.volume_id = volume_id
        """
        The ID of the volume from which the volume snapshot originated.
        """
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

def get_volume_snapshot(most_recent=None,name=None,name_regex=None,region=None,opts=None):
    """
    Volume snapshots are saved instances of a block storage volume. Use this data
    source to retrieve the ID of a DigitalOcean volume snapshot for use in other
    resources.

    > This content is derived from https://github.com/terraform-providers/terraform-provider-digitalocean/blob/master/website/docs/d/volume_snapshot.html.markdown.
    """
    __args__ = dict()

    __args__['mostRecent'] = most_recent
    __args__['name'] = name
    __args__['nameRegex'] = name_regex
    __args__['region'] = region
    if opts is None:
        opts = pulumi.ResourceOptions()
    if opts.version is None:
        opts.version = utilities.get_version()
    __ret__ = pulumi.runtime.invoke('digitalocean:index/getVolumeSnapshot:getVolumeSnapshot', __args__, opts=opts).value

    return GetVolumeSnapshotResult(
        created_at=__ret__.get('createdAt'),
        min_disk_size=__ret__.get('minDiskSize'),
        most_recent=__ret__.get('mostRecent'),
        name=__ret__.get('name'),
        name_regex=__ret__.get('nameRegex'),
        region=__ret__.get('region'),
        regions=__ret__.get('regions'),
        size=__ret__.get('size'),
        volume_id=__ret__.get('volumeId'),
        id=__ret__.get('id'))
