// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.DigitalOcean
{
    public static class GetFloatingIp
    {
        public static Task<GetFloatingIpResult> InvokeAsync(GetFloatingIpArgs args, InvokeOptions? options = null)
            => Pulumi.Deployment.Instance.InvokeAsync<GetFloatingIpResult>("digitalocean:index/getFloatingIp:getFloatingIp", args ?? new GetFloatingIpArgs(), options.WithVersion());
    }


    public sealed class GetFloatingIpArgs : Pulumi.InvokeArgs
    {
        /// <summary>
        /// The allocated IP address of the specific floating IP to retrieve.
        /// </summary>
        [Input("ipAddress", required: true)]
        public string IpAddress { get; set; } = null!;

        public GetFloatingIpArgs()
        {
        }
    }


    [OutputType]
    public sealed class GetFloatingIpResult
    {
        public readonly int DropletId;
        /// <summary>
        /// The provider-assigned unique ID for this managed resource.
        /// </summary>
        public readonly string Id;
        public readonly string IpAddress;
        public readonly string Region;
        public readonly string Urn;

        [OutputConstructor]
        private GetFloatingIpResult(
            int dropletId,

            string id,

            string ipAddress,

            string region,

            string urn)
        {
            DropletId = dropletId;
            Id = id;
            IpAddress = ipAddress;
            Region = region;
            Urn = urn;
        }
    }
}
