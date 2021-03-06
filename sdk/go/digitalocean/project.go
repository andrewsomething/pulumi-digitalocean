// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

package digitalocean

import (
	"reflect"

	"github.com/pulumi/pulumi/sdk/v2/go/pulumi"
)

type Project struct {
	pulumi.CustomResourceState

	// the date and time when the project was created, (ISO8601)
	CreatedAt pulumi.StringOutput `pulumi:"createdAt"`
	// the description of the project
	Description pulumi.StringPtrOutput `pulumi:"description"`
	// the environment of the project's resources. The possible values are: `Development`, `Staging`, `Production`)
	Environment pulumi.StringPtrOutput `pulumi:"environment"`
	IsDefault   pulumi.BoolOutput      `pulumi:"isDefault"`
	// The name of the Project
	Name pulumi.StringOutput `pulumi:"name"`
	// the id of the project owner.
	OwnerId pulumi.IntOutput `pulumi:"ownerId"`
	// the unique universal identifier of the project owner.
	OwnerUuid pulumi.StringOutput `pulumi:"ownerUuid"`
	// the purpose of the project, (Default: "Web Application")
	Purpose pulumi.StringPtrOutput `pulumi:"purpose"`
	// a list of uniform resource names (URNs) for the resources associated with the project
	Resources pulumi.StringArrayOutput `pulumi:"resources"`
	// the date and time when the project was last updated, (ISO8601)
	UpdatedAt pulumi.StringOutput `pulumi:"updatedAt"`
}

// NewProject registers a new resource with the given unique name, arguments, and options.
func NewProject(ctx *pulumi.Context,
	name string, args *ProjectArgs, opts ...pulumi.ResourceOption) (*Project, error) {
	if args == nil {
		args = &ProjectArgs{}
	}
	var resource Project
	err := ctx.RegisterResource("digitalocean:index/project:Project", name, args, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// GetProject gets an existing Project resource's state with the given name, ID, and optional
// state properties that are used to uniquely qualify the lookup (nil if not required).
func GetProject(ctx *pulumi.Context,
	name string, id pulumi.IDInput, state *ProjectState, opts ...pulumi.ResourceOption) (*Project, error) {
	var resource Project
	err := ctx.ReadResource("digitalocean:index/project:Project", name, id, state, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// Input properties used for looking up and filtering Project resources.
type projectState struct {
	// the date and time when the project was created, (ISO8601)
	CreatedAt *string `pulumi:"createdAt"`
	// the description of the project
	Description *string `pulumi:"description"`
	// the environment of the project's resources. The possible values are: `Development`, `Staging`, `Production`)
	Environment *string `pulumi:"environment"`
	IsDefault   *bool   `pulumi:"isDefault"`
	// The name of the Project
	Name *string `pulumi:"name"`
	// the id of the project owner.
	OwnerId *int `pulumi:"ownerId"`
	// the unique universal identifier of the project owner.
	OwnerUuid *string `pulumi:"ownerUuid"`
	// the purpose of the project, (Default: "Web Application")
	Purpose *string `pulumi:"purpose"`
	// a list of uniform resource names (URNs) for the resources associated with the project
	Resources []string `pulumi:"resources"`
	// the date and time when the project was last updated, (ISO8601)
	UpdatedAt *string `pulumi:"updatedAt"`
}

type ProjectState struct {
	// the date and time when the project was created, (ISO8601)
	CreatedAt pulumi.StringPtrInput
	// the description of the project
	Description pulumi.StringPtrInput
	// the environment of the project's resources. The possible values are: `Development`, `Staging`, `Production`)
	Environment pulumi.StringPtrInput
	IsDefault   pulumi.BoolPtrInput
	// The name of the Project
	Name pulumi.StringPtrInput
	// the id of the project owner.
	OwnerId pulumi.IntPtrInput
	// the unique universal identifier of the project owner.
	OwnerUuid pulumi.StringPtrInput
	// the purpose of the project, (Default: "Web Application")
	Purpose pulumi.StringPtrInput
	// a list of uniform resource names (URNs) for the resources associated with the project
	Resources pulumi.StringArrayInput
	// the date and time when the project was last updated, (ISO8601)
	UpdatedAt pulumi.StringPtrInput
}

func (ProjectState) ElementType() reflect.Type {
	return reflect.TypeOf((*projectState)(nil)).Elem()
}

type projectArgs struct {
	// the description of the project
	Description *string `pulumi:"description"`
	// the environment of the project's resources. The possible values are: `Development`, `Staging`, `Production`)
	Environment *string `pulumi:"environment"`
	// The name of the Project
	Name *string `pulumi:"name"`
	// the purpose of the project, (Default: "Web Application")
	Purpose *string `pulumi:"purpose"`
	// a list of uniform resource names (URNs) for the resources associated with the project
	Resources []string `pulumi:"resources"`
}

// The set of arguments for constructing a Project resource.
type ProjectArgs struct {
	// the description of the project
	Description pulumi.StringPtrInput
	// the environment of the project's resources. The possible values are: `Development`, `Staging`, `Production`)
	Environment pulumi.StringPtrInput
	// The name of the Project
	Name pulumi.StringPtrInput
	// the purpose of the project, (Default: "Web Application")
	Purpose pulumi.StringPtrInput
	// a list of uniform resource names (URNs) for the resources associated with the project
	Resources pulumi.StringArrayInput
}

func (ProjectArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*projectArgs)(nil)).Elem()
}
