// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.DigitalOcean.Outputs
{

    [OutputType]
    public sealed class KubernetesClusterNodePool
    {
        public readonly int? ActualNodeCount;
        public readonly bool? AutoScale;
        /// <summary>
        /// A unique ID that can be used to identify and reference a Kubernetes cluster.
        /// </summary>
        public readonly string? Id;
        public readonly ImmutableDictionary<string, string>? Labels;
        public readonly int? MaxNodes;
        public readonly int? MinNodes;
        /// <summary>
        /// A name for the Kubernetes cluster.
        /// </summary>
        public readonly string Name;
        public readonly int? NodeCount;
        public readonly ImmutableArray<Outputs.KubernetesClusterNodePoolNode> Nodes;
        public readonly string Size;
        /// <summary>
        /// A list of tag names to be applied to the Kubernetes cluster.
        /// </summary>
        public readonly ImmutableArray<string> Tags;

        [OutputConstructor]
        private KubernetesClusterNodePool(
            int? actualNodeCount,

            bool? autoScale,

            string? id,

            ImmutableDictionary<string, string>? labels,

            int? maxNodes,

            int? minNodes,

            string name,

            int? nodeCount,

            ImmutableArray<Outputs.KubernetesClusterNodePoolNode> nodes,

            string size,

            ImmutableArray<string> tags)
        {
            ActualNodeCount = actualNodeCount;
            AutoScale = autoScale;
            Id = id;
            Labels = labels;
            MaxNodes = maxNodes;
            MinNodes = minNodes;
            Name = name;
            NodeCount = nodeCount;
            Nodes = nodes;
            Size = size;
            Tags = tags;
        }
    }
}
