# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import json
import warnings
import pulumi
import pulumi.runtime
from typing import Union
from . import utilities, tables

class GetProjectsResult:
    """
    A collection of values returned by getProjects.
    """
    def __init__(__self__, filters=None, id=None, projects=None, sorts=None):
        if filters and not isinstance(filters, list):
            raise TypeError("Expected argument 'filters' to be a list")
        __self__.filters = filters
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        __self__.id = id
        """
        The provider-assigned unique ID for this managed resource.
        """
        if projects and not isinstance(projects, list):
            raise TypeError("Expected argument 'projects' to be a list")
        __self__.projects = projects
        """
        A set of projects satisfying any `filter` and `sort` criteria. Each project has
        the following attributes:
        - `id` - The ID of the project
        - `name` - The name of the project
        - `description` - The description of the project
        - `purpose` -  The purpose of the project (Default: "Web Application")
        - `environment` - The environment of the project's resources. The possible values are: `Development`, `Staging`, `Production`.
        - `resources` - A set of uniform resource names (URNs) for the resources associated with the project
        - `owner_uuid` - The unique universal identifier of the project owner
        - `owner_id` - The ID of the project owner
        - `created_at` - The date and time when the project was created, (ISO8601)
        - `updated_at` - The date and time when the project was last updated, (ISO8601)
        """
        if sorts and not isinstance(sorts, list):
            raise TypeError("Expected argument 'sorts' to be a list")
        __self__.sorts = sorts
class AwaitableGetProjectsResult(GetProjectsResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetProjectsResult(
            filters=self.filters,
            id=self.id,
            projects=self.projects,
            sorts=self.sorts)

def get_projects(filters=None,sorts=None,opts=None):
    """
    Retrieve information about all DigitalOcean projects associated with an account, with
    the ability to filter and sort the results. If no filters are specified, all projects
    will be returned.

    Note: You can use the [`.Project`](https://www.terraform.io/docs/providers/do/d/project.html) data source to
    obtain metadata about a single project if you already know the `id` to retrieve or the unique
    `name` of the project.

    ## Example Usage



    ```python
    import pulumi
    import pulumi_digitalocean as digitalocean

    staging = digitalocean.get_projects(filters=[{
        "key": "environment",
        "values": ["Staging"],
    }])
    ```



    :param list filters: Filter the results.
           The `filter` block is documented below.
    :param list sorts: Sort the results.
           The `sort` block is documented below.

    The **filters** object supports the following:

      * `key` (`str`) - Filter the projects by this key. This may be one of `name`,
        `purpose`, `description`, `environment`, or `is_default`.
      * `values` (`list`) - A list of values to match against the `key` field. Only retrieves projects
        where the `key` field takes on one or more of the values provided here.

    The **sorts** object supports the following:

      * `direction` (`str`) - The sort direction. This may be either `asc` or `desc`.
      * `key` (`str`) - Sort the projects by this key. This may be one of `name`,
        `purpose`, `description`, or `environment`.
    """
    __args__ = dict()


    __args__['filters'] = filters
    __args__['sorts'] = sorts
    if opts is None:
        opts = pulumi.InvokeOptions()
    if opts.version is None:
        opts.version = utilities.get_version()
    __ret__ = pulumi.runtime.invoke('digitalocean:index/getProjects:getProjects', __args__, opts=opts).value

    return AwaitableGetProjectsResult(
        filters=__ret__.get('filters'),
        id=__ret__.get('id'),
        projects=__ret__.get('projects'),
        sorts=__ret__.get('sorts'))
