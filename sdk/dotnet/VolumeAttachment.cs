// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.DigitalOcean
{
    /// <summary>
    /// Manages attaching a Volume to a Droplet.
    /// 
    /// &gt; **NOTE:** Volumes can be attached either directly on the `digitalocean..Droplet` resource, or using the `digitalocean..VolumeAttachment` resource - but the two cannot be used together. If both are used against the same Droplet, the volume attachments will constantly drift.
    /// 
    /// &gt; This content is derived from https://github.com/terraform-providers/terraform-provider-digitalocean/blob/master/website/docs/r/volume_attachment.html.markdown.
    /// </summary>
    public partial class VolumeAttachment : Pulumi.CustomResource
    {
        /// <summary>
        /// ID of the Droplet to attach the volume to.
        /// </summary>
        [Output("dropletId")]
        public Output<int> DropletId { get; private set; } = null!;

        /// <summary>
        /// ID of the Volume to be attached to the Droplet.
        /// </summary>
        [Output("volumeId")]
        public Output<string> VolumeId { get; private set; } = null!;


        /// <summary>
        /// Create a VolumeAttachment resource with the given unique name, arguments, and options.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resource</param>
        /// <param name="args">The arguments used to populate this resource's properties</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public VolumeAttachment(string name, VolumeAttachmentArgs args, CustomResourceOptions? options = null)
            : base("digitalocean:index/volumeAttachment:VolumeAttachment", name, args ?? ResourceArgs.Empty, MakeResourceOptions(options, ""))
        {
        }

        private VolumeAttachment(string name, Input<string> id, VolumeAttachmentState? state = null, CustomResourceOptions? options = null)
            : base("digitalocean:index/volumeAttachment:VolumeAttachment", name, state, MakeResourceOptions(options, id))
        {
        }

        private static CustomResourceOptions MakeResourceOptions(CustomResourceOptions? options, Input<string>? id)
        {
            var defaultOptions = new CustomResourceOptions
            {
                Version = Utilities.Version,
            };
            var merged = CustomResourceOptions.Merge(defaultOptions, options);
            // Override the ID if one was specified for consistency with other language SDKs.
            merged.Id = id ?? merged.Id;
            return merged;
        }
        /// <summary>
        /// Get an existing VolumeAttachment resource's state with the given name, ID, and optional extra
        /// properties used to qualify the lookup.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resulting resource.</param>
        /// <param name="id">The unique provider ID of the resource to lookup.</param>
        /// <param name="state">Any extra arguments used during the lookup.</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public static VolumeAttachment Get(string name, Input<string> id, VolumeAttachmentState? state = null, CustomResourceOptions? options = null)
        {
            return new VolumeAttachment(name, id, state, options);
        }
    }

    public sealed class VolumeAttachmentArgs : Pulumi.ResourceArgs
    {
        /// <summary>
        /// ID of the Droplet to attach the volume to.
        /// </summary>
        [Input("dropletId", required: true)]
        public Input<int> DropletId { get; set; } = null!;

        /// <summary>
        /// ID of the Volume to be attached to the Droplet.
        /// </summary>
        [Input("volumeId", required: true)]
        public Input<string> VolumeId { get; set; } = null!;

        public VolumeAttachmentArgs()
        {
        }
    }

    public sealed class VolumeAttachmentState : Pulumi.ResourceArgs
    {
        /// <summary>
        /// ID of the Droplet to attach the volume to.
        /// </summary>
        [Input("dropletId")]
        public Input<int>? DropletId { get; set; }

        /// <summary>
        /// ID of the Volume to be attached to the Droplet.
        /// </summary>
        [Input("volumeId")]
        public Input<string>? VolumeId { get; set; }

        public VolumeAttachmentState()
        {
        }
    }
}
