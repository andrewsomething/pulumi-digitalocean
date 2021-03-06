// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as inputs from "../types/input";

export interface DatabaseClusterMaintenanceWindow {
    /**
     * The day of the week on which to apply maintenance updates.
     */
    day: pulumi.Input<string>;
    /**
     * The hour in UTC at which maintenance updates will be applied in 24 hour format.
     */
    hour: pulumi.Input<string>;
}

export interface DatabaseFirewallRule {
    /**
     * The date and time when the firewall rule was created.
     */
    createdAt?: pulumi.Input<string>;
    type: pulumi.Input<string>;
    /**
     * A unique identifier for the firewall rule.
     */
    uuid?: pulumi.Input<string>;
    value: pulumi.Input<string>;
}

export interface FirewallInboundRule {
    /**
     * The ports on which traffic will be allowed
     * specified as a string containing a single port, a range (e.g. "8000-9000"),
     * or "1-65535" to open all ports for a protocol. Required for when protocol is
     * `tcp` or `udp`.
     */
    portRange?: pulumi.Input<string>;
    /**
     * The type of traffic to be allowed.
     * This may be one of "tcp", "udp", or "icmp".
     */
    protocol: pulumi.Input<string>;
    /**
     * An array of strings containing the IPv4
     * addresses, IPv6 addresses, IPv4 CIDRs, and/or IPv6 CIDRs from which the
     * inbound traffic will be accepted.
     */
    sourceAddresses?: pulumi.Input<pulumi.Input<string>[]>;
    /**
     * An array containing the IDs of
     * the Droplets from which the inbound traffic will be accepted.
     */
    sourceDropletIds?: pulumi.Input<pulumi.Input<number>[]>;
    /**
     * An array containing the IDs
     * of the Load Balancers from which the inbound traffic will be accepted.
     */
    sourceLoadBalancerUids?: pulumi.Input<pulumi.Input<string>[]>;
    /**
     * An array containing the names of Tags
     * corresponding to groups of Droplets from which the inbound traffic
     * will be accepted.
     */
    sourceTags?: pulumi.Input<pulumi.Input<string>[]>;
}

export interface FirewallOutboundRule {
    /**
     * An array of strings containing the IPv4
     * addresses, IPv6 addresses, IPv4 CIDRs, and/or IPv6 CIDRs to which the
     * outbound traffic will be allowed.
     */
    destinationAddresses?: pulumi.Input<pulumi.Input<string>[]>;
    /**
     * An array containing the IDs of
     * the Droplets to which the outbound traffic will be allowed.
     */
    destinationDropletIds?: pulumi.Input<pulumi.Input<number>[]>;
    /**
     * An array containing the IDs
     * of the Load Balancers to which the outbound traffic will be allowed.
     */
    destinationLoadBalancerUids?: pulumi.Input<pulumi.Input<string>[]>;
    /**
     * An array containing the names of Tags
     * corresponding to groups of Droplets to which the outbound traffic will
     * be allowed.
     * traffic.
     */
    destinationTags?: pulumi.Input<pulumi.Input<string>[]>;
    /**
     * The ports on which traffic will be allowed
     * specified as a string containing a single port, a range (e.g. "8000-9000"),
     * or "1-65535" to open all ports for a protocol. Required for when protocol is
     * `tcp` or `udp`.
     */
    portRange?: pulumi.Input<string>;
    /**
     * The type of traffic to be allowed.
     * This may be one of "tcp", "udp", or "icmp".
     */
    protocol: pulumi.Input<string>;
}

export interface FirewallPendingChange {
    dropletId?: pulumi.Input<number>;
    removing?: pulumi.Input<boolean>;
    /**
     * A status string indicating the current state of the Firewall.
     * This can be "waiting", "succeeded", or "failed".
     */
    status?: pulumi.Input<string>;
}

export interface GetDropletsFilter {
    /**
     * Filter the Droplets by this key. This may be one of '`backups`, `createdAt`, `disk`, `id`,
     * `image`, `ipv4Address`, `ipv4AddressPrivate`, `ipv6`, `ipv6Address`, `ipv6AddressPrivate`, `locked`,
     * `memory`, `monitoring`, `name`, `priceHourly`, `priceMonthly`, `privateNetworking`, `region`, `size`,
     * `status`, `tags`, `urn`, `vcpus`, `volumeIds`, or `vpcUuid`'.
     */
    key: string;
    /**
     * A list of values to match against the `key` field. Only retrieves Droplets
     * where the `key` field takes on one or more of the values provided here.
     */
    values: string[];
}

