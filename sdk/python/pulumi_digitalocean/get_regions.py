# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import json
import warnings
import pulumi
import pulumi.runtime
from typing import Union
from . import utilities, tables

class GetRegionsResult:
    """
    A collection of values returned by getRegions.
    """
    def __init__(__self__, filters=None, id=None, regions=None, sorts=None):
        if filters and not isinstance(filters, list):
            raise TypeError("Expected argument 'filters' to be a list")
        __self__.filters = filters
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        __self__.id = id
        """
        The provider-assigned unique ID for this managed resource.
        """
        if regions and not isinstance(regions, list):
            raise TypeError("Expected argument 'regions' to be a list")
        __self__.regions = regions
        """
        A set of regions satisfying any `filter` and `sort` criteria. Each region has the following attributes:  
        - `slug` - A human-readable string that is used as a unique identifier for each region.
        - `name` - The display name of the region.
        - `available` - A boolean value that represents whether new Droplets can be created in this region.
        - `sizes` - A set of identifying slugs for the Droplet sizes available in this region.
        - `features` - A set of features available in this region.
        """
        if sorts and not isinstance(sorts, list):
            raise TypeError("Expected argument 'sorts' to be a list")
        __self__.sorts = sorts
class AwaitableGetRegionsResult(GetRegionsResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetRegionsResult(
            filters=self.filters,
            id=self.id,
            regions=self.regions,
            sorts=self.sorts)

def get_regions(filters=None,sorts=None,opts=None):
    """
    Retrieve information about all supported DigitalOcean regions, with the ability to
    filter and sort the results. If no filters are specified, all regions will be returned.

    Note: You can use the [`.getRegion`](https://www.terraform.io/docs/providers/do/d/region.html) data source
    to obtain metadata about a single region if you already know the `slug` to retrieve.

    ## Example Usage



    ```python
    import pulumi
    import pulumi_digitalocean as digitalocean

    available = digitalocean.get_regions(filters=[{
        "key": "available",
        "values": ["true"],
    }])
    ```



    :param list filters: Filter the results.
           The `filter` block is documented below.
    :param list sorts: Sort the results.
           The `sort` block is documented below.

    The **filters** object supports the following:

      * `key` (`str`) - Filter the regions by this key. This may be one of `slug`,
        `name`, `available`, `features`, or `sizes`.
      * `values` (`list`) - A list of values to match against the `key` field. Only retrieves regions
        where the `key` field takes on one or more of the values provided here.

    The **sorts** object supports the following:

      * `direction` (`str`) - The sort direction. This may be either `asc` or `desc`.
      * `key` (`str`) - Sort the regions by this key. This may be one of `slug`,
        `name`, or `available`.
    """
    __args__ = dict()


    __args__['filters'] = filters
    __args__['sorts'] = sorts
    if opts is None:
        opts = pulumi.InvokeOptions()
    if opts.version is None:
        opts.version = utilities.get_version()
    __ret__ = pulumi.runtime.invoke('digitalocean:index/getRegions:getRegions', __args__, opts=opts).value

    return AwaitableGetRegionsResult(
        filters=__ret__.get('filters'),
        id=__ret__.get('id'),
        regions=__ret__.get('regions'),
        sorts=__ret__.get('sorts'))
