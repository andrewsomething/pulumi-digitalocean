// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.DigitalOcean
{
    public static partial class Invokes
    {
        /// <summary>
        /// Retrieve information about all supported DigitalOcean regions, with the ability to
        /// filter and sort the results. If no filters are specified, all regions will be returned.
        /// 
        /// Note: You can use the [`digitalocean..getRegion`](https://www.terraform.io/docs/providers/do/d/region.html) data source
        /// to obtain metadata about a single region if you already know the `slug` to retrieve.
        /// 
        /// &gt; This content is derived from https://github.com/terraform-providers/terraform-provider-digitalocean/blob/master/website/docs/d/regions.html.md.
        /// </summary>
        [Obsolete("Use GetRegions.InvokeAsync() instead")]
        public static Task<GetRegionsResult> GetRegions(GetRegionsArgs? args = null, InvokeOptions? options = null)
            => Pulumi.Deployment.Instance.InvokeAsync<GetRegionsResult>("digitalocean:index/getRegions:getRegions", args ?? InvokeArgs.Empty, options.WithVersion());
    }
    public static class GetRegions
    {
        /// <summary>
        /// Retrieve information about all supported DigitalOcean regions, with the ability to
        /// filter and sort the results. If no filters are specified, all regions will be returned.
        /// 
        /// Note: You can use the [`digitalocean..getRegion`](https://www.terraform.io/docs/providers/do/d/region.html) data source
        /// to obtain metadata about a single region if you already know the `slug` to retrieve.
        /// 
        /// &gt; This content is derived from https://github.com/terraform-providers/terraform-provider-digitalocean/blob/master/website/docs/d/regions.html.md.
        /// </summary>
        public static Task<GetRegionsResult> InvokeAsync(GetRegionsArgs? args = null, InvokeOptions? options = null)
            => Pulumi.Deployment.Instance.InvokeAsync<GetRegionsResult>("digitalocean:index/getRegions:getRegions", args ?? InvokeArgs.Empty, options.WithVersion());
    }

    public sealed class GetRegionsArgs : Pulumi.InvokeArgs
    {
        [Input("filters")]
        private List<Inputs.GetRegionsFiltersArgs>? _filters;

        /// <summary>
        /// Filter the results.
        /// The `filter` block is documented below.
        /// </summary>
        public List<Inputs.GetRegionsFiltersArgs> Filters
        {
            get => _filters ?? (_filters = new List<Inputs.GetRegionsFiltersArgs>());
            set => _filters = value;
        }

        [Input("sorts")]
        private List<Inputs.GetRegionsSortsArgs>? _sorts;

        /// <summary>
        /// Sort the results.
        /// The `sort` block is documented below.
        /// </summary>
        public List<Inputs.GetRegionsSortsArgs> Sorts
        {
            get => _sorts ?? (_sorts = new List<Inputs.GetRegionsSortsArgs>());
            set => _sorts = value;
        }

        public GetRegionsArgs()
        {
        }
    }

    [OutputType]
    public sealed class GetRegionsResult
    {
        public readonly ImmutableArray<Outputs.GetRegionsFiltersResult> Filters;
        /// <summary>
        /// A set of regions satisfying any `filter` and `sort` criteria. Each region has the following attributes:  
        /// - `slug` - A human-readable string that is used as a unique identifier for each region.
        /// - `name` - The display name of the region.
        /// - `available` - A boolean value that represents whether new Droplets can be created in this region.
        /// - `sizes` - A set of identifying slugs for the Droplet sizes available in this region.
        /// - `features` - A set of features available in this region.
        /// </summary>
        public readonly ImmutableArray<Outputs.GetRegionsRegionsResult> Regions;
        public readonly ImmutableArray<Outputs.GetRegionsSortsResult> Sorts;
        /// <summary>
        /// id is the provider-assigned unique ID for this managed resource.
        /// </summary>
        public readonly string Id;

        [OutputConstructor]
        private GetRegionsResult(
            ImmutableArray<Outputs.GetRegionsFiltersResult> filters,
            ImmutableArray<Outputs.GetRegionsRegionsResult> regions,
            ImmutableArray<Outputs.GetRegionsSortsResult> sorts,
            string id)
        {
            Filters = filters;
            Regions = regions;
            Sorts = sorts;
            Id = id;
        }
    }

    namespace Inputs
    {

    public sealed class GetRegionsFiltersArgs : Pulumi.InvokeArgs
    {
        /// <summary>
        /// Filter the regions by this key. This may be one of `slug`,
        /// `name`, `available`, `features`, or `sizes`.
        /// </summary>
        [Input("key", required: true)]
        public string Key { get; set; } = null!;

        [Input("values", required: true)]
        private List<string>? _values;

        /// <summary>
        /// A list of values to match against the `key` field. Only retrieves regions
        /// where the `key` field takes on one or more of the values provided here.
        /// </summary>
        public List<string> Values
        {
            get => _values ?? (_values = new List<string>());
            set => _values = value;
        }

        public GetRegionsFiltersArgs()
        {
        }
    }

    public sealed class GetRegionsSortsArgs : Pulumi.InvokeArgs
    {
        /// <summary>
        /// The sort direction. This may be either `asc` or `desc`.
        /// </summary>
        [Input("direction")]
        public string? Direction { get; set; }

        /// <summary>
        /// Sort the regions by this key. This may be one of `slug`,
        /// `name`, or `available`.
        /// </summary>
        [Input("key", required: true)]
        public string Key { get; set; } = null!;

        public GetRegionsSortsArgs()
        {
        }
    }
    }

    namespace Outputs
    {

    [OutputType]
    public sealed class GetRegionsFiltersResult
    {
        /// <summary>
        /// Filter the regions by this key. This may be one of `slug`,
        /// `name`, `available`, `features`, or `sizes`.
        /// </summary>
        public readonly string Key;
        /// <summary>
        /// A list of values to match against the `key` field. Only retrieves regions
        /// where the `key` field takes on one or more of the values provided here.
        /// </summary>
        public readonly ImmutableArray<string> Values;

        [OutputConstructor]
        private GetRegionsFiltersResult(
            string key,
            ImmutableArray<string> values)
        {
            Key = key;
            Values = values;
        }
    }

    [OutputType]
    public sealed class GetRegionsRegionsResult
    {
        public readonly bool Available;
        public readonly ImmutableArray<string> Features;
        public readonly string Name;
        public readonly ImmutableArray<string> Sizes;
        public readonly string Slug;

        [OutputConstructor]
        private GetRegionsRegionsResult(
            bool available,
            ImmutableArray<string> features,
            string name,
            ImmutableArray<string> sizes,
            string slug)
        {
            Available = available;
            Features = features;
            Name = name;
            Sizes = sizes;
            Slug = slug;
        }
    }

    [OutputType]
    public sealed class GetRegionsSortsResult
    {
        /// <summary>
        /// The sort direction. This may be either `asc` or `desc`.
        /// </summary>
        public readonly string? Direction;
        /// <summary>
        /// Sort the regions by this key. This may be one of `slug`,
        /// `name`, or `available`.
        /// </summary>
        public readonly string Key;

        [OutputConstructor]
        private GetRegionsSortsResult(
            string? direction,
            string key)
        {
            Direction = direction;
            Key = key;
        }
    }
    }
}
