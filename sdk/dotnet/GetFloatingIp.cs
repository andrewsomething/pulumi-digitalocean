// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.Digitalocean
{
    public static partial class Invokes
    {
        /// <summary>
        /// &gt; This content is derived from https://github.com/terraform-providers/terraform-provider-digitalocean/blob/master/website/docs/d/floating_ip.html.markdown.
        /// </summary>
        public static Task<GetFloatingIpResult> GetFloatingIp(GetFloatingIpArgs args, InvokeOptions? options = null)
            => Pulumi.Deployment.Instance.InvokeAsync<GetFloatingIpResult>("digitalocean:index/getFloatingIp:getFloatingIp", args, options.WithVersion());
    }

    public sealed class GetFloatingIpArgs : Pulumi.ResourceArgs
    {
        /// <summary>
        /// The allocated IP address of the specific floating IP to retrieve.
        /// </summary>
        [Input("ipAddress", required: true)]
        public Input<string> IpAddress { get; set; } = null!;

        public GetFloatingIpArgs()
        {
        }
    }

    [OutputType]
    public sealed class GetFloatingIpResult
    {
        public readonly int DropletId;
        public readonly string IpAddress;
        public readonly string Region;
        public readonly string Urn;
        /// <summary>
        /// id is the provider-assigned unique ID for this managed resource.
        /// </summary>
        public readonly string Id;

        [OutputConstructor]
        private GetFloatingIpResult(
            int dropletId,
            string ipAddress,
            string region,
            string urn,
            string id)
        {
            DropletId = dropletId;
            IpAddress = ipAddress;
            Region = region;
            Urn = urn;
            Id = id;
        }
    }
}
