// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.DigitalOcean
{
    /// <summary>
    /// Provides a DigitalOcean Tag resource. A Tag is a label that can be applied to a
    /// Droplet resource in order to better organize or facilitate the lookups and
    /// actions on it. Tags created with this resource can be referenced in your Droplet
    /// configuration via their ID or name.
    /// 
    /// &gt; This content is derived from https://github.com/terraform-providers/terraform-provider-digitalocean/blob/master/website/docs/r/tag.html.markdown.
    /// </summary>
    public partial class Tag : Pulumi.CustomResource
    {
        /// <summary>
        /// The name of the tag
        /// </summary>
        [Output("name")]
        public Output<string> Name { get; private set; } = null!;


        /// <summary>
        /// Create a Tag resource with the given unique name, arguments, and options.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resource</param>
        /// <param name="args">The arguments used to populate this resource's properties</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public Tag(string name, TagArgs? args = null, CustomResourceOptions? options = null)
            : base("digitalocean:index/tag:Tag", name, args ?? ResourceArgs.Empty, MakeResourceOptions(options, ""))
        {
        }

        private Tag(string name, Input<string> id, TagState? state = null, CustomResourceOptions? options = null)
            : base("digitalocean:index/tag:Tag", name, state, MakeResourceOptions(options, id))
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
        /// Get an existing Tag resource's state with the given name, ID, and optional extra
        /// properties used to qualify the lookup.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resulting resource.</param>
        /// <param name="id">The unique provider ID of the resource to lookup.</param>
        /// <param name="state">Any extra arguments used during the lookup.</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public static Tag Get(string name, Input<string> id, TagState? state = null, CustomResourceOptions? options = null)
        {
            return new Tag(name, id, state, options);
        }
    }

    public sealed class TagArgs : Pulumi.ResourceArgs
    {
        /// <summary>
        /// The name of the tag
        /// </summary>
        [Input("name")]
        public Input<string>? Name { get; set; }

        public TagArgs()
        {
        }
    }

    public sealed class TagState : Pulumi.ResourceArgs
    {
        /// <summary>
        /// The name of the tag
        /// </summary>
        [Input("name")]
        public Input<string>? Name { get; set; }

        public TagState()
        {
        }
    }
}
