// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as utilities from "./utilities";

import {Region} from "./index";

/**
 * Provides a resource which can be used to create a snapshot from an existing DigitalOcean Droplet.
 * 
 * ## Example Usage
 * 
 * ```typescript
 * import * as pulumi from "@pulumi/pulumi";
 * import * as digitalocean from "@pulumi/digitalocean";
 * 
 * const web = new digitalocean.Droplet("web", {
 *     image: "centos-7-x64",
 *     region: "nyc3",
 *     size: "s-1vcpu-1gb",
 * });
 * const web_snapshot = new digitalocean.DropletSnapshot("web-snapshot", {
 *     dropletId: web.id,
 * });
 * ```
 */
export class DropletSnapshot extends pulumi.CustomResource {
    /**
     * Get an existing DropletSnapshot resource's state with the given name, ID, and optional extra
     * properties used to qualify the lookup.
     *
     * @param name The _unique_ name of the resulting resource.
     * @param id The _unique_ provider ID of the resource to lookup.
     * @param state Any extra arguments used during the lookup.
     */
    public static get(name: string, id: pulumi.Input<pulumi.ID>, state?: DropletSnapshotState, opts?: pulumi.CustomResourceOptions): DropletSnapshot {
        return new DropletSnapshot(name, <any>state, { ...opts, id: id });
    }

    /** @internal */
    public static readonly __pulumiType = 'digitalocean:index/dropletSnapshot:DropletSnapshot';

    /**
     * Returns true if the given object is an instance of DropletSnapshot.  This is designed to work even
     * when multiple copies of the Pulumi SDK have been loaded into the same process.
     */
    public static isInstance(obj: any): obj is DropletSnapshot {
        if (obj === undefined || obj === null) {
            return false;
        }
        return obj['__pulumiType'] === DropletSnapshot.__pulumiType;
    }

    /**
     * The date and time the Droplet snapshot was created.
     */
    public /*out*/ readonly createdAt!: pulumi.Output<string>;
    /**
     * The ID of the Droplet from which the snapshot will be taken.
     */
    public readonly dropletId!: pulumi.Output<string>;
    /**
     * The minimum size in gigabytes required for a Droplet to be created based on this snapshot.
     */
    public /*out*/ readonly minDiskSize!: pulumi.Output<number>;
    /**
     * A name for the Droplet snapshot.
     */
    public readonly name!: pulumi.Output<string>;
    /**
     * A list of DigitalOcean region "slugs" indicating where the droplet snapshot is available.
     */
    public /*out*/ readonly regions!: pulumi.Output<Region[]>;
    /**
     * The billable size of the Droplet snapshot in gigabytes.
     */
    public /*out*/ readonly size!: pulumi.Output<number>;

    /**
     * Create a DropletSnapshot resource with the given unique name, arguments, and options.
     *
     * @param name The _unique_ name of the resource.
     * @param args The arguments to use to populate this resource's properties.
     * @param opts A bag of options that control this resource's behavior.
     */
    constructor(name: string, args: DropletSnapshotArgs, opts?: pulumi.CustomResourceOptions)
    constructor(name: string, argsOrState?: DropletSnapshotArgs | DropletSnapshotState, opts?: pulumi.CustomResourceOptions) {
        let inputs: pulumi.Inputs = {};
        if (opts && opts.id) {
            const state = argsOrState as DropletSnapshotState | undefined;
            inputs["createdAt"] = state ? state.createdAt : undefined;
            inputs["dropletId"] = state ? state.dropletId : undefined;
            inputs["minDiskSize"] = state ? state.minDiskSize : undefined;
            inputs["name"] = state ? state.name : undefined;
            inputs["regions"] = state ? state.regions : undefined;
            inputs["size"] = state ? state.size : undefined;
        } else {
            const args = argsOrState as DropletSnapshotArgs | undefined;
            if (!args || args.dropletId === undefined) {
                throw new Error("Missing required property 'dropletId'");
            }
            inputs["dropletId"] = args ? args.dropletId : undefined;
            inputs["name"] = args ? args.name : undefined;
            inputs["createdAt"] = undefined /*out*/;
            inputs["minDiskSize"] = undefined /*out*/;
            inputs["regions"] = undefined /*out*/;
            inputs["size"] = undefined /*out*/;
        }
        super(DropletSnapshot.__pulumiType, name, inputs, opts);
    }
}

/**
 * Input properties used for looking up and filtering DropletSnapshot resources.
 */
export interface DropletSnapshotState {
    /**
     * The date and time the Droplet snapshot was created.
     */
    readonly createdAt?: pulumi.Input<string>;
    /**
     * The ID of the Droplet from which the snapshot will be taken.
     */
    readonly dropletId?: pulumi.Input<string>;
    /**
     * The minimum size in gigabytes required for a Droplet to be created based on this snapshot.
     */
    readonly minDiskSize?: pulumi.Input<number>;
    /**
     * A name for the Droplet snapshot.
     */
    readonly name?: pulumi.Input<string>;
    /**
     * A list of DigitalOcean region "slugs" indicating where the droplet snapshot is available.
     */
    readonly regions?: pulumi.Input<pulumi.Input<Region>[]>;
    /**
     * The billable size of the Droplet snapshot in gigabytes.
     */
    readonly size?: pulumi.Input<number>;
}

/**
 * The set of arguments for constructing a DropletSnapshot resource.
 */
export interface DropletSnapshotArgs {
    /**
     * The ID of the Droplet from which the snapshot will be taken.
     */
    readonly dropletId: pulumi.Input<string>;
    /**
     * A name for the Droplet snapshot.
     */
    readonly name?: pulumi.Input<string>;
}
