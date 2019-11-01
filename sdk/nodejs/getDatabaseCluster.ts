// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as inputs from "./types/input";
import * as outputs from "./types/output";
import * as utilities from "./utilities";

/**
 * Provides information on a DigitalOcean database cluster resource.
 *
 * > This content is derived from https://github.com/terraform-providers/terraform-provider-digitalocean/blob/master/website/docs/d/database_cluster.html.markdown.
 */
export function getDatabaseCluster(args: GetDatabaseClusterArgs, opts?: pulumi.InvokeOptions): Promise<GetDatabaseClusterResult> & GetDatabaseClusterResult {
    if (!opts) {
        opts = {}
    }

    if (!opts.version) {
        opts.version = utilities.getVersion();
    }
    const promise: Promise<GetDatabaseClusterResult> = pulumi.runtime.invoke("digitalocean:index/getDatabaseCluster:getDatabaseCluster", {
        "name": args.name,
        "tags": args.tags,
    }, opts);

    return pulumi.utils.liftProperties(promise, opts);
}

/**
 * A collection of arguments for invoking getDatabaseCluster.
 */
export interface GetDatabaseClusterArgs {
    /**
     * The name of the database cluster.
     */
    readonly name: string;
    readonly tags?: string[];
}

/**
 * A collection of values returned by getDatabaseCluster.
 */
export interface GetDatabaseClusterResult {
    /**
     * Name of the cluster's default database.
     */
    readonly database: string;
    /**
     * Database engine used by the cluster (ex. `pg` for PostreSQL).
     */
    readonly engine: string;
    /**
     * Database cluster's hostname.
     */
    readonly host: string;
    /**
     * Defines when the automatic maintenance should be performed for the database cluster.
     */
    readonly maintenanceWindows: outputs.GetDatabaseClusterMaintenanceWindow[];
    readonly name: string;
    /**
     * Number of nodes that will be included in the cluster.
     */
    readonly nodeCount: number;
    /**
     * Password for the cluster's default user.
     */
    readonly password: string;
    /**
     * Network port that the database cluster is listening on.
     */
    readonly port: number;
    /**
     * Same as `host`, but only accessible from resources within the account and in the same region.
     */
    readonly privateHost: string;
    /**
     * Same as `uri`, but only accessible from resources within the account and in the same region.
     */
    readonly privateUri: string;
    /**
     * DigitalOcean region where the cluster will reside.
     */
    readonly region: string;
    /**
     * Database droplet size associated with the cluster (ex. `db-s-1vcpu-1gb`).
     */
    readonly size: string;
    readonly tags?: string[];
    /**
     * The full URI for connecting to the database cluster.
     */
    readonly uri: string;
    /**
     * The uniform resource name of the database cluster.
     */
    readonly urn: string;
    /**
     * Username for the cluster's default user.
     */
    readonly user: string;
    /**
     * Engine version used by the cluster (ex. `11` for PostgreSQL 11).
     */
    readonly version: string;
    /**
     * id is the provider-assigned unique ID for this managed resource.
     */
    readonly id: string;
}
