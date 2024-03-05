#!/usr/bin/python
# Copyright (c) 2020, 2024 Oracle and/or its affiliates.
# This software is made available to you under the terms of the GPL 3.0 license or the Apache 2.0 license.
# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)
# Apache License v2.0
# See LICENSE.TXT for details.
# GENERATED FILE - DO NOT EDIT - MANUAL CHANGES WILL BE OVERWRITTEN


from __future__ import absolute_import, division, print_function

__metaclass__ = type

ANSIBLE_METADATA = {
    "metadata_version": "1.1",
    "status": ["preview"],
    "supported_by": "community",
}

DOCUMENTATION = """
---
module: oci_compute_management_instance_configuration_actions
short_description: Perform actions on an InstanceConfiguration resource in Oracle Cloud Infrastructure
description:
    - Perform actions on an InstanceConfiguration resource in Oracle Cloud Infrastructure
    - "For I(action=change_compartment), moves an instance configuration into a different compartment within the same tenancy.
      For information about moving resources between compartments, see
      L(Moving Resources to a Different Compartment,https://docs.cloud.oracle.com/iaas/Content/Identity/Tasks/managingcompartments.htm#moveRes).
      When you move an instance configuration to a different compartment, associated resources such as
      instance pools are not moved.
      **Important:** Most of the properties for an existing instance configuration, including the compartment,
      cannot be modified after you create the instance configuration. Although you can move an instance configuration
      to a different compartment, you will not be able to use the instance configuration to manage instance pools
      in the new compartment. If you want to update an instance configuration to point to a different compartment,
      you should instead create a new instance configuration in the target compartment using
      L(CreateInstanceConfiguration,https://docs.cloud.oracle.com/iaas/api/#/en/iaas/20160918/InstanceConfiguration/CreateInstanceConfiguration)."
    - For I(action=launch), creates an instance from an instance configuration.
      If the instance configuration does not include all of the parameters that are
      required to create an instance, such as the availability domain and subnet ID, you must
      provide these parameters when you create an instance from the instance configuration.
      For more information, see the L(InstanceConfiguration,https://docs.cloud.oracle.com/en-us/iaas/api/#/en/iaas/latest/InstanceConfiguration/)
      resource.
      To determine whether capacity is available for a specific shape before you create an instance,
      use the L(CreateComputeCapacityReport,https://docs.cloud.oracle.com/en-us/iaas/api/#/en/iaas/latest/ComputeCapacityReport/CreateComputeCapacityReport)
      operation.
version_added: "2.9.0"
author: Oracle (@oracle)
options:
    compartment_id:
        description:
            - The L(OCID,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the compartment to
              move the instance configuration to.
            - Required for I(action=change_compartment).
        type: str
    instance_configuration_id:
        description:
            - The OCID of the instance configuration.
        type: str
        aliases: ["id"]
        required: true
    options:
        description:
            - The Compute Instance Configuration parameters.
            - Applicable only for I(action=launch).
            - Applicable when instance_type is 'instance_options'
        type: list
        elements: dict
        suboptions:
            instance_type:
                description:
                    - The type of instance details. Supported instanceType is compute
                    - Required when instance_type is 'instance_options'
                type: str
                required: true
            block_volumes:
                description:
                    - Block volume parameters.
                    - Applicable when instance_type is 'instance_options'
                type: list
                elements: dict
                suboptions:
                    attach_details:
                        description:
                            - ""
                            - Applicable when instance_type is 'instance_options'
                        type: dict
                        suboptions:
                            use_chap:
                                description:
                                    - Whether to use CHAP authentication for the volume attachment. Defaults to false.
                                    - Applicable when type is 'iscsi'
                                type: bool
                            display_name:
                                description:
                                    - A user-friendly name. Does not have to be unique, and it's changeable.
                                      Avoid entering confidential information.
                                type: str
                                aliases: ["name"]
                            is_read_only:
                                description:
                                    - Whether the attachment should be created in read-only mode.
                                type: bool
                            device:
                                description:
                                    - The device name.
                                type: str
                            is_shareable:
                                description:
                                    - Whether the attachment should be created in shareable mode. If an attachment
                                      is created in shareable mode, then other instances can attach the same volume, provided
                                      that they also create their attachments in shareable mode. Only certain volume types can
                                      be attached in shareable mode. Defaults to false if not specified.
                                type: bool
                            type:
                                description:
                                    - "The type of volume. The only supported values are \\"iscsi\\" and \\"paravirtualized\\"."
                                type: str
                                choices:
                                    - "iscsi"
                                    - "paravirtualized"
                                required: true
                            is_pv_encryption_in_transit_enabled:
                                description:
                                    - Whether to enable in-transit encryption for the data volume's paravirtualized attachment. The default value is false.
                                    - Applicable when type is 'paravirtualized'
                                type: bool
                    create_details:
                        description:
                            - ""
                            - Applicable when instance_type is 'instance_options'
                        type: dict
                        suboptions:
                            availability_domain:
                                description:
                                    - The availability domain of the volume.
                                    - "Example: `Uocm:PHX-AD-1`"
                                    - Applicable when instance_type is 'instance_options'
                                type: str
                            backup_policy_id:
                                description:
                                    - If provided, specifies the ID of the volume backup policy to assign to the newly
                                      created volume. If omitted, no policy will be assigned.
                                    - Applicable when instance_type is 'instance_options'
                                type: str
                            compartment_id:
                                description:
                                    - The OCID of the compartment that contains the volume.
                                    - Applicable when instance_type is 'instance_options'
                                type: str
                            is_auto_tune_enabled:
                                description:
                                    - Specifies whether the auto-tune performance is enabled for this boot volume. This field is deprecated.
                                      Use the `InstanceConfigurationDetachedVolumeAutotunePolicy` instead to enable the volume for detached autotune.
                                    - Applicable when instance_type is 'instance_options'
                                type: bool
                            block_volume_replicas:
                                description:
                                    - The list of block volume replicas to be enabled for this volume
                                      in the specified destination availability domains.
                                    - Applicable when instance_type is 'instance_options'
                                type: list
                                elements: dict
                                suboptions:
                                    display_name:
                                        description:
                                            - "The display name of the block volume replica. You may optionally specify a *display name* for
                                              the block volume replica, otherwise a default is provided."
                                            - Applicable when instance_type is 'instance_options'
                                        type: str
                                        aliases: ["name"]
                                    availability_domain:
                                        description:
                                            - The availability domain of the block volume replica.
                                            - "Example: `Uocm:PHX-AD-1`"
                                            - Required when instance_type is 'instance_options'
                                        type: str
                                        required: true
                            defined_tags:
                                description:
                                    - Defined tags for this resource. Each key is predefined and scoped to a
                                      namespace. For more information, see L(Resource
                                      Tags,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/resourcetags.htm).
                                    - "Example: `{\\"Operations\\": {\\"CostCenter\\": \\"42\\"}}`"
                                    - Applicable when instance_type is 'instance_options'
                                type: dict
                            display_name:
                                description:
                                    - A user-friendly name. Does not have to be unique, and it's changeable.
                                      Avoid entering confidential information.
                                    - Applicable when instance_type is 'instance_options'
                                type: str
                                aliases: ["name"]
                            freeform_tags:
                                description:
                                    - Free-form tags for this resource. Each tag is a simple key-value pair with no
                                      predefined name, type, or namespace. For more information, see L(Resource
                                      Tags,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/resourcetags.htm).
                                    - "Example: `{\\"Department\\": \\"Finance\\"}`"
                                    - Applicable when instance_type is 'instance_options'
                                type: dict
                            kms_key_id:
                                description:
                                    - The OCID of the Vault service key to assign as the master encryption key
                                      for the volume.
                                    - Applicable when instance_type is 'instance_options'
                                type: str
                            vpus_per_gb:
                                description:
                                    - The number of volume performance units (VPUs) that will be applied to this volume per GB,
                                      representing the Block Volume service's elastic performance options.
                                      See L(Block Volume Performance
                                      Levels,https://docs.cloud.oracle.com/iaas/Content/Block/Concepts/blockvolumeperformance.htm#perf_levels) for more
                                      information.
                                    - "Allowed values:"
                                    - " * `0`: Represents Lower Cost option."
                                    - " * `10`: Represents Balanced option."
                                    - " * `20`: Represents Higher Performance option."
                                    - " * `30`-`120`: Represents the Ultra High Performance option."
                                    - For performance autotune enabled volumes, it would be the Default(Minimum) VPUs/GB.
                                    - Applicable when instance_type is 'instance_options'
                                type: int
                            size_in_gbs:
                                description:
                                    - The size of the volume in GBs.
                                    - Applicable when instance_type is 'instance_options'
                                type: int
                            source_details:
                                description:
                                    - ""
                                    - Applicable when instance_type is 'instance_options'
                                type: dict
                                suboptions:
                                    type:
                                        description:
                                            - ""
                                        type: str
                                        choices:
                                            - "volumeBackup"
                                            - "volume"
                                        required: true
                                    id:
                                        description:
                                            - The OCID of the volume backup.
                                        type: str
                            autotune_policies:
                                description:
                                    - The list of autotune policies enabled for this volume.
                                    - Applicable when instance_type is 'instance_options'
                                type: list
                                elements: dict
                                suboptions:
                                    max_vpus_per_gb:
                                        description:
                                            - This will be the maximum VPUs/GB performance level that the volume will be auto-tuned
                                              temporarily based on performance monitoring.
                                            - Required when autotune_type is 'PERFORMANCE_BASED'
                                        type: int
                                    autotune_type:
                                        description:
                                            - This specifies the type of autotunes supported by OCI.
                                        type: str
                                        choices:
                                            - "PERFORMANCE_BASED"
                                            - "DETACHED_VOLUME"
                                        required: true
                    volume_id:
                        description:
                            - The OCID of the volume.
                            - Applicable when instance_type is 'instance_options'
                        type: str
            launch_details:
                description:
                    - ""
                    - Applicable when instance_type is 'instance_options'
                type: dict
                suboptions:
                    availability_domain:
                        description:
                            - The availability domain of the instance.
                            - "Example: `Uocm:PHX-AD-1`"
                            - Applicable when instance_type is 'instance_options'
                        type: str
                    capacity_reservation_id:
                        description:
                            - The OCID of the compute capacity reservation this instance is launched under.
                            - Applicable when instance_type is 'instance_options'
                        type: str
                    compartment_id:
                        description:
                            - The OCID of the compartment containing the instance.
                              Instances created from instance configurations are placed in the same compartment
                              as the instance that was used to create the instance configuration.
                            - Applicable when instance_type is 'instance_options'
                        type: str
                    create_vnic_details:
                        description:
                            - ""
                            - Applicable when instance_type is 'instance_options'
                        type: dict
                        suboptions:
                            assign_public_ip:
                                description:
                                    - Whether the VNIC should be assigned a public IP address. See the `assignPublicIp` attribute of
                                      L(CreateVnicDetails,https://docs.cloud.oracle.com/en-us/iaas/api/#/en/iaas/latest/CreateVnicDetails/)
                                      for more information.
                                    - Applicable when instance_type is 'instance_options'
                                type: bool
                            assign_private_dns_record:
                                description:
                                    - Whether the VNIC should be assigned a private DNS record. See the `assignPrivateDnsRecord` attribute of
                                      L(CreateVnicDetails,https://docs.cloud.oracle.com/en-us/iaas/api/#/en/iaas/latest/CreateVnicDetails/)
                                      for more information.
                                    - Applicable when instance_type is 'instance_options'
                                type: bool
                            defined_tags:
                                description:
                                    - Defined tags for this resource. Each key is predefined and scoped to a
                                      namespace. For more information, see L(Resource
                                      Tags,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/resourcetags.htm).
                                    - "Example: `{\\"Operations\\": {\\"CostCenter\\": \\"42\\"}}`"
                                    - Applicable when instance_type is 'instance_options'
                                type: dict
                            display_name:
                                description:
                                    - A user-friendly name. Does not have to be unique, and it's changeable.
                                      Avoid entering confidential information.
                                    - Applicable when instance_type is 'instance_options'
                                type: str
                                aliases: ["name"]
                            freeform_tags:
                                description:
                                    - Free-form tags for this resource. Each tag is a simple key-value pair with no
                                      predefined name, type, or namespace. For more information, see L(Resource
                                      Tags,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/resourcetags.htm).
                                    - "Example: `{\\"Department\\": \\"Finance\\"}`"
                                    - Applicable when instance_type is 'instance_options'
                                type: dict
                            hostname_label:
                                description:
                                    - The hostname for the VNIC's primary private IP.
                                      See the `hostnameLabel` attribute of L(CreateVnicDetails,https://docs.cloud.oracle.com/en-
                                      us/iaas/api/#/en/iaas/latest/CreateVnicDetails/) for more information.
                                    - Applicable when instance_type is 'instance_options'
                                type: str
                            nsg_ids:
                                description:
                                    - A list of the OCIDs of the network security groups (NSGs) to add the VNIC to. For more
                                      information about NSGs, see
                                      L(NetworkSecurityGroup,https://docs.cloud.oracle.com/en-us/iaas/api/#/en/iaas/latest/NetworkSecurityGroup/).
                                    - Applicable when instance_type is 'instance_options'
                                type: list
                                elements: str
                            private_ip:
                                description:
                                    - A private IP address of your choice to assign to the VNIC.
                                      See the `privateIp` attribute of L(CreateVnicDetails,https://docs.cloud.oracle.com/en-
                                      us/iaas/api/#/en/iaas/latest/CreateVnicDetails/) for more information.
                                    - Applicable when instance_type is 'instance_options'
                                type: str
                            skip_source_dest_check:
                                description:
                                    - Whether the source/destination check is disabled on the VNIC.
                                      See the `skipSourceDestCheck` attribute of L(CreateVnicDetails,https://docs.cloud.oracle.com/en-
                                      us/iaas/api/#/en/iaas/latest/CreateVnicDetails/) for more information.
                                    - Applicable when instance_type is 'instance_options'
                                type: bool
                            subnet_id:
                                description:
                                    - The OCID of the subnet to create the VNIC in.
                                      See the `subnetId` attribute of L(CreateVnicDetails,https://docs.cloud.oracle.com/en-
                                      us/iaas/api/#/en/iaas/latest/CreateVnicDetails/) for more information.
                                    - Applicable when instance_type is 'instance_options'
                                type: str
                    defined_tags:
                        description:
                            - Defined tags for this resource. Each key is predefined and scoped to a
                              namespace. For more information, see L(Resource
                              Tags,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/resourcetags.htm).
                            - "Example: `{\\"Operations\\": {\\"CostCenter\\": \\"42\\"}}`"
                            - Applicable when instance_type is 'instance_options'
                        type: dict
                    display_name:
                        description:
                            - A user-friendly name. Does not have to be unique, and it's changeable.
                              Avoid entering confidential information.
                            - Applicable when instance_type is 'instance_options'
                        type: str
                        aliases: ["name"]
                    extended_metadata:
                        description:
                            - Additional metadata key/value pairs that you provide. They serve the same purpose and
                              functionality as fields in the `metadata` object.
                            - They are distinguished from `metadata` fields in that these can be nested JSON objects
                              (whereas `metadata` fields are string/string maps only).
                            - The combined size of the `metadata` and `extendedMetadata` objects can be a maximum of
                              32,000 bytes.
                            - Applicable when instance_type is 'instance_options'
                        type: dict
                    freeform_tags:
                        description:
                            - Free-form tags for this resource. Each tag is a simple key-value pair with no
                              predefined name, type, or namespace. For more information, see L(Resource
                              Tags,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/resourcetags.htm).
                            - "Example: `{\\"Department\\": \\"Finance\\"}`"
                            - Applicable when instance_type is 'instance_options'
                        type: dict
                    ipxe_script:
                        description:
                            - This is an advanced option.
                            - When a bare metal or virtual machine
                              instance boots, the iPXE firmware that runs on the instance is
                              configured to run an iPXE script to continue the boot process.
                            - If you want more control over the boot process, you can provide
                              your own custom iPXE script that will run when the instance boots;
                              however, you should be aware that the same iPXE script will run
                              every time an instance boots; not only after the initial
                              LaunchInstance call.
                            - "The default iPXE script connects to the instance's local boot
                              volume over iSCSI and performs a network boot. If you use a custom iPXE
                              script and want to network-boot from the instance's local boot volume
                              over iSCSI the same way as the default iPXE script, you should use the
                              following iSCSI IP address: 169.254.0.2, and boot volume IQN:
                              iqn.2015-02.oracle.boot."
                            - For more information about the Bring Your Own Image feature of
                              Oracle Cloud Infrastructure, see
                              L(Bring Your Own Image,https://docs.cloud.oracle.com/iaas/Content/Compute/References/bringyourownimage.htm).
                            - For more information about iPXE, see http://ipxe.org.
                            - Applicable when instance_type is 'instance_options'
                        type: str
                    metadata:
                        description:
                            - Custom metadata key/value pairs that you provide, such as the SSH public key
                              required to connect to the instance.
                            - "A metadata service runs on every launched instance. The service is an HTTP
                              endpoint listening on 169.254.169.254. You can use the service to:"
                            - "* Provide information to L(Cloud-Init,https://cloudinit.readthedocs.org/en/latest/)
                                to be used for various system initialization tasks."
                            - "* Get information about the instance, including the custom metadata that you
                                provide when you launch the instance."
                            - "**Providing Cloud-Init Metadata**"
                            - "You can use the following metadata key names to provide information to
                               Cloud-Init:"
                            - "**\\"ssh_authorized_keys\\"** - Provide one or more public SSH keys to be
                               included in the `~/.ssh/authorized_keys` file for the default user on the
                               instance. Use a newline character to separate multiple keys. The SSH
                               keys must be in the format necessary for the `authorized_keys` file, as shown
                               in the example below."
                            - "**\\"user_data\\"** - Provide your own base64-encoded data to be used by
                               Cloud-Init to run custom scripts or provide custom Cloud-Init configuration. For
                               information about how to take advantage of user data, see the
                               L(Cloud-Init Documentation,http://cloudinit.readthedocs.org/en/latest/topics/format.html)."
                            - "**Metadata Example**"
                            - "     \\"metadata\\" : {
                                       \\"quake_bot_level\\" : \\"Severe\\",
                                       \\"ssh_authorized_keys\\" : \\"ssh-rsa <your_public_SSH_key>== rsa-key-20160227\\",
                                       \\"user_data\\" : \\"<your_public_SSH_key>==\\"
                                    }
                               **Getting Metadata on the Instance**"
                            - "To get information about your instance, connect to the instance using SSH and issue any of the
                               following GET requests:"
                            - "    curl -H \\"Authorization: Bearer Oracle\\" http://169.254.169.254/opc/v2/instance/
                                   curl -H \\"Authorization: Bearer Oracle\\" http://169.254.169.254/opc/v2/instance/metadata/
                                   curl -H \\"Authorization: Bearer Oracle\\" http://169.254.169.254/opc/v2/instance/metadata/<any-key-name>"
                            -  You'll get back a response that includes all the instance information; only the metadata information; or
                               the metadata information for the specified key name, respectively.
                            -  The combined size of the `metadata` and `extendedMetadata` objects can be a maximum of 32,000 bytes.
                            - Applicable when instance_type is 'instance_options'
                        type: dict
                    shape:
                        description:
                            - The shape of an instance. The shape determines the number of CPUs, amount of memory,
                              and other resources allocated to the instance.
                            - You can enumerate all available shapes by calling L(ListShapes,https://docs.cloud.oracle.com/en-
                              us/iaas/api/#/en/iaas/latest/Shape/ListShapes).
                            - Applicable when instance_type is 'instance_options'
                        type: str
                    shape_config:
                        description:
                            - ""
                            - Applicable when instance_type is 'instance_options'
                        type: dict
                        suboptions:
                            ocpus:
                                description:
                                    - The total number of OCPUs available to the instance.
                                    - Applicable when instance_type is 'instance_options'
                                type: float
                            vcpus:
                                description:
                                    - The total number of VCPUs available to the instance. This can be used instead of OCPUs,
                                      in which case the actual number of OCPUs will be calculated based on this value
                                      and the actual hardware. This must be a multiple of 2.
                                    - Applicable when instance_type is 'instance_options'
                                type: int
                            memory_in_gbs:
                                description:
                                    - The total amount of memory available to the instance, in gigabytes.
                                    - Applicable when instance_type is 'instance_options'
                                type: float
                            baseline_ocpu_utilization:
                                description:
                                    - The baseline OCPU utilization for a subcore burstable VM instance. Leave this attribute blank for a
                                      non-burstable instance, or explicitly specify non-burstable with `BASELINE_1_1`.
                                    - "The following values are supported:
                                      - `BASELINE_1_8` - baseline usage is 1/8 of an OCPU.
                                      - `BASELINE_1_2` - baseline usage is 1/2 of an OCPU.
                                      - `BASELINE_1_1` - baseline usage is an entire OCPU. This represents a non-burstable instance."
                                    - Applicable when instance_type is 'instance_options'
                                type: str
                                choices:
                                    - "BASELINE_1_8"
                                    - "BASELINE_1_2"
                                    - "BASELINE_1_1"
                            nvmes:
                                description:
                                    - The number of NVMe drives to be used for storage. A single drive has 6.8 TB available.
                                    - Applicable when instance_type is 'instance_options'
                                type: int
                    platform_config:
                        description:
                            - ""
                            - Applicable when instance_type is 'instance_options'
                        type: dict
                        suboptions:
                            percentage_of_cores_enabled:
                                description:
                                    - The percentage of cores enabled. Value must be a multiple of 25%. If the requested percentage
                                      results in a fractional number of cores, the system rounds up the number of cores across processors
                                      and provisions an instance with a whole number of cores.
                                    - If the applications that you run on the instance use a core-based licensing model and need fewer cores
                                      than the full size of the shape, you can disable cores to reduce your licensing costs. The instance
                                      itself is billed for the full shape, regardless of whether all cores are enabled.
                                    - Applicable when type is one of ['AMD_MILAN_BM', 'INTEL_ICELAKE_BM', 'AMD_ROME_BM']
                                type: int
                            numa_nodes_per_socket:
                                description:
                                    - The number of NUMA nodes per socket (NPS).
                                    - Applicable when type is one of ['AMD_MILAN_BM', 'AMD_MILAN_BM_GPU', 'AMD_ROME_BM_GPU', 'INTEL_ICELAKE_BM', 'AMD_ROME_BM']
                                type: str
                                choices:
                                    - "NPS0"
                                    - "NPS1"
                                    - "NPS2"
                                    - "NPS4"
                            is_symmetric_multi_threading_enabled:
                                description:
                                    - Whether symmetric multithreading is enabled on the instance. Symmetric multithreading is also
                                      called simultaneous multithreading (SMT) or Intel Hyper-Threading.
                                    - Intel and AMD processors have two hardware execution threads per core (OCPU). SMT permits multiple
                                      independent threads of execution, to better use the resources and increase the efficiency
                                      of the CPU. When multithreading is disabled, only one thread is permitted to run on each core, which
                                      can provide higher or more predictable performance for some workloads.
                                    - Applicable when type is one of ['AMD_MILAN_BM', 'AMD_MILAN_BM_GPU', 'AMD_ROME_BM_GPU', 'INTEL_ICELAKE_BM', 'AMD_ROME_BM']
                                type: bool
                            is_access_control_service_enabled:
                                description:
                                    - Whether the Access Control Service is enabled on the instance. When enabled,
                                      the platform can enforce PCIe device isolation, required for VFIO device pass-through.
                                    - Applicable when type is one of ['AMD_MILAN_BM', 'AMD_MILAN_BM_GPU', 'AMD_ROME_BM_GPU', 'AMD_ROME_BM']
                                type: bool
                            are_virtual_instructions_enabled:
                                description:
                                    - Whether virtualization instructions are available. For example, Secure Virtual Machine for AMD shapes
                                      or VT-x for Intel shapes.
                                    - Applicable when type is one of ['AMD_MILAN_BM', 'AMD_MILAN_BM_GPU', 'AMD_ROME_BM_GPU', 'AMD_ROME_BM']
                                type: bool
                            is_input_output_memory_management_unit_enabled:
                                description:
                                    - Whether the input-output memory management unit is enabled.
                                    - Applicable when type is one of ['AMD_MILAN_BM', 'AMD_MILAN_BM_GPU', 'AMD_ROME_BM_GPU', 'INTEL_ICELAKE_BM', 'AMD_ROME_BM']
                                type: bool
                            type:
                                description:
                                    - The type of platform being configured.
                                type: str
                                choices:
                                    - "AMD_MILAN_BM"
                                    - "INTEL_VM"
                                    - "AMD_MILAN_BM_GPU"
                                    - "INTEL_ICELAKE_BM"
                                    - "AMD_ROME_BM"
                                    - "INTEL_SKYLAKE_BM"
                                    - "AMD_ROME_BM_GPU"
                                    - "AMD_VM"
                                required: true
                            is_secure_boot_enabled:
                                description:
                                    - Whether Secure Boot is enabled on the instance.
                                type: bool
                            is_trusted_platform_module_enabled:
                                description:
                                    - Whether the Trusted Platform Module (TPM) is enabled on the instance.
                                type: bool
                            is_measured_boot_enabled:
                                description:
                                    - Whether the Measured Boot feature is enabled on the instance.
                                type: bool
                            is_memory_encryption_enabled:
                                description:
                                    - Whether the instance is a confidential instance. If this value is `true`, the instance is a confidential instance. The
                                      default value is `false`.
                                type: bool
                    source_details:
                        description:
                            - ""
                            - Applicable when instance_type is 'instance_options'
                        type: dict
                        suboptions:
                            boot_volume_size_in_gbs:
                                description:
                                    - The size of the boot volume in GBs. The minimum value is 50 GB and the maximum
                                      value is 32,768 GB (32 TB).
                                    - Applicable when source_type is 'image'
                                type: int
                            image_id:
                                description:
                                    - The OCID of the image used to boot the instance.
                                    - Applicable when source_type is 'image'
                                type: str
                            kms_key_id:
                                description:
                                    - The OCID of the Vault service key to assign as the master encryption key for the boot volume.
                                    - Applicable when source_type is 'image'
                                type: str
                            boot_volume_vpus_per_gb:
                                description:
                                    - The number of volume performance units (VPUs) that will be applied to this volume per GB,
                                      representing the Block Volume service's elastic performance options.
                                      See L(Block Volume Performance
                                      Levels,https://docs.cloud.oracle.com/iaas/Content/Block/Concepts/blockvolumeperformance.htm#perf_levels) for more
                                      information.
                                    - "Allowed values:"
                                    - " * `10`: Represents Balanced option."
                                    - " * `20`: Represents Higher Performance option."
                                    - " * `30`-`120`: Represents the Ultra High Performance option."
                                    - For performance autotune enabled volumes, it would be the Default(Minimum) VPUs/GB.
                                    - Applicable when source_type is 'image'
                                type: int
                            instance_source_image_filter_details:
                                description:
                                    - ""
                                    - Applicable when source_type is 'image'
                                type: dict
                                suboptions:
                                    compartment_id:
                                        description:
                                            - The OCID of the compartment containing images to search
                                            - Applicable when source_type is 'image'
                                        type: str
                                    defined_tags_filter:
                                        description:
                                            - Filter based on these defined tags. Each key is predefined and scoped to a
                                              namespace. For more information, see L(Resource
                                              Tags,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/resourcetags.htm).
                                            - Applicable when source_type is 'image'
                                        type: dict
                                    operating_system:
                                        description:
                                            - The image's operating system.
                                            - "Example: `Oracle Linux`"
                                            - Applicable when source_type is 'image'
                                        type: str
                                    operating_system_version:
                                        description:
                                            - The image's operating system version.
                                            - "Example: `7.2`"
                                            - Applicable when source_type is 'image'
                                        type: str
                            source_type:
                                description:
                                    - The source type for the instance.
                                      Use `image` when specifying the image OCID. Use `bootVolume` when specifying
                                      the boot volume OCID.
                                type: str
                                choices:
                                    - "image"
                                    - "bootVolume"
                                required: true
                            boot_volume_id:
                                description:
                                    - The OCID of the boot volume used to boot the instance.
                                    - Applicable when source_type is 'bootVolume'
                                type: str
                    fault_domain:
                        description:
                            - A fault domain is a grouping of hardware and infrastructure within an availability domain.
                              Each availability domain contains three fault domains. Fault domains let you distribute your
                              instances so that they are not on the same physical hardware within a single availability domain.
                              A hardware failure or Compute hardware maintenance that affects one fault domain does not affect
                              instances in other fault domains.
                            - If you do not specify the fault domain, the system selects one for you.
                            - To get a list of fault domains, use the
                              L(ListFaultDomains,https://docs.cloud.oracle.com/en-us/iaas/api/#/en/identity/20160918/FaultDomain/ListFaultDomains) operation in
                              the
                              Identity and Access Management Service API.
                            - "Example: `FAULT-DOMAIN-1`"
                            - Applicable when instance_type is 'instance_options'
                        type: str
                    dedicated_vm_host_id:
                        description:
                            - The OCID of the dedicated virtual machine host to place the instance on.
                            - Dedicated VM hosts can be used when launching individual instances from an instance configuration. They
                              cannot be used to launch instance pools.
                            - Applicable when instance_type is 'instance_options'
                        type: str
                    launch_mode:
                        description:
                            - "Specifies the configuration mode for launching virtual machine (VM) instances. The configuration modes are:
                              * `NATIVE` - VM instances launch with iSCSI boot and VFIO devices. The default value for platform images.
                              * `EMULATED` - VM instances launch with emulated devices, such as the E1000 network driver and emulated SCSI disk controller.
                              * `PARAVIRTUALIZED` - VM instances launch with paravirtualized devices using VirtIO drivers.
                              * `CUSTOM` - VM instances launch with custom configuration settings specified in the `LaunchOptions` parameter."
                            - Applicable when instance_type is 'instance_options'
                        type: str
                        choices:
                            - "NATIVE"
                            - "EMULATED"
                            - "PARAVIRTUALIZED"
                            - "CUSTOM"
                    launch_options:
                        description:
                            - ""
                            - Applicable when instance_type is 'instance_options'
                        type: dict
                        suboptions:
                            boot_volume_type:
                                description:
                                    - "Emulation type for the boot volume.
                                      * `ISCSI` - ISCSI attached block storage device.
                                      * `SCSI` - Emulated SCSI disk.
                                      * `IDE` - Emulated IDE disk.
                                      * `VFIO` - Direct attached Virtual Function storage. This is the default option for local data
                                      volumes on platform images.
                                      * `PARAVIRTUALIZED` - Paravirtualized disk. This is the default for boot volumes and remote block
                                      storage volumes on platform images."
                                    - Applicable when instance_type is 'instance_options'
                                type: str
                                choices:
                                    - "ISCSI"
                                    - "SCSI"
                                    - "IDE"
                                    - "VFIO"
                                    - "PARAVIRTUALIZED"
                            firmware:
                                description:
                                    - "Firmware used to boot VM. Select the option that matches your operating system.
                                      * `BIOS` - Boot VM using BIOS style firmware. This is compatible with both 32 bit and 64 bit operating
                                      systems that boot using MBR style bootloaders.
                                      * `UEFI_64` - Boot VM using UEFI style firmware compatible with 64 bit operating systems. This is the
                                      default for platform images."
                                    - Applicable when instance_type is 'instance_options'
                                type: str
                                choices:
                                    - "BIOS"
                                    - "UEFI_64"
                            network_type:
                                description:
                                    - "Emulation type for the physical network interface card (NIC).
                                      * `E1000` - Emulated Gigabit ethernet controller. Compatible with Linux e1000 network driver.
                                      * `VFIO` - Direct attached Virtual Function network controller. This is the networking type
                                      when you launch an instance using hardware-assisted (SR-IOV) networking.
                                      * `PARAVIRTUALIZED` - VM instances launch with paravirtualized devices using VirtIO drivers."
                                    - Applicable when instance_type is 'instance_options'
                                type: str
                                choices:
                                    - "E1000"
                                    - "VFIO"
                                    - "PARAVIRTUALIZED"
                            remote_data_volume_type:
                                description:
                                    - "Emulation type for volume.
                                      * `ISCSI` - ISCSI attached block storage device.
                                      * `SCSI` - Emulated SCSI disk.
                                      * `IDE` - Emulated IDE disk.
                                      * `VFIO` - Direct attached Virtual Function storage. This is the default option for local data
                                      volumes on platform images.
                                      * `PARAVIRTUALIZED` - Paravirtualized disk. This is the default for boot volumes and remote block
                                      storage volumes on platform images."
                                    - Applicable when instance_type is 'instance_options'
                                type: str
                                choices:
                                    - "ISCSI"
                                    - "SCSI"
                                    - "IDE"
                                    - "VFIO"
                                    - "PARAVIRTUALIZED"
                            is_pv_encryption_in_transit_enabled:
                                description:
                                    - Deprecated. Instead use `isPvEncryptionInTransitEnabled` in
                                      L(InstanceConfigurationLaunchInstanceDetails,https://docs.cloud.oracle.com/en-
                                      us/iaas/api/#/en/iaas/latest/datatypes/InstanceConfigurationLaunchInstanceDetails).
                                    - Applicable when instance_type is 'instance_options'
                                type: bool
                            is_consistent_volume_naming_enabled:
                                description:
                                    - Whether to enable consistent volume naming feature. Defaults to false.
                                    - Applicable when instance_type is 'instance_options'
                                type: bool
                    agent_config:
                        description:
                            - ""
                            - Applicable when instance_type is 'instance_options'
                        type: dict
                        suboptions:
                            is_monitoring_disabled:
                                description:
                                    - Whether Oracle Cloud Agent can gather performance metrics and monitor the instance using the
                                      monitoring plugins. Default value is false (monitoring plugins are enabled).
                                    - "These are the monitoring plugins: Compute Instance Monitoring
                                      and Custom Logs Monitoring."
                                    - The monitoring plugins are controlled by this parameter and by the per-plugin
                                      configuration in the `pluginsConfig` object.
                                    - "- If `isMonitoringDisabled` is true, all of the monitoring plugins are disabled, regardless of
                                      the per-plugin configuration.
                                      - If `isMonitoringDisabled` is false, all of the monitoring plugins are enabled. You
                                      can optionally disable individual monitoring plugins by providing a value in the `pluginsConfig`
                                      object."
                                    - Applicable when instance_type is 'instance_options'
                                type: bool
                            is_management_disabled:
                                description:
                                    - Whether Oracle Cloud Agent can run all the available management plugins.
                                      Default value is false (management plugins are enabled).
                                    - "These are the management plugins: OS Management Service Agent and Compute Instance
                                      Run Command."
                                    - The management plugins are controlled by this parameter and by the per-plugin
                                      configuration in the `pluginsConfig` object.
                                    - "- If `isManagementDisabled` is true, all of the management plugins are disabled, regardless of
                                      the per-plugin configuration.
                                      - If `isManagementDisabled` is false, all of the management plugins are enabled. You
                                      can optionally disable individual management plugins by providing a value in the `pluginsConfig`
                                      object."
                                    - Applicable when instance_type is 'instance_options'
                                type: bool
                            are_all_plugins_disabled:
                                description:
                                    - Whether Oracle Cloud Agent can run all the available plugins.
                                      This includes the management and monitoring plugins.
                                    - To get a list of available plugins, use the
                                      L(ListInstanceagentAvailablePlugins,https://docs.cloud.oracle.com/en-
                                      us/iaas/api/#/en/instanceagent/20180530/Plugin/ListInstanceagentAvailablePlugins)
                                      operation in the Oracle Cloud Agent API. For more information about the available plugins, see
                                      L(Managing Plugins with Oracle Cloud Agent,https://docs.cloud.oracle.com/iaas/Content/Compute/Tasks/manage-plugins.htm).
                                    - Applicable when instance_type is 'instance_options'
                                type: bool
                            plugins_config:
                                description:
                                    - The configuration of plugins associated with this instance.
                                    - Applicable when instance_type is 'instance_options'
                                type: list
                                elements: dict
                                suboptions:
                                    name:
                                        description:
                                            - The plugin name. To get a list of available plugins, use the
                                              L(ListInstanceagentAvailablePlugins,https://docs.cloud.oracle.com/en-
                                              us/iaas/api/#/en/instanceagent/20180530/Plugin/ListInstanceagentAvailablePlugins)
                                              operation in the Oracle Cloud Agent API. For more information about the available plugins, see
                                              L(Managing Plugins with Oracle Cloud Agent,https://docs.cloud.oracle.com/iaas/Content/Compute/Tasks/manage-
                                              plugins.htm).
                                            - Required when instance_type is 'instance_options'
                                        type: str
                                        required: true
                                    desired_state:
                                        description:
                                            - Whether the plugin should be enabled or disabled.
                                            - To enable the monitoring and management plugins, the `isMonitoringDisabled` and
                                              `isManagementDisabled` attributes must also be set to false.
                                            - Required when instance_type is 'instance_options'
                                        type: str
                                        choices:
                                            - "ENABLED"
                                            - "DISABLED"
                                        required: true
                    is_pv_encryption_in_transit_enabled:
                        description:
                            - Whether to enable in-transit encryption for the data volume's paravirtualized attachment. The default value is false.
                            - Applicable when instance_type is 'instance_options'
                        type: bool
                    preferred_maintenance_action:
                        description:
                            - "The preferred maintenance action for an instance. The default is LIVE_MIGRATE, if live migration is supported.
                              * `LIVE_MIGRATE` - Run maintenance using a live migration.
                              * `REBOOT` - Run maintenance using a reboot."
                            - Applicable when instance_type is 'instance_options'
                        type: str
                        choices:
                            - "LIVE_MIGRATE"
                            - "REBOOT"
                    instance_options:
                        description:
                            - ""
                            - Applicable when instance_type is 'instance_options'
                        type: dict
                        suboptions:
                            are_legacy_imds_endpoints_disabled:
                                description:
                                    - Whether to disable the legacy (/v1) instance metadata service endpoints.
                                      Customers who have migrated to /v2 should set this to true for added security.
                                      Default is false.
                                    - Applicable when instance_type is 'instance_options'
                                type: bool
                    availability_config:
                        description:
                            - ""
                            - Applicable when instance_type is 'instance_options'
                        type: dict
                        suboptions:
                            is_live_migration_preferred:
                                description:
                                    - Whether to live migrate supported VM instances to a healthy physical VM host without
                                      disrupting running instances during infrastructure maintenance events. If null, Oracle
                                      chooses the best option for migrating the VM during infrastructure maintenance events.
                                    - Applicable when instance_type is 'instance_options'
                                type: bool
                            recovery_action:
                                description:
                                    - "The lifecycle state for an instance when it is recovered after infrastructure maintenance.
                                      * `RESTORE_INSTANCE` - The instance is restored to the lifecycle state it was in before the maintenance event.
                                      If the instance was running, it is automatically rebooted. This is the default action when a value is not set.
                                      * `STOP_INSTANCE` - The instance is recovered in the stopped state."
                                    - Applicable when instance_type is 'instance_options'
                                type: str
                                choices:
                                    - "RESTORE_INSTANCE"
                                    - "STOP_INSTANCE"
                    preemptible_instance_config:
                        description:
                            - ""
                            - Applicable when instance_type is 'instance_options'
                        type: dict
                        suboptions:
                            preemption_action:
                                description:
                                    - ""
                                    - Required when instance_type is 'instance_options'
                                type: dict
                                required: true
                                suboptions:
                                    type:
                                        description:
                                            - The type of action to run when the instance is interrupted for eviction.
                                        type: str
                                        choices:
                                            - "TERMINATE"
                                        required: true
                                    preserve_boot_volume:
                                        description:
                                            - Whether to preserve the boot volume that was used to launch the preemptible instance when the instance is
                                              terminated. Defaults to false if not specified.
                                        type: bool
            secondary_vnics:
                description:
                    - Secondary VNIC parameters.
                    - Applicable when instance_type is 'instance_options'
                type: list
                elements: dict
                suboptions:
                    create_vnic_details:
                        description:
                            - ""
                            - Applicable when instance_type is 'instance_options'
                        type: dict
                        suboptions:
                            assign_public_ip:
                                description:
                                    - Whether the VNIC should be assigned a public IP address. See the `assignPublicIp` attribute of
                                      L(CreateVnicDetails,https://docs.cloud.oracle.com/en-us/iaas/api/#/en/iaas/latest/CreateVnicDetails/)
                                      for more information.
                                    - Applicable when instance_type is 'instance_options'
                                type: bool
                            assign_private_dns_record:
                                description:
                                    - Whether the VNIC should be assigned a private DNS record. See the `assignPrivateDnsRecord` attribute of
                                      L(CreateVnicDetails,https://docs.cloud.oracle.com/en-us/iaas/api/#/en/iaas/latest/CreateVnicDetails/)
                                      for more information.
                                    - Applicable when instance_type is 'instance_options'
                                type: bool
                            defined_tags:
                                description:
                                    - Defined tags for this resource. Each key is predefined and scoped to a
                                      namespace. For more information, see L(Resource
                                      Tags,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/resourcetags.htm).
                                    - "Example: `{\\"Operations\\": {\\"CostCenter\\": \\"42\\"}}`"
                                    - Applicable when instance_type is 'instance_options'
                                type: dict
                            display_name:
                                description:
                                    - A user-friendly name. Does not have to be unique, and it's changeable.
                                      Avoid entering confidential information.
                                    - Applicable when instance_type is 'instance_options'
                                type: str
                                aliases: ["name"]
                            freeform_tags:
                                description:
                                    - Free-form tags for this resource. Each tag is a simple key-value pair with no
                                      predefined name, type, or namespace. For more information, see L(Resource
                                      Tags,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/resourcetags.htm).
                                    - "Example: `{\\"Department\\": \\"Finance\\"}`"
                                    - Applicable when instance_type is 'instance_options'
                                type: dict
                            hostname_label:
                                description:
                                    - The hostname for the VNIC's primary private IP.
                                      See the `hostnameLabel` attribute of L(CreateVnicDetails,https://docs.cloud.oracle.com/en-
                                      us/iaas/api/#/en/iaas/latest/CreateVnicDetails/) for more information.
                                    - Applicable when instance_type is 'instance_options'
                                type: str
                            nsg_ids:
                                description:
                                    - A list of the OCIDs of the network security groups (NSGs) to add the VNIC to. For more
                                      information about NSGs, see
                                      L(NetworkSecurityGroup,https://docs.cloud.oracle.com/en-us/iaas/api/#/en/iaas/latest/NetworkSecurityGroup/).
                                    - Applicable when instance_type is 'instance_options'
                                type: list
                                elements: str
                            private_ip:
                                description:
                                    - A private IP address of your choice to assign to the VNIC.
                                      See the `privateIp` attribute of L(CreateVnicDetails,https://docs.cloud.oracle.com/en-
                                      us/iaas/api/#/en/iaas/latest/CreateVnicDetails/) for more information.
                                    - Applicable when instance_type is 'instance_options'
                                type: str
                            skip_source_dest_check:
                                description:
                                    - Whether the source/destination check is disabled on the VNIC.
                                      See the `skipSourceDestCheck` attribute of L(CreateVnicDetails,https://docs.cloud.oracle.com/en-
                                      us/iaas/api/#/en/iaas/latest/CreateVnicDetails/) for more information.
                                    - Applicable when instance_type is 'instance_options'
                                type: bool
                            subnet_id:
                                description:
                                    - The OCID of the subnet to create the VNIC in.
                                      See the `subnetId` attribute of L(CreateVnicDetails,https://docs.cloud.oracle.com/en-
                                      us/iaas/api/#/en/iaas/latest/CreateVnicDetails/) for more information.
                                    - Applicable when instance_type is 'instance_options'
                                type: str
                    display_name:
                        description:
                            - A user-friendly name. Does not have to be unique, and it's changeable.
                              Avoid entering confidential information.
                            - Applicable when instance_type is 'instance_options'
                        type: str
                        aliases: ["name"]
                    nic_index:
                        description:
                            - Which physical network interface card (NIC) the VNIC will use. Defaults to 0.
                              Certain bare metal instance shapes have two active physical NICs (0 and 1). If
                              you add a secondary VNIC to one of these instances, you can specify which NIC
                              the VNIC will use. For more information, see
                              L(Virtual Network Interface Cards (VNICs),https://docs.cloud.oracle.com/iaas/Content/Network/Tasks/managingVNICs.htm).
                            - Applicable when instance_type is 'instance_options'
                        type: int
    instance_type:
        description:
            - The type of instance details. Supported instanceType is compute
            - Required for I(action=launch).
        type: str
        choices:
            - "instance_options"
            - "compute"
        default: "compute"
    block_volumes:
        description:
            - Block volume parameters.
            - Applicable only for I(action=launch).
            - Applicable when instance_type is 'compute'
        type: list
        elements: dict
        suboptions:
            attach_details:
                description:
                    - ""
                    - Applicable when instance_type is 'compute'
                type: dict
                suboptions:
                    use_chap:
                        description:
                            - Whether to use CHAP authentication for the volume attachment. Defaults to false.
                            - Applicable when type is 'iscsi'
                        type: bool
                    display_name:
                        description:
                            - A user-friendly name. Does not have to be unique, and it's changeable.
                              Avoid entering confidential information.
                        type: str
                        aliases: ["name"]
                    is_read_only:
                        description:
                            - Whether the attachment should be created in read-only mode.
                        type: bool
                    device:
                        description:
                            - The device name.
                        type: str
                    is_shareable:
                        description:
                            - Whether the attachment should be created in shareable mode. If an attachment
                              is created in shareable mode, then other instances can attach the same volume, provided
                              that they also create their attachments in shareable mode. Only certain volume types can
                              be attached in shareable mode. Defaults to false if not specified.
                        type: bool
                    type:
                        description:
                            - "The type of volume. The only supported values are \\"iscsi\\" and \\"paravirtualized\\"."
                        type: str
                        choices:
                            - "iscsi"
                            - "paravirtualized"
                        required: true
                    is_pv_encryption_in_transit_enabled:
                        description:
                            - Whether to enable in-transit encryption for the data volume's paravirtualized attachment. The default value is false.
                            - Applicable when type is 'paravirtualized'
                        type: bool
            create_details:
                description:
                    - ""
                    - Applicable when instance_type is 'compute'
                type: dict
                suboptions:
                    availability_domain:
                        description:
                            - The availability domain of the volume.
                            - "Example: `Uocm:PHX-AD-1`"
                            - Applicable when instance_type is 'compute'
                        type: str
                    backup_policy_id:
                        description:
                            - If provided, specifies the ID of the volume backup policy to assign to the newly
                              created volume. If omitted, no policy will be assigned.
                            - Applicable when instance_type is 'compute'
                        type: str
                    compartment_id:
                        description:
                            - The OCID of the compartment that contains the volume.
                            - Applicable when instance_type is 'compute'
                        type: str
                    is_auto_tune_enabled:
                        description:
                            - Specifies whether the auto-tune performance is enabled for this boot volume. This field is deprecated.
                              Use the `InstanceConfigurationDetachedVolumeAutotunePolicy` instead to enable the volume for detached autotune.
                            - Applicable when instance_type is 'compute'
                        type: bool
                    block_volume_replicas:
                        description:
                            - The list of block volume replicas to be enabled for this volume
                              in the specified destination availability domains.
                            - Applicable when instance_type is 'compute'
                        type: list
                        elements: dict
                        suboptions:
                            display_name:
                                description:
                                    - "The display name of the block volume replica. You may optionally specify a *display name* for
                                      the block volume replica, otherwise a default is provided."
                                    - Applicable when instance_type is 'compute'
                                type: str
                                aliases: ["name"]
                            availability_domain:
                                description:
                                    - The availability domain of the block volume replica.
                                    - "Example: `Uocm:PHX-AD-1`"
                                    - Required when instance_type is 'compute'
                                type: str
                                required: true
                    defined_tags:
                        description:
                            - Defined tags for this resource. Each key is predefined and scoped to a
                              namespace. For more information, see L(Resource
                              Tags,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/resourcetags.htm).
                            - "Example: `{\\"Operations\\": {\\"CostCenter\\": \\"42\\"}}`"
                            - Applicable when instance_type is 'compute'
                        type: dict
                    display_name:
                        description:
                            - A user-friendly name. Does not have to be unique, and it's changeable.
                              Avoid entering confidential information.
                            - Applicable when instance_type is 'compute'
                        type: str
                        aliases: ["name"]
                    freeform_tags:
                        description:
                            - Free-form tags for this resource. Each tag is a simple key-value pair with no
                              predefined name, type, or namespace. For more information, see L(Resource
                              Tags,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/resourcetags.htm).
                            - "Example: `{\\"Department\\": \\"Finance\\"}`"
                            - Applicable when instance_type is 'compute'
                        type: dict
                    kms_key_id:
                        description:
                            - The OCID of the Vault service key to assign as the master encryption key
                              for the volume.
                            - Applicable when instance_type is 'compute'
                        type: str
                    vpus_per_gb:
                        description:
                            - The number of volume performance units (VPUs) that will be applied to this volume per GB,
                              representing the Block Volume service's elastic performance options.
                              See L(Block Volume Performance
                              Levels,https://docs.cloud.oracle.com/iaas/Content/Block/Concepts/blockvolumeperformance.htm#perf_levels) for more information.
                            - "Allowed values:"
                            - " * `0`: Represents Lower Cost option."
                            - " * `10`: Represents Balanced option."
                            - " * `20`: Represents Higher Performance option."
                            - " * `30`-`120`: Represents the Ultra High Performance option."
                            - For performance autotune enabled volumes, it would be the Default(Minimum) VPUs/GB.
                            - Applicable when instance_type is 'compute'
                        type: int
                    size_in_gbs:
                        description:
                            - The size of the volume in GBs.
                            - Applicable when instance_type is 'compute'
                        type: int
                    source_details:
                        description:
                            - ""
                            - Applicable when instance_type is 'compute'
                        type: dict
                        suboptions:
                            type:
                                description:
                                    - ""
                                type: str
                                choices:
                                    - "volumeBackup"
                                    - "volume"
                                required: true
                            id:
                                description:
                                    - The OCID of the volume backup.
                                type: str
                    autotune_policies:
                        description:
                            - The list of autotune policies enabled for this volume.
                            - Applicable when instance_type is 'compute'
                        type: list
                        elements: dict
                        suboptions:
                            max_vpus_per_gb:
                                description:
                                    - This will be the maximum VPUs/GB performance level that the volume will be auto-tuned
                                      temporarily based on performance monitoring.
                                    - Required when autotune_type is 'PERFORMANCE_BASED'
                                type: int
                            autotune_type:
                                description:
                                    - This specifies the type of autotunes supported by OCI.
                                type: str
                                choices:
                                    - "PERFORMANCE_BASED"
                                    - "DETACHED_VOLUME"
                                required: true
            volume_id:
                description:
                    - The OCID of the volume.
                    - Applicable when instance_type is 'compute'
                type: str
    launch_details:
        description:
            - ""
            - Applicable only for I(action=launch).
            - Applicable when instance_type is 'compute'
        type: dict
        suboptions:
            availability_domain:
                description:
                    - The availability domain of the instance.
                    - "Example: `Uocm:PHX-AD-1`"
                    - Applicable when instance_type is 'compute'
                type: str
            capacity_reservation_id:
                description:
                    - The OCID of the compute capacity reservation this instance is launched under.
                    - Applicable when instance_type is 'compute'
                type: str
            compartment_id:
                description:
                    - The OCID of the compartment containing the instance.
                      Instances created from instance configurations are placed in the same compartment
                      as the instance that was used to create the instance configuration.
                    - Applicable when instance_type is 'compute'
                type: str
            create_vnic_details:
                description:
                    - ""
                    - Applicable when instance_type is 'compute'
                type: dict
                suboptions:
                    assign_public_ip:
                        description:
                            - Whether the VNIC should be assigned a public IP address. See the `assignPublicIp` attribute of
                              L(CreateVnicDetails,https://docs.cloud.oracle.com/en-us/iaas/api/#/en/iaas/latest/CreateVnicDetails/)
                              for more information.
                            - Applicable when instance_type is 'compute'
                        type: bool
                    assign_private_dns_record:
                        description:
                            - Whether the VNIC should be assigned a private DNS record. See the `assignPrivateDnsRecord` attribute of
                              L(CreateVnicDetails,https://docs.cloud.oracle.com/en-us/iaas/api/#/en/iaas/latest/CreateVnicDetails/)
                              for more information.
                            - Applicable when instance_type is 'compute'
                        type: bool
                    defined_tags:
                        description:
                            - Defined tags for this resource. Each key is predefined and scoped to a
                              namespace. For more information, see L(Resource
                              Tags,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/resourcetags.htm).
                            - "Example: `{\\"Operations\\": {\\"CostCenter\\": \\"42\\"}}`"
                            - Applicable when instance_type is 'compute'
                        type: dict
                    display_name:
                        description:
                            - A user-friendly name. Does not have to be unique, and it's changeable.
                              Avoid entering confidential information.
                            - Applicable when instance_type is 'compute'
                        type: str
                        aliases: ["name"]
                    freeform_tags:
                        description:
                            - Free-form tags for this resource. Each tag is a simple key-value pair with no
                              predefined name, type, or namespace. For more information, see L(Resource
                              Tags,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/resourcetags.htm).
                            - "Example: `{\\"Department\\": \\"Finance\\"}`"
                            - Applicable when instance_type is 'compute'
                        type: dict
                    hostname_label:
                        description:
                            - The hostname for the VNIC's primary private IP.
                              See the `hostnameLabel` attribute of L(CreateVnicDetails,https://docs.cloud.oracle.com/en-
                              us/iaas/api/#/en/iaas/latest/CreateVnicDetails/) for more information.
                            - Applicable when instance_type is 'compute'
                        type: str
                    nsg_ids:
                        description:
                            - A list of the OCIDs of the network security groups (NSGs) to add the VNIC to. For more
                              information about NSGs, see
                              L(NetworkSecurityGroup,https://docs.cloud.oracle.com/en-us/iaas/api/#/en/iaas/latest/NetworkSecurityGroup/).
                            - Applicable when instance_type is 'compute'
                        type: list
                        elements: str
                    private_ip:
                        description:
                            - A private IP address of your choice to assign to the VNIC.
                              See the `privateIp` attribute of L(CreateVnicDetails,https://docs.cloud.oracle.com/en-
                              us/iaas/api/#/en/iaas/latest/CreateVnicDetails/) for more information.
                            - Applicable when instance_type is 'compute'
                        type: str
                    skip_source_dest_check:
                        description:
                            - Whether the source/destination check is disabled on the VNIC.
                              See the `skipSourceDestCheck` attribute of L(CreateVnicDetails,https://docs.cloud.oracle.com/en-
                              us/iaas/api/#/en/iaas/latest/CreateVnicDetails/) for more information.
                            - Applicable when instance_type is 'compute'
                        type: bool
                    subnet_id:
                        description:
                            - The OCID of the subnet to create the VNIC in.
                              See the `subnetId` attribute of L(CreateVnicDetails,https://docs.cloud.oracle.com/en-
                              us/iaas/api/#/en/iaas/latest/CreateVnicDetails/) for more information.
                            - Applicable when instance_type is 'compute'
                        type: str
            defined_tags:
                description:
                    - Defined tags for this resource. Each key is predefined and scoped to a
                      namespace. For more information, see L(Resource Tags,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/resourcetags.htm).
                    - "Example: `{\\"Operations\\": {\\"CostCenter\\": \\"42\\"}}`"
                    - Applicable when instance_type is 'compute'
                type: dict
            display_name:
                description:
                    - A user-friendly name. Does not have to be unique, and it's changeable.
                      Avoid entering confidential information.
                    - Applicable when instance_type is 'compute'
                type: str
                aliases: ["name"]
            extended_metadata:
                description:
                    - Additional metadata key/value pairs that you provide. They serve the same purpose and
                      functionality as fields in the `metadata` object.
                    - They are distinguished from `metadata` fields in that these can be nested JSON objects
                      (whereas `metadata` fields are string/string maps only).
                    - The combined size of the `metadata` and `extendedMetadata` objects can be a maximum of
                      32,000 bytes.
                    - Applicable when instance_type is 'compute'
                type: dict
            freeform_tags:
                description:
                    - Free-form tags for this resource. Each tag is a simple key-value pair with no
                      predefined name, type, or namespace. For more information, see L(Resource
                      Tags,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/resourcetags.htm).
                    - "Example: `{\\"Department\\": \\"Finance\\"}`"
                    - Applicable when instance_type is 'compute'
                type: dict
            ipxe_script:
                description:
                    - This is an advanced option.
                    - When a bare metal or virtual machine
                      instance boots, the iPXE firmware that runs on the instance is
                      configured to run an iPXE script to continue the boot process.
                    - If you want more control over the boot process, you can provide
                      your own custom iPXE script that will run when the instance boots;
                      however, you should be aware that the same iPXE script will run
                      every time an instance boots; not only after the initial
                      LaunchInstance call.
                    - "The default iPXE script connects to the instance's local boot
                      volume over iSCSI and performs a network boot. If you use a custom iPXE
                      script and want to network-boot from the instance's local boot volume
                      over iSCSI the same way as the default iPXE script, you should use the
                      following iSCSI IP address: 169.254.0.2, and boot volume IQN:
                      iqn.2015-02.oracle.boot."
                    - For more information about the Bring Your Own Image feature of
                      Oracle Cloud Infrastructure, see
                      L(Bring Your Own Image,https://docs.cloud.oracle.com/iaas/Content/Compute/References/bringyourownimage.htm).
                    - For more information about iPXE, see http://ipxe.org.
                    - Applicable when instance_type is 'compute'
                type: str
            metadata:
                description:
                    - Custom metadata key/value pairs that you provide, such as the SSH public key
                      required to connect to the instance.
                    - "A metadata service runs on every launched instance. The service is an HTTP
                      endpoint listening on 169.254.169.254. You can use the service to:"
                    - "* Provide information to L(Cloud-Init,https://cloudinit.readthedocs.org/en/latest/)
                        to be used for various system initialization tasks."
                    - "* Get information about the instance, including the custom metadata that you
                        provide when you launch the instance."
                    - "**Providing Cloud-Init Metadata**"
                    - "You can use the following metadata key names to provide information to
                       Cloud-Init:"
                    - "**\\"ssh_authorized_keys\\"** - Provide one or more public SSH keys to be
                       included in the `~/.ssh/authorized_keys` file for the default user on the
                       instance. Use a newline character to separate multiple keys. The SSH
                       keys must be in the format necessary for the `authorized_keys` file, as shown
                       in the example below."
                    - "**\\"user_data\\"** - Provide your own base64-encoded data to be used by
                       Cloud-Init to run custom scripts or provide custom Cloud-Init configuration. For
                       information about how to take advantage of user data, see the
                       L(Cloud-Init Documentation,http://cloudinit.readthedocs.org/en/latest/topics/format.html)."
                    - "**Metadata Example**"
                    - "     \\"metadata\\" : {
                               \\"quake_bot_level\\" : \\"Severe\\",
                               \\"ssh_authorized_keys\\" : \\"ssh-rsa <your_public_SSH_key>== rsa-key-20160227\\",
                               \\"user_data\\" : \\"<your_public_SSH_key>==\\"
                            }
                       **Getting Metadata on the Instance**"
                    - "To get information about your instance, connect to the instance using SSH and issue any of the
                       following GET requests:"
                    - "    curl -H \\"Authorization: Bearer Oracle\\" http://169.254.169.254/opc/v2/instance/
                           curl -H \\"Authorization: Bearer Oracle\\" http://169.254.169.254/opc/v2/instance/metadata/
                           curl -H \\"Authorization: Bearer Oracle\\" http://169.254.169.254/opc/v2/instance/metadata/<any-key-name>"
                    -  You'll get back a response that includes all the instance information; only the metadata information; or
                       the metadata information for the specified key name, respectively.
                    -  The combined size of the `metadata` and `extendedMetadata` objects can be a maximum of 32,000 bytes.
                    - Applicable when instance_type is 'compute'
                type: dict
            shape:
                description:
                    - The shape of an instance. The shape determines the number of CPUs, amount of memory,
                      and other resources allocated to the instance.
                    - You can enumerate all available shapes by calling L(ListShapes,https://docs.cloud.oracle.com/en-
                      us/iaas/api/#/en/iaas/latest/Shape/ListShapes).
                    - Applicable when instance_type is 'compute'
                type: str
            shape_config:
                description:
                    - ""
                    - Applicable when instance_type is 'compute'
                type: dict
                suboptions:
                    ocpus:
                        description:
                            - The total number of OCPUs available to the instance.
                            - Applicable when instance_type is 'compute'
                        type: float
                    vcpus:
                        description:
                            - The total number of VCPUs available to the instance. This can be used instead of OCPUs,
                              in which case the actual number of OCPUs will be calculated based on this value
                              and the actual hardware. This must be a multiple of 2.
                            - Applicable when instance_type is 'compute'
                        type: int
                    memory_in_gbs:
                        description:
                            - The total amount of memory available to the instance, in gigabytes.
                            - Applicable when instance_type is 'compute'
                        type: float
                    baseline_ocpu_utilization:
                        description:
                            - The baseline OCPU utilization for a subcore burstable VM instance. Leave this attribute blank for a
                              non-burstable instance, or explicitly specify non-burstable with `BASELINE_1_1`.
                            - "The following values are supported:
                              - `BASELINE_1_8` - baseline usage is 1/8 of an OCPU.
                              - `BASELINE_1_2` - baseline usage is 1/2 of an OCPU.
                              - `BASELINE_1_1` - baseline usage is an entire OCPU. This represents a non-burstable instance."
                            - Applicable when instance_type is 'compute'
                        type: str
                        choices:
                            - "BASELINE_1_8"
                            - "BASELINE_1_2"
                            - "BASELINE_1_1"
                    nvmes:
                        description:
                            - The number of NVMe drives to be used for storage. A single drive has 6.8 TB available.
                            - Applicable when instance_type is 'compute'
                        type: int
            platform_config:
                description:
                    - ""
                    - Applicable when instance_type is 'compute'
                type: dict
                suboptions:
                    percentage_of_cores_enabled:
                        description:
                            - The percentage of cores enabled. Value must be a multiple of 25%. If the requested percentage
                              results in a fractional number of cores, the system rounds up the number of cores across processors
                              and provisions an instance with a whole number of cores.
                            - If the applications that you run on the instance use a core-based licensing model and need fewer cores
                              than the full size of the shape, you can disable cores to reduce your licensing costs. The instance
                              itself is billed for the full shape, regardless of whether all cores are enabled.
                            - Applicable when type is one of ['AMD_MILAN_BM', 'INTEL_ICELAKE_BM', 'AMD_ROME_BM']
                        type: int
                    numa_nodes_per_socket:
                        description:
                            - The number of NUMA nodes per socket (NPS).
                            - Applicable when type is one of ['AMD_MILAN_BM', 'AMD_MILAN_BM_GPU', 'AMD_ROME_BM_GPU', 'INTEL_ICELAKE_BM', 'AMD_ROME_BM']
                        type: str
                        choices:
                            - "NPS0"
                            - "NPS1"
                            - "NPS2"
                            - "NPS4"
                    is_symmetric_multi_threading_enabled:
                        description:
                            - Whether symmetric multithreading is enabled on the instance. Symmetric multithreading is also
                              called simultaneous multithreading (SMT) or Intel Hyper-Threading.
                            - Intel and AMD processors have two hardware execution threads per core (OCPU). SMT permits multiple
                              independent threads of execution, to better use the resources and increase the efficiency
                              of the CPU. When multithreading is disabled, only one thread is permitted to run on each core, which
                              can provide higher or more predictable performance for some workloads.
                            - Applicable when type is one of ['AMD_MILAN_BM', 'AMD_MILAN_BM_GPU', 'AMD_ROME_BM_GPU', 'INTEL_ICELAKE_BM', 'AMD_ROME_BM']
                        type: bool
                    is_access_control_service_enabled:
                        description:
                            - Whether the Access Control Service is enabled on the instance. When enabled,
                              the platform can enforce PCIe device isolation, required for VFIO device pass-through.
                            - Applicable when type is one of ['AMD_MILAN_BM', 'AMD_MILAN_BM_GPU', 'AMD_ROME_BM_GPU', 'AMD_ROME_BM']
                        type: bool
                    are_virtual_instructions_enabled:
                        description:
                            - Whether virtualization instructions are available. For example, Secure Virtual Machine for AMD shapes
                              or VT-x for Intel shapes.
                            - Applicable when type is one of ['AMD_MILAN_BM', 'AMD_MILAN_BM_GPU', 'AMD_ROME_BM_GPU', 'AMD_ROME_BM']
                        type: bool
                    is_input_output_memory_management_unit_enabled:
                        description:
                            - Whether the input-output memory management unit is enabled.
                            - Applicable when type is one of ['AMD_MILAN_BM', 'AMD_MILAN_BM_GPU', 'AMD_ROME_BM_GPU', 'INTEL_ICELAKE_BM', 'AMD_ROME_BM']
                        type: bool
                    type:
                        description:
                            - The type of platform being configured.
                        type: str
                        choices:
                            - "AMD_MILAN_BM"
                            - "INTEL_VM"
                            - "AMD_MILAN_BM_GPU"
                            - "INTEL_ICELAKE_BM"
                            - "AMD_ROME_BM"
                            - "INTEL_SKYLAKE_BM"
                            - "AMD_ROME_BM_GPU"
                            - "AMD_VM"
                        required: true
                    is_secure_boot_enabled:
                        description:
                            - Whether Secure Boot is enabled on the instance.
                        type: bool
                    is_trusted_platform_module_enabled:
                        description:
                            - Whether the Trusted Platform Module (TPM) is enabled on the instance.
                        type: bool
                    is_measured_boot_enabled:
                        description:
                            - Whether the Measured Boot feature is enabled on the instance.
                        type: bool
                    is_memory_encryption_enabled:
                        description:
                            - Whether the instance is a confidential instance. If this value is `true`, the instance is a confidential instance. The default
                              value is `false`.
                        type: bool
            source_details:
                description:
                    - ""
                    - Applicable when instance_type is 'compute'
                type: dict
                suboptions:
                    boot_volume_size_in_gbs:
                        description:
                            - The size of the boot volume in GBs. The minimum value is 50 GB and the maximum
                              value is 32,768 GB (32 TB).
                            - Applicable when source_type is 'image'
                        type: int
                    image_id:
                        description:
                            - The OCID of the image used to boot the instance.
                            - Applicable when source_type is 'image'
                        type: str
                    kms_key_id:
                        description:
                            - The OCID of the Vault service key to assign as the master encryption key for the boot volume.
                            - Applicable when source_type is 'image'
                        type: str
                    boot_volume_vpus_per_gb:
                        description:
                            - The number of volume performance units (VPUs) that will be applied to this volume per GB,
                              representing the Block Volume service's elastic performance options.
                              See L(Block Volume Performance
                              Levels,https://docs.cloud.oracle.com/iaas/Content/Block/Concepts/blockvolumeperformance.htm#perf_levels) for more information.
                            - "Allowed values:"
                            - " * `10`: Represents Balanced option."
                            - " * `20`: Represents Higher Performance option."
                            - " * `30`-`120`: Represents the Ultra High Performance option."
                            - For performance autotune enabled volumes, it would be the Default(Minimum) VPUs/GB.
                            - Applicable when source_type is 'image'
                        type: int
                    instance_source_image_filter_details:
                        description:
                            - ""
                            - Applicable when source_type is 'image'
                        type: dict
                        suboptions:
                            compartment_id:
                                description:
                                    - The OCID of the compartment containing images to search
                                    - Applicable when source_type is 'image'
                                type: str
                            defined_tags_filter:
                                description:
                                    - Filter based on these defined tags. Each key is predefined and scoped to a
                                      namespace. For more information, see L(Resource
                                      Tags,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/resourcetags.htm).
                                    - Applicable when source_type is 'image'
                                type: dict
                            operating_system:
                                description:
                                    - The image's operating system.
                                    - "Example: `Oracle Linux`"
                                    - Applicable when source_type is 'image'
                                type: str
                            operating_system_version:
                                description:
                                    - The image's operating system version.
                                    - "Example: `7.2`"
                                    - Applicable when source_type is 'image'
                                type: str
                    source_type:
                        description:
                            - The source type for the instance.
                              Use `image` when specifying the image OCID. Use `bootVolume` when specifying
                              the boot volume OCID.
                        type: str
                        choices:
                            - "image"
                            - "bootVolume"
                        required: true
                    boot_volume_id:
                        description:
                            - The OCID of the boot volume used to boot the instance.
                            - Applicable when source_type is 'bootVolume'
                        type: str
            fault_domain:
                description:
                    - A fault domain is a grouping of hardware and infrastructure within an availability domain.
                      Each availability domain contains three fault domains. Fault domains let you distribute your
                      instances so that they are not on the same physical hardware within a single availability domain.
                      A hardware failure or Compute hardware maintenance that affects one fault domain does not affect
                      instances in other fault domains.
                    - If you do not specify the fault domain, the system selects one for you.
                    - To get a list of fault domains, use the
                      L(ListFaultDomains,https://docs.cloud.oracle.com/en-us/iaas/api/#/en/identity/20160918/FaultDomain/ListFaultDomains) operation in the
                      Identity and Access Management Service API.
                    - "Example: `FAULT-DOMAIN-1`"
                    - Applicable when instance_type is 'compute'
                type: str
            dedicated_vm_host_id:
                description:
                    - The OCID of the dedicated virtual machine host to place the instance on.
                    - Dedicated VM hosts can be used when launching individual instances from an instance configuration. They
                      cannot be used to launch instance pools.
                    - Applicable when instance_type is 'compute'
                type: str
            launch_mode:
                description:
                    - "Specifies the configuration mode for launching virtual machine (VM) instances. The configuration modes are:
                      * `NATIVE` - VM instances launch with iSCSI boot and VFIO devices. The default value for platform images.
                      * `EMULATED` - VM instances launch with emulated devices, such as the E1000 network driver and emulated SCSI disk controller.
                      * `PARAVIRTUALIZED` - VM instances launch with paravirtualized devices using VirtIO drivers.
                      * `CUSTOM` - VM instances launch with custom configuration settings specified in the `LaunchOptions` parameter."
                    - Applicable when instance_type is 'compute'
                type: str
                choices:
                    - "NATIVE"
                    - "EMULATED"
                    - "PARAVIRTUALIZED"
                    - "CUSTOM"
            launch_options:
                description:
                    - ""
                    - Applicable when instance_type is 'compute'
                type: dict
                suboptions:
                    boot_volume_type:
                        description:
                            - "Emulation type for the boot volume.
                              * `ISCSI` - ISCSI attached block storage device.
                              * `SCSI` - Emulated SCSI disk.
                              * `IDE` - Emulated IDE disk.
                              * `VFIO` - Direct attached Virtual Function storage. This is the default option for local data
                              volumes on platform images.
                              * `PARAVIRTUALIZED` - Paravirtualized disk. This is the default for boot volumes and remote block
                              storage volumes on platform images."
                            - Applicable when instance_type is 'compute'
                        type: str
                        choices:
                            - "ISCSI"
                            - "SCSI"
                            - "IDE"
                            - "VFIO"
                            - "PARAVIRTUALIZED"
                    firmware:
                        description:
                            - "Firmware used to boot VM. Select the option that matches your operating system.
                              * `BIOS` - Boot VM using BIOS style firmware. This is compatible with both 32 bit and 64 bit operating
                              systems that boot using MBR style bootloaders.
                              * `UEFI_64` - Boot VM using UEFI style firmware compatible with 64 bit operating systems. This is the
                              default for platform images."
                            - Applicable when instance_type is 'compute'
                        type: str
                        choices:
                            - "BIOS"
                            - "UEFI_64"
                    network_type:
                        description:
                            - "Emulation type for the physical network interface card (NIC).
                              * `E1000` - Emulated Gigabit ethernet controller. Compatible with Linux e1000 network driver.
                              * `VFIO` - Direct attached Virtual Function network controller. This is the networking type
                              when you launch an instance using hardware-assisted (SR-IOV) networking.
                              * `PARAVIRTUALIZED` - VM instances launch with paravirtualized devices using VirtIO drivers."
                            - Applicable when instance_type is 'compute'
                        type: str
                        choices:
                            - "E1000"
                            - "VFIO"
                            - "PARAVIRTUALIZED"
                    remote_data_volume_type:
                        description:
                            - "Emulation type for volume.
                              * `ISCSI` - ISCSI attached block storage device.
                              * `SCSI` - Emulated SCSI disk.
                              * `IDE` - Emulated IDE disk.
                              * `VFIO` - Direct attached Virtual Function storage. This is the default option for local data
                              volumes on platform images.
                              * `PARAVIRTUALIZED` - Paravirtualized disk. This is the default for boot volumes and remote block
                              storage volumes on platform images."
                            - Applicable when instance_type is 'compute'
                        type: str
                        choices:
                            - "ISCSI"
                            - "SCSI"
                            - "IDE"
                            - "VFIO"
                            - "PARAVIRTUALIZED"
                    is_pv_encryption_in_transit_enabled:
                        description:
                            - Deprecated. Instead use `isPvEncryptionInTransitEnabled` in
                              L(InstanceConfigurationLaunchInstanceDetails,https://docs.cloud.oracle.com/en-
                              us/iaas/api/#/en/iaas/latest/datatypes/InstanceConfigurationLaunchInstanceDetails).
                            - Applicable when instance_type is 'compute'
                        type: bool
                    is_consistent_volume_naming_enabled:
                        description:
                            - Whether to enable consistent volume naming feature. Defaults to false.
                            - Applicable when instance_type is 'compute'
                        type: bool
            agent_config:
                description:
                    - ""
                    - Applicable when instance_type is 'compute'
                type: dict
                suboptions:
                    is_monitoring_disabled:
                        description:
                            - Whether Oracle Cloud Agent can gather performance metrics and monitor the instance using the
                              monitoring plugins. Default value is false (monitoring plugins are enabled).
                            - "These are the monitoring plugins: Compute Instance Monitoring
                              and Custom Logs Monitoring."
                            - The monitoring plugins are controlled by this parameter and by the per-plugin
                              configuration in the `pluginsConfig` object.
                            - "- If `isMonitoringDisabled` is true, all of the monitoring plugins are disabled, regardless of
                              the per-plugin configuration.
                              - If `isMonitoringDisabled` is false, all of the monitoring plugins are enabled. You
                              can optionally disable individual monitoring plugins by providing a value in the `pluginsConfig`
                              object."
                            - Applicable when instance_type is 'compute'
                        type: bool
                    is_management_disabled:
                        description:
                            - Whether Oracle Cloud Agent can run all the available management plugins.
                              Default value is false (management plugins are enabled).
                            - "These are the management plugins: OS Management Service Agent and Compute Instance
                              Run Command."
                            - The management plugins are controlled by this parameter and by the per-plugin
                              configuration in the `pluginsConfig` object.
                            - "- If `isManagementDisabled` is true, all of the management plugins are disabled, regardless of
                              the per-plugin configuration.
                              - If `isManagementDisabled` is false, all of the management plugins are enabled. You
                              can optionally disable individual management plugins by providing a value in the `pluginsConfig`
                              object."
                            - Applicable when instance_type is 'compute'
                        type: bool
                    are_all_plugins_disabled:
                        description:
                            - Whether Oracle Cloud Agent can run all the available plugins.
                              This includes the management and monitoring plugins.
                            - To get a list of available plugins, use the
                              L(ListInstanceagentAvailablePlugins,https://docs.cloud.oracle.com/en-
                              us/iaas/api/#/en/instanceagent/20180530/Plugin/ListInstanceagentAvailablePlugins)
                              operation in the Oracle Cloud Agent API. For more information about the available plugins, see
                              L(Managing Plugins with Oracle Cloud Agent,https://docs.cloud.oracle.com/iaas/Content/Compute/Tasks/manage-plugins.htm).
                            - Applicable when instance_type is 'compute'
                        type: bool
                    plugins_config:
                        description:
                            - The configuration of plugins associated with this instance.
                            - Applicable when instance_type is 'compute'
                        type: list
                        elements: dict
                        suboptions:
                            name:
                                description:
                                    - The plugin name. To get a list of available plugins, use the
                                      L(ListInstanceagentAvailablePlugins,https://docs.cloud.oracle.com/en-
                                      us/iaas/api/#/en/instanceagent/20180530/Plugin/ListInstanceagentAvailablePlugins)
                                      operation in the Oracle Cloud Agent API. For more information about the available plugins, see
                                      L(Managing Plugins with Oracle Cloud Agent,https://docs.cloud.oracle.com/iaas/Content/Compute/Tasks/manage-plugins.htm).
                                    - Required when instance_type is 'compute'
                                type: str
                                required: true
                            desired_state:
                                description:
                                    - Whether the plugin should be enabled or disabled.
                                    - To enable the monitoring and management plugins, the `isMonitoringDisabled` and
                                      `isManagementDisabled` attributes must also be set to false.
                                    - Required when instance_type is 'compute'
                                type: str
                                choices:
                                    - "ENABLED"
                                    - "DISABLED"
                                required: true
            is_pv_encryption_in_transit_enabled:
                description:
                    - Whether to enable in-transit encryption for the data volume's paravirtualized attachment. The default value is false.
                    - Applicable when instance_type is 'compute'
                type: bool
            preferred_maintenance_action:
                description:
                    - "The preferred maintenance action for an instance. The default is LIVE_MIGRATE, if live migration is supported.
                      * `LIVE_MIGRATE` - Run maintenance using a live migration.
                      * `REBOOT` - Run maintenance using a reboot."
                    - Applicable when instance_type is 'compute'
                type: str
                choices:
                    - "LIVE_MIGRATE"
                    - "REBOOT"
            instance_options:
                description:
                    - ""
                    - Applicable when instance_type is 'compute'
                type: dict
                suboptions:
                    are_legacy_imds_endpoints_disabled:
                        description:
                            - Whether to disable the legacy (/v1) instance metadata service endpoints.
                              Customers who have migrated to /v2 should set this to true for added security.
                              Default is false.
                            - Applicable when instance_type is 'compute'
                        type: bool
            availability_config:
                description:
                    - ""
                    - Applicable when instance_type is 'compute'
                type: dict
                suboptions:
                    is_live_migration_preferred:
                        description:
                            - Whether to live migrate supported VM instances to a healthy physical VM host without
                              disrupting running instances during infrastructure maintenance events. If null, Oracle
                              chooses the best option for migrating the VM during infrastructure maintenance events.
                            - Applicable when instance_type is 'compute'
                        type: bool
                    recovery_action:
                        description:
                            - "The lifecycle state for an instance when it is recovered after infrastructure maintenance.
                              * `RESTORE_INSTANCE` - The instance is restored to the lifecycle state it was in before the maintenance event.
                              If the instance was running, it is automatically rebooted. This is the default action when a value is not set.
                              * `STOP_INSTANCE` - The instance is recovered in the stopped state."
                            - Applicable when instance_type is 'compute'
                        type: str
                        choices:
                            - "RESTORE_INSTANCE"
                            - "STOP_INSTANCE"
            preemptible_instance_config:
                description:
                    - ""
                    - Applicable when instance_type is 'compute'
                type: dict
                suboptions:
                    preemption_action:
                        description:
                            - ""
                            - Required when instance_type is 'compute'
                        type: dict
                        required: true
                        suboptions:
                            type:
                                description:
                                    - The type of action to run when the instance is interrupted for eviction.
                                type: str
                                choices:
                                    - "TERMINATE"
                                required: true
                            preserve_boot_volume:
                                description:
                                    - Whether to preserve the boot volume that was used to launch the preemptible instance when the instance is terminated.
                                      Defaults to false if not specified.
                                type: bool
    secondary_vnics:
        description:
            - Secondary VNIC parameters.
            - Applicable only for I(action=launch).
            - Applicable when instance_type is 'compute'
        type: list
        elements: dict
        suboptions:
            create_vnic_details:
                description:
                    - ""
                    - Applicable when instance_type is 'compute'
                type: dict
                suboptions:
                    assign_public_ip:
                        description:
                            - Whether the VNIC should be assigned a public IP address. See the `assignPublicIp` attribute of
                              L(CreateVnicDetails,https://docs.cloud.oracle.com/en-us/iaas/api/#/en/iaas/latest/CreateVnicDetails/)
                              for more information.
                            - Applicable when instance_type is 'compute'
                        type: bool
                    assign_private_dns_record:
                        description:
                            - Whether the VNIC should be assigned a private DNS record. See the `assignPrivateDnsRecord` attribute of
                              L(CreateVnicDetails,https://docs.cloud.oracle.com/en-us/iaas/api/#/en/iaas/latest/CreateVnicDetails/)
                              for more information.
                            - Applicable when instance_type is 'compute'
                        type: bool
                    defined_tags:
                        description:
                            - Defined tags for this resource. Each key is predefined and scoped to a
                              namespace. For more information, see L(Resource
                              Tags,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/resourcetags.htm).
                            - "Example: `{\\"Operations\\": {\\"CostCenter\\": \\"42\\"}}`"
                            - Applicable when instance_type is 'compute'
                        type: dict
                    display_name:
                        description:
                            - A user-friendly name. Does not have to be unique, and it's changeable.
                              Avoid entering confidential information.
                            - Applicable when instance_type is 'compute'
                        type: str
                        aliases: ["name"]
                    freeform_tags:
                        description:
                            - Free-form tags for this resource. Each tag is a simple key-value pair with no
                              predefined name, type, or namespace. For more information, see L(Resource
                              Tags,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/resourcetags.htm).
                            - "Example: `{\\"Department\\": \\"Finance\\"}`"
                            - Applicable when instance_type is 'compute'
                        type: dict
                    hostname_label:
                        description:
                            - The hostname for the VNIC's primary private IP.
                              See the `hostnameLabel` attribute of L(CreateVnicDetails,https://docs.cloud.oracle.com/en-
                              us/iaas/api/#/en/iaas/latest/CreateVnicDetails/) for more information.
                            - Applicable when instance_type is 'compute'
                        type: str
                    nsg_ids:
                        description:
                            - A list of the OCIDs of the network security groups (NSGs) to add the VNIC to. For more
                              information about NSGs, see
                              L(NetworkSecurityGroup,https://docs.cloud.oracle.com/en-us/iaas/api/#/en/iaas/latest/NetworkSecurityGroup/).
                            - Applicable when instance_type is 'compute'
                        type: list
                        elements: str
                    private_ip:
                        description:
                            - A private IP address of your choice to assign to the VNIC.
                              See the `privateIp` attribute of L(CreateVnicDetails,https://docs.cloud.oracle.com/en-
                              us/iaas/api/#/en/iaas/latest/CreateVnicDetails/) for more information.
                            - Applicable when instance_type is 'compute'
                        type: str
                    skip_source_dest_check:
                        description:
                            - Whether the source/destination check is disabled on the VNIC.
                              See the `skipSourceDestCheck` attribute of L(CreateVnicDetails,https://docs.cloud.oracle.com/en-
                              us/iaas/api/#/en/iaas/latest/CreateVnicDetails/) for more information.
                            - Applicable when instance_type is 'compute'
                        type: bool
                    subnet_id:
                        description:
                            - The OCID of the subnet to create the VNIC in.
                              See the `subnetId` attribute of L(CreateVnicDetails,https://docs.cloud.oracle.com/en-
                              us/iaas/api/#/en/iaas/latest/CreateVnicDetails/) for more information.
                            - Applicable when instance_type is 'compute'
                        type: str
            display_name:
                description:
                    - A user-friendly name. Does not have to be unique, and it's changeable.
                      Avoid entering confidential information.
                    - Applicable when instance_type is 'compute'
                type: str
                aliases: ["name"]
            nic_index:
                description:
                    - Which physical network interface card (NIC) the VNIC will use. Defaults to 0.
                      Certain bare metal instance shapes have two active physical NICs (0 and 1). If
                      you add a secondary VNIC to one of these instances, you can specify which NIC
                      the VNIC will use. For more information, see
                      L(Virtual Network Interface Cards (VNICs),https://docs.cloud.oracle.com/iaas/Content/Network/Tasks/managingVNICs.htm).
                    - Applicable when instance_type is 'compute'
                type: int
    action:
        description:
            - The action to perform on the InstanceConfiguration.
        type: str
        required: true
        choices:
            - "change_compartment"
            - "launch"
extends_documentation_fragment: [ oracle.oci.oracle ]
"""

