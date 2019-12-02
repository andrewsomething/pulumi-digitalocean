// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

package digitalocean

import (
	"github.com/pkg/errors"
	"github.com/pulumi/pulumi/sdk/go/pulumi"
)

// Provides a DigitalOcean database replica resource.
//
// > This content is derived from https://github.com/terraform-providers/terraform-provider-digitalocean/blob/master/website/docs/r/database_replica.html.markdown.
type DatabaseReplica struct {
	s *pulumi.ResourceState
}

// NewDatabaseReplica registers a new resource with the given unique name, arguments, and options.
func NewDatabaseReplica(ctx *pulumi.Context,
	name string, args *DatabaseReplicaArgs, opts ...pulumi.ResourceOpt) (*DatabaseReplica, error) {
	if args == nil || args.ClusterId == nil {
		return nil, errors.New("missing required argument 'ClusterId'")
	}
	inputs := make(map[string]interface{})
	if args == nil {
		inputs["clusterId"] = nil
		inputs["name"] = nil
		inputs["region"] = nil
		inputs["size"] = nil
		inputs["tags"] = nil
	} else {
		inputs["clusterId"] = args.ClusterId
		inputs["name"] = args.Name
		inputs["region"] = args.Region
		inputs["size"] = args.Size
		inputs["tags"] = args.Tags
	}
	inputs["database"] = nil
	inputs["host"] = nil
	inputs["password"] = nil
	inputs["port"] = nil
	inputs["privateHost"] = nil
	inputs["privateUri"] = nil
	inputs["uri"] = nil
	inputs["user"] = nil
	s, err := ctx.RegisterResource("digitalocean:index/databaseReplica:DatabaseReplica", name, true, inputs, opts...)
	if err != nil {
		return nil, err
	}
	return &DatabaseReplica{s: s}, nil
}

// GetDatabaseReplica gets an existing DatabaseReplica resource's state with the given name, ID, and optional
// state properties that are used to uniquely qualify the lookup (nil if not required).
func GetDatabaseReplica(ctx *pulumi.Context,
	name string, id pulumi.ID, state *DatabaseReplicaState, opts ...pulumi.ResourceOpt) (*DatabaseReplica, error) {
	inputs := make(map[string]interface{})
	if state != nil {
		inputs["clusterId"] = state.ClusterId
		inputs["database"] = state.Database
		inputs["host"] = state.Host
		inputs["name"] = state.Name
		inputs["password"] = state.Password
		inputs["port"] = state.Port
		inputs["privateHost"] = state.PrivateHost
		inputs["privateUri"] = state.PrivateUri
		inputs["region"] = state.Region
		inputs["size"] = state.Size
		inputs["tags"] = state.Tags
		inputs["uri"] = state.Uri
		inputs["user"] = state.User
	}
	s, err := ctx.ReadResource("digitalocean:index/databaseReplica:DatabaseReplica", name, id, inputs, opts...)
	if err != nil {
		return nil, err
	}
	return &DatabaseReplica{s: s}, nil
}

// URN is this resource's unique name assigned by Pulumi.
func (r *DatabaseReplica) URN() pulumi.URNOutput {
	return r.s.URN()
}

// ID is this resource's unique identifier assigned by its provider.
func (r *DatabaseReplica) ID() pulumi.IDOutput {
	return r.s.ID()
}

// The ID of the original source database cluster.
func (r *DatabaseReplica) ClusterId() pulumi.StringOutput {
	return (pulumi.StringOutput)(r.s.State["clusterId"])
}

// Name of the replica's default database.
func (r *DatabaseReplica) Database() pulumi.StringOutput {
	return (pulumi.StringOutput)(r.s.State["database"])
}

// Database replica's hostname.
func (r *DatabaseReplica) Host() pulumi.StringOutput {
	return (pulumi.StringOutput)(r.s.State["host"])
}

// The name for the database replica.
func (r *DatabaseReplica) Name() pulumi.StringOutput {
	return (pulumi.StringOutput)(r.s.State["name"])
}

// Password for the replica's default user.
func (r *DatabaseReplica) Password() pulumi.StringOutput {
	return (pulumi.StringOutput)(r.s.State["password"])
}

// Network port that the database replica is listening on.
func (r *DatabaseReplica) Port() pulumi.IntOutput {
	return (pulumi.IntOutput)(r.s.State["port"])
}

// Same as `host`, but only accessible from resources within the account and in the same region.
func (r *DatabaseReplica) PrivateHost() pulumi.StringOutput {
	return (pulumi.StringOutput)(r.s.State["privateHost"])
}

// Same as `uri`, but only accessible from resources within the account and in the same region.
func (r *DatabaseReplica) PrivateUri() pulumi.StringOutput {
	return (pulumi.StringOutput)(r.s.State["privateUri"])
}

// DigitalOcean region where the replica will reside.
func (r *DatabaseReplica) Region() pulumi.StringOutput {
	return (pulumi.StringOutput)(r.s.State["region"])
}

// Database Droplet size associated with the replica (ex. `db-s-1vcpu-1gb`).
func (r *DatabaseReplica) Size() pulumi.StringOutput {
	return (pulumi.StringOutput)(r.s.State["size"])
}

func (r *DatabaseReplica) Tags() pulumi.ArrayOutput {
	return (pulumi.ArrayOutput)(r.s.State["tags"])
}

// The full URI for connecting to the database replica.
func (r *DatabaseReplica) Uri() pulumi.StringOutput {
	return (pulumi.StringOutput)(r.s.State["uri"])
}

// Username for the replica's default user.
func (r *DatabaseReplica) User() pulumi.StringOutput {
	return (pulumi.StringOutput)(r.s.State["user"])
}

// Input properties used for looking up and filtering DatabaseReplica resources.
type DatabaseReplicaState struct {
	// The ID of the original source database cluster.
	ClusterId interface{}
	// Name of the replica's default database.
	Database interface{}
	// Database replica's hostname.
	Host interface{}
	// The name for the database replica.
	Name interface{}
	// Password for the replica's default user.
	Password interface{}
	// Network port that the database replica is listening on.
	Port interface{}
	// Same as `host`, but only accessible from resources within the account and in the same region.
	PrivateHost interface{}
	// Same as `uri`, but only accessible from resources within the account and in the same region.
	PrivateUri interface{}
	// DigitalOcean region where the replica will reside.
	Region interface{}
	// Database Droplet size associated with the replica (ex. `db-s-1vcpu-1gb`).
	Size interface{}
	Tags interface{}
	// The full URI for connecting to the database replica.
	Uri interface{}
	// Username for the replica's default user.
	User interface{}
}

// The set of arguments for constructing a DatabaseReplica resource.
type DatabaseReplicaArgs struct {
	// The ID of the original source database cluster.
	ClusterId interface{}
	// The name for the database replica.
	Name interface{}
	// DigitalOcean region where the replica will reside.
	Region interface{}
	// Database Droplet size associated with the replica (ex. `db-s-1vcpu-1gb`).
	Size interface{}
	Tags interface{}
}