export interface GetDropletsSort {
    /**
     * The sort direction. This may be either `asc` or `desc`.
     */
    direction?: string;
    /**
     * Sort the Droplets by this key. This may be one of `backups`, `createdAt`, `disk`, `id`,
     * `image`, `ipv4Address`, `ipv4AddressPrivate`, `ipv6`, `ipv6Address`, `ipv6AddressPrivate`, `locked`,
     * `memory`, `monitoring`, `name`, `priceHourly`, `priceMonthly`, `privateNetworking`, `region`, `size`,
     * `status`, `urn`, `vcpus`, or `vpcUuid`.
     */
    key: string;
}

export interface GetImagesFilter {
    /**
     * Filter the images by this key. This may be one of `distribution`, `errorMessage`,
     * `id`, `image`, `minDiskSize`, `name`, `private`, `regions`, `sizeGigabytes`, `slug`, `status`,
     * `tags`, or `type`.
     */
    key: string;
    /**
     * A list of values to match against the `key` field. Only retrieves images
     * where the `key` field takes on one or more of the values provided here.
     */
    values: string[];
}

export interface GetImagesSort {
    /**
     * The sort direction. This may be either `asc` or `desc`.
     */
    direction?: string;
    /**
     * Sort the images by this key. This may be one of `distribution`, `errorMessage`, `id`,
     * `image`, `minDiskSize`, `name`, `private`, `sizeGigabytes`, `slug`, `status`, or `type`.
     */
    key: string;
}

export interface GetProjectsFilter {
    /**
     * Filter the projects by this key. This may be one of `name`,
     * `purpose`, `description`, `environment`, or `isDefault`.
     */
    key: string;
    /**
     * A list of values to match against the `key` field. Only retrieves projects
     * where the `key` field takes on one or more of the values provided here.
     */
    values: string[];
}

export interface GetProjectsSort {
    /**
     * The sort direction. This may be either `asc` or `desc`.
     */
    direction?: string;
    /**
     * Sort the projects by this key. This may be one of `name`,
     * `purpose`, `description`, or `environment`.
     */
    key: string;
}

export interface GetRegionsFilter {
    /**
     * Filter the regions by this key. This may be one of `slug`,
     * `name`, `available`, `features`, or `sizes`.
     */
    key: string;
    /**
     * A list of values to match against the `key` field. Only retrieves regions
     * where the `key` field takes on one or more of the values provided here.
     */
    values: string[];
}

export interface GetRegionsSort {
    /**
     * The sort direction. This may be either `asc` or `desc`.
     */
    direction?: string;
    /**
     * Sort the regions by this key. This may be one of `slug`,
     * `name`, or `available`.
     */
    key: string;
}

export interface GetSizesFilter {
    /**
     * Filter the sizes by this key. This may be one of `slug`,
     * `regions`, `memory`, `vcpus`, `disk`, `transfer`, `priceMonthly`,
     * `priceHourly`, or `available`.
     */
    key: string;
    /**
     * Only retrieves images which keys has value that matches
     * one of the values provided here.
     */
    values: string[];
}

export interface GetSizesSort {
    /**
     * The sort direction. This may be either `asc` or `desc`.
     */
    direction?: string;
    /**
     * Sort the sizes by this key. This may be one of `slug`,
     * `memory`, `vcpus`, `disk`, `transfer`, `priceMonthly`, or `priceHourly`.
     */
    key: string;
}

export interface GetSpacesBucketsFilter {
    /**
     * Filter the images by this key. This may be one of `bucketDomainName`, `name`, `region`, or `urn`.
     */
    key: string;
    /**
     * A list of values to match against the `key` field. Only retrieves images
     * where the `key` field takes on one or more of the values provided here.
     */
    values: string[];
}

export interface GetSpacesBucketsSort {
    /**
     * The sort direction. This may be either `asc` or `desc`.
     */
    direction?: string;
    /**
     * Sort the images by this key. This may be one of `bucketDomainName`, `name`, `region`, or `urn`.
     */
    key: string;
}

export interface KubernetesClusterKubeConfig {
    clientCertificate?: pulumi.Input<string>;
    clientKey?: pulumi.Input<string>;
    clusterCaCertificate?: pulumi.Input<string>;
    expiresAt?: pulumi.Input<string>;
    host?: pulumi.Input<string>;
    rawConfig?: pulumi.Input<string>;
    token?: pulumi.Input<string>;
}