EXAMPLES = """
- name: Perform action change_compartment on instance_configuration
  oci_compute_management_instance_configuration_actions:
    # required
    compartment_id: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
    instance_configuration_id: "ocid1.instanceconfiguration.oc1..xxxxxxEXAMPLExxxxxx"
    action: change_compartment

- name: Perform action launch on instance_configuration with instance_type = instance_options
  oci_compute_management_instance_configuration_actions:
    # required
    instance_type: instance_options

    # optional
    options:
    - # required
      instance_type: instance_type_example

      # optional
      block_volumes:
      - # optional
        attach_details:
          # required
          type: iscsi

          # optional
          use_chap: true
          display_name: display_name_example
          is_read_only: true
          device: device_example
          is_shareable: true
        create_details:
          # optional
          availability_domain: Uocm:PHX-AD-1
          backup_policy_id: "ocid1.backuppolicy.oc1..xxxxxxEXAMPLExxxxxx"
          compartment_id: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
          is_auto_tune_enabled: true
          block_volume_replicas:
          - # required
            availability_domain: Uocm:PHX-AD-1

            # optional
            display_name: display_name_example
          defined_tags: {'Operations': {'CostCenter': 'US'}}
          display_name: display_name_example
          freeform_tags: {'Department': 'Finance'}
          kms_key_id: "ocid1.kmskey.oc1..xxxxxxEXAMPLExxxxxx"
          vpus_per_gb: 56
          size_in_gbs: 56
          source_details:
            # required
            type: volumeBackup

            # optional
            id: "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx"
          autotune_policies:
          - # required
            max_vpus_per_gb: 56
            autotune_type: PERFORMANCE_BASED
        volume_id: "ocid1.volume.oc1..xxxxxxEXAMPLExxxxxx"
      launch_details:
        # optional
        availability_domain: Uocm:PHX-AD-1
        capacity_reservation_id: "ocid1.capacityreservation.oc1..xxxxxxEXAMPLExxxxxx"
        compartment_id: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
        create_vnic_details:
          # optional
          assign_public_ip: true
          assign_private_dns_record: true
          defined_tags: {'Operations': {'CostCenter': 'US'}}
          display_name: display_name_example
          freeform_tags: {'Department': 'Finance'}
          hostname_label: hostname_label_example
          nsg_ids: [ "nsg_ids_example" ]
          private_ip: private_ip_example
          skip_source_dest_check: true
          subnet_id: "ocid1.subnet.oc1..xxxxxxEXAMPLExxxxxx"
        defined_tags: {'Operations': {'CostCenter': 'US'}}
        display_name: display_name_example
        extended_metadata: null
        freeform_tags: {'Department': 'Finance'}
        ipxe_script: ipxe_script_example
        metadata: null
        shape: shape_example
        shape_config:
          # optional
          ocpus: 3.4
          vcpus: 56
          memory_in_gbs: 3.4
          baseline_ocpu_utilization: BASELINE_1_8
          nvmes: 56
        platform_config:
          # required
          type: AMD_MILAN_BM

          # optional
          percentage_of_cores_enabled: 56
          numa_nodes_per_socket: NPS0
          is_symmetric_multi_threading_enabled: true
          is_access_control_service_enabled: true
          are_virtual_instructions_enabled: true
          is_input_output_memory_management_unit_enabled: true
          is_secure_boot_enabled: true
          is_trusted_platform_module_enabled: true
          is_measured_boot_enabled: true
          is_memory_encryption_enabled: true
        source_details:
          # required
          source_type: image

          # optional
          boot_volume_size_in_gbs: 56
          image_id: "ocid1.image.oc1..xxxxxxEXAMPLExxxxxx"
          kms_key_id: "ocid1.kmskey.oc1..xxxxxxEXAMPLExxxxxx"
          boot_volume_vpus_per_gb: 56
          instance_source_image_filter_details:
            # optional
            compartment_id: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
            defined_tags_filter: null
            operating_system: operating_system_example
            operating_system_version: operating_system_version_example
        fault_domain: FAULT-DOMAIN-1
        dedicated_vm_host_id: "ocid1.dedicatedvmhost.oc1..xxxxxxEXAMPLExxxxxx"
        launch_mode: NATIVE
        launch_options:
          # optional
          boot_volume_type: ISCSI
          firmware: BIOS
          network_type: E1000
          remote_data_volume_type: ISCSI
          is_pv_encryption_in_transit_enabled: true
          is_consistent_volume_naming_enabled: true
        agent_config:
          # optional
          is_monitoring_disabled: true
          is_management_disabled: true
          are_all_plugins_disabled: true
          plugins_config:
          - # required
            name: name_example
            desired_state: ENABLED
        is_pv_encryption_in_transit_enabled: true
        preferred_maintenance_action: LIVE_MIGRATE
        instance_options:
          # optional
          are_legacy_imds_endpoints_disabled: true
        availability_config:
          # optional
          is_live_migration_preferred: true
          recovery_action: RESTORE_INSTANCE
        preemptible_instance_config:
          # required
          preemption_action:
            # required
            type: TERMINATE

            # optional
            preserve_boot_volume: true
      secondary_vnics:
      - # optional
        create_vnic_details:
          # optional
          assign_public_ip: true
          assign_private_dns_record: true
          defined_tags: {'Operations': {'CostCenter': 'US'}}
          display_name: display_name_example
          freeform_tags: {'Department': 'Finance'}
          hostname_label: hostname_label_example
          nsg_ids: [ "nsg_ids_example" ]
          private_ip: private_ip_example
          skip_source_dest_check: true
          subnet_id: "ocid1.subnet.oc1..xxxxxxEXAMPLExxxxxx"
        display_name: display_name_example
        nic_index: 56

- name: Perform action launch on instance_configuration with instance_type = compute
  oci_compute_management_instance_configuration_actions:

    # optional
    instance_type: compute
    block_volumes:
    - # optional
      attach_details:
        # required
        type: iscsi

        # optional
        use_chap: true
        display_name: display_name_example
        is_read_only: true
        device: device_example
        is_shareable: true
      create_details:
        # optional
        availability_domain: Uocm:PHX-AD-1
        backup_policy_id: "ocid1.backuppolicy.oc1..xxxxxxEXAMPLExxxxxx"
        compartment_id: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
        is_auto_tune_enabled: true
        block_volume_replicas:
        - # required
          availability_domain: Uocm:PHX-AD-1

          # optional
          display_name: display_name_example
        defined_tags: {'Operations': {'CostCenter': 'US'}}
        display_name: display_name_example
        freeform_tags: {'Department': 'Finance'}
        kms_key_id: "ocid1.kmskey.oc1..xxxxxxEXAMPLExxxxxx"
        vpus_per_gb: 56
        size_in_gbs: 56
        source_details:
          # required
          type: volumeBackup

          # optional
          id: "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx"
        autotune_policies:
        - # required
          max_vpus_per_gb: 56
          autotune_type: PERFORMANCE_BASED
      volume_id: "ocid1.volume.oc1..xxxxxxEXAMPLExxxxxx"
    launch_details:
      # optional
      availability_domain: Uocm:PHX-AD-1
      capacity_reservation_id: "ocid1.capacityreservation.oc1..xxxxxxEXAMPLExxxxxx"
      compartment_id: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
      create_vnic_details:
        # optional
        assign_public_ip: true
        assign_private_dns_record: true
        defined_tags: {'Operations': {'CostCenter': 'US'}}
        display_name: display_name_example
        freeform_tags: {'Department': 'Finance'}
        hostname_label: hostname_label_example
        nsg_ids: [ "nsg_ids_example" ]
        private_ip: private_ip_example
        skip_source_dest_check: true
        subnet_id: "ocid1.subnet.oc1..xxxxxxEXAMPLExxxxxx"
      defined_tags: {'Operations': {'CostCenter': 'US'}}
      display_name: display_name_example
      extended_metadata: null
      freeform_tags: {'Department': 'Finance'}
      ipxe_script: ipxe_script_example
      metadata: null
      shape: shape_example
      shape_config:
        # optional
        ocpus: 3.4
        vcpus: 56
        memory_in_gbs: 3.4
        baseline_ocpu_utilization: BASELINE_1_8
        nvmes: 56
      platform_config:
        # required
        type: AMD_MILAN_BM

        # optional
        percentage_of_cores_enabled: 56
        numa_nodes_per_socket: NPS0
        is_symmetric_multi_threading_enabled: true
        is_access_control_service_enabled: true
        are_virtual_instructions_enabled: true
        is_input_output_memory_management_unit_enabled: true
        is_secure_boot_enabled: true
        is_trusted_platform_module_enabled: true
        is_measured_boot_enabled: true
        is_memory_encryption_enabled: true
      source_details:
        # required
        source_type: image

        # optional
        boot_volume_size_in_gbs: 56
        image_id: "ocid1.image.oc1..xxxxxxEXAMPLExxxxxx"
        kms_key_id: "ocid1.kmskey.oc1..xxxxxxEXAMPLExxxxxx"
        boot_volume_vpus_per_gb: 56
        instance_source_image_filter_details:
          # optional
          compartment_id: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
          defined_tags_filter: null
          operating_system: operating_system_example
          operating_system_version: operating_system_version_example
      fault_domain: FAULT-DOMAIN-1
      dedicated_vm_host_id: "ocid1.dedicatedvmhost.oc1..xxxxxxEXAMPLExxxxxx"
      launch_mode: NATIVE
      launch_options:
        # optional
        boot_volume_type: ISCSI
        firmware: BIOS
        network_type: E1000
        remote_data_volume_type: ISCSI
        is_pv_encryption_in_transit_enabled: true
        is_consistent_volume_naming_enabled: true
      agent_config:
        # optional
        is_monitoring_disabled: true
        is_management_disabled: true
        are_all_plugins_disabled: true
        plugins_config:
        - # required
          name: name_example
          desired_state: ENABLED
      is_pv_encryption_in_transit_enabled: true
      preferred_maintenance_action: LIVE_MIGRATE
      instance_options:
        # optional
        are_legacy_imds_endpoints_disabled: true
      availability_config:
        # optional
        is_live_migration_preferred: true
        recovery_action: RESTORE_INSTANCE
      preemptible_instance_config:
        # required
        preemption_action:
          # required
          type: TERMINATE

          # optional
          preserve_boot_volume: true
    secondary_vnics:
    - # optional
      create_vnic_details:
        # optional
        assign_public_ip: true
        assign_private_dns_record: true
        defined_tags: {'Operations': {'CostCenter': 'US'}}
        display_name: display_name_example
        freeform_tags: {'Department': 'Finance'}
        hostname_label: hostname_label_example
        nsg_ids: [ "nsg_ids_example" ]
        private_ip: private_ip_example
        skip_source_dest_check: true
        subnet_id: "ocid1.subnet.oc1..xxxxxxEXAMPLExxxxxx"
      display_name: display_name_example
      nic_index: 56

"""

