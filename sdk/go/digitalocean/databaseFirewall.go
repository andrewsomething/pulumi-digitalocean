// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

package digitalocean

import (
	"github.com/pkg/errors"
	"github.com/pulumi/pulumi/sdk/go/pulumi"
)

// Provides a DigitalOcean database firewall resource allowing you to restrict
// connections to your database to trusted sources. You may limit connections to
// specific Droplets, Kubernetes clusters, or IP addresses.
//
// > This content is derived from https://github.com/terraform-providers/terraform-provider-digitalocean/blob/master/website/docs/r/database_firewall.html.markdown.
type DatabaseFirewall struct {
	s *pulumi.ResourceState
}

// NewDatabaseFirewall registers a new resource with the given unique name, arguments, and options.
func NewDatabaseFirewall(ctx *pulumi.Context,
	name string, args *DatabaseFirewallArgs, opts ...pulumi.ResourceOpt) (*DatabaseFirewall, error) {
	if args == nil || args.ClusterId == nil {
		return nil, errors.New("missing required argument 'ClusterId'")
	}
	if args == nil || args.Rules == nil {
		return nil, errors.New("missing required argument 'Rules'")
	}
	inputs := make(map[string]interface{})
	if args == nil {
		inputs["clusterId"] = nil
		inputs["rules"] = nil
	} else {
		inputs["clusterId"] = args.ClusterId
		inputs["rules"] = args.Rules
	}
	s, err := ctx.RegisterResource("digitalocean:index:DatabaseFirewall", name, true, inputs, opts...)
	if err != nil {
		return nil, err
	}
	return &DatabaseFirewall{s: s}, nil
}

// GetDatabaseFirewall gets an existing DatabaseFirewall resource's state with the given name, ID, and optional
// state properties that are used to uniquely qualify the lookup (nil if not required).
func GetDatabaseFirewall(ctx *pulumi.Context,
	name string, id pulumi.ID, state *DatabaseFirewallState, opts ...pulumi.ResourceOpt) (*DatabaseFirewall, error) {
	inputs := make(map[string]interface{})
	if state != nil {
		inputs["clusterId"] = state.ClusterId
		inputs["rules"] = state.Rules
	}
	s, err := ctx.ReadResource("digitalocean:index:DatabaseFirewall", name, id, inputs, opts...)
	if err != nil {
		return nil, err
	}
	return &DatabaseFirewall{s: s}, nil
}

// URN is this resource's unique name assigned by Pulumi.
func (r *DatabaseFirewall) URN() pulumi.URNOutput {
	return r.s.URN()
}

// ID is this resource's unique identifier assigned by its provider.
func (r *DatabaseFirewall) ID() pulumi.IDOutput {
	return r.s.ID()
}

// The ID of the target database cluster.
func (r *DatabaseFirewall) ClusterId() pulumi.StringOutput {
	return (pulumi.StringOutput)(r.s.State["clusterId"])
}

// A rule specifying a resource allowed to access the database cluster. The following arguments must be specified:
// - `type` - (Required) The type of resource that the firewall rule allows to access the database cluster. The possible values are: `droplet`, `k8s`, `ipAddr`, or `tag`.
// - `value` - (Required) The ID of the specific resource, the name of a tag applied to a group of resources, or the IP address that the firewall rule allows to access the database cluster.
func (r *DatabaseFirewall) Rules() pulumi.ArrayOutput {
	return (pulumi.ArrayOutput)(r.s.State["rules"])
}

// Input properties used for looking up and filtering DatabaseFirewall resources.
type DatabaseFirewallState struct {
	// The ID of the target database cluster.
	ClusterId interface{}
	// A rule specifying a resource allowed to access the database cluster. The following arguments must be specified:
	// - `type` - (Required) The type of resource that the firewall rule allows to access the database cluster. The possible values are: `droplet`, `k8s`, `ipAddr`, or `tag`.
	// - `value` - (Required) The ID of the specific resource, the name of a tag applied to a group of resources, or the IP address that the firewall rule allows to access the database cluster.
	Rules interface{}
}

// The set of arguments for constructing a DatabaseFirewall resource.
type DatabaseFirewallArgs struct {
	// The ID of the target database cluster.
	ClusterId interface{}
	// A rule specifying a resource allowed to access the database cluster. The following arguments must be specified:
	// - `type` - (Required) The type of resource that the firewall rule allows to access the database cluster. The possible values are: `droplet`, `k8s`, `ipAddr`, or `tag`.
	// - `value` - (Required) The ID of the specific resource, the name of a tag applied to a group of resources, or the IP address that the firewall rule allows to access the database cluster.
	Rules interface{}
}