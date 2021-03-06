// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

package digitalocean

import (
	"github.com/pulumi/pulumi/sdk/v2/go/pulumi"
)

func GetImages(ctx *pulumi.Context, args *GetImagesArgs, opts ...pulumi.InvokeOption) (*GetImagesResult, error) {
	var rv GetImagesResult
	err := ctx.Invoke("digitalocean:index/getImages:getImages", args, &rv, opts...)
	if err != nil {
		return nil, err
	}
	return &rv, nil
}

// A collection of arguments for invoking getImages.
type GetImagesArgs struct {
	// Filter the results.
	// The `filter` block is documented below.
	Filters []GetImagesFilter `pulumi:"filters"`
	// Sort the results.
	// The `sort` block is documented below.
	Sorts []GetImagesSort `pulumi:"sorts"`
}

// A collection of values returned by getImages.
type GetImagesResult struct {
	Filters []GetImagesFilter `pulumi:"filters"`
	// The provider-assigned unique ID for this managed resource.
	Id string `pulumi:"id"`
	// A set of images satisfying any `filter` and `sort` criteria. Each image has the following attributes:
	// - `slug`: Unique text identifier of the image.
	// - `id`: The ID of the image.
	// - `name`: The name of the image.
	// - `type`: Type of the image.
	// - `distribution` - The name of the distribution of the OS of the image.
	// - `minDiskSize`: The minimum 'disk' required for the image.
	// - `sizeGigabytes`: The size of the image in GB.
	// - `private` - Is image a public image or not. Public images represent
	// Linux distributions or One-Click Applications, while non-public images represent
	// snapshots and backups and are only available within your account.
	// - `regions`: A set of the regions that the image is available in.
	// - `tags`: A set of tags applied to the image
	// - `created`: When the image was created
	// - `status`: Current status of the image
	// - `errorMessage`: Any applicable error message pertaining to the image
	// - `image` - The id of the image (legacy parameter).
	Images []GetImagesImage `pulumi:"images"`
	Sorts  []GetImagesSort  `pulumi:"sorts"`
}