RETURN = """
instance:
    description:
        - Details of the InstanceConfiguration resource acted upon by the current operation
    returned: on success
    type: complex
    contains:
        availability_domain:
            description:
                - The availability domain the instance is running in.
                - "Example: `Uocm:PHX-AD-1`"
            returned: on success
            type: str
            sample: Uocm:PHX-AD-1
        capacity_reservation_id:
            description:
                - The OCID of the compute capacity reservation this instance is launched under.
                  When this field contains an empty string or is null, the instance is not currently in a capacity reservation.
                  For more information, see L(Capacity Reservations,https://docs.cloud.oracle.com/iaas/Content/Compute/Tasks/reserve-capacity.htm#default).
            returned: on success
            type: str
            sample: "ocid1.capacityreservation.oc1..xxxxxxEXAMPLExxxxxx"
        compartment_id:
            description:
                - The OCID of the compartment that contains the instance.
            returned: on success
            type: str
            sample: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
        dedicated_vm_host_id:
            description:
                - The OCID of the dedicated virtual machine host that the instance is placed on.
            returned: on success
            type: str
            sample: "ocid1.dedicatedvmhost.oc1..xxxxxxEXAMPLExxxxxx"
        defined_tags:
            description:
                - Defined tags for this resource. Each key is predefined and scoped to a
                  namespace. For more information, see L(Resource Tags,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/resourcetags.htm).
                - "Example: `{\\"Operations\\": {\\"CostCenter\\": \\"42\\"}}`"
            returned: on success
            type: dict
            sample: {'Operations': {'CostCenter': 'US'}}
        display_name:
            description:
                - A user-friendly name. Does not have to be unique, and it's changeable.
                  Avoid entering confidential information.
            returned: on success
            type: str
            sample: display_name_example
        extended_metadata:
            description:
                - Additional metadata key/value pairs that you provide. They serve the same purpose and functionality
                  as fields in the `metadata` object.
                - They are distinguished from `metadata` fields in that these can be nested JSON objects (whereas `metadata`
                  fields are string/string maps only).
            returned: on success
            type: dict
            sample: {}
        fault_domain:
            description:
                - The name of the fault domain the instance is running in.
                - A fault domain is a grouping of hardware and infrastructure within an availability domain.
                  Each availability domain contains three fault domains. Fault domains let you distribute your
                  instances so that they are not on the same physical hardware within a single availability domain.
                  A hardware failure or Compute hardware maintenance that affects one fault domain does not affect
                  instances in other fault domains.
                - If you do not specify the fault domain, the system selects one for you.
                - "Example: `FAULT-DOMAIN-1`"
            returned: on success
            type: str
            sample: FAULT-DOMAIN-1
        freeform_tags:
            description:
                - Free-form tags for this resource. Each tag is a simple key-value pair with no
                  predefined name, type, or namespace. For more information, see L(Resource
                  Tags,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/resourcetags.htm).
                - "Example: `{\\"Department\\": \\"Finance\\"}`"
            returned: on success
            type: dict
            sample: {'Department': 'Finance'}
        id:
            description:
                - The OCID of the instance.
            returned: on success
            type: str
            sample: "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx"
        image_id:
            description:
                - Deprecated. Use `sourceDetails` instead.
            returned: on success
            type: str
            sample: "ocid1.image.oc1..xxxxxxEXAMPLExxxxxx"
        ipxe_script:
            description:
                - When a bare metal or virtual machine
                  instance boots, the iPXE firmware that runs on the instance is
                  configured to run an iPXE script to continue the boot process.
                - If you want more control over the boot process, you can provide
                  your own custom iPXE script that will run when the instance boots.
                  Be aware that the same iPXE script will run
                  every time an instance boots, not only after the initial
                  LaunchInstance call.
                - "The default iPXE script connects to the instance's local boot
                  volume over iSCSI and performs a network boot. If you use a custom iPXE
                  script and want to network-boot from the instance's local boot volume
                  over iSCSI the same way as the default iPXE script, use the
                  following iSCSI IP address: 169.254.0.2, and boot volume IQN:
                  iqn.2015-02.oracle.boot."
                - If your instance boot volume attachment type is paravirtualized,
                  the boot volume is attached to the instance through virtio-scsi and no iPXE script is used.
                  If your instance boot volume attachment type is paravirtualized
                  and you use custom iPXE to network boot into your instance,
                  the primary boot volume is attached as a data volume through virtio-scsi drive.
                - For more information about the Bring Your Own Image feature of
                  Oracle Cloud Infrastructure, see
                  L(Bring Your Own Image,https://docs.cloud.oracle.com/iaas/Content/Compute/References/bringyourownimage.htm).
                - For more information about iPXE, see http://ipxe.org.
            returned: on success
            type: str
            sample: ipxe_script_example
        launch_mode:
            description:
                - "Specifies the configuration mode for launching virtual machine (VM) instances. The configuration modes are:
                  * `NATIVE` - VM instances launch with iSCSI boot and VFIO devices. The default value for platform images.
                  * `EMULATED` - VM instances launch with emulated devices, such as the E1000 network driver and emulated SCSI disk controller.
                  * `PARAVIRTUALIZED` - VM instances launch with paravirtualized devices using VirtIO drivers.
                  * `CUSTOM` - VM instances launch with custom configuration settings specified in the `LaunchOptions` parameter."
            returned: on success
            type: str
            sample: NATIVE
        launch_options:
            description:
                - ""
            returned: on success
            type: complex
            contains:
                boot_volume_type:
                    description:
                        - "Emulation type for the boot volume.
                          * `ISCSI` - ISCSI attached block storage device.
                          * `SCSI` - Emulated SCSI disk.
                          * `IDE` - Emulated IDE disk.
                          * `VFIO` - Direct attached Virtual Function storage. This is the default option for local data
                          volumes on platform images.
                          * `PARAVIRTUALIZED` - Paravirtualized disk. This is the default for boot volumes and remote block
                          storage volumes on platform images."
                    returned: on success
                    type: str
                    sample: ISCSI
                firmware:
                    description:
                        - "Firmware used to boot VM. Select the option that matches your operating system.
                          * `BIOS` - Boot VM using BIOS style firmware. This is compatible with both 32 bit and 64 bit operating
                          systems that boot using MBR style bootloaders.
                          * `UEFI_64` - Boot VM using UEFI style firmware compatible with 64 bit operating systems. This is the
                          default for platform images."
                    returned: on success
                    type: str
                    sample: BIOS
                network_type:
                    description:
                        - "Emulation type for the physical network interface card (NIC).
                          * `E1000` - Emulated Gigabit ethernet controller. Compatible with Linux e1000 network driver.
                          * `VFIO` - Direct attached Virtual Function network controller. This is the networking type
                          when you launch an instance using hardware-assisted (SR-IOV) networking.
                          * `PARAVIRTUALIZED` - VM instances launch with paravirtualized devices using VirtIO drivers."
                    returned: on success
                    type: str
                    sample: E1000
                remote_data_volume_type:
                    description:
                        - "Emulation type for volume.
                          * `ISCSI` - ISCSI attached block storage device.
                          * `SCSI` - Emulated SCSI disk.
                          * `IDE` - Emulated IDE disk.
                          * `VFIO` - Direct attached Virtual Function storage. This is the default option for local data
                          volumes on platform images.
                          * `PARAVIRTUALIZED` - Paravirtualized disk. This is the default for boot volumes and remote block
                          storage volumes on platform images."
                    returned: on success
                    type: str
                    sample: ISCSI
                is_pv_encryption_in_transit_enabled:
                    description:
                        - Deprecated. Instead use `isPvEncryptionInTransitEnabled` in
                          L(LaunchInstanceDetails,https://docs.cloud.oracle.com/en-us/iaas/api/#/en/iaas/latest/datatypes/LaunchInstanceDetails).
                    returned: on success
                    type: bool
                    sample: true
                is_consistent_volume_naming_enabled:
                    description:
                        - Whether to enable consistent volume naming feature. Defaults to false.
                    returned: on success
                    type: bool
                    sample: true
        instance_options:
            description:
                - ""
            returned: on success
            type: complex
            contains:
                are_legacy_imds_endpoints_disabled:
                    description:
                        - Whether to disable the legacy (/v1) instance metadata service endpoints.
                          Customers who have migrated to /v2 should set this to true for added security.
                          Default is false.
                    returned: on success
                    type: bool
                    sample: true
        availability_config:
            description:
                - ""
            returned: on success
            type: complex
            contains:
                is_live_migration_preferred:
                    description:
                        - Whether to live migrate supported VM instances to a healthy physical VM host without
                          disrupting running instances during infrastructure maintenance events. If null, Oracle
                          chooses the best option for migrating the VM during infrastructure maintenance events.
                    returned: on success
                    type: bool
                    sample: true
                recovery_action:
                    description:
                        - "The lifecycle state for an instance when it is recovered after infrastructure maintenance.
                          * `RESTORE_INSTANCE` - The instance is restored to the lifecycle state it was in before the maintenance event.
                          If the instance was running, it is automatically rebooted. This is the default action when a value is not set.
                          * `STOP_INSTANCE` - The instance is recovered in the stopped state."
                    returned: on success
                    type: str
                    sample: RESTORE_INSTANCE
        preemptible_instance_config:
            description:
                - ""
            returned: on success
            type: complex
            contains:
                preemption_action:
                    description:
                        - ""
                    returned: on success
                    type: complex
                    contains:
                        type:
                            description:
                                - The type of action to run when the instance is interrupted for eviction.
                            returned: on success
                            type: str
                            sample: TERMINATE
                        preserve_boot_volume:
                            description:
                                - Whether to preserve the boot volume that was used to launch the preemptible instance when the instance is terminated. Defaults
                                  to false if not specified.
                            returned: on success
                            type: bool
                            sample: true
        lifecycle_state:
            description:
                - The current state of the instance.
            returned: on success
            type: str
            sample: MOVING
        metadata:
            description:
                - Custom metadata that you provide.
            returned: on success
            type: dict
            sample: {}
        region:
            description:
                - The region that contains the availability domain the instance is running in.
                - For the us-phoenix-1 and us-ashburn-1 regions, `phx` and `iad` are returned, respectively.
                  For all other regions, the full region name is returned.
                - "Examples: `phx`, `eu-frankfurt-1`"
            returned: on success
            type: str
            sample: us-phoenix-1
        shape:
            description:
                - The shape of the instance. The shape determines the number of CPUs and the amount of memory
                  allocated to the instance. You can enumerate all available shapes by calling
                  L(ListShapes,https://docs.cloud.oracle.com/en-us/iaas/api/#/en/iaas/latest/Shape/ListShapes).
            returned: on success
            type: str
            sample: shape_example
        shape_config:
            description:
                - ""
            returned: on success
            type: complex
            contains:
                ocpus:
                    description:
                        - The total number of OCPUs available to the instance.
                    returned: on success
                    type: float
                    sample: 3.4
                memory_in_gbs:
                    description:
                        - The total amount of memory available to the instance, in gigabytes.
                    returned: on success
                    type: float
                    sample: 3.4
                baseline_ocpu_utilization:
                    description:
                        - The baseline OCPU utilization for a subcore burstable VM instance. Leave this attribute blank for a
                          non-burstable instance, or explicitly specify non-burstable with `BASELINE_1_1`.
                        - "The following values are supported:
                          - `BASELINE_1_8` - baseline usage is 1/8 of an OCPU.
                          - `BASELINE_1_2` - baseline usage is 1/2 of an OCPU.
                          - `BASELINE_1_1` - baseline usage is the entire OCPU. This represents a non-burstable instance."
                    returned: on success
                    type: str
                    sample: BASELINE_1_8
                processor_description:
                    description:
                        - A short description of the instance's processor (CPU).
                    returned: on success
                    type: str
                    sample: processor_description_example
                networking_bandwidth_in_gbps:
                    description:
                        - The networking bandwidth available to the instance, in gigabits per second.
                    returned: on success
                    type: float
                    sample: 3.4
                max_vnic_attachments:
                    description:
                        - The maximum number of VNIC attachments for the instance.
                    returned: on success
                    type: int
                    sample: 56
                gpus:
                    description:
                        - The number of GPUs available to the instance.
                    returned: on success
                    type: int
                    sample: 56
                gpu_description:
                    description:
                        - A short description of the instance's graphics processing unit (GPU).
                        - If the instance does not have any GPUs, this field is `null`.
                    returned: on success
                    type: str
                    sample: gpu_description_example
                local_disks:
                    description:
                        - The number of local disks available to the instance.
                    returned: on success
                    type: int
                    sample: 56
                local_disks_total_size_in_gbs:
                    description:
                        - The aggregate size of all local disks, in gigabytes.
                        - If the instance does not have any local disks, this field is `null`.
                    returned: on success
                    type: float
                    sample: 3.4
                local_disk_description:
                    description:
                        - A short description of the local disks available to this instance.
                        - If the instance does not have any local disks, this field is `null`.
                    returned: on success
                    type: str
                    sample: local_disk_description_example
                vcpus:
                    description:
                        - The total number of VCPUs available to the instance. This can be used instead of OCPUs,
                          in which case the actual number of OCPUs will be calculated based on this value
                          and the actual hardware. This must be a multiple of 2.
                    returned: on success
                    type: int
                    sample: 56
        is_cross_numa_node:
            description:
                - Whether the instance's OCPUs and memory are distributed across multiple NUMA nodes.
            returned: on success
            type: bool
            sample: true
        source_details:
            description:
                - ""
            returned: on success
            type: complex
            contains:
                boot_volume_id:
                    description:
                        - The OCID of the boot volume used to boot the instance.
                    returned: on success
                    type: str
                    sample: "ocid1.bootvolume.oc1..xxxxxxEXAMPLExxxxxx"
                source_type:
                    description:
                        - The source type for the instance.
                          Use `image` when specifying the image OCID. Use `bootVolume` when specifying
                          the boot volume OCID.
                    returned: on success
                    type: str
                    sample: bootVolume
                boot_volume_size_in_gbs:
                    description:
                        - The size of the boot volume in GBs. Minimum value is 50 GB and maximum value is 32,768 GB (32 TB).
                    returned: on success
                    type: int
                    sample: 56
                image_id:
                    description:
                        - The OCID of the image used to boot the instance.
                    returned: on success
                    type: str
                    sample: "ocid1.image.oc1..xxxxxxEXAMPLExxxxxx"
                kms_key_id:
                    description:
                        - The OCID of the Vault service key to assign as the master encryption key for the boot volume.
                    returned: on success
                    type: str
                    sample: "ocid1.kmskey.oc1..xxxxxxEXAMPLExxxxxx"
                boot_volume_vpus_per_gb:
                    description:
                        - The number of volume performance units (VPUs) that will be applied to this volume per GB,
                          representing the Block Volume service's elastic performance options.
                          See L(Block Volume Performance
                          Levels,https://docs.cloud.oracle.com/iaas/Content/Block/Concepts/blockvolumeperformance.htm#perf_levels) for more information.
                        - "Allowed values:"
                        - " * `10`: Represents Balanced option."
                        - " * `20`: Represents Higher Performance option."
                        - " * `30`-`120`: Represents the Ultra High Performance option."
                        - For volumes with the auto-tuned performance feature enabled, this is set to the default (minimum) VPUs/GB.
                    returned: on success
                    type: int
                    sample: 56
                instance_source_image_filter_details:
                    description:
                        - ""
                    returned: on success
                    type: complex
                    contains:
                        compartment_id:
                            description:
                                - The OCID of the compartment containing images to search
                            returned: on success
                            type: str
                            sample: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
                        defined_tags_filter:
                            description:
                                - Filter based on these defined tags. Each key is predefined and scoped to a
                                  namespace. For more information, see L(Resource
                                  Tags,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/resourcetags.htm).
                            returned: on success
                            type: dict
                            sample: {}
                        operating_system:
                            description:
                                - The image's operating system.
                                - "Example: `Oracle Linux`"
                            returned: on success
                            type: str
                            sample: operating_system_example
                        operating_system_version:
                            description:
                                - The image's operating system version.
                                - "Example: `7.2`"
                            returned: on success
                            type: str
                            sample: operating_system_version_example
        system_tags:
            description:
                - "System tags for this resource. Each key is predefined and scoped to a namespace.
                  Example: `{\\"foo-namespace\\": {\\"bar-key\\": \\"value\\"}}`"
            returned: on success
            type: dict
            sample: {}
        time_created:
            description:
                - The date and time the instance was created, in the format defined by L(RFC3339,https://tools.ietf.org/html/rfc3339).
                - "Example: `2016-08-25T21:10:29.600Z`"
            returned: on success
            type: str
            sample: "2013-10-20T19:20:30+01:00"
        agent_config:
            description:
                - ""
            returned: on success
            type: complex
            contains:
                is_monitoring_disabled:
                    description:
                        - Whether Oracle Cloud Agent can gather performance metrics and monitor the instance using the
                          monitoring plugins.
                        - "These are the monitoring plugins: Compute Instance Monitoring
                          and Custom Logs Monitoring."
                        - The monitoring plugins are controlled by this parameter and by the per-plugin
                          configuration in the `pluginsConfig` object.
                        - "- If `isMonitoringDisabled` is true, all of the monitoring plugins are disabled, regardless of
                          the per-plugin configuration.
                          - If `isMonitoringDisabled` is false, all of the monitoring plugins are enabled. You
                          can optionally disable individual monitoring plugins by providing a value in the `pluginsConfig`
                          object."
                    returned: on success
                    type: bool
                    sample: true
                is_management_disabled:
                    description:
                        - Whether Oracle Cloud Agent can run all the available management plugins.
                        - "These are the management plugins: OS Management Service Agent and Compute Instance
                          Run Command."
                        - The management plugins are controlled by this parameter and by the per-plugin
                          configuration in the `pluginsConfig` object.
                        - "- If `isManagementDisabled` is true, all of the management plugins are disabled, regardless of
                          the per-plugin configuration.
                          - If `isManagementDisabled` is false, all of the management plugins are enabled. You
                          can optionally disable individual management plugins by providing a value in the `pluginsConfig`
                          object."
                    returned: on success
                    type: bool
                    sample: true
                are_all_plugins_disabled:
                    description:
                        - Whether Oracle Cloud Agent can run all of the available plugins.
                          This includes the management and monitoring plugins.
                        - For more information about the available plugins, see
                          L(Managing Plugins with Oracle Cloud Agent,https://docs.cloud.oracle.com/iaas/Content/Compute/Tasks/manage-plugins.htm).
                    returned: on success
                    type: bool
                    sample: true
                plugins_config:
                    description:
                        - The configuration of plugins associated with this instance.
                    returned: on success
                    type: complex
                    contains:
                        name:
                            description:
                                - The plugin name. To get a list of available plugins, use the
                                  L(ListInstanceagentAvailablePlugins,https://docs.cloud.oracle.com/en-
                                  us/iaas/api/#/en/instanceagent/20180530/Plugin/ListInstanceagentAvailablePlugins)
                                  operation in the Oracle Cloud Agent API. For more information about the available plugins, see
                                  L(Managing Plugins with Oracle Cloud Agent,https://docs.cloud.oracle.com/iaas/Content/Compute/Tasks/manage-plugins.htm).
                            returned: on success
                            type: str
                            sample: name_example
                        desired_state:
                            description:
                                - Whether the plugin should be enabled or disabled.
                                - To enable the monitoring and management plugins, the `isMonitoringDisabled` and
                                  `isManagementDisabled` attributes must also be set to false.
                            returned: on success
                            type: str
                            sample: ENABLED
        time_maintenance_reboot_due:
            description:
                - "The date and time the instance is expected to be stopped / started,  in the format defined by L(RFC3339,https://tools.ietf.org/html/rfc3339).
                  After that time if instance hasn't been rebooted, Oracle will reboot the instance within 24 hours of the due time.
                  Regardless of how the instance was stopped, the flag will be reset to empty as soon as instance reaches Stopped state.
                  Example: `2018-05-25T21:10:29.600Z`"
            returned: on success
            type: str
            sample: "2013-10-20T19:20:30+01:00"
        platform_config:
            description:
                - ""
            returned: on success
            type: complex
            contains:
                is_access_control_service_enabled:
                    description:
                        - Whether the Access Control Service is enabled on the instance. When enabled,
                          the platform can enforce PCIe device isolation, required for VFIO device pass-through.
                    returned: on success
                    type: bool
                    sample: true
                are_virtual_instructions_enabled:
                    description:
                        - Whether virtualization instructions are available. For example, Secure Virtual Machine for AMD shapes
                          or VT-x for Intel shapes.
                    returned: on success
                    type: bool
                    sample: true
                numa_nodes_per_socket:
                    description:
                        - The number of NUMA nodes per socket (NPS).
                    returned: on success
                    type: str
                    sample: NPS0
                is_symmetric_multi_threading_enabled:
                    description:
                        - Whether symmetric multithreading is enabled on the instance. Symmetric multithreading is also
                          called simultaneous multithreading (SMT) or Intel Hyper-Threading.
                        - Intel and AMD processors have two hardware execution threads per core (OCPU). SMT permits multiple
                          independent threads of execution, to better use the resources and increase the efficiency
                          of the CPU. When multithreading is disabled, only one thread is permitted to run on each core, which
                          can provide higher or more predictable performance for some workloads.
                    returned: on success
                    type: bool
                    sample: true
                is_input_output_memory_management_unit_enabled:
                    description:
                        - Whether the input-output memory management unit is enabled.
                    returned: on success
                    type: bool
                    sample: true
                percentage_of_cores_enabled:
                    description:
                        - The percentage of cores enabled. Value must be a multiple of 25%. If the requested percentage
                          results in a fractional number of cores, the system rounds up the number of cores across processors
                          and provisions an instance with a whole number of cores.
                        - If the applications that you run on the instance use a core-based licensing model and need fewer cores
                          than the full size of the shape, you can disable cores to reduce your licensing costs. The instance
                          itself is billed for the full shape, regardless of whether all cores are enabled.
                    returned: on success
                    type: int
                    sample: 56
                type:
                    description:
                        - The type of platform being configured.
                    returned: on success
                    type: str
                    sample: AMD_MILAN_BM
                is_secure_boot_enabled:
                    description:
                        - Whether Secure Boot is enabled on the instance.
                    returned: on success
                    type: bool
                    sample: true
                is_trusted_platform_module_enabled:
                    description:
                        - Whether the Trusted Platform Module (TPM) is enabled on the instance.
                    returned: on success
                    type: bool
                    sample: true
                is_measured_boot_enabled:
                    description:
                        - Whether the Measured Boot feature is enabled on the instance.
                    returned: on success
                    type: bool
                    sample: true
                is_memory_encryption_enabled:
                    description:
                        - Whether the instance is a confidential instance. If this value is `true`, the instance is a confidential instance. The default value
                          is `false`.
                    returned: on success
                    type: bool
                    sample: true
        instance_configuration_id:
            description:
                - The OCID of the Instance Configuration used to source launch details for this instance. Any other fields supplied in the instance launch
                  request override the details stored in the Instance Configuration for this instance launch.
            returned: on success
            type: str
            sample: "ocid1.instanceconfiguration.oc1..xxxxxxEXAMPLExxxxxx"
    sample: {
        "availability_domain": "Uocm:PHX-AD-1",
        "capacity_reservation_id": "ocid1.capacityreservation.oc1..xxxxxxEXAMPLExxxxxx",
        "compartment_id": "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx",
        "dedicated_vm_host_id": "ocid1.dedicatedvmhost.oc1..xxxxxxEXAMPLExxxxxx",
        "defined_tags": {'Operations': {'CostCenter': 'US'}},
        "display_name": "display_name_example",
        "extended_metadata": {},
        "fault_domain": "FAULT-DOMAIN-1",
        "freeform_tags": {'Department': 'Finance'},
        "id": "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx",
        "image_id": "ocid1.image.oc1..xxxxxxEXAMPLExxxxxx",
        "ipxe_script": "ipxe_script_example",
        "launch_mode": "NATIVE",
        "launch_options": {
            "boot_volume_type": "ISCSI",
            "firmware": "BIOS",
            "network_type": "E1000",
            "remote_data_volume_type": "ISCSI",
            "is_pv_encryption_in_transit_enabled": true,
            "is_consistent_volume_naming_enabled": true
        },
        "instance_options": {
            "are_legacy_imds_endpoints_disabled": true
        },
        "availability_config": {
            "is_live_migration_preferred": true,
            "recovery_action": "RESTORE_INSTANCE"
        },
        "preemptible_instance_config": {
            "preemption_action": {
                "type": "TERMINATE",
                "preserve_boot_volume": true
            }
        },
        "lifecycle_state": "MOVING",
        "metadata": {},
        "region": "us-phoenix-1",
        "shape": "shape_example",
        "shape_config": {
            "ocpus": 3.4,
            "memory_in_gbs": 3.4,
            "baseline_ocpu_utilization": "BASELINE_1_8",
            "processor_description": "processor_description_example",
            "networking_bandwidth_in_gbps": 3.4,
            "max_vnic_attachments": 56,
            "gpus": 56,
            "gpu_description": "gpu_description_example",
            "local_disks": 56,
            "local_disks_total_size_in_gbs": 3.4,
            "local_disk_description": "local_disk_description_example",
            "vcpus": 56
        },
        "is_cross_numa_node": true,
        "source_details": {
            "boot_volume_id": "ocid1.bootvolume.oc1..xxxxxxEXAMPLExxxxxx",
            "source_type": "bootVolume",
            "boot_volume_size_in_gbs": 56,
            "image_id": "ocid1.image.oc1..xxxxxxEXAMPLExxxxxx",
            "kms_key_id": "ocid1.kmskey.oc1..xxxxxxEXAMPLExxxxxx",
            "boot_volume_vpus_per_gb": 56,
            "instance_source_image_filter_details": {
                "compartment_id": "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx",
                "defined_tags_filter": {},
                "operating_system": "operating_system_example",
                "operating_system_version": "operating_system_version_example"
            }
        },
        "system_tags": {},
        "time_created": "2013-10-20T19:20:30+01:00",
        "agent_config": {
            "is_monitoring_disabled": true,
            "is_management_disabled": true,
            "are_all_plugins_disabled": true,
            "plugins_config": [{
                "name": "name_example",
                "desired_state": "ENABLED"
            }]
        },
        "time_maintenance_reboot_due": "2013-10-20T19:20:30+01:00",
        "platform_config": {
            "is_access_control_service_enabled": true,
            "are_virtual_instructions_enabled": true,
            "numa_nodes_per_socket": "NPS0",
            "is_symmetric_multi_threading_enabled": true,
            "is_input_output_memory_management_unit_enabled": true,
            "percentage_of_cores_enabled": 56,
            "type": "AMD_MILAN_BM",
            "is_secure_boot_enabled": true,
            "is_trusted_platform_module_enabled": true,
            "is_measured_boot_enabled": true,
            "is_memory_encryption_enabled": true
        },
        "instance_configuration_id": "ocid1.instanceconfiguration.oc1..xxxxxxEXAMPLExxxxxx"
    }

instance_configuration:
    description:
        - Details of the InstanceConfiguration resource acted upon by the current operation
    returned: on success
    type: complex
    contains:
        compartment_id:
            description:
                - The L(OCID,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the compartment
                  containing the instance configuration.
            returned: on success
            type: str
            sample: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
        defined_tags:
            description:
                - Defined tags for this resource. Each key is predefined and scoped to a
                  namespace. For more information, see L(Resource Tags,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/resourcetags.htm).
                - "Example: `{\\"Operations\\": {\\"CostCenter\\": \\"42\\"}}`"
            returned: on success
            type: dict
            sample: {'Operations': {'CostCenter': 'US'}}
        display_name:
            description:
                - A user-friendly name. Does not have to be unique, and it's changeable.
                  Avoid entering confidential information.
            returned: on success
            type: str
            sample: display_name_example
        freeform_tags:
            description:
                - Free-form tags for this resource. Each tag is a simple key-value pair with no
                  predefined name, type, or namespace. For more information, see L(Resource
                  Tags,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/resourcetags.htm).
                - "Example: `{\\"Department\\": \\"Finance\\"}`"
            returned: on success
            type: dict
            sample: {'Department': 'Finance'}
        id:
            description:
                - The L(OCID,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the instance configuration.
            returned: on success
            type: str
            sample: "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx"
        instance_details:
            description:
                - ""
            returned: on success
            type: complex
            contains:
                block_volumes:
                    description:
                        - Block volume parameters.
                    returned: on success
                    type: complex
                    contains:
                        attach_details:
                            description:
                                - ""
                            returned: on success
                            type: complex
                            contains:
                                use_chap:
                                    description:
                                        - Whether to use CHAP authentication for the volume attachment. Defaults to false.
                                    returned: on success
                                    type: bool
                                    sample: true
                                display_name:
                                    description:
                                        - A user-friendly name. Does not have to be unique, and it's changeable.
                                          Avoid entering confidential information.
                                    returned: on success
                                    type: str
                                    sample: display_name_example
                                is_read_only:
                                    description:
                                        - Whether the attachment should be created in read-only mode.
                                    returned: on success
                                    type: bool
                                    sample: true
                                device:
                                    description:
                                        - The device name.
                                    returned: on success
                                    type: str
                                    sample: device_example
                                is_shareable:
                                    description:
                                        - Whether the attachment should be created in shareable mode. If an attachment
                                          is created in shareable mode, then other instances can attach the same volume, provided
                                          that they also create their attachments in shareable mode. Only certain volume types can
                                          be attached in shareable mode. Defaults to false if not specified.
                                    returned: on success
                                    type: bool
                                    sample: true
                                type:
                                    description:
                                        - "The type of volume. The only supported values are \\"iscsi\\" and \\"paravirtualized\\"."
                                    returned: on success
                                    type: str
                                    sample: iscsi
                                is_pv_encryption_in_transit_enabled:
                                    description:
                                        - Whether to enable in-transit encryption for the data volume's paravirtualized attachment. The default value is false.
                                    returned: on success
                                    type: bool
                                    sample: true
                        create_details:
                            description:
                                - ""
                            returned: on success
                            type: complex
                            contains:
                                availability_domain:
                                    description:
                                        - The availability domain of the volume.
                                        - "Example: `Uocm:PHX-AD-1`"
                                    returned: on success
                                    type: str
                                    sample: Uocm:PHX-AD-1
                                backup_policy_id:
                                    description:
                                        - If provided, specifies the ID of the volume backup policy to assign to the newly
                                          created volume. If omitted, no policy will be assigned.
                                    returned: on success
                                    type: str
                                    sample: "ocid1.backuppolicy.oc1..xxxxxxEXAMPLExxxxxx"
                                compartment_id:
                                    description:
                                        - The OCID of the compartment that contains the volume.
                                    returned: on success
                                    type: str
                                    sample: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
                                is_auto_tune_enabled:
                                    description:
                                        - Specifies whether the auto-tune performance is enabled for this boot volume. This field is deprecated.
                                          Use the `InstanceConfigurationDetachedVolumeAutotunePolicy` instead to enable the volume for detached autotune.
                                    returned: on success
                                    type: bool
                                    sample: true
                                block_volume_replicas:
                                    description:
                                        - The list of block volume replicas to be enabled for this volume
                                          in the specified destination availability domains.
                                    returned: on success
                                    type: complex
                                    contains:
                                        display_name:
                                            description:
                                                - "The display name of the block volume replica. You may optionally specify a *display name* for
                                                  the block volume replica, otherwise a default is provided."
                                            returned: on success
                                            type: str
                                            sample: display_name_example
                                        availability_domain:
                                            description:
                                                - The availability domain of the block volume replica.
                                                - "Example: `Uocm:PHX-AD-1`"
                                            returned: on success
                                            type: str
                                            sample: Uocm:PHX-AD-1
                                defined_tags:
                                    description:
                                        - Defined tags for this resource. Each key is predefined and scoped to a
                                          namespace. For more information, see L(Resource
                                          Tags,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/resourcetags.htm).
                                        - "Example: `{\\"Operations\\": {\\"CostCenter\\": \\"42\\"}}`"
                                    returned: on success
                                    type: dict
                                    sample: {'Operations': {'CostCenter': 'US'}}
                                display_name:
                                    description:
                                        - A user-friendly name. Does not have to be unique, and it's changeable.
                                          Avoid entering confidential information.
                                    returned: on success
                                    type: str
                                    sample: display_name_example
                                freeform_tags:
                                    description:
                                        - Free-form tags for this resource. Each tag is a simple key-value pair with no
                                          predefined name, type, or namespace. For more information, see L(Resource
                                          Tags,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/resourcetags.htm).
                                        - "Example: `{\\"Department\\": \\"Finance\\"}`"
                                    returned: on success
                                    type: dict
                                    sample: {'Department': 'Finance'}
                                kms_key_id:
                                    description:
                                        - The OCID of the Vault service key to assign as the master encryption key
                                          for the volume.
                                    returned: on success
                                    type: str
                                    sample: "ocid1.kmskey.oc1..xxxxxxEXAMPLExxxxxx"
                                vpus_per_gb:
                                    description:
                                        - The number of volume performance units (VPUs) that will be applied to this volume per GB,
                                          representing the Block Volume service's elastic performance options.
                                          See L(Block Volume Performance
                                          Levels,https://docs.cloud.oracle.com/iaas/Content/Block/Concepts/blockvolumeperformance.htm#perf_levels) for more
                                          information.
                                        - "Allowed values:"
                                        - " * `0`: Represents Lower Cost option."
                                        - " * `10`: Represents Balanced option."
                                        - " * `20`: Represents Higher Performance option."
                                        - " * `30`-`120`: Represents the Ultra High Performance option."
                                        - For performance autotune enabled volumes, it would be the Default(Minimum) VPUs/GB.
                                    returned: on success
                                    type: int
                                    sample: 56
                                size_in_gbs:
                                    description:
                                        - The size of the volume in GBs.
                                    returned: on success
                                    type: int
                                    sample: 56
                                source_details:
                                    description:
                                        - ""
                                    returned: on success
                                    type: complex
                                    contains:
                                        type:
                                            description:
                                                - ""
                                            returned: on success
                                            type: str
                                            sample: volume
                                        id:
                                            description:
                                                - The OCID of the volume.
                                            returned: on success
                                            type: str
                                            sample: "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx"
                                autotune_policies:
                                    description:
                                        - The list of autotune policies enabled for this volume.
                                    returned: on success
                                    type: complex
                                    contains:
                                        autotune_type:
                                            description:
                                                - This specifies the type of autotunes supported by OCI.
                                            returned: on success
                                            type: str
                                            sample: DETACHED_VOLUME
                                        max_vpus_per_gb:
                                            description:
                                                - This will be the maximum VPUs/GB performance level that the volume will be auto-tuned
                                                  temporarily based on performance monitoring.
                                            returned: on success
                                            type: int
                                            sample: 56
                        volume_id:
                            description:
                                - The OCID of the volume.
                            returned: on success
                            type: str
                            sample: "ocid1.volume.oc1..xxxxxxEXAMPLExxxxxx"
                launch_details:
                    description:
                        - ""
                    returned: on success
                    type: complex
                    contains:
                        availability_domain:
                            description:
                                - The availability domain of the instance.
                                - "Example: `Uocm:PHX-AD-1`"
                            returned: on success
                            type: str
                            sample: Uocm:PHX-AD-1
                        capacity_reservation_id:
                            description:
                                - The OCID of the compute capacity reservation this instance is launched under.
                            returned: on success
                            type: str
                            sample: "ocid1.capacityreservation.oc1..xxxxxxEXAMPLExxxxxx"
                        compartment_id:
                            description:
                                - The OCID of the compartment containing the instance.
                                  Instances created from instance configurations are placed in the same compartment
                                  as the instance that was used to create the instance configuration.
                            returned: on success
                            type: str
                            sample: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
                        create_vnic_details:
                            description:
                                - ""
                            returned: on success
                            type: complex
                            contains:
                                assign_public_ip:
                                    description:
                                        - Whether the VNIC should be assigned a public IP address. See the `assignPublicIp` attribute of
                                          L(CreateVnicDetails,https://docs.cloud.oracle.com/en-us/iaas/api/#/en/iaas/latest/CreateVnicDetails/)
                                          for more information.
                                    returned: on success
                                    type: bool
                                    sample: true
                                assign_private_dns_record:
                                    description:
                                        - Whether the VNIC should be assigned a private DNS record. See the `assignPrivateDnsRecord` attribute of
                                          L(CreateVnicDetails,https://docs.cloud.oracle.com/en-us/iaas/api/#/en/iaas/latest/CreateVnicDetails/)
                                          for more information.
                                    returned: on success
                                    type: bool
                                    sample: true
                                defined_tags:
                                    description:
                                        - Defined tags for this resource. Each key is predefined and scoped to a
                                          namespace. For more information, see L(Resource
                                          Tags,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/resourcetags.htm).
                                        - "Example: `{\\"Operations\\": {\\"CostCenter\\": \\"42\\"}}`"
                                    returned: on success
                                    type: dict
                                    sample: {'Operations': {'CostCenter': 'US'}}
                                display_name:
                                    description:
                                        - A user-friendly name. Does not have to be unique, and it's changeable.
                                          Avoid entering confidential information.
                                    returned: on success
                                    type: str
                                    sample: display_name_example
                                freeform_tags:
                                    description:
                                        - Free-form tags for this resource. Each tag is a simple key-value pair with no
                                          predefined name, type, or namespace. For more information, see L(Resource
                                          Tags,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/resourcetags.htm).
                                        - "Example: `{\\"Department\\": \\"Finance\\"}`"
                                    returned: on success
                                    type: dict
                                    sample: {'Department': 'Finance'}
                                hostname_label:
                                    description:
                                        - The hostname for the VNIC's primary private IP.
                                          See the `hostnameLabel` attribute of L(CreateVnicDetails,https://docs.cloud.oracle.com/en-
                                          us/iaas/api/#/en/iaas/latest/CreateVnicDetails/) for more information.
                                    returned: on success
                                    type: str
                                    sample: hostname_label_example
                                nsg_ids:
                                    description:
                                        - A list of the OCIDs of the network security groups (NSGs) to add the VNIC to. For more
                                          information about NSGs, see
                                          L(NetworkSecurityGroup,https://docs.cloud.oracle.com/en-us/iaas/api/#/en/iaas/latest/NetworkSecurityGroup/).
                                    returned: on success
                                    type: list
                                    sample: []
                                private_ip:
                                    description:
                                        - A private IP address of your choice to assign to the VNIC.
                                          See the `privateIp` attribute of L(CreateVnicDetails,https://docs.cloud.oracle.com/en-
                                          us/iaas/api/#/en/iaas/latest/CreateVnicDetails/) for more information.
                                    returned: on success
                                    type: str
                                    sample: private_ip_example
                                skip_source_dest_check:
                                    description:
                                        - Whether the source/destination check is disabled on the VNIC.
                                          See the `skipSourceDestCheck` attribute of L(CreateVnicDetails,https://docs.cloud.oracle.com/en-
                                          us/iaas/api/#/en/iaas/latest/CreateVnicDetails/) for more information.
                                    returned: on success
                                    type: bool
                                    sample: true
                                subnet_id:
                                    description:
                                        - The OCID of the subnet to create the VNIC in.
                                          See the `subnetId` attribute of L(CreateVnicDetails,https://docs.cloud.oracle.com/en-
                                          us/iaas/api/#/en/iaas/latest/CreateVnicDetails/) for more information.
                                    returned: on success
                                    type: str
                                    sample: "ocid1.subnet.oc1..xxxxxxEXAMPLExxxxxx"
                        defined_tags:
                            description:
                                - Defined tags for this resource. Each key is predefined and scoped to a
                                  namespace. For more information, see L(Resource
                                  Tags,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/resourcetags.htm).
                                - "Example: `{\\"Operations\\": {\\"CostCenter\\": \\"42\\"}}`"
                            returned: on success
                            type: dict
                            sample: {'Operations': {'CostCenter': 'US'}}
                        display_name:
                            description:
                                - A user-friendly name. Does not have to be unique, and it's changeable.
                                  Avoid entering confidential information.
                            returned: on success
                            type: str
                            sample: display_name_example
                        extended_metadata:
                            description:
                                - Additional metadata key/value pairs that you provide. They serve the same purpose and
                                  functionality as fields in the `metadata` object.
                                - They are distinguished from `metadata` fields in that these can be nested JSON objects
                                  (whereas `metadata` fields are string/string maps only).
                                - The combined size of the `metadata` and `extendedMetadata` objects can be a maximum of
                                  32,000 bytes.
                            returned: on success
                            type: dict
                            sample: {}
                        freeform_tags:
                            description:
                                - Free-form tags for this resource. Each tag is a simple key-value pair with no
                                  predefined name, type, or namespace. For more information, see L(Resource
                                  Tags,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/resourcetags.htm).
                                - "Example: `{\\"Department\\": \\"Finance\\"}`"
                            returned: on success
                            type: dict
                            sample: {'Department': 'Finance'}
                        ipxe_script:
                            description:
                                - This is an advanced option.
                                - When a bare metal or virtual machine
                                  instance boots, the iPXE firmware that runs on the instance is
                                  configured to run an iPXE script to continue the boot process.
                                - If you want more control over the boot process, you can provide
                                  your own custom iPXE script that will run when the instance boots;
                                  however, you should be aware that the same iPXE script will run
                                  every time an instance boots; not only after the initial
                                  LaunchInstance call.
                                - "The default iPXE script connects to the instance's local boot
                                  volume over iSCSI and performs a network boot. If you use a custom iPXE
                                  script and want to network-boot from the instance's local boot volume
                                  over iSCSI the same way as the default iPXE script, you should use the
                                  following iSCSI IP address: 169.254.0.2, and boot volume IQN:
                                  iqn.2015-02.oracle.boot."
                                - For more information about the Bring Your Own Image feature of
                                  Oracle Cloud Infrastructure, see
                                  L(Bring Your Own Image,https://docs.cloud.oracle.com/iaas/Content/Compute/References/bringyourownimage.htm).
                                - For more information about iPXE, see http://ipxe.org.
                            returned: on success
                            type: str
                            sample: ipxe_script_example
                        metadata:
                            description:
                                - Custom metadata key/value pairs that you provide, such as the SSH public key
                                  required to connect to the instance.
                                - "A metadata service runs on every launched instance. The service is an HTTP
                                  endpoint listening on 169.254.169.254. You can use the service to:"
                                - "* Provide information to L(Cloud-Init,https://cloudinit.readthedocs.org/en/latest/)
                                    to be used for various system initialization tasks."
                                - "* Get information about the instance, including the custom metadata that you
                                    provide when you launch the instance."
                                - "**Providing Cloud-Init Metadata**"
                                - "You can use the following metadata key names to provide information to
                                   Cloud-Init:"
                                - "**\\"ssh_authorized_keys\\"** - Provide one or more public SSH keys to be
                                   included in the `~/.ssh/authorized_keys` file for the default user on the
                                   instance. Use a newline character to separate multiple keys. The SSH
                                   keys must be in the format necessary for the `authorized_keys` file, as shown
                                   in the example below."
                                - "**\\"user_data\\"** - Provide your own base64-encoded data to be used by
                                   Cloud-Init to run custom scripts or provide custom Cloud-Init configuration. For
                                   information about how to take advantage of user data, see the
                                   L(Cloud-Init Documentation,http://cloudinit.readthedocs.org/en/latest/topics/format.html)."
                                - "**Metadata Example**"
                                - "     \\"metadata\\" : {
                                           \\"quake_bot_level\\" : \\"Severe\\",
                                           \\"ssh_authorized_keys\\" : \\"ssh-rsa <your_public_SSH_key>== rsa-key-20160227\\",
                                           \\"user_data\\" : \\"<your_public_SSH_key>==\\"
                                        }
                                   **Getting Metadata on the Instance**"
                                - "To get information about your instance, connect to the instance using SSH and issue any of the
                                   following GET requests:"
                                - "    curl -H \\"Authorization: Bearer Oracle\\" http://169.254.169.254/opc/v2/instance/
                                       curl -H \\"Authorization: Bearer Oracle\\" http://169.254.169.254/opc/v2/instance/metadata/
                                       curl -H \\"Authorization: Bearer Oracle\\" http://169.254.169.254/opc/v2/instance/metadata/<any-key-name>"
                                -  You'll get back a response that includes all the instance information; only the metadata information; or
                                   the metadata information for the specified key name, respectively.
                                -  The combined size of the `metadata` and `extendedMetadata` objects can be a maximum of 32,000 bytes.
                            returned: on success
                            type: dict
                            sample: {}
                        shape:
                            description:
                                - The shape of an instance. The shape determines the number of CPUs, amount of memory,
                                  and other resources allocated to the instance.
                                - You can enumerate all available shapes by calling L(ListShapes,https://docs.cloud.oracle.com/en-
                                  us/iaas/api/#/en/iaas/latest/Shape/ListShapes).
                            returned: on success
                            type: str
                            sample: shape_example
                        shape_config:
                            description:
                                - ""
                            returned: on success
                            type: complex
                            contains:
                                ocpus:
                                    description:
                                        - The total number of OCPUs available to the instance.
                                    returned: on success
                                    type: float
                                    sample: 3.4
                                vcpus:
                                    description:
                                        - The total number of VCPUs available to the instance. This can be used instead of OCPUs,
                                          in which case the actual number of OCPUs will be calculated based on this value
                                          and the actual hardware. This must be a multiple of 2.
                                    returned: on success
                                    type: int
                                    sample: 56
                                memory_in_gbs:
                                    description:
                                        - The total amount of memory available to the instance, in gigabytes.
                                    returned: on success
                                    type: float
                                    sample: 3.4
                                baseline_ocpu_utilization:
                                    description:
                                        - The baseline OCPU utilization for a subcore burstable VM instance. Leave this attribute blank for a
                                          non-burstable instance, or explicitly specify non-burstable with `BASELINE_1_1`.
                                        - "The following values are supported:
                                          - `BASELINE_1_8` - baseline usage is 1/8 of an OCPU.
                                          - `BASELINE_1_2` - baseline usage is 1/2 of an OCPU.
                                          - `BASELINE_1_1` - baseline usage is an entire OCPU. This represents a non-burstable instance."
                                    returned: on success
                                    type: str
                                    sample: BASELINE_1_8
                                nvmes:
                                    description:
                                        - The number of NVMe drives to be used for storage. A single drive has 6.8 TB available.
                                    returned: on success
                                    type: int
                                    sample: 56
                        platform_config:
                            description:
                                - ""
                            returned: on success
                            type: complex
                            contains:
                                is_access_control_service_enabled:
                                    description:
                                        - Whether the Access Control Service is enabled on the instance. When enabled,
                                          the platform can enforce PCIe device isolation, required for VFIO device pass-through.
                                    returned: on success
                                    type: bool
                                    sample: true
                                are_virtual_instructions_enabled:
                                    description:
                                        - Whether virtualization instructions are available. For example, Secure Virtual Machine for AMD shapes
                                          or VT-x for Intel shapes.
                                    returned: on success
                                    type: bool
                                    sample: true
                                numa_nodes_per_socket:
                                    description:
                                        - The number of NUMA nodes per socket (NPS).
                                    returned: on success
                                    type: str
                                    sample: NPS0
                                is_symmetric_multi_threading_enabled:
                                    description:
                                        - Whether symmetric multithreading is enabled on the instance. Symmetric multithreading is also
                                          called simultaneous multithreading (SMT) or Intel Hyper-Threading.
                                        - Intel and AMD processors have two hardware execution threads per core (OCPU). SMT permits multiple
                                          independent threads of execution, to better use the resources and increase the efficiency
                                          of the CPU. When multithreading is disabled, only one thread is permitted to run on each core, which
                                          can provide higher or more predictable performance for some workloads.
                                    returned: on success
                                    type: bool
                                    sample: true
                                is_input_output_memory_management_unit_enabled:
                                    description:
                                        - Whether the input-output memory management unit is enabled.
                                    returned: on success
                                    type: bool
                                    sample: true
                                percentage_of_cores_enabled:
                                    description:
                                        - The percentage of cores enabled. Value must be a multiple of 25%. If the requested percentage
                                          results in a fractional number of cores, the system rounds up the number of cores across processors
                                          and provisions an instance with a whole number of cores.
                                        - If the applications that you run on the instance use a core-based licensing model and need fewer cores
                                          than the full size of the shape, you can disable cores to reduce your licensing costs. The instance
                                          itself is billed for the full shape, regardless of whether all cores are enabled.
                                    returned: on success
                                    type: int
                                    sample: 56
                                type:
                                    description:
                                        - The type of platform being configured.
                                    returned: on success
                                    type: str
                                    sample: AMD_MILAN_BM
                                is_secure_boot_enabled:
                                    description:
                                        - Whether Secure Boot is enabled on the instance.
                                    returned: on success
                                    type: bool
                                    sample: true
                                is_trusted_platform_module_enabled:
                                    description:
                                        - Whether the Trusted Platform Module (TPM) is enabled on the instance.
                                    returned: on success
                                    type: bool
                                    sample: true
                                is_measured_boot_enabled:
                                    description:
                                        - Whether the Measured Boot feature is enabled on the instance.
                                    returned: on success
                                    type: bool
                                    sample: true
                                is_memory_encryption_enabled:
                                    description:
                                        - Whether the instance is a confidential instance. If this value is `true`, the instance is a confidential instance. The
                                          default value is `false`.
                                    returned: on success
                                    type: bool
                                    sample: true
                        source_details:
                            description:
                                - ""
                            returned: on success
                            type: complex
                            contains:
                                boot_volume_id:
                                    description:
                                        - The OCID of the boot volume used to boot the instance.
                                    returned: on success
                                    type: str
                                    sample: "ocid1.bootvolume.oc1..xxxxxxEXAMPLExxxxxx"
                                source_type:
                                    description:
                                        - The source type for the instance.
                                          Use `image` when specifying the image OCID. Use `bootVolume` when specifying
                                          the boot volume OCID.
                                    returned: on success
                                    type: str
                                    sample: bootVolume
                                boot_volume_size_in_gbs:
                                    description:
                                        - The size of the boot volume in GBs. The minimum value is 50 GB and the maximum
                                          value is 32,768 GB (32 TB).
                                    returned: on success
                                    type: int
                                    sample: 56
                                image_id:
                                    description:
                                        - The OCID of the image used to boot the instance.
                                    returned: on success
                                    type: str
                                    sample: "ocid1.image.oc1..xxxxxxEXAMPLExxxxxx"
                                kms_key_id:
                                    description:
                                        - The OCID of the Vault service key to assign as the master encryption key for the boot volume.
                                    returned: on success
                                    type: str
                                    sample: "ocid1.kmskey.oc1..xxxxxxEXAMPLExxxxxx"
                                boot_volume_vpus_per_gb:
                                    description:
                                        - The number of volume performance units (VPUs) that will be applied to this volume per GB,
                                          representing the Block Volume service's elastic performance options.
                                          See L(Block Volume Performance
                                          Levels,https://docs.cloud.oracle.com/iaas/Content/Block/Concepts/blockvolumeperformance.htm#perf_levels) for more
                                          information.
                                        - "Allowed values:"
                                        - " * `10`: Represents Balanced option."
                                        - " * `20`: Represents Higher Performance option."
                                        - " * `30`-`120`: Represents the Ultra High Performance option."
                                        - For performance autotune enabled volumes, it would be the Default(Minimum) VPUs/GB.
                                    returned: on success
                                    type: int
                                    sample: 56
                                instance_source_image_filter_details:
                                    description:
                                        - ""
                                    returned: on success
                                    type: complex
                                    contains:
                                        compartment_id:
                                            description:
                                                - The OCID of the compartment containing images to search
                                            returned: on success
                                            type: str
                                            sample: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
                                        defined_tags_filter:
                                            description:
                                                - Filter based on these defined tags. Each key is predefined and scoped to a
                                                  namespace. For more information, see L(Resource
                                                  Tags,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/resourcetags.htm).
                                            returned: on success
                                            type: dict
                                            sample: {}
                                        operating_system:
                                            description:
                                                - The image's operating system.
                                                - "Example: `Oracle Linux`"
                                            returned: on success
                                            type: str
                                            sample: operating_system_example
                                        operating_system_version:
                                            description:
                                                - The image's operating system version.
                                                - "Example: `7.2`"
                                            returned: on success
                                            type: str
                                            sample: operating_system_version_example
                        fault_domain:
                            description:
                                - A fault domain is a grouping of hardware and infrastructure within an availability domain.
                                  Each availability domain contains three fault domains. Fault domains let you distribute your
                                  instances so that they are not on the same physical hardware within a single availability domain.
                                  A hardware failure or Compute hardware maintenance that affects one fault domain does not affect
                                  instances in other fault domains.
                                - If you do not specify the fault domain, the system selects one for you.
                                - To get a list of fault domains, use the
                                  L(ListFaultDomains,https://docs.cloud.oracle.com/en-us/iaas/api/#/en/identity/20160918/FaultDomain/ListFaultDomains) operation
                                  in the
                                  Identity and Access Management Service API.
                                - "Example: `FAULT-DOMAIN-1`"
                            returned: on success
                            type: str
                            sample: FAULT-DOMAIN-1
                        dedicated_vm_host_id:
                            description:
                                - The OCID of the dedicated virtual machine host to place the instance on.
                                - Dedicated VM hosts can be used when launching individual instances from an instance configuration. They
                                  cannot be used to launch instance pools.
                            returned: on success
                            type: str
                            sample: "ocid1.dedicatedvmhost.oc1..xxxxxxEXAMPLExxxxxx"
                        launch_mode:
                            description:
                                - "Specifies the configuration mode for launching virtual machine (VM) instances. The configuration modes are:
                                  * `NATIVE` - VM instances launch with iSCSI boot and VFIO devices. The default value for platform images.
                                  * `EMULATED` - VM instances launch with emulated devices, such as the E1000 network driver and emulated SCSI disk controller.
                                  * `PARAVIRTUALIZED` - VM instances launch with paravirtualized devices using VirtIO drivers.
                                  * `CUSTOM` - VM instances launch with custom configuration settings specified in the `LaunchOptions` parameter."
                            returned: on success
                            type: str
                            sample: NATIVE
                        launch_options:
                            description:
                                - ""
                            returned: on success
                            type: complex
                            contains:
                                boot_volume_type:
                                    description:
                                        - "Emulation type for the boot volume.
                                          * `ISCSI` - ISCSI attached block storage device.
                                          * `SCSI` - Emulated SCSI disk.
                                          * `IDE` - Emulated IDE disk.
                                          * `VFIO` - Direct attached Virtual Function storage. This is the default option for local data
                                          volumes on platform images.
                                          * `PARAVIRTUALIZED` - Paravirtualized disk. This is the default for boot volumes and remote block
                                          storage volumes on platform images."
                                    returned: on success
                                    type: str
                                    sample: ISCSI
                                firmware:
                                    description:
                                        - "Firmware used to boot VM. Select the option that matches your operating system.
                                          * `BIOS` - Boot VM using BIOS style firmware. This is compatible with both 32 bit and 64 bit operating
                                          systems that boot using MBR style bootloaders.
                                          * `UEFI_64` - Boot VM using UEFI style firmware compatible with 64 bit operating systems. This is the
                                          default for platform images."
                                    returned: on success
                                    type: str
                                    sample: BIOS
                                network_type:
                                    description:
                                        - "Emulation type for the physical network interface card (NIC).
                                          * `E1000` - Emulated Gigabit ethernet controller. Compatible with Linux e1000 network driver.
                                          * `VFIO` - Direct attached Virtual Function network controller. This is the networking type
                                          when you launch an instance using hardware-assisted (SR-IOV) networking.
                                          * `PARAVIRTUALIZED` - VM instances launch with paravirtualized devices using VirtIO drivers."
                                    returned: on success
                                    type: str
                                    sample: E1000
                                remote_data_volume_type:
                                    description:
                                        - "Emulation type for volume.
                                          * `ISCSI` - ISCSI attached block storage device.
                                          * `SCSI` - Emulated SCSI disk.
                                          * `IDE` - Emulated IDE disk.
                                          * `VFIO` - Direct attached Virtual Function storage. This is the default option for local data
                                          volumes on platform images.
                                          * `PARAVIRTUALIZED` - Paravirtualized disk. This is the default for boot volumes and remote block
                                          storage volumes on platform images."
                                    returned: on success
                                    type: str
                                    sample: ISCSI
                                is_pv_encryption_in_transit_enabled:
                                    description:
                                        - Deprecated. Instead use `isPvEncryptionInTransitEnabled` in
                                          L(InstanceConfigurationLaunchInstanceDetails,https://docs.cloud.oracle.com/en-
                                          us/iaas/api/#/en/iaas/latest/datatypes/InstanceConfigurationLaunchInstanceDetails).
                                    returned: on success
                                    type: bool
                                    sample: true
                                is_consistent_volume_naming_enabled:
                                    description:
                                        - Whether to enable consistent volume naming feature. Defaults to false.
                                    returned: on success
                                    type: bool
                                    sample: true
                        agent_config:
                            description:
                                - ""
                            returned: on success
                            type: complex
                            contains:
                                is_monitoring_disabled:
                                    description:
                                        - Whether Oracle Cloud Agent can gather performance metrics and monitor the instance using the
                                          monitoring plugins. Default value is false (monitoring plugins are enabled).
                                        - "These are the monitoring plugins: Compute Instance Monitoring
                                          and Custom Logs Monitoring."
                                        - The monitoring plugins are controlled by this parameter and by the per-plugin
                                          configuration in the `pluginsConfig` object.
                                        - "- If `isMonitoringDisabled` is true, all of the monitoring plugins are disabled, regardless of
                                          the per-plugin configuration.
                                          - If `isMonitoringDisabled` is false, all of the monitoring plugins are enabled. You
                                          can optionally disable individual monitoring plugins by providing a value in the `pluginsConfig`
                                          object."
                                    returned: on success
                                    type: bool
                                    sample: true
                                is_management_disabled:
                                    description:
                                        - Whether Oracle Cloud Agent can run all the available management plugins.
                                          Default value is false (management plugins are enabled).
                                        - "These are the management plugins: OS Management Service Agent and Compute Instance
                                          Run Command."
                                        - The management plugins are controlled by this parameter and by the per-plugin
                                          configuration in the `pluginsConfig` object.
                                        - "- If `isManagementDisabled` is true, all of the management plugins are disabled, regardless of
                                          the per-plugin configuration.
                                          - If `isManagementDisabled` is false, all of the management plugins are enabled. You
                                          can optionally disable individual management plugins by providing a value in the `pluginsConfig`
                                          object."
                                    returned: on success
                                    type: bool
                                    sample: true
                                are_all_plugins_disabled:
                                    description:
                                        - Whether Oracle Cloud Agent can run all the available plugins.
                                          This includes the management and monitoring plugins.
                                        - To get a list of available plugins, use the
                                          L(ListInstanceagentAvailablePlugins,https://docs.cloud.oracle.com/en-
                                          us/iaas/api/#/en/instanceagent/20180530/Plugin/ListInstanceagentAvailablePlugins)
                                          operation in the Oracle Cloud Agent API. For more information about the available plugins, see
                                          L(Managing Plugins with Oracle Cloud Agent,https://docs.cloud.oracle.com/iaas/Content/Compute/Tasks/manage-
                                          plugins.htm).
                                    returned: on success
                                    type: bool
                                    sample: true
                                plugins_config:
                                    description:
                                        - The configuration of plugins associated with this instance.
                                    returned: on success
                                    type: complex
                                    contains:
                                        name:
                                            description:
                                                - The plugin name. To get a list of available plugins, use the
                                                  L(ListInstanceagentAvailablePlugins,https://docs.cloud.oracle.com/en-
                                                  us/iaas/api/#/en/instanceagent/20180530/Plugin/ListInstanceagentAvailablePlugins)
                                                  operation in the Oracle Cloud Agent API. For more information about the available plugins, see
                                                  L(Managing Plugins with Oracle Cloud Agent,https://docs.cloud.oracle.com/iaas/Content/Compute/Tasks/manage-
                                                  plugins.htm).
                                            returned: on success
                                            type: str
                                            sample: name_example
                                        desired_state:
                                            description:
                                                - Whether the plugin should be enabled or disabled.
                                                - To enable the monitoring and management plugins, the `isMonitoringDisabled` and
                                                  `isManagementDisabled` attributes must also be set to false.
                                            returned: on success
                                            type: str
                                            sample: ENABLED
                        is_pv_encryption_in_transit_enabled:
                            description:
                                - Whether to enable in-transit encryption for the data volume's paravirtualized attachment. The default value is false.
                            returned: on success
                            type: bool
                            sample: true
                        preferred_maintenance_action:
                            description:
                                - "The preferred maintenance action for an instance. The default is LIVE_MIGRATE, if live migration is supported.
                                  * `LIVE_MIGRATE` - Run maintenance using a live migration.
                                  * `REBOOT` - Run maintenance using a reboot."
                            returned: on success
                            type: str
                            sample: LIVE_MIGRATE
                        instance_options:
                            description:
                                - ""
                            returned: on success
                            type: complex
                            contains:
                                are_legacy_imds_endpoints_disabled:
                                    description:
                                        - Whether to disable the legacy (/v1) instance metadata service endpoints.
                                          Customers who have migrated to /v2 should set this to true for added security.
                                          Default is false.
                                    returned: on success
                                    type: bool
                                    sample: true
                        availability_config:
                            description:
                                - ""
                            returned: on success
                            type: complex
                            contains:
                                is_live_migration_preferred:
                                    description:
                                        - Whether to live migrate supported VM instances to a healthy physical VM host without
                                          disrupting running instances during infrastructure maintenance events. If null, Oracle
                                          chooses the best option for migrating the VM during infrastructure maintenance events.
                                    returned: on success
                                    type: bool
                                    sample: true
                                recovery_action:
                                    description:
                                        - "The lifecycle state for an instance when it is recovered after infrastructure maintenance.
                                          * `RESTORE_INSTANCE` - The instance is restored to the lifecycle state it was in before the maintenance event.
                                          If the instance was running, it is automatically rebooted. This is the default action when a value is not set.
                                          * `STOP_INSTANCE` - The instance is recovered in the stopped state."
                                    returned: on success
                                    type: str
                                    sample: RESTORE_INSTANCE
                        preemptible_instance_config:
                            description:
                                - ""
                            returned: on success
                            type: complex
                            contains:
                                preemption_action:
                                    description:
                                        - ""
                                    returned: on success
                                    type: complex
                                    contains:
                                        type:
                                            description:
                                                - The type of action to run when the instance is interrupted for eviction.
                                            returned: on success
                                            type: str
                                            sample: TERMINATE
                                        preserve_boot_volume:
                                            description:
                                                - Whether to preserve the boot volume that was used to launch the preemptible instance when the instance is
                                                  terminated. Defaults to false if not specified.
                                            returned: on success
                                            type: bool
                                            sample: true
                secondary_vnics:
                    description:
                        - Secondary VNIC parameters.
                    returned: on success
                    type: complex
                    contains:
                        create_vnic_details:
                            description:
                                - ""
                            returned: on success
                            type: complex
                            contains:
                                assign_public_ip:
                                    description:
                                        - Whether the VNIC should be assigned a public IP address. See the `assignPublicIp` attribute of
                                          L(CreateVnicDetails,https://docs.cloud.oracle.com/en-us/iaas/api/#/en/iaas/latest/CreateVnicDetails/)
                                          for more information.
                                    returned: on success
                                    type: bool
                                    sample: true
                                assign_private_dns_record:
                                    description:
                                        - Whether the VNIC should be assigned a private DNS record. See the `assignPrivateDnsRecord` attribute of
                                          L(CreateVnicDetails,https://docs.cloud.oracle.com/en-us/iaas/api/#/en/iaas/latest/CreateVnicDetails/)
                                          for more information.
                                    returned: on success
                                    type: bool
                                    sample: true
                                defined_tags:
                                    description:
                                        - Defined tags for this resource. Each key is predefined and scoped to a
                                          namespace. For more information, see L(Resource
                                          Tags,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/resourcetags.htm).
                                        - "Example: `{\\"Operations\\": {\\"CostCenter\\": \\"42\\"}}`"
                                    returned: on success
                                    type: dict
                                    sample: {'Operations': {'CostCenter': 'US'}}
                                display_name:
                                    description:
                                        - A user-friendly name. Does not have to be unique, and it's changeable.
                                          Avoid entering confidential information.
                                    returned: on success
                                    type: str
                                    sample: display_name_example
                                freeform_tags:
                                    description:
                                        - Free-form tags for this resource. Each tag is a simple key-value pair with no
                                          predefined name, type, or namespace. For more information, see L(Resource
                                          Tags,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/resourcetags.htm).
                                        - "Example: `{\\"Department\\": \\"Finance\\"}`"
                                    returned: on success
                                    type: dict
                                    sample: {'Department': 'Finance'}
                                hostname_label:
                                    description:
                                        - The hostname for the VNIC's primary private IP.
                                          See the `hostnameLabel` attribute of L(CreateVnicDetails,https://docs.cloud.oracle.com/en-
                                          us/iaas/api/#/en/iaas/latest/CreateVnicDetails/) for more information.
                                    returned: on success
                                    type: str
                                    sample: hostname_label_example
                                nsg_ids:
                                    description:
                                        - A list of the OCIDs of the network security groups (NSGs) to add the VNIC to. For more
                                          information about NSGs, see
                                          L(NetworkSecurityGroup,https://docs.cloud.oracle.com/en-us/iaas/api/#/en/iaas/latest/NetworkSecurityGroup/).
                                    returned: on success
                                    type: list
                                    sample: []
                                private_ip:
                                    description:
                                        - A private IP address of your choice to assign to the VNIC.
                                          See the `privateIp` attribute of L(CreateVnicDetails,https://docs.cloud.oracle.com/en-
                                          us/iaas/api/#/en/iaas/latest/CreateVnicDetails/) for more information.
                                    returned: on success
                                    type: str
                                    sample: private_ip_example
                                skip_source_dest_check:
                                    description:
                                        - Whether the source/destination check is disabled on the VNIC.
                                          See the `skipSourceDestCheck` attribute of L(CreateVnicDetails,https://docs.cloud.oracle.com/en-
                                          us/iaas/api/#/en/iaas/latest/CreateVnicDetails/) for more information.
                                    returned: on success
                                    type: bool
                                    sample: true
                                subnet_id:
                                    description:
                                        - The OCID of the subnet to create the VNIC in.
                                          See the `subnetId` attribute of L(CreateVnicDetails,https://docs.cloud.oracle.com/en-
                                          us/iaas/api/#/en/iaas/latest/CreateVnicDetails/) for more information.
                                    returned: on success
                                    type: str
                                    sample: "ocid1.subnet.oc1..xxxxxxEXAMPLExxxxxx"
                        display_name:
                            description:
                                - A user-friendly name. Does not have to be unique, and it's changeable.
                                  Avoid entering confidential information.
                            returned: on success
                            type: str
                            sample: display_name_example
                        nic_index:
                            description:
                                - Which physical network interface card (NIC) the VNIC will use. Defaults to 0.
                                  Certain bare metal instance shapes have two active physical NICs (0 and 1). If
                                  you add a secondary VNIC to one of these instances, you can specify which NIC
                                  the VNIC will use. For more information, see
                                  L(Virtual Network Interface Cards (VNICs),https://docs.cloud.oracle.com/iaas/Content/Network/Tasks/managingVNICs.htm).
                            returned: on success
                            type: int
                            sample: 56
                instance_type:
                    description:
                        - The type of instance details. Supported instanceType is compute
                    returned: on success
                    type: str
                    sample: compute
                options:
                    description:
                        - The Compute Instance Configuration parameters.
                    returned: on success
                    type: complex
                    contains:
                        instance_type:
                            description:
                                - The type of instance details. Supported instanceType is compute
                            returned: on success
                            type: str
                            sample: instance_type_example
                        block_volumes:
                            description:
                                - Block volume parameters.
                            returned: on success
                            type: complex
                            contains:
                                attach_details:
                                    description:
                                        - ""
                                    returned: on success
                                    type: complex
                                    contains:
                                        use_chap:
                                            description:
                                                - Whether to use CHAP authentication for the volume attachment. Defaults to false.
                                            returned: on success
                                            type: bool
                                            sample: true
                                        display_name:
                                            description:
                                                - A user-friendly name. Does not have to be unique, and it's changeable.
                                                  Avoid entering confidential information.
                                            returned: on success
                                            type: str
                                            sample: display_name_example
                                        is_read_only:
                                            description:
                                                - Whether the attachment should be created in read-only mode.
                                            returned: on success
                                            type: bool
                                            sample: true
                                        device:
                                            description:
                                                - The device name.
                                            returned: on success
                                            type: str
                                            sample: device_example
                                        is_shareable:
                                            description:
                                                - Whether the attachment should be created in shareable mode. If an attachment
                                                  is created in shareable mode, then other instances can attach the same volume, provided
                                                  that they also create their attachments in shareable mode. Only certain volume types can
                                                  be attached in shareable mode. Defaults to false if not specified.
                                            returned: on success
                                            type: bool
                                            sample: true
                                        type:
                                            description:
                                                - "The type of volume. The only supported values are \\"iscsi\\" and \\"paravirtualized\\"."
                                            returned: on success
                                            type: str
                                            sample: iscsi
                                        is_pv_encryption_in_transit_enabled:
                                            description:
                                                - Whether to enable in-transit encryption for the data volume's paravirtualized attachment. The default value is
                                                  false.
                                            returned: on success
                                            type: bool
                                            sample: true
                                create_details:
                                    description:
                                        - ""
                                    returned: on success
                                    type: complex
                                    contains:
                                        availability_domain:
                                            description:
                                                - The availability domain of the volume.
                                                - "Example: `Uocm:PHX-AD-1`"
                                            returned: on success
                                            type: str
                                            sample: Uocm:PHX-AD-1
                                        backup_policy_id:
                                            description:
                                                - If provided, specifies the ID of the volume backup policy to assign to the newly
                                                  created volume. If omitted, no policy will be assigned.
                                            returned: on success
                                            type: str
                                            sample: "ocid1.backuppolicy.oc1..xxxxxxEXAMPLExxxxxx"
                                        compartment_id:
                                            description:
                                                - The OCID of the compartment that contains the volume.
                                            returned: on success
                                            type: str
                                            sample: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
                                        is_auto_tune_enabled:
                                            description:
                                                - Specifies whether the auto-tune performance is enabled for this boot volume. This field is deprecated.
                                                  Use the `InstanceConfigurationDetachedVolumeAutotunePolicy` instead to enable the volume for detached
                                                  autotune.
                                            returned: on success
                                            type: bool
                                            sample: true
                                        block_volume_replicas:
                                            description:
                                                - The list of block volume replicas to be enabled for this volume
                                                  in the specified destination availability domains.
                                            returned: on success
                                            type: complex
                                            contains:
                                                display_name:
                                                    description:
                                                        - "The display name of the block volume replica. You may optionally specify a *display name* for
                                                          the block volume replica, otherwise a default is provided."
                                                    returned: on success
                                                    type: str
                                                    sample: display_name_example
                                                availability_domain:
                                                    description:
                                                        - The availability domain of the block volume replica.
                                                        - "Example: `Uocm:PHX-AD-1`"
                                                    returned: on success
                                                    type: str
                                                    sample: Uocm:PHX-AD-1
                                        defined_tags:
                                            description:
                                                - Defined tags for this resource. Each key is predefined and scoped to a
                                                  namespace. For more information, see L(Resource
                                                  Tags,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/resourcetags.htm).
                                                - "Example: `{\\"Operations\\": {\\"CostCenter\\": \\"42\\"}}`"
                                            returned: on success
                                            type: dict
                                            sample: {'Operations': {'CostCenter': 'US'}}
                                        display_name:
                                            description:
                                                - A user-friendly name. Does not have to be unique, and it's changeable.
                                                  Avoid entering confidential information.
                                            returned: on success
                                            type: str
                                            sample: display_name_example
                                        freeform_tags:
                                            description:
                                                - Free-form tags for this resource. Each tag is a simple key-value pair with no
                                                  predefined name, type, or namespace. For more information, see L(Resource
                                                  Tags,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/resourcetags.htm).
                                                - "Example: `{\\"Department\\": \\"Finance\\"}`"
                                            returned: on success
                                            type: dict
                                            sample: {'Department': 'Finance'}
                                        kms_key_id:
                                            description:
                                                - The OCID of the Vault service key to assign as the master encryption key
                                                  for the volume.
                                            returned: on success
                                            type: str
                                            sample: "ocid1.kmskey.oc1..xxxxxxEXAMPLExxxxxx"
                                        vpus_per_gb:
                                            description:
                                                - The number of volume performance units (VPUs) that will be applied to this volume per GB,
                                                  representing the Block Volume service's elastic performance options.
                                                  See L(Block Volume Performance
                                                  Levels,https://docs.cloud.oracle.com/iaas/Content/Block/Concepts/blockvolumeperformance.htm#perf_levels) for
                                                  more information.
                                                - "Allowed values:"
                                                - " * `0`: Represents Lower Cost option."
                                                - " * `10`: Represents Balanced option."
                                                - " * `20`: Represents Higher Performance option."
                                                - " * `30`-`120`: Represents the Ultra High Performance option."
                                                - For performance autotune enabled volumes, it would be the Default(Minimum) VPUs/GB.
                                            returned: on success
                                            type: int
                                            sample: 56
                                        size_in_gbs:
                                            description:
                                                - The size of the volume in GBs.
                                            returned: on success
                                            type: int
                                            sample: 56
                                        source_details:
                                            description:
                                                - ""
                                            returned: on success
                                            type: complex
                                            contains:
                                                type:
                                                    description:
                                                        - ""
                                                    returned: on success
                                                    type: str
                                                    sample: volume
                                                id:
                                                    description:
                                                        - The OCID of the volume.
                                                    returned: on success
                                                    type: str
                                                    sample: "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx"
                                        autotune_policies:
                                            description:
                                                - The list of autotune policies enabled for this volume.
                                            returned: on success
                                            type: complex
                                            contains:
                                                autotune_type:
                                                    description:
                                                        - This specifies the type of autotunes supported by OCI.
                                                    returned: on success
                                                    type: str
                                                    sample: DETACHED_VOLUME
                                                max_vpus_per_gb:
                                                    description:
                                                        - This will be the maximum VPUs/GB performance level that the volume will be auto-tuned
                                                          temporarily based on performance monitoring.
                                                    returned: on success
                                                    type: int
                                                    sample: 56
                                volume_id:
                                    description:
                                        - The OCID of the volume.
                                    returned: on success
                                    type: str
                                    sample: "ocid1.volume.oc1..xxxxxxEXAMPLExxxxxx"
                        launch_details:
                            description:
                                - ""
                            returned: on success
                            type: complex
                            contains:
                                availability_domain:
                                    description:
                                        - The availability domain of the instance.
                                        - "Example: `Uocm:PHX-AD-1`"
                                    returned: on success
                                    type: str
                                    sample: Uocm:PHX-AD-1
                                capacity_reservation_id:
                                    description:
                                        - The OCID of the compute capacity reservation this instance is launched under.
                                    returned: on success
                                    type: str
                                    sample: "ocid1.capacityreservation.oc1..xxxxxxEXAMPLExxxxxx"
                                compartment_id:
                                    description:
                                        - The OCID of the compartment containing the instance.
                                          Instances created from instance configurations are placed in the same compartment
                                          as the instance that was used to create the instance configuration.
                                    returned: on success
                                    type: str
                                    sample: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
                                create_vnic_details:
                                    description:
                                        - ""
                                    returned: on success
                                    type: complex
                                    contains:
                                        assign_public_ip:
                                            description:
                                                - Whether the VNIC should be assigned a public IP address. See the `assignPublicIp` attribute of
                                                  L(CreateVnicDetails,https://docs.cloud.oracle.com/en-us/iaas/api/#/en/iaas/latest/CreateVnicDetails/)
                                                  for more information.
                                            returned: on success
                                            type: bool
                                            sample: true
                                        assign_private_dns_record:
                                            description:
                                                - Whether the VNIC should be assigned a private DNS record. See the `assignPrivateDnsRecord` attribute of
                                                  L(CreateVnicDetails,https://docs.cloud.oracle.com/en-us/iaas/api/#/en/iaas/latest/CreateVnicDetails/)
                                                  for more information.
                                            returned: on success
                                            type: bool
                                            sample: true
                                        defined_tags:
                                            description:
                                                - Defined tags for this resource. Each key is predefined and scoped to a
                                                  namespace. For more information, see L(Resource
                                                  Tags,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/resourcetags.htm).
                                                - "Example: `{\\"Operations\\": {\\"CostCenter\\": \\"42\\"}}`"
                                            returned: on success
                                            type: dict
                                            sample: {'Operations': {'CostCenter': 'US'}}
                                        display_name:
                                            description:
                                                - A user-friendly name. Does not have to be unique, and it's changeable.
                                                  Avoid entering confidential information.
                                            returned: on success
                                            type: str
                                            sample: display_name_example
                                        freeform_tags:
                                            description:
                                                - Free-form tags for this resource. Each tag is a simple key-value pair with no
                                                  predefined name, type, or namespace. For more information, see L(Resource
                                                  Tags,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/resourcetags.htm).
                                                - "Example: `{\\"Department\\": \\"Finance\\"}`"
                                            returned: on success
                                            type: dict
                                            sample: {'Department': 'Finance'}
                                        hostname_label:
                                            description:
                                                - The hostname for the VNIC's primary private IP.
                                                  See the `hostnameLabel` attribute of L(CreateVnicDetails,https://docs.cloud.oracle.com/en-
                                                  us/iaas/api/#/en/iaas/latest/CreateVnicDetails/) for more information.
                                            returned: on success
                                            type: str
                                            sample: hostname_label_example
                                        nsg_ids:
                                            description:
                                                - A list of the OCIDs of the network security groups (NSGs) to add the VNIC to. For more
                                                  information about NSGs, see
                                                  L(NetworkSecurityGroup,https://docs.cloud.oracle.com/en-us/iaas/api/#/en/iaas/latest/NetworkSecurityGroup/).
                                            returned: on success
                                            type: list
                                            sample: []
                                        private_ip:
                                            description:
                                                - A private IP address of your choice to assign to the VNIC.
                                                  See the `privateIp` attribute of L(CreateVnicDetails,https://docs.cloud.oracle.com/en-
                                                  us/iaas/api/#/en/iaas/latest/CreateVnicDetails/) for more information.
                                            returned: on success
                                            type: str
                                            sample: private_ip_example
                                        skip_source_dest_check:
                                            description:
                                                - Whether the source/destination check is disabled on the VNIC.
                                                  See the `skipSourceDestCheck` attribute of L(CreateVnicDetails,https://docs.cloud.oracle.com/en-
                                                  us/iaas/api/#/en/iaas/latest/CreateVnicDetails/) for more information.
                                            returned: on success
                                            type: bool
                                            sample: true
                                        subnet_id:
                                            description:
                                                - The OCID of the subnet to create the VNIC in.
                                                  See the `subnetId` attribute of L(CreateVnicDetails,https://docs.cloud.oracle.com/en-
                                                  us/iaas/api/#/en/iaas/latest/CreateVnicDetails/) for more information.
                                            returned: on success
                                            type: str
                                            sample: "ocid1.subnet.oc1..xxxxxxEXAMPLExxxxxx"
                                defined_tags:
                                    description:
                                        - Defined tags for this resource. Each key is predefined and scoped to a
                                          namespace. For more information, see L(Resource
                                          Tags,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/resourcetags.htm).
                                        - "Example: `{\\"Operations\\": {\\"CostCenter\\": \\"42\\"}}`"
                                    returned: on success
                                    type: dict
                                    sample: {'Operations': {'CostCenter': 'US'}}
                                display_name:
                                    description:
                                        - A user-friendly name. Does not have to be unique, and it's changeable.
                                          Avoid entering confidential information.
                                    returned: on success
                                    type: str
                                    sample: display_name_example
                                extended_metadata:
                                    description:
                                        - Additional metadata key/value pairs that you provide. They serve the same purpose and
                                          functionality as fields in the `metadata` object.
                                        - They are distinguished from `metadata` fields in that these can be nested JSON objects
                                          (whereas `metadata` fields are string/string maps only).
                                        - The combined size of the `metadata` and `extendedMetadata` objects can be a maximum of
                                          32,000 bytes.
                                    returned: on success
                                    type: dict
                                    sample: {}
                                freeform_tags:
                                    description:
                                        - Free-form tags for this resource. Each tag is a simple key-value pair with no
                                          predefined name, type, or namespace. For more information, see L(Resource
                                          Tags,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/resourcetags.htm).
                                        - "Example: `{\\"Department\\": \\"Finance\\"}`"
                                    returned: on success
                                    type: dict
                                    sample: {'Department': 'Finance'}
                                ipxe_script:
                                    description:
                                        - This is an advanced option.
                                        - When a bare metal or virtual machine
                                          instance boots, the iPXE firmware that runs on the instance is
                                          configured to run an iPXE script to continue the boot process.
                                        - If you want more control over the boot process, you can provide
                                          your own custom iPXE script that will run when the instance boots;
                                          however, you should be aware that the same iPXE script will run
                                          every time an instance boots; not only after the initial
                                          LaunchInstance call.
                                        - "The default iPXE script connects to the instance's local boot
                                          volume over iSCSI and performs a network boot. If you use a custom iPXE
                                          script and want to network-boot from the instance's local boot volume
                                          over iSCSI the same way as the default iPXE script, you should use the
                                          following iSCSI IP address: 169.254.0.2, and boot volume IQN:
                                          iqn.2015-02.oracle.boot."
                                        - For more information about the Bring Your Own Image feature of
                                          Oracle Cloud Infrastructure, see
                                          L(Bring Your Own Image,https://docs.cloud.oracle.com/iaas/Content/Compute/References/bringyourownimage.htm).
                                        - For more information about iPXE, see http://ipxe.org.
                                    returned: on success
                                    type: str
                                    sample: ipxe_script_example
                                metadata:
                                    description:
                                        - Custom metadata key/value pairs that you provide, such as the SSH public key
                                          required to connect to the instance.
                                        - "A metadata service runs on every launched instance. The service is an HTTP
                                          endpoint listening on 169.254.169.254. You can use the service to:"
                                        - "* Provide information to L(Cloud-Init,https://cloudinit.readthedocs.org/en/latest/)
                                            to be used for various system initialization tasks."
                                        - "* Get information about the instance, including the custom metadata that you
                                            provide when you launch the instance."
                                        - "**Providing Cloud-Init Metadata**"
                                        - "You can use the following metadata key names to provide information to
                                           Cloud-Init:"
                                        - "**\\"ssh_authorized_keys\\"** - Provide one or more public SSH keys to be
                                           included in the `~/.ssh/authorized_keys` file for the default user on the
                                           instance. Use a newline character to separate multiple keys. The SSH
                                           keys must be in the format necessary for the `authorized_keys` file, as shown
                                           in the example below."
                                        - "**\\"user_data\\"** - Provide your own base64-encoded data to be used by
                                           Cloud-Init to run custom scripts or provide custom Cloud-Init configuration. For
                                           information about how to take advantage of user data, see the
                                           L(Cloud-Init Documentation,http://cloudinit.readthedocs.org/en/latest/topics/format.html)."
                                        - "**Metadata Example**"
                                        - "     \\"metadata\\" : {
                                                   \\"quake_bot_level\\" : \\"Severe\\",
                                                   \\"ssh_authorized_keys\\" : \\"ssh-rsa <your_public_SSH_key>== rsa-key-20160227\\",
                                                   \\"user_data\\" : \\"<your_public_SSH_key>==\\"
                                                }
                                           **Getting Metadata on the Instance**"
                                        - "To get information about your instance, connect to the instance using SSH and issue any of the
                                           following GET requests:"
                                        - "    curl -H \\"Authorization: Bearer Oracle\\" http://169.254.169.254/opc/v2/instance/
                                               curl -H \\"Authorization: Bearer Oracle\\" http://169.254.169.254/opc/v2/instance/metadata/
                                               curl -H \\"Authorization: Bearer Oracle\\" http://169.254.169.254/opc/v2/instance/metadata/<any-key-name>"
                                        -  You'll get back a response that includes all the instance information; only the metadata information; or
                                           the metadata information for the specified key name, respectively.
                                        -  The combined size of the `metadata` and `extendedMetadata` objects can be a maximum of 32,000 bytes.
                                    returned: on success
                                    type: dict
                                    sample: {}
                                shape:
                                    description:
                                        - The shape of an instance. The shape determines the number of CPUs, amount of memory,
                                          and other resources allocated to the instance.
                                        - You can enumerate all available shapes by calling L(ListShapes,https://docs.cloud.oracle.com/en-
                                          us/iaas/api/#/en/iaas/latest/Shape/ListShapes).
                                    returned: on success
                                    type: str
                                    sample: shape_example
                                shape_config:
                                    description:
                                        - ""
                                    returned: on success
                                    type: complex
                                    contains:
                                        ocpus:
                                            description:
                                                - The total number of OCPUs available to the instance.
                                            returned: on success
                                            type: float
                                            sample: 3.4
                                        vcpus:
                                            description:
                                                - The total number of VCPUs available to the instance. This can be used instead of OCPUs,
                                                  in which case the actual number of OCPUs will be calculated based on this value
                                                  and the actual hardware. This must be a multiple of 2.
                                            returned: on success
                                            type: int
                                            sample: 56
                                        memory_in_gbs:
                                            description:
                                                - The total amount of memory available to the instance, in gigabytes.
                                            returned: on success
                                            type: float
                                            sample: 3.4
                                        baseline_ocpu_utilization:
                                            description:
                                                - The baseline OCPU utilization for a subcore burstable VM instance. Leave this attribute blank for a
                                                  non-burstable instance, or explicitly specify non-burstable with `BASELINE_1_1`.
                                                - "The following values are supported:
                                                  - `BASELINE_1_8` - baseline usage is 1/8 of an OCPU.
                                                  - `BASELINE_1_2` - baseline usage is 1/2 of an OCPU.
                                                  - `BASELINE_1_1` - baseline usage is an entire OCPU. This represents a non-burstable instance."
                                            returned: on success
                                            type: str
                                            sample: BASELINE_1_8
                                        nvmes:
                                            description:
                                                - The number of NVMe drives to be used for storage. A single drive has 6.8 TB available.
                                            returned: on success
                                            type: int
                                            sample: 56
                                platform_config:
                                    description:
                                        - ""
                                    returned: on success
                                    type: complex
                                    contains:
                                        is_access_control_service_enabled:
                                            description:
                                                - Whether the Access Control Service is enabled on the instance. When enabled,
                                                  the platform can enforce PCIe device isolation, required for VFIO device pass-through.
                                            returned: on success
                                            type: bool
                                            sample: true
                                        are_virtual_instructions_enabled:
                                            description:
                                                - Whether virtualization instructions are available. For example, Secure Virtual Machine for AMD shapes
                                                  or VT-x for Intel shapes.
                                            returned: on success
                                            type: bool
                                            sample: true
                                        numa_nodes_per_socket:
                                            description:
                                                - The number of NUMA nodes per socket (NPS).
                                            returned: on success
                                            type: str
                                            sample: NPS0
                                        is_symmetric_multi_threading_enabled:
                                            description:
                                                - Whether symmetric multithreading is enabled on the instance. Symmetric multithreading is also
                                                  called simultaneous multithreading (SMT) or Intel Hyper-Threading.
                                                - Intel and AMD processors have two hardware execution threads per core (OCPU). SMT permits multiple
                                                  independent threads of execution, to better use the resources and increase the efficiency
                                                  of the CPU. When multithreading is disabled, only one thread is permitted to run on each core, which
                                                  can provide higher or more predictable performance for some workloads.
                                            returned: on success
                                            type: bool
                                            sample: true
                                        is_input_output_memory_management_unit_enabled:
                                            description:
                                                - Whether the input-output memory management unit is enabled.
                                            returned: on success
                                            type: bool
                                            sample: true
                                        percentage_of_cores_enabled:
                                            description:
                                                - The percentage of cores enabled. Value must be a multiple of 25%. If the requested percentage
                                                  results in a fractional number of cores, the system rounds up the number of cores across processors
                                                  and provisions an instance with a whole number of cores.
                                                - If the applications that you run on the instance use a core-based licensing model and need fewer cores
                                                  than the full size of the shape, you can disable cores to reduce your licensing costs. The instance
                                                  itself is billed for the full shape, regardless of whether all cores are enabled.
                                            returned: on success
                                            type: int
                                            sample: 56
                                        type:
                                            description:
                                                - The type of platform being configured.
                                            returned: on success
                                            type: str
                                            sample: AMD_MILAN_BM
                                        is_secure_boot_enabled:
                                            description:
                                                - Whether Secure Boot is enabled on the instance.
                                            returned: on success
                                            type: bool
                                            sample: true
                                        is_trusted_platform_module_enabled:
                                            description:
                                                - Whether the Trusted Platform Module (TPM) is enabled on the instance.
                                            returned: on success
                                            type: bool
                                            sample: true
                                        is_measured_boot_enabled:
                                            description:
                                                - Whether the Measured Boot feature is enabled on the instance.
                                            returned: on success
                                            type: bool
                                            sample: true
                                        is_memory_encryption_enabled:
                                            description:
                                                - Whether the instance is a confidential instance. If this value is `true`, the instance is a confidential
                                                  instance. The default value is `false`.
                                            returned: on success
                                            type: bool
                                            sample: true
                                source_details:
                                    description:
                                        - ""
                                    returned: on success
                                    type: complex
                                    contains:
                                        boot_volume_id:
                                            description:
                                                - The OCID of the boot volume used to boot the instance.
                                            returned: on success
                                            type: str
                                            sample: "ocid1.bootvolume.oc1..xxxxxxEXAMPLExxxxxx"
                                        source_type:
                                            description:
                                                - The source type for the instance.
                                                  Use `image` when specifying the image OCID. Use `bootVolume` when specifying
                                                  the boot volume OCID.
                                            returned: on success
                                            type: str
                                            sample: bootVolume
                                        boot_volume_size_in_gbs:
                                            description:
                                                - The size of the boot volume in GBs. The minimum value is 50 GB and the maximum
                                                  value is 32,768 GB (32 TB).
                                            returned: on success
                                            type: int
                                            sample: 56
                                        image_id:
                                            description:
                                                - The OCID of the image used to boot the instance.
                                            returned: on success
                                            type: str
                                            sample: "ocid1.image.oc1..xxxxxxEXAMPLExxxxxx"
                                        kms_key_id:
                                            description:
                                                - The OCID of the Vault service key to assign as the master encryption key for the boot volume.
                                            returned: on success
                                            type: str
                                            sample: "ocid1.kmskey.oc1..xxxxxxEXAMPLExxxxxx"
                                        boot_volume_vpus_per_gb:
                                            description:
                                                - The number of volume performance units (VPUs) that will be applied to this volume per GB,
                                                  representing the Block Volume service's elastic performance options.
                                                  See L(Block Volume Performance
                                                  Levels,https://docs.cloud.oracle.com/iaas/Content/Block/Concepts/blockvolumeperformance.htm#perf_levels) for
                                                  more information.
                                                - "Allowed values:"
                                                - " * `10`: Represents Balanced option."
                                                - " * `20`: Represents Higher Performance option."
                                                - " * `30`-`120`: Represents the Ultra High Performance option."
                                                - For performance autotune enabled volumes, it would be the Default(Minimum) VPUs/GB.
                                            returned: on success
                                            type: int
                                            sample: 56
                                        instance_source_image_filter_details:
                                            description:
                                                - ""
                                            returned: on success
                                            type: complex
                                            contains:
                                                compartment_id:
                                                    description:
                                                        - The OCID of the compartment containing images to search
                                                    returned: on success
                                                    type: str
                                                    sample: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
                                                defined_tags_filter:
                                                    description:
                                                        - Filter based on these defined tags. Each key is predefined and scoped to a
                                                          namespace. For more information, see L(Resource
                                                          Tags,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/resourcetags.htm).
                                                    returned: on success
                                                    type: dict
                                                    sample: {}
                                                operating_system:
                                                    description:
                                                        - The image's operating system.
                                                        - "Example: `Oracle Linux`"
                                                    returned: on success
                                                    type: str
                                                    sample: operating_system_example
                                                operating_system_version:
                                                    description:
                                                        - The image's operating system version.
                                                        - "Example: `7.2`"
                                                    returned: on success
                                                    type: str
                                                    sample: operating_system_version_example
                                fault_domain:
                                    description:
                                        - A fault domain is a grouping of hardware and infrastructure within an availability domain.
                                          Each availability domain contains three fault domains. Fault domains let you distribute your
                                          instances so that they are not on the same physical hardware within a single availability domain.
                                          A hardware failure or Compute hardware maintenance that affects one fault domain does not affect
                                          instances in other fault domains.
                                        - If you do not specify the fault domain, the system selects one for you.
                                        - To get a list of fault domains, use the
                                          L(ListFaultDomains,https://docs.cloud.oracle.com/en-us/iaas/api/#/en/identity/20160918/FaultDomain/ListFaultDomains)
                                          operation in the
                                          Identity and Access Management Service API.
                                        - "Example: `FAULT-DOMAIN-1`"
                                    returned: on success
                                    type: str
                                    sample: FAULT-DOMAIN-1
                                dedicated_vm_host_id:
                                    description:
                                        - The OCID of the dedicated virtual machine host to place the instance on.
                                        - Dedicated VM hosts can be used when launching individual instances from an instance configuration. They
                                          cannot be used to launch instance pools.
                                    returned: on success
                                    type: str
                                    sample: "ocid1.dedicatedvmhost.oc1..xxxxxxEXAMPLExxxxxx"
                                launch_mode:
                                    description:
                                        - "Specifies the configuration mode for launching virtual machine (VM) instances. The configuration modes are:
                                          * `NATIVE` - VM instances launch with iSCSI boot and VFIO devices. The default value for platform images.
                                          * `EMULATED` - VM instances launch with emulated devices, such as the E1000 network driver and emulated SCSI disk
                                          controller.
                                          * `PARAVIRTUALIZED` - VM instances launch with paravirtualized devices using VirtIO drivers.
                                          * `CUSTOM` - VM instances launch with custom configuration settings specified in the `LaunchOptions` parameter."
                                    returned: on success
                                    type: str
                                    sample: NATIVE
                                launch_options:
                                    description:
                                        - ""
                                    returned: on success
                                    type: complex
                                    contains:
                                        boot_volume_type:
                                            description:
                                                - "Emulation type for the boot volume.
                                                  * `ISCSI` - ISCSI attached block storage device.
                                                  * `SCSI` - Emulated SCSI disk.
                                                  * `IDE` - Emulated IDE disk.
                                                  * `VFIO` - Direct attached Virtual Function storage. This is the default option for local data
                                                  volumes on platform images.
                                                  * `PARAVIRTUALIZED` - Paravirtualized disk. This is the default for boot volumes and remote block
                                                  storage volumes on platform images."
                                            returned: on success
                                            type: str
                                            sample: ISCSI
                                        firmware:
                                            description:
                                                - "Firmware used to boot VM. Select the option that matches your operating system.
                                                  * `BIOS` - Boot VM using BIOS style firmware. This is compatible with both 32 bit and 64 bit operating
                                                  systems that boot using MBR style bootloaders.
                                                  * `UEFI_64` - Boot VM using UEFI style firmware compatible with 64 bit operating systems. This is the
                                                  default for platform images."
                                            returned: on success
                                            type: str
                                            sample: BIOS
                                        network_type:
                                            description:
                                                - "Emulation type for the physical network interface card (NIC).
                                                  * `E1000` - Emulated Gigabit ethernet controller. Compatible with Linux e1000 network driver.
                                                  * `VFIO` - Direct attached Virtual Function network controller. This is the networking type
                                                  when you launch an instance using hardware-assisted (SR-IOV) networking.
                                                  * `PARAVIRTUALIZED` - VM instances launch with paravirtualized devices using VirtIO drivers."
                                            returned: on success
                                            type: str
                                            sample: E1000
                                        remote_data_volume_type:
                                            description:
                                                - "Emulation type for volume.
                                                  * `ISCSI` - ISCSI attached block storage device.
                                                  * `SCSI` - Emulated SCSI disk.
                                                  * `IDE` - Emulated IDE disk.
                                                  * `VFIO` - Direct attached Virtual Function storage. This is the default option for local data
                                                  volumes on platform images.
                                                  * `PARAVIRTUALIZED` - Paravirtualized disk. This is the default for boot volumes and remote block
                                                  storage volumes on platform images."
                                            returned: on success
                                            type: str
                                            sample: ISCSI
                                        is_pv_encryption_in_transit_enabled:
                                            description:
                                                - Deprecated. Instead use `isPvEncryptionInTransitEnabled` in
                                                  L(InstanceConfigurationLaunchInstanceDetails,https://docs.cloud.oracle.com/en-
                                                  us/iaas/api/#/en/iaas/latest/datatypes/InstanceConfigurationLaunchInstanceDetails).
                                            returned: on success
                                            type: bool
                                            sample: true
                                        is_consistent_volume_naming_enabled:
                                            description:
                                                - Whether to enable consistent volume naming feature. Defaults to false.
                                            returned: on success
                                            type: bool
                                            sample: true
                                agent_config:
                                    description:
                                        - ""
                                    returned: on success
                                    type: complex
                                    contains:
                                        is_monitoring_disabled:
                                            description:
                                                - Whether Oracle Cloud Agent can gather performance metrics and monitor the instance using the
                                                  monitoring plugins. Default value is false (monitoring plugins are enabled).
                                                - "These are the monitoring plugins: Compute Instance Monitoring
                                                  and Custom Logs Monitoring."
                                                - The monitoring plugins are controlled by this parameter and by the per-plugin
                                                  configuration in the `pluginsConfig` object.
                                                - "- If `isMonitoringDisabled` is true, all of the monitoring plugins are disabled, regardless of
                                                  the per-plugin configuration.
                                                  - If `isMonitoringDisabled` is false, all of the monitoring plugins are enabled. You
                                                  can optionally disable individual monitoring plugins by providing a value in the `pluginsConfig`
                                                  object."
                                            returned: on success
                                            type: bool
                                            sample: true
                                        is_management_disabled:
                                            description:
                                                - Whether Oracle Cloud Agent can run all the available management plugins.
                                                  Default value is false (management plugins are enabled).
                                                - "These are the management plugins: OS Management Service Agent and Compute Instance
                                                  Run Command."
                                                - The management plugins are controlled by this parameter and by the per-plugin
                                                  configuration in the `pluginsConfig` object.
                                                - "- If `isManagementDisabled` is true, all of the management plugins are disabled, regardless of
                                                  the per-plugin configuration.
                                                  - If `isManagementDisabled` is false, all of the management plugins are enabled. You
                                                  can optionally disable individual management plugins by providing a value in the `pluginsConfig`
                                                  object."
                                            returned: on success
                                            type: bool
                                            sample: true
                                        are_all_plugins_disabled:
                                            description:
                                                - Whether Oracle Cloud Agent can run all the available plugins.
                                                  This includes the management and monitoring plugins.
                                                - To get a list of available plugins, use the
                                                  L(ListInstanceagentAvailablePlugins,https://docs.cloud.oracle.com/en-
                                                  us/iaas/api/#/en/instanceagent/20180530/Plugin/ListInstanceagentAvailablePlugins)
                                                  operation in the Oracle Cloud Agent API. For more information about the available plugins, see
                                                  L(Managing Plugins with Oracle Cloud Agent,https://docs.cloud.oracle.com/iaas/Content/Compute/Tasks/manage-
                                                  plugins.htm).
                                            returned: on success
                                            type: bool
                                            sample: true
                                        plugins_config:
                                            description:
                                                - The configuration of plugins associated with this instance.
                                            returned: on success
                                            type: complex
                                            contains:
                                                name:
                                                    description:
                                                        - The plugin name. To get a list of available plugins, use the
                                                          L(ListInstanceagentAvailablePlugins,https://docs.cloud.oracle.com/en-
                                                          us/iaas/api/#/en/instanceagent/20180530/Plugin/ListInstanceagentAvailablePlugins)
                                                          operation in the Oracle Cloud Agent API. For more information about the available plugins, see
                                                          L(Managing Plugins with Oracle Cloud
                                                          Agent,https://docs.cloud.oracle.com/iaas/Content/Compute/Tasks/manage-plugins.htm).
                                                    returned: on success
                                                    type: str
                                                    sample: name_example
                                                desired_state:
                                                    description:
                                                        - Whether the plugin should be enabled or disabled.
                                                        - To enable the monitoring and management plugins, the `isMonitoringDisabled` and
                                                          `isManagementDisabled` attributes must also be set to false.
                                                    returned: on success
                                                    type: str
                                                    sample: ENABLED
                                is_pv_encryption_in_transit_enabled:
                                    description:
                                        - Whether to enable in-transit encryption for the data volume's paravirtualized attachment. The default value is false.
                                    returned: on success
                                    type: bool
                                    sample: true
                                preferred_maintenance_action:
                                    description:
                                        - "The preferred maintenance action for an instance. The default is LIVE_MIGRATE, if live migration is supported.
                                          * `LIVE_MIGRATE` - Run maintenance using a live migration.
                                          * `REBOOT` - Run maintenance using a reboot."
                                    returned: on success
                                    type: str
                                    sample: LIVE_MIGRATE
                                instance_options:
                                    description:
                                        - ""
                                    returned: on success
                                    type: complex
                                    contains:
                                        are_legacy_imds_endpoints_disabled:
                                            description:
                                                - Whether to disable the legacy (/v1) instance metadata service endpoints.
                                                  Customers who have migrated to /v2 should set this to true for added security.
                                                  Default is false.
                                            returned: on success
                                            type: bool
                                            sample: true
                                availability_config:
                                    description:
                                        - ""
                                    returned: on success
                                    type: complex
                                    contains:
                                        is_live_migration_preferred:
                                            description:
                                                - Whether to live migrate supported VM instances to a healthy physical VM host without
                                                  disrupting running instances during infrastructure maintenance events. If null, Oracle
                                                  chooses the best option for migrating the VM during infrastructure maintenance events.
                                            returned: on success
                                            type: bool
                                            sample: true
                                        recovery_action:
                                            description:
                                                - "The lifecycle state for an instance when it is recovered after infrastructure maintenance.
                                                  * `RESTORE_INSTANCE` - The instance is restored to the lifecycle state it was in before the maintenance event.
                                                  If the instance was running, it is automatically rebooted. This is the default action when a value is not set.
                                                  * `STOP_INSTANCE` - The instance is recovered in the stopped state."
                                            returned: on success
                                            type: str
                                            sample: RESTORE_INSTANCE
                                preemptible_instance_config:
                                    description:
                                        - ""
                                    returned: on success
                                    type: complex
                                    contains:
                                        preemption_action:
                                            description:
                                                - ""
                                            returned: on success
                                            type: complex
                                            contains:
                                                type:
                                                    description:
                                                        - The type of action to run when the instance is interrupted for eviction.
                                                    returned: on success
                                                    type: str
                                                    sample: TERMINATE
                                                preserve_boot_volume:
                                                    description:
                                                        - Whether to preserve the boot volume that was used to launch the preemptible instance when the instance
                                                          is terminated. Defaults to false if not specified.
                                                    returned: on success
                                                    type: bool
                                                    sample: true
                        secondary_vnics:
                            description:
                                - Secondary VNIC parameters.
                            returned: on success
                            type: complex
                            contains:
                                create_vnic_details:
                                    description:
                                        - ""
                                    returned: on success
                                    type: complex
                                    contains:
                                        assign_public_ip:
                                            description:
                                                - Whether the VNIC should be assigned a public IP address. See the `assignPublicIp` attribute of
                                                  L(CreateVnicDetails,https://docs.cloud.oracle.com/en-us/iaas/api/#/en/iaas/latest/CreateVnicDetails/)
                                                  for more information.
                                            returned: on success
                                            type: bool
                                            sample: true
                                        assign_private_dns_record:
                                            description:
                                                - Whether the VNIC should be assigned a private DNS record. See the `assignPrivateDnsRecord` attribute of
                                                  L(CreateVnicDetails,https://docs.cloud.oracle.com/en-us/iaas/api/#/en/iaas/latest/CreateVnicDetails/)
                                                  for more information.
                                            returned: on success
                                            type: bool
                                            sample: true
                                        defined_tags:
                                            description:
                                                - Defined tags for this resource. Each key is predefined and scoped to a
                                                  namespace. For more information, see L(Resource
                                                  Tags,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/resourcetags.htm).
                                                - "Example: `{\\"Operations\\": {\\"CostCenter\\": \\"42\\"}}`"
                                            returned: on success
                                            type: dict
                                            sample: {'Operations': {'CostCenter': 'US'}}
                                        display_name:
                                            description:
                                                - A user-friendly name. Does not have to be unique, and it's changeable.
                                                  Avoid entering confidential information.
                                            returned: on success
                                            type: str
                                            sample: display_name_example
                                        freeform_tags:
                                            description:
                                                - Free-form tags for this resource. Each tag is a simple key-value pair with no
                                                  predefined name, type, or namespace. For more information, see L(Resource
                                                  Tags,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/resourcetags.htm).
                                                - "Example: `{\\"Department\\": \\"Finance\\"}`"
                                            returned: on success
                                            type: dict
                                            sample: {'Department': 'Finance'}
                                        hostname_label:
                                            description:
                                                - The hostname for the VNIC's primary private IP.
                                                  See the `hostnameLabel` attribute of L(CreateVnicDetails,https://docs.cloud.oracle.com/en-
                                                  us/iaas/api/#/en/iaas/latest/CreateVnicDetails/) for more information.
                                            returned: on success
                                            type: str
                                            sample: hostname_label_example
                                        nsg_ids:
                                            description:
                                                - A list of the OCIDs of the network security groups (NSGs) to add the VNIC to. For more
                                                  information about NSGs, see
                                                  L(NetworkSecurityGroup,https://docs.cloud.oracle.com/en-us/iaas/api/#/en/iaas/latest/NetworkSecurityGroup/).
                                            returned: on success
                                            type: list
                                            sample: []
                                        private_ip:
                                            description:
                                                - A private IP address of your choice to assign to the VNIC.
                                                  See the `privateIp` attribute of L(CreateVnicDetails,https://docs.cloud.oracle.com/en-
                                                  us/iaas/api/#/en/iaas/latest/CreateVnicDetails/) for more information.
                                            returned: on success
                                            type: str
                                            sample: private_ip_example
                                        skip_source_dest_check:
                                            description:
                                                - Whether the source/destination check is disabled on the VNIC.
                                                  See the `skipSourceDestCheck` attribute of L(CreateVnicDetails,https://docs.cloud.oracle.com/en-
                                                  us/iaas/api/#/en/iaas/latest/CreateVnicDetails/) for more information.
                                            returned: on success
                                            type: bool
                                            sample: true
                                        subnet_id:
                                            description:
                                                - The OCID of the subnet to create the VNIC in.
                                                  See the `subnetId` attribute of L(CreateVnicDetails,https://docs.cloud.oracle.com/en-
                                                  us/iaas/api/#/en/iaas/latest/CreateVnicDetails/) for more information.
                                            returned: on success
                                            type: str
                                            sample: "ocid1.subnet.oc1..xxxxxxEXAMPLExxxxxx"
                                display_name:
                                    description:
                                        - A user-friendly name. Does not have to be unique, and it's changeable.
                                          Avoid entering confidential information.
                                    returned: on success
                                    type: str
                                    sample: display_name_example
                                nic_index:
                                    description:
                                        - Which physical network interface card (NIC) the VNIC will use. Defaults to 0.
                                          Certain bare metal instance shapes have two active physical NICs (0 and 1). If
                                          you add a secondary VNIC to one of these instances, you can specify which NIC
                                          the VNIC will use. For more information, see
                                          L(Virtual Network Interface Cards (VNICs),https://docs.cloud.oracle.com/iaas/Content/Network/Tasks/managingVNICs.htm).
                                    returned: on success
                                    type: int
                                    sample: 56
        deferred_fields:
            description:
                - Parameters that were not specified when the instance configuration was created, but that
                  are required to launch an instance from the instance configuration. See the
                  L(LaunchInstanceConfiguration,https://docs.cloud.oracle.com/en-us/iaas/api/#/en/iaas/latest/Instance/LaunchInstanceConfiguration) operation.
            returned: on success
            type: list
            sample: []
        time_created:
            description:
                - The date and time the instance configuration was created, in the format defined by L(RFC3339,https://tools.ietf.org/html/rfc3339).
                - "Example: `2016-08-25T21:10:29.600Z`"
            returned: on success
            type: str
            sample: "2013-10-20T19:20:30+01:00"
    sample: {
        "compartment_id": "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx",
        "defined_tags": {'Operations': {'CostCenter': 'US'}},
        "display_name": "display_name_example",
        "freeform_tags": {'Department': 'Finance'},
        "id": "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx",
        "instance_details": {
            "block_volumes": [{
                "attach_details": {
                    "use_chap": true,
                    "display_name": "display_name_example",
                    "is_read_only": true,
                    "device": "device_example",
                    "is_shareable": true,
                    "type": "iscsi",
                    "is_pv_encryption_in_transit_enabled": true
                },
                "create_details": {
                    "availability_domain": "Uocm:PHX-AD-1",
                    "backup_policy_id": "ocid1.backuppolicy.oc1..xxxxxxEXAMPLExxxxxx",
                    "compartment_id": "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx",
                    "is_auto_tune_enabled": true,
                    "block_volume_replicas": [{
                        "display_name": "display_name_example",
                        "availability_domain": "Uocm:PHX-AD-1"
                    }],
                    "defined_tags": {'Operations': {'CostCenter': 'US'}},
                    "display_name": "display_name_example",
                    "freeform_tags": {'Department': 'Finance'},
                    "kms_key_id": "ocid1.kmskey.oc1..xxxxxxEXAMPLExxxxxx",
                    "vpus_per_gb": 56,
                    "size_in_gbs": 56,
                    "source_details": {
                        "type": "volume",
                        "id": "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx"
                    },
                    "autotune_policies": [{
                        "autotune_type": "DETACHED_VOLUME",
                        "max_vpus_per_gb": 56
                    }]
                },
                "volume_id": "ocid1.volume.oc1..xxxxxxEXAMPLExxxxxx"
            }],
            "launch_details": {
                "availability_domain": "Uocm:PHX-AD-1",
                "capacity_reservation_id": "ocid1.capacityreservation.oc1..xxxxxxEXAMPLExxxxxx",
                "compartment_id": "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx",
                "create_vnic_details": {
                    "assign_public_ip": true,
                    "assign_private_dns_record": true,
                    "defined_tags": {'Operations': {'CostCenter': 'US'}},
                    "display_name": "display_name_example",
                    "freeform_tags": {'Department': 'Finance'},
                    "hostname_label": "hostname_label_example",
                    "nsg_ids": [],
                    "private_ip": "private_ip_example",
                    "skip_source_dest_check": true,
                    "subnet_id": "ocid1.subnet.oc1..xxxxxxEXAMPLExxxxxx"
                },
                "defined_tags": {'Operations': {'CostCenter': 'US'}},
                "display_name": "display_name_example",
                "extended_metadata": {},
                "freeform_tags": {'Department': 'Finance'},
                "ipxe_script": "ipxe_script_example",
                "metadata": {},
                "shape": "shape_example",
                "shape_config": {
                    "ocpus": 3.4,
                    "vcpus": 56,
                    "memory_in_gbs": 3.4,
                    "baseline_ocpu_utilization": "BASELINE_1_8",
                    "nvmes": 56
                },
                "platform_config": {
                    "is_access_control_service_enabled": true,
                    "are_virtual_instructions_enabled": true,
                    "numa_nodes_per_socket": "NPS0",
                    "is_symmetric_multi_threading_enabled": true,
                    "is_input_output_memory_management_unit_enabled": true,
                    "percentage_of_cores_enabled": 56,
                    "type": "AMD_MILAN_BM",
                    "is_secure_boot_enabled": true,
                    "is_trusted_platform_module_enabled": true,
                    "is_measured_boot_enabled": true,
                    "is_memory_encryption_enabled": true
                },
                "source_details": {
                    "boot_volume_id": "ocid1.bootvolume.oc1..xxxxxxEXAMPLExxxxxx",
                    "source_type": "bootVolume",
                    "boot_volume_size_in_gbs": 56,
                    "image_id": "ocid1.image.oc1..xxxxxxEXAMPLExxxxxx",
                    "kms_key_id": "ocid1.kmskey.oc1..xxxxxxEXAMPLExxxxxx",
                    "boot_volume_vpus_per_gb": 56,
                    "instance_source_image_filter_details": {
                        "compartment_id": "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx",
                        "defined_tags_filter": {},
                        "operating_system": "operating_system_example",
                        "operating_system_version": "operating_system_version_example"
                    }
                },
                "fault_domain": "FAULT-DOMAIN-1",
                "dedicated_vm_host_id": "ocid1.dedicatedvmhost.oc1..xxxxxxEXAMPLExxxxxx",
                "launch_mode": "NATIVE",
                "launch_options": {
                    "boot_volume_type": "ISCSI",
                    "firmware": "BIOS",
                    "network_type": "E1000",
                    "remote_data_volume_type": "ISCSI",
                    "is_pv_encryption_in_transit_enabled": true,
                    "is_consistent_volume_naming_enabled": true
                },
                "agent_config": {
                    "is_monitoring_disabled": true,
                    "is_management_disabled": true,
                    "are_all_plugins_disabled": true,
                    "plugins_config": [{
                        "name": "name_example",
                        "desired_state": "ENABLED"
                    }]
                },
                "is_pv_encryption_in_transit_enabled": true,
                "preferred_maintenance_action": "LIVE_MIGRATE",
                "instance_options": {
                    "are_legacy_imds_endpoints_disabled": true
                },
                "availability_config": {
                    "is_live_migration_preferred": true,
                    "recovery_action": "RESTORE_INSTANCE"
                },
                "preemptible_instance_config": {
                    "preemption_action": {
                        "type": "TERMINATE",
                        "preserve_boot_volume": true
                    }
                }
            },
            "secondary_vnics": [{
                "create_vnic_details": {
                    "assign_public_ip": true,
                    "assign_private_dns_record": true,
                    "defined_tags": {'Operations': {'CostCenter': 'US'}},
                    "display_name": "display_name_example",
                    "freeform_tags": {'Department': 'Finance'},
                    "hostname_label": "hostname_label_example",
                    "nsg_ids": [],
                    "private_ip": "private_ip_example",
                    "skip_source_dest_check": true,
                    "subnet_id": "ocid1.subnet.oc1..xxxxxxEXAMPLExxxxxx"
                },
                "display_name": "display_name_example",
                "nic_index": 56
            }],
            "instance_type": "compute",
            "options": [{
                "instance_type": "instance_type_example",
                "block_volumes": [{
                    "attach_details": {
                        "use_chap": true,
                        "display_name": "display_name_example",
                        "is_read_only": true,
                        "device": "device_example",
                        "is_shareable": true,
                        "type": "iscsi",
                        "is_pv_encryption_in_transit_enabled": true
                    },
                    "create_details": {
                        "availability_domain": "Uocm:PHX-AD-1",
                        "backup_policy_id": "ocid1.backuppolicy.oc1..xxxxxxEXAMPLExxxxxx",
                        "compartment_id": "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx",
                        "is_auto_tune_enabled": true,
                        "block_volume_replicas": [{
                            "display_name": "display_name_example",
                            "availability_domain": "Uocm:PHX-AD-1"
                        }],
                        "defined_tags": {'Operations': {'CostCenter': 'US'}},
                        "display_name": "display_name_example",
                        "freeform_tags": {'Department': 'Finance'},
                        "kms_key_id": "ocid1.kmskey.oc1..xxxxxxEXAMPLExxxxxx",
                        "vpus_per_gb": 56,
                        "size_in_gbs": 56,
                        "source_details": {
                            "type": "volume",
                            "id": "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx"
                        },
                        "autotune_policies": [{
                            "autotune_type": "DETACHED_VOLUME",
                            "max_vpus_per_gb": 56
                        }]
                    },
                    "volume_id": "ocid1.volume.oc1..xxxxxxEXAMPLExxxxxx"
                }],
                "launch_details": {
                    "availability_domain": "Uocm:PHX-AD-1",
                    "capacity_reservation_id": "ocid1.capacityreservation.oc1..xxxxxxEXAMPLExxxxxx",
                    "compartment_id": "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx",
                    "create_vnic_details": {
                        "assign_public_ip": true,
                        "assign_private_dns_record": true,
                        "defined_tags": {'Operations': {'CostCenter': 'US'}},
                        "display_name": "display_name_example",
                        "freeform_tags": {'Department': 'Finance'},
                        "hostname_label": "hostname_label_example",
                        "nsg_ids": [],
                        "private_ip": "private_ip_example",
                        "skip_source_dest_check": true,
                        "subnet_id": "ocid1.subnet.oc1..xxxxxxEXAMPLExxxxxx"
                    },
                    "defined_tags": {'Operations': {'CostCenter': 'US'}},
                    "display_name": "display_name_example",
                    "extended_metadata": {},
                    "freeform_tags": {'Department': 'Finance'},
                    "ipxe_script": "ipxe_script_example",
                    "metadata": {},
                    "shape": "shape_example",
                    "shape_config": {
                        "ocpus": 3.4,
                        "vcpus": 56,
                        "memory_in_gbs": 3.4,
                        "baseline_ocpu_utilization": "BASELINE_1_8",
                        "nvmes": 56
                    },
                    "platform_config": {
                        "is_access_control_service_enabled": true,
                        "are_virtual_instructions_enabled": true,
                        "numa_nodes_per_socket": "NPS0",
                        "is_symmetric_multi_threading_enabled": true,
                        "is_input_output_memory_management_unit_enabled": true,
                        "percentage_of_cores_enabled": 56,
                        "type": "AMD_MILAN_BM",
                        "is_secure_boot_enabled": true,
                        "is_trusted_platform_module_enabled": true,
                        "is_measured_boot_enabled": true,
                        "is_memory_encryption_enabled": true
                    },
                    "source_details": {
                        "boot_volume_id": "ocid1.bootvolume.oc1..xxxxxxEXAMPLExxxxxx",
                        "source_type": "bootVolume",
                        "boot_volume_size_in_gbs": 56,
                        "image_id": "ocid1.image.oc1..xxxxxxEXAMPLExxxxxx",
                        "kms_key_id": "ocid1.kmskey.oc1..xxxxxxEXAMPLExxxxxx",
                        "boot_volume_vpus_per_gb": 56,
                        "instance_source_image_filter_details": {
                            "compartment_id": "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx",
                            "defined_tags_filter": {},
                            "operating_system": "operating_system_example",
                            "operating_system_version": "operating_system_version_example"
                        }
                    },
                    "fault_domain": "FAULT-DOMAIN-1",
                    "dedicated_vm_host_id": "ocid1.dedicatedvmhost.oc1..xxxxxxEXAMPLExxxxxx",
                    "launch_mode": "NATIVE",
                    "launch_options": {
                        "boot_volume_type": "ISCSI",
                        "firmware": "BIOS",
                        "network_type": "E1000",
                        "remote_data_volume_type": "ISCSI",
                        "is_pv_encryption_in_transit_enabled": true,
                        "is_consistent_volume_naming_enabled": true
                    },
                    "agent_config": {
                        "is_monitoring_disabled": true,
                        "is_management_disabled": true,
                        "are_all_plugins_disabled": true,
                        "plugins_config": [{
                            "name": "name_example",
                            "desired_state": "ENABLED"
                        }]
                    },
                    "is_pv_encryption_in_transit_enabled": true,
                    "preferred_maintenance_action": "LIVE_MIGRATE",
                    "instance_options": {
                        "are_legacy_imds_endpoints_disabled": true
                    },
                    "availability_config": {
                        "is_live_migration_preferred": true,
                        "recovery_action": "RESTORE_INSTANCE"
                    },
                    "preemptible_instance_config": {
                        "preemption_action": {
                            "type": "TERMINATE",
                            "preserve_boot_volume": true
                        }
                    }
                },
                "secondary_vnics": [{
                    "create_vnic_details": {
                        "assign_public_ip": true,
                        "assign_private_dns_record": true,
                        "defined_tags": {'Operations': {'CostCenter': 'US'}},
                        "display_name": "display_name_example",
                        "freeform_tags": {'Department': 'Finance'},
                        "hostname_label": "hostname_label_example",
                        "nsg_ids": [],
                        "private_ip": "private_ip_example",
                        "skip_source_dest_check": true,
                        "subnet_id": "ocid1.subnet.oc1..xxxxxxEXAMPLExxxxxx"
                    },
                    "display_name": "display_name_example",
                    "nic_index": 56
                }]
            }]
        },
        "deferred_fields": [],
        "time_created": "2013-10-20T19:20:30+01:00"
    }
"""

