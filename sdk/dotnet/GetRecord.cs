// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.DigitalOcean
{
    public static partial class Invokes
    {
        /// <summary>
        /// &gt; This content is derived from https://github.com/terraform-providers/terraform-provider-digitalocean/blob/master/website/docs/d/record.html.markdown.
        /// </summary>
        public static Task<GetRecordResult> GetRecord(GetRecordArgs args, InvokeOptions? options = null)
            => Pulumi.Deployment.Instance.InvokeAsync<GetRecordResult>("digitalocean:index/getRecord:getRecord", args ?? ResourceArgs.Empty, options.WithVersion());
    }

    public sealed class GetRecordArgs : Pulumi.ResourceArgs
    {
        /// <summary>
        /// The domain name of the record.
        /// </summary>
        [Input("domain", required: true)]
        public Input<string> Domain { get; set; } = null!;

        /// <summary>
        /// The name of the record.
        /// </summary>
        [Input("name", required: true)]
        public Input<string> Name { get; set; } = null!;

        public GetRecordArgs()
        {
        }
    }

    [OutputType]
    public sealed class GetRecordResult
    {
        public readonly string Data;
        public readonly string Domain;
        public readonly int Flags;
        public readonly string Name;
        public readonly int Port;
        public readonly int Priority;
        public readonly string Tag;
        public readonly int Ttl;
        public readonly string Type;
        public readonly int Weight;
        /// <summary>
        /// id is the provider-assigned unique ID for this managed resource.
        /// </summary>
        public readonly string Id;

        [OutputConstructor]
        private GetRecordResult(
            string data,
            string domain,
            int flags,
            string name,
            int port,
            int priority,
            string tag,
            int ttl,
            string type,
            int weight,
            string id)
        {
            Data = data;
            Domain = domain;
            Flags = flags;
            Name = name;
            Port = port;
            Priority = priority;
            Tag = tag;
            Ttl = ttl;
            Type = type;
            Weight = weight;
            Id = id;
        }
    }
}