export interface KubernetesClusterNodePool {
    actualNodeCount?: pulumi.Input<number>;
    autoScale?: pulumi.Input<boolean>;
    /**
     * A unique ID that can be used to identify and reference a Kubernetes cluster.
     */
    id?: pulumi.Input<string>;
    labels?: pulumi.Input<{[key: string]: pulumi.Input<string>}>;
    maxNodes?: pulumi.Input<number>;
    minNodes?: pulumi.Input<number>;
    /**
     * A name for the Kubernetes cluster.
     */
    name: pulumi.Input<string>;
    nodeCount?: pulumi.Input<number>;
    nodes?: pulumi.Input<pulumi.Input<inputs.KubernetesClusterNodePoolNode>[]>;
    size: pulumi.Input<string>;
    /**
     * A list of tag names to be applied to the Kubernetes cluster.
     */
    tags?: pulumi.Input<pulumi.Input<string>[]>;
}

export interface KubernetesClusterNodePoolNode {
    /**
     * The date and time when the Kubernetes cluster was created.
     */
    createdAt?: pulumi.Input<string>;
    dropletId?: pulumi.Input<string>;
    /**
     * A unique ID that can be used to identify and reference a Kubernetes cluster.
     */
    id?: pulumi.Input<string>;
    /**
     * A name for the Kubernetes cluster.
     */
    name?: pulumi.Input<string>;
    /**
     * A string indicating the current status of the cluster. Potential values include running, provisioning, and errored.
     */
    status?: pulumi.Input<string>;
    /**
     * The date and time when the Kubernetes cluster was last updated.
     * * `kube_config.0` - A representation of the Kubernetes cluster's kubeconfig with the following attributes:
     * - `rawConfig` - The full contents of the Kubernetes cluster's kubeconfig file.
     * - `host` - The URL of the API server on the Kubernetes master node.
     * - `clusterCaCertificate` - The base64 encoded public certificate for the cluster's certificate authority.
     * - `token` - The DigitalOcean API access token used by clients to access the cluster.
     * - `clientKey` - The base64 encoded private key used by clients to access the cluster. Only available if token authentication is not supported on your cluster.
     * - `clientCertificate` - The base64 encoded public certificate used by clients to access the cluster. Only available if token authentication is not supported on your cluster.
     * - `expiresAt` - The date and time when the credentials will expire and need to be regenerated.
     */
    updatedAt?: pulumi.Input<string>;
}

export interface KubernetesNodePoolNode {
    createdAt?: pulumi.Input<string>;
    dropletId?: pulumi.Input<string>;
    /**
     * A unique ID that can be used to identify and reference the node pool.
     */
    id?: pulumi.Input<string>;
    /**
     * A name for the node pool.
     */
    name?: pulumi.Input<string>;
    status?: pulumi.Input<string>;
    updatedAt?: pulumi.Input<string>;
}

export interface LoadBalancerForwardingRule {
    /**
     * The ID of the TLS certificate to be used for SSL termination.
     */
    certificateId?: pulumi.Input<string>;
    /**
     * An integer representing the port on which the Load Balancer instance will listen.
     */
    entryPort: pulumi.Input<number>;
    /**
     * The protocol used for traffic to the Load Balancer. The possible values are: `http`, `https`, `http2` or `tcp`.
     */
    entryProtocol: pulumi.Input<string>;
    /**
     * An integer representing the port on the backend Droplets to which the Load Balancer will send traffic.
     */
    targetPort: pulumi.Input<number>;
    /**
     * The protocol used for traffic from the Load Balancer to the backend Droplets. The possible values are: `http`, `https`, `http2` or `tcp`.
     */
    targetProtocol: pulumi.Input<string>;
    /**
     * A boolean value indicating whether SSL encrypted traffic will be passed through to the backend Droplets. The default value is `false`.
     */
    tlsPassthrough?: pulumi.Input<boolean>;
}