from ansible_collections.oracle.oci.plugins.module_utils import (
    oci_common_utils,
    oci_wait_utils,
    oci_config_utils,
)
from ansible_collections.oracle.oci.plugins.module_utils.oci_resource_utils import (
    OCIActionsHelperBase,
    OCIAnsibleModule,
    get_custom_class,
)

try:
    from oci.work_requests import WorkRequestClient
    from oci.core import ComputeManagementClient
    from oci.core.models import ChangeInstanceConfigurationCompartmentDetails
    from oci.core.models import InstanceConfigurationInstanceDetails

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


class InstanceConfigurationActionsHelperGen(OCIActionsHelperBase):
    """
    Supported actions:
        change_compartment
        launch
    """

    def __init__(self, *args, **kwargs):
        super(InstanceConfigurationActionsHelperGen, self).__init__(*args, **kwargs)
        self.work_request_client = oci_config_utils.create_service_client(
            self.module, WorkRequestClient
        )

    @staticmethod
    def get_module_resource_id_param():
        return "instance_configuration_id"

    def get_module_resource_id(self):
        return self.module.params.get("instance_configuration_id")

    def get_get_fn(self):
        return self.client.get_instance_configuration

    def get_resource(self):
        return oci_common_utils.call_with_backoff(
            self.client.get_instance_configuration,
            instance_configuration_id=self.module.params.get(
                "instance_configuration_id"
            ),
        )

    def get_response_field_name(self, action):
        response_fields = dict(
            launch="instance", change_compartment="instance_configuration",
        )
        return response_fields.get(action, "instance_configuration")

    def change_compartment(self):
        action_details = oci_common_utils.convert_input_data_to_model_class(
            self.module.params, ChangeInstanceConfigurationCompartmentDetails
        )
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.change_instance_configuration_compartment,
            call_fn_args=(),
            call_fn_kwargs=dict(
                instance_configuration_id=self.module.params.get(
                    "instance_configuration_id"
                ),
                change_instance_configuration_compartment_details=action_details,
            ),
            waiter_type=oci_wait_utils.NONE_WAITER_KEY,
            operation="{0}_{1}".format(
                self.module.params.get("action").upper(),
                oci_common_utils.ACTION_OPERATION_KEY,
            ),
            waiter_client=self.get_waiter_client(),
            resource_helper=self,
            wait_for_states=self.get_action_desired_states(
                self.module.params.get("action")
            ),
        )

    def launch(self):
        action_details = oci_common_utils.convert_input_data_to_model_class(
            self.module.params, InstanceConfigurationInstanceDetails
        )
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.launch_instance_configuration,
            call_fn_args=(),
            call_fn_kwargs=dict(
                instance_configuration_id=self.module.params.get(
                    "instance_configuration_id"
                ),
                instance_configuration=action_details,
            ),
            waiter_type=oci_wait_utils.WORK_REQUEST_WAITER_KEY,
            operation="{0}_{1}".format(
                self.module.params.get("action").upper(),
                oci_common_utils.ACTION_OPERATION_KEY,
            ),
            waiter_client=self.work_request_client,
            resource_helper=self,
            wait_for_states=oci_common_utils.get_work_request_completed_states(),
        )


