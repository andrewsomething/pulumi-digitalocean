// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.DigitalOcean.Inputs
{

    public sealed class KubernetesClusterNodePoolGetArgs : Pulumi.ResourceArgs
    {
        [Input("actualNodeCount")]
        public Input<int>? ActualNodeCount { get; set; }

        [Input("autoScale")]
        public Input<bool>? AutoScale { get; set; }

        /// <summary>
        /// A unique ID that can be used to identify and reference a Kubernetes cluster.
        /// </summary>
        [Input("id")]
        public Input<string>? Id { get; set; }

        [Input("labels")]
        private InputMap<string>? _labels;
        public InputMap<string> Labels
        {
            get => _labels ?? (_labels = new InputMap<string>());
            set => _labels = value;
        }

        [Input("maxNodes")]
        public Input<int>? MaxNodes { get; set; }

        [Input("minNodes")]
        public Input<int>? MinNodes { get; set; }

        /// <summary>
        /// A name for the Kubernetes cluster.
        /// </summary>
        [Input("name", required: true)]
        public Input<string> Name { get; set; } = null!;

        [Input("nodeCount")]
        public Input<int>? NodeCount { get; set; }

        [Input("nodes")]
        private InputList<Inputs.KubernetesClusterNodePoolNodeGetArgs>? _nodes;
        public InputList<Inputs.KubernetesClusterNodePoolNodeGetArgs> Nodes
        {
            get => _nodes ?? (_nodes = new InputList<Inputs.KubernetesClusterNodePoolNodeGetArgs>());
            set => _nodes = value;
        }

        [Input("size", required: true)]
        public Input<string> Size { get; set; } = null!;

        [Input("tags")]
        private InputList<string>? _tags;

        /// <summary>
        /// A list of tag names to be applied to the Kubernetes cluster.
        /// </summary>
        public InputList<string> Tags
        {
            get => _tags ?? (_tags = new InputList<string>());
            set => _tags = value;
        }

        public KubernetesClusterNodePoolGetArgs()
        {
        }
    }
}