export interface LoadBalancerHealthcheck {
    /**
     * The number of seconds between between two consecutive health checks. If not specified, the default value is `10`.
     */
    checkIntervalSeconds?: pulumi.Input<number>;
    /**
     * The number of times a health check must pass for a backend Droplet to be marked "healthy" and be re-added to the pool. If not specified, the default value is `5`.
     */
    healthyThreshold?: pulumi.Input<number>;
    /**
     * The path on the backend Droplets to which the Load Balancer instance will send a request.
     */
    path?: pulumi.Input<string>;
    /**
     * An integer representing the port on the backend Droplets on which the health check will attempt a connection.
     */
    port: pulumi.Input<number>;
    /**
     * The protocol used for health checks sent to the backend Droplets. The possible values are `http` or `tcp`.
     */
    protocol: pulumi.Input<string>;
    /**
     * The number of seconds the Load Balancer instance will wait for a response until marking a health check as failed. If not specified, the default value is `5`.
     */
    responseTimeoutSeconds?: pulumi.Input<number>;
    /**
     * The number of times a health check must fail for a backend Droplet to be marked "unhealthy" and be removed from the pool. If not specified, the default value is `3`.
     */
    unhealthyThreshold?: pulumi.Input<number>;
}

export interface LoadBalancerStickySessions {
    /**
     * The name to be used for the cookie sent to the client. This attribute is required when using `cookies` for the sticky sessions type.
     */
    cookieName?: pulumi.Input<string>;
    /**
     * The number of seconds until the cookie set by the Load Balancer expires. This attribute is required when using `cookies` for the sticky sessions type.
     */
    cookieTtlSeconds?: pulumi.Input<number>;
    /**
     * An attribute indicating how and if requests from a client will be persistently served by the same backend Droplet. The possible values are `cookies` or `none`. If not specified, the default value is `none`.
     */
    type?: pulumi.Input<string>;
}

export interface SpacesBucketCorsRule {
    /**
     * A list of headers that will be included in the CORS preflight request's `Access-Control-Request-Headers`. A header may contain one wildcard (e.g. `x-amz-*`).
     */
    allowedHeaders?: pulumi.Input<pulumi.Input<string>[]>;
    /**
     * A list of HTTP methods (e.g. `GET`) which are allowed from the specified origin.
     */
    allowedMethods: pulumi.Input<pulumi.Input<string>[]>;
    /**
     * A list of hosts from which requests using the specified methods are allowed. A host may contain one wildcard (e.g. http://*.example.com).
     */
    allowedOrigins: pulumi.Input<pulumi.Input<string>[]>;
    /**
     * The time in seconds that browser can cache the response for a preflight request.
     */
    maxAgeSeconds?: pulumi.Input<number>;
}

export interface SpacesBucketLifecycleRule {
    /**
     * Specifies the number of days after initiating a multipart
     * upload when the multipart upload must be completed or else Spaces will abort the upload.
     */
    abortIncompleteMultipartUploadDays?: pulumi.Input<number>;
    /**
     * Specifies lifecycle rule status.
     */
    enabled: pulumi.Input<boolean>;
    /**
     * Specifies a time period after which applicable objects expire (documented below).
     */
    expiration?: pulumi.Input<inputs.SpacesBucketLifecycleRuleExpiration>;
    /**
     * Unique identifier for the rule.
     */
    id?: pulumi.Input<string>;
    /**
     * Specifies when non-current object versions expire (documented below).
     */
    noncurrentVersionExpiration?: pulumi.Input<inputs.SpacesBucketLifecycleRuleNoncurrentVersionExpiration>;
    /**
     * Object key prefix identifying one or more objects to which the rule applies.
     */
    prefix?: pulumi.Input<string>;
}

export interface SpacesBucketLifecycleRuleExpiration {
    /**
     * Specifies the date/time after which you want applicable objects to expire. The argument uses
     * RFC3339 format, e.g. "2020-03-22T15:03:55Z" or parts thereof e.g. "2019-02-28".
     */
    date?: pulumi.Input<string>;
    /**
     * Specifies the number of days after object creation when the applicable objects will expire.
     */
    days?: pulumi.Input<number>;
    /**
     * On a versioned bucket (versioning-enabled or versioning-suspended
     * bucket), setting this to true directs Spaces to delete expired object delete markers.
     */
    expiredObjectDeleteMarker?: pulumi.Input<boolean>;
}

export interface SpacesBucketLifecycleRuleNoncurrentVersionExpiration {
    /**
     * Specifies the number of days after which an object's non-current versions expire.
     */
    days?: pulumi.Input<number>;
}

export interface SpacesBucketVersioning {
    /**
     * Enable versioning. Once you version-enable a bucket, it can never return to an unversioned
     * state. You can, however, suspend versioning on that bucket.
     */
    enabled?: pulumi.Input<boolean>;
}
