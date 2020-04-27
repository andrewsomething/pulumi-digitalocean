// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as inputs from "./types/input";
import * as outputs from "./types/output";
import * as utilities from "./utilities";

/**
 * Retrieve information about all supported DigitalOcean regions, with the ability to
 * filter and sort the results. If no filters are specified, all regions will be returned.
 * 
 * Note: You can use the [`digitalocean..getRegion`](https://www.terraform.io/docs/providers/do/d/region.html) data source
 * to obtain metadata about a single region if you already know the `slug` to retrieve.
 * 
 * ## Example Usage
 * 
 * 
 * 
 * ```typescript
 * import * as pulumi from "@pulumi/pulumi";
 * import * as digitalocean from "@pulumi/digitalocean";
 * 
 * const available = pulumi.output(digitalocean.getRegions({
 *     filters: [{
 *         key: "available",
 *         values: ["true"],
 *     }],
 * }, { async: true }));
 * ```
 *
 * > This content is derived from https://github.com/terraform-providers/terraform-provider-digitalocean/blob/master/website/docs/d/regions.html.md.
 */
export function getRegions(args?: GetRegionsArgs, opts?: pulumi.InvokeOptions): Promise<GetRegionsResult> {
    args = args || {};
    if (!opts) {
        opts = {}
    }

    if (!opts.version) {
        opts.version = utilities.getVersion();
    }
    return pulumi.runtime.invoke("digitalocean:index/getRegions:getRegions", {
        "filters": args.filters,
        "sorts": args.sorts,
    }, opts);
}

/**
 * A collection of arguments for invoking getRegions.
 */
export interface GetRegionsArgs {
    /**
     * Filter the results.
     * The `filter` block is documented below.
     */
    readonly filters?: inputs.GetRegionsFilter[];
    /**
     * Sort the results.
     * The `sort` block is documented below.
     */
    readonly sorts?: inputs.GetRegionsSort[];
}

/**
 * A collection of values returned by getRegions.
 */
export interface GetRegionsResult {
    readonly filters?: outputs.GetRegionsFilter[];
    /**
     * A set of regions satisfying any `filter` and `sort` criteria. Each region has the following attributes:  
     * - `slug` - A human-readable string that is used as a unique identifier for each region.
     * - `name` - The display name of the region.
     * - `available` - A boolean value that represents whether new Droplets can be created in this region.
     * - `sizes` - A set of identifying slugs for the Droplet sizes available in this region.
     * - `features` - A set of features available in this region.
     */
    readonly regions: outputs.GetRegionsRegion[];
    readonly sorts?: outputs.GetRegionsSort[];
    /**
     * The provider-assigned unique ID for this managed resource.
     */
    readonly id: string;
}
