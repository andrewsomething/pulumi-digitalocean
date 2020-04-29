// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as inputs from "./types/input";
import * as outputs from "./types/output";
import * as utilities from "./utilities";

/**
 * Get information on Spaces buckets for use in other resources, with the ability to filter and sort the results.
 * If no filters are specified, all Spaces buckets will be returned.
 * 
 * Note: You can use the [`digitalocean..SpacesBucket`](https://www.terraform.io/docs/providers/do/d/spaces_bucket.html) data source to
 * obtain metadata about a single bucket if you already know its `name` and `region`.
 * 
 * ## Example Usage
 * 
 * 
 * 
 * ```typescript
 * import * as pulumi from "@pulumi/pulumi";
 * import * as digitalocean from "@pulumi/digitalocean";
 * 
 * const nyc3 = pulumi.output(digitalocean.getSpacesBuckets({
 *     filters: [{
 *         key: "region",
 *         values: ["nyc3"],
 *     }],
 * }, { async: true }));
 * ```
 *
 * > This content is derived from https://github.com/terraform-providers/terraform-provider-digitalocean/blob/master/website/docs/d/spaces_buckets.html.md.
 */
export function getSpacesBuckets(args?: GetSpacesBucketsArgs, opts?: pulumi.InvokeOptions): Promise<GetSpacesBucketsResult> {
    args = args || {};
    if (!opts) {
        opts = {}
    }

    if (!opts.version) {
        opts.version = utilities.getVersion();
    }
    return pulumi.runtime.invoke("digitalocean:index/getSpacesBuckets:getSpacesBuckets", {
        "filters": args.filters,
        "sorts": args.sorts,
    }, opts);
}

/**
 * A collection of arguments for invoking getSpacesBuckets.
 */
export interface GetSpacesBucketsArgs {
    /**
     * Filter the results.
     * The `filter` block is documented below.
     */
    readonly filters?: inputs.GetSpacesBucketsFilter[];
    /**
     * Sort the results.
     * The `sort` block is documented below.
     */
    readonly sorts?: inputs.GetSpacesBucketsSort[];
}

/**
 * A collection of values returned by getSpacesBuckets.
 */
export interface GetSpacesBucketsResult {
    /**
     * A list of Spaces buckets satisfying any `filter` and `sort` criteria. Each bucket has the following attributes:  
     */
    readonly buckets: outputs.GetSpacesBucketsBucket[];
    readonly filters?: outputs.GetSpacesBucketsFilter[];
    readonly sorts?: outputs.GetSpacesBucketsSort[];
    /**
     * The provider-assigned unique ID for this managed resource.
     */
    readonly id: string;
}