InstanceConfigurationActionsHelperCustom = get_custom_class(
    "InstanceConfigurationActionsHelperCustom"
)


class ResourceHelper(
    InstanceConfigurationActionsHelperCustom, InstanceConfigurationActionsHelperGen
):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec(
        supports_create=False, supports_wait=False
    )
    module_args.update(
        dict(
            compartment_id=dict(type="str"),
            instance_configuration_id=dict(aliases=["id"], type="str", required=True),
            options=dict(
                type="list",
                elements="dict",
                options=dict(
                    instance_type=dict(type="str", required=True),
                    block_volumes=dict(
                        type="list",
                        elements="dict",
                        options=dict(
                            attach_details=dict(
                                type="dict",
                                options=dict(
                                    use_chap=dict(type="bool"),
                                    display_name=dict(aliases=["name"], type="str"),
                                    is_read_only=dict(type="bool"),
                                    device=dict(type="str"),
                                    is_shareable=dict(type="bool"),
                                    type=dict(
                                        type="str",
                                        required=True,
                                        choices=["iscsi", "paravirtualized"],
                                    ),
                                    is_pv_encryption_in_transit_enabled=dict(
                                        type="bool"
                                    ),
                                ),
                            ),
                            create_details=dict(
                                type="dict",
                                options=dict(
                                    availability_domain=dict(type="str"),
                                    backup_policy_id=dict(type="str"),
                                    compartment_id=dict(type="str"),
                                    is_auto_tune_enabled=dict(type="bool"),
                                    block_volume_replicas=dict(
                                        type="list",
                                        elements="dict",
                                        options=dict(
                                            display_name=dict(
                                                aliases=["name"], type="str"
                                            ),
                                            availability_domain=dict(
                                                type="str", required=True
                                            ),
                                        ),
                                    ),
                                    defined_tags=dict(type="dict"),
                                    display_name=dict(aliases=["name"], type="str"),
                                    freeform_tags=dict(type="dict"),
                                    kms_key_id=dict(type="str"),
                                    vpus_per_gb=dict(type="int"),
                                    size_in_gbs=dict(type="int"),
                                    source_details=dict(
                                        type="dict",
                                        options=dict(
                                            type=dict(
                                                type="str",
                                                required=True,
                                                choices=["volumeBackup", "volume"],
                                            ),
                                            id=dict(type="str"),
                                        ),
                                    ),
                                    autotune_policies=dict(
                                        type="list",
                                        elements="dict",
                                        options=dict(
                                            max_vpus_per_gb=dict(type="int"),
                                            autotune_type=dict(
                                                type="str",
                                                required=True,
                                                choices=[
                                                    "PERFORMANCE_BASED",
                                                    "DETACHED_VOLUME",
                                                ],
                                            ),
                                        ),
                                    ),
                                ),
                            ),
                            volume_id=dict(type="str"),
                        ),
                    ),
                    launch_details=dict(
                        type="dict",
                        options=dict(
                            availability_domain=dict(type="str"),
                            capacity_reservation_id=dict(type="str"),
                            compartment_id=dict(type="str"),
                            create_vnic_details=dict(
                                type="dict",
                                options=dict(
                                    assign_public_ip=dict(type="bool"),
                                    assign_private_dns_record=dict(type="bool"),
                                    defined_tags=dict(type="dict"),
                                    display_name=dict(aliases=["name"], type="str"),
                                    freeform_tags=dict(type="dict"),
                                    hostname_label=dict(type="str"),
                                    nsg_ids=dict(type="list", elements="str"),
                                    private_ip=dict(type="str"),
                                    skip_source_dest_check=dict(type="bool"),
                                    subnet_id=dict(type="str"),
                                ),
                            ),
                            defined_tags=dict(type="dict"),
                            display_name=dict(aliases=["name"], type="str"),
                            extended_metadata=dict(type="dict"),
                            freeform_tags=dict(type="dict"),
                            ipxe_script=dict(type="str"),
                            metadata=dict(type="dict"),
                            shape=dict(type="str"),
                            shape_config=dict(
                                type="dict",
                                options=dict(
                                    ocpus=dict(type="float"),
                                    vcpus=dict(type="int"),
                                    memory_in_gbs=dict(type="float"),
                                    baseline_ocpu_utilization=dict(
                                        type="str",
                                        choices=[
                                            "BASELINE_1_8",
                                            "BASELINE_1_2",
                                            "BASELINE_1_1",
                                        ],
                                    ),
                                    nvmes=dict(type="int"),
                                ),
                            ),
                            platform_config=dict(
                                type="dict",
                                options=dict(
                                    percentage_of_cores_enabled=dict(type="int"),
                                    numa_nodes_per_socket=dict(
                                        type="str",
                                        choices=["NPS0", "NPS1", "NPS2", "NPS4"],
                                    ),
                                    is_symmetric_multi_threading_enabled=dict(
                                        type="bool"
                                    ),
                                    is_access_control_service_enabled=dict(type="bool"),
                                    are_virtual_instructions_enabled=dict(type="bool"),
                                    is_input_output_memory_management_unit_enabled=dict(
                                        type="bool"
                                    ),
                                    type=dict(
                                        type="str",
                                        required=True,
                                        choices=[
                                            "AMD_MILAN_BM",
                                            "INTEL_VM",
                                            "AMD_MILAN_BM_GPU",
                                            "INTEL_ICELAKE_BM",
                                            "AMD_ROME_BM",
                                            "INTEL_SKYLAKE_BM",
                                            "AMD_ROME_BM_GPU",
                                            "AMD_VM",
                                        ],
                                    ),
                                    is_secure_boot_enabled=dict(type="bool"),
                                    is_trusted_platform_module_enabled=dict(
                                        type="bool"
                                    ),
                                    is_measured_boot_enabled=dict(type="bool"),
                                    is_memory_encryption_enabled=dict(type="bool"),
                                ),
                            ),
                            source_details=dict(
                                type="dict",
                                options=dict(
                                    boot_volume_size_in_gbs=dict(type="int"),
                                    image_id=dict(type="str"),
                                    kms_key_id=dict(type="str"),
                                    boot_volume_vpus_per_gb=dict(type="int"),
                                    instance_source_image_filter_details=dict(
                                        type="dict",
                                        options=dict(
                                            compartment_id=dict(type="str"),
                                            defined_tags_filter=dict(type="dict"),
                                            operating_system=dict(type="str"),
                                            operating_system_version=dict(type="str"),
                                        ),
                                    ),
                                    source_type=dict(
                                        type="str",
                                        required=True,
                                        choices=["image", "bootVolume"],
                                    ),
                                    boot_volume_id=dict(type="str"),
                                ),
                            ),
                            fault_domain=dict(type="str"),
                            dedicated_vm_host_id=dict(type="str"),
                            launch_mode=dict(
                                type="str",
                                choices=[
                                    "NATIVE",
                                    "EMULATED",
                                    "PARAVIRTUALIZED",
                                    "CUSTOM",
                                ],
                            ),
                            launch_options=dict(
                                type="dict",
                                options=dict(
                                    boot_volume_type=dict(
                                        type="str",
                                        choices=[
                                            "ISCSI",
                                            "SCSI",
                                            "IDE",
                                            "VFIO",
                                            "PARAVIRTUALIZED",
                                        ],
                                    ),
                                    firmware=dict(
                                        type="str", choices=["BIOS", "UEFI_64"]
                                    ),
                                    network_type=dict(
                                        type="str",
                                        choices=["E1000", "VFIO", "PARAVIRTUALIZED"],
                                    ),
                                    remote_data_volume_type=dict(
                                        type="str",
                                        choices=[
                                            "ISCSI",
                                            "SCSI",
                                            "IDE",
                                            "VFIO",
                                            "PARAVIRTUALIZED",
                                        ],
                                    ),
                                    is_pv_encryption_in_transit_enabled=dict(
                                        type="bool"
                                    ),
                                    is_consistent_volume_naming_enabled=dict(
                                        type="bool"
                                    ),
                                ),
                            ),
                            agent_config=dict(
                                type="dict",
                                options=dict(
                                    is_monitoring_disabled=dict(type="bool"),
                                    is_management_disabled=dict(type="bool"),
                                    are_all_plugins_disabled=dict(type="bool"),
                                    plugins_config=dict(
                                        type="list",
                                        elements="dict",
                                        options=dict(
                                            name=dict(type="str", required=True),
                                            desired_state=dict(
                                                type="str",
                                                required=True,
                                                choices=["ENABLED", "DISABLED"],
                                            ),
                                        ),
                                    ),
                                ),
                            ),
                            is_pv_encryption_in_transit_enabled=dict(type="bool"),
                            preferred_maintenance_action=dict(
                                type="str", choices=["LIVE_MIGRATE", "REBOOT"]
                            ),
                            instance_options=dict(
                                type="dict",
                                options=dict(
                                    are_legacy_imds_endpoints_disabled=dict(type="bool")
                                ),
                            ),
                            availability_config=dict(
                                type="dict",
                                options=dict(
                                    is_live_migration_preferred=dict(type="bool"),
                                    recovery_action=dict(
                                        type="str",
                                        choices=["RESTORE_INSTANCE", "STOP_INSTANCE"],
                                    ),
                                ),
                            ),
                            preemptible_instance_config=dict(
                                type="dict",
                                options=dict(
                                    preemption_action=dict(
                                        type="dict",
                                        required=True,
                                        options=dict(
                                            type=dict(
                                                type="str",
                                                required=True,
                                                choices=["TERMINATE"],
                                            ),
                                            preserve_boot_volume=dict(type="bool"),
                                        ),
                                    )
                                ),
                            ),
                        ),
                    ),
                    secondary_vnics=dict(
                        type="list",
                        elements="dict",
                        options=dict(
                            create_vnic_details=dict(
                                type="dict",
                                options=dict(
                                    assign_public_ip=dict(type="bool"),
                                    assign_private_dns_record=dict(type="bool"),
                                    defined_tags=dict(type="dict"),
                                    display_name=dict(aliases=["name"], type="str"),
                                    freeform_tags=dict(type="dict"),
                                    hostname_label=dict(type="str"),
                                    nsg_ids=dict(type="list", elements="str"),
                                    private_ip=dict(type="str"),
                                    skip_source_dest_check=dict(type="bool"),
                                    subnet_id=dict(type="str"),
                                ),
                            ),
                            display_name=dict(aliases=["name"], type="str"),
                            nic_index=dict(type="int"),
                        ),
                    ),
                ),
            ),
            instance_type=dict(
                type="str", default="compute", choices=["instance_options", "compute"]
            ),
            block_volumes=dict(
                type="list",
                elements="dict",
                options=dict(
                    attach_details=dict(
                        type="dict",
                        options=dict(
                            use_chap=dict(type="bool"),
                            display_name=dict(aliases=["name"], type="str"),
                            is_read_only=dict(type="bool"),
                            device=dict(type="str"),
                            is_shareable=dict(type="bool"),
                            type=dict(
                                type="str",
                                required=True,
                                choices=["iscsi", "paravirtualized"],
                            ),
                            is_pv_encryption_in_transit_enabled=dict(type="bool"),
                        ),
                    ),
                    create_details=dict(
                        type="dict",
                        options=dict(
                            availability_domain=dict(type="str"),
                            backup_policy_id=dict(type="str"),
                            compartment_id=dict(type="str"),
                            is_auto_tune_enabled=dict(type="bool"),
                            block_volume_replicas=dict(
                                type="list",
                                elements="dict",
                                options=dict(
                                    display_name=dict(aliases=["name"], type="str"),
                                    availability_domain=dict(type="str", required=True),
                                ),
                            ),
                            defined_tags=dict(type="dict"),
                            display_name=dict(aliases=["name"], type="str"),
                            freeform_tags=dict(type="dict"),
                            kms_key_id=dict(type="str"),
                            vpus_per_gb=dict(type="int"),
                            size_in_gbs=dict(type="int"),
                            source_details=dict(
                                type="dict",
                                options=dict(
                                    type=dict(
                                        type="str",
                                        required=True,
                                        choices=["volumeBackup", "volume"],
                                    ),
                                    id=dict(type="str"),
                                ),
                            ),
                            autotune_policies=dict(
                                type="list",
                                elements="dict",
                                options=dict(
                                    max_vpus_per_gb=dict(type="int"),
                                    autotune_type=dict(
                                        type="str",
                                        required=True,
                                        choices=[
                                            "PERFORMANCE_BASED",
                                            "DETACHED_VOLUME",
                                        ],
                                    ),
                                ),
                            ),
                        ),
                    ),
                    volume_id=dict(type="str"),
                ),
            ),
            launch_details=dict(
                type="dict",
                options=dict(
                    availability_domain=dict(type="str"),
                    capacity_reservation_id=dict(type="str"),
                    compartment_id=dict(type="str"),
                    create_vnic_details=dict(
                        type="dict",
                        options=dict(
                            assign_public_ip=dict(type="bool"),
                            assign_private_dns_record=dict(type="bool"),
                            defined_tags=dict(type="dict"),
                            display_name=dict(aliases=["name"], type="str"),
                            freeform_tags=dict(type="dict"),
                            hostname_label=dict(type="str"),
                            nsg_ids=dict(type="list", elements="str"),
                            private_ip=dict(type="str"),
                            skip_source_dest_check=dict(type="bool"),
                            subnet_id=dict(type="str"),
                        ),
                    ),
                    defined_tags=dict(type="dict"),
                    display_name=dict(aliases=["name"], type="str"),
                    extended_metadata=dict(type="dict"),
                    freeform_tags=dict(type="dict"),
                    ipxe_script=dict(type="str"),
                    metadata=dict(type="dict"),
                    shape=dict(type="str"),
                    shape_config=dict(
                        type="dict",
                        options=dict(
                            ocpus=dict(type="float"),
                            vcpus=dict(type="int"),
                            memory_in_gbs=dict(type="float"),
                            baseline_ocpu_utilization=dict(
                                type="str",
                                choices=[
                                    "BASELINE_1_8",
                                    "BASELINE_1_2",
                                    "BASELINE_1_1",
                                ],
                            ),
                            nvmes=dict(type="int"),
                        ),
                    ),
                    platform_config=dict(
                        type="dict",
                        options=dict(
                            percentage_of_cores_enabled=dict(type="int"),
                            numa_nodes_per_socket=dict(
                                type="str", choices=["NPS0", "NPS1", "NPS2", "NPS4"]
                            ),
                            is_symmetric_multi_threading_enabled=dict(type="bool"),
                            is_access_control_service_enabled=dict(type="bool"),
                            are_virtual_instructions_enabled=dict(type="bool"),
                            is_input_output_memory_management_unit_enabled=dict(
                                type="bool"
                            ),
                            type=dict(
                                type="str",
                                required=True,
                                choices=[
                                    "AMD_MILAN_BM",
                                    "INTEL_VM",
                                    "AMD_MILAN_BM_GPU",
                                    "INTEL_ICELAKE_BM",
                                    "AMD_ROME_BM",
                                    "INTEL_SKYLAKE_BM",
                                    "AMD_ROME_BM_GPU",
                                    "AMD_VM",
                                ],
                            ),
                            is_secure_boot_enabled=dict(type="bool"),
                            is_trusted_platform_module_enabled=dict(type="bool"),
                            is_measured_boot_enabled=dict(type="bool"),
                            is_memory_encryption_enabled=dict(type="bool"),
                        ),
                    ),
                    source_details=dict(
                        type="dict",
                        options=dict(
                            boot_volume_size_in_gbs=dict(type="int"),
                            image_id=dict(type="str"),
                            kms_key_id=dict(type="str"),
                            boot_volume_vpus_per_gb=dict(type="int"),
                            instance_source_image_filter_details=dict(
                                type="dict",
                                options=dict(
                                    compartment_id=dict(type="str"),
                                    defined_tags_filter=dict(type="dict"),
                                    operating_system=dict(type="str"),
                                    operating_system_version=dict(type="str"),
                                ),
                            ),
                            source_type=dict(
                                type="str",
                                required=True,
                                choices=["image", "bootVolume"],
                            ),
                            boot_volume_id=dict(type="str"),
                        ),
                    ),
                    fault_domain=dict(type="str"),
                    dedicated_vm_host_id=dict(type="str"),
                    launch_mode=dict(
                        type="str",
                        choices=["NATIVE", "EMULATED", "PARAVIRTUALIZED", "CUSTOM"],
                    ),
                    launch_options=dict(
                        type="dict",
                        options=dict(
                            boot_volume_type=dict(
                                type="str",
                                choices=[
                                    "ISCSI",
                                    "SCSI",
                                    "IDE",
                                    "VFIO",
                                    "PARAVIRTUALIZED",
                                ],
                            ),
                            firmware=dict(type="str", choices=["BIOS", "UEFI_64"]),
                            network_type=dict(
                                type="str", choices=["E1000", "VFIO", "PARAVIRTUALIZED"]
                            ),
                            remote_data_volume_type=dict(
                                type="str",
                                choices=[
                                    "ISCSI",
                                    "SCSI",
                                    "IDE",
                                    "VFIO",
                                    "PARAVIRTUALIZED",
                                ],
                            ),
                            is_pv_encryption_in_transit_enabled=dict(type="bool"),
                            is_consistent_volume_naming_enabled=dict(type="bool"),
                        ),
                    ),
                    agent_config=dict(
                        type="dict",
                        options=dict(
                            is_monitoring_disabled=dict(type="bool"),
                            is_management_disabled=dict(type="bool"),
                            are_all_plugins_disabled=dict(type="bool"),
                            plugins_config=dict(
                                type="list",
                                elements="dict",
                                options=dict(
                                    name=dict(type="str", required=True),
                                    desired_state=dict(
                                        type="str",
                                        required=True,
                                        choices=["ENABLED", "DISABLED"],
                                    ),
                                ),
                            ),
                        ),
                    ),
                    is_pv_encryption_in_transit_enabled=dict(type="bool"),
                    preferred_maintenance_action=dict(
                        type="str", choices=["LIVE_MIGRATE", "REBOOT"]
                    ),
                    instance_options=dict(
                        type="dict",
                        options=dict(
                            are_legacy_imds_endpoints_disabled=dict(type="bool")
                        ),
                    ),
                    availability_config=dict(
                        type="dict",
                        options=dict(
                            is_live_migration_preferred=dict(type="bool"),
                            recovery_action=dict(
                                type="str",
                                choices=["RESTORE_INSTANCE", "STOP_INSTANCE"],
                            ),
                        ),
                    ),
                    preemptible_instance_config=dict(
                        type="dict",
                        options=dict(
                            preemption_action=dict(
                                type="dict",
                                required=True,
                                options=dict(
                                    type=dict(
                                        type="str", required=True, choices=["TERMINATE"]
                                    ),
                                    preserve_boot_volume=dict(type="bool"),
                                ),
                            )
                        ),
                    ),
                ),
            ),
            secondary_vnics=dict(
                type="list",
                elements="dict",
                options=dict(
                    create_vnic_details=dict(
                        type="dict",
                        options=dict(
                            assign_public_ip=dict(type="bool"),
                            assign_private_dns_record=dict(type="bool"),
                            defined_tags=dict(type="dict"),
                            display_name=dict(aliases=["name"], type="str"),
                            freeform_tags=dict(type="dict"),
                            hostname_label=dict(type="str"),
                            nsg_ids=dict(type="list", elements="str"),
                            private_ip=dict(type="str"),
                            skip_source_dest_check=dict(type="bool"),
                            subnet_id=dict(type="str"),
                        ),
                    ),
                    display_name=dict(aliases=["name"], type="str"),
                    nic_index=dict(type="int"),
                ),
            ),
            action=dict(
                type="str", required=True, choices=["change_compartment", "launch"]
            ),
        )
    )

    module = OCIAnsibleModule(argument_spec=module_args, supports_check_mode=True)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_helper = ResourceHelper(
        module=module,
        resource_type="instance_configuration",
        service_client_class=ComputeManagementClient,
        namespace="core",
    )

    result = resource_helper.perform_action(module.params.get("action"))

    module.exit_json(**result)


if __name__ == "__main__":
    main()
