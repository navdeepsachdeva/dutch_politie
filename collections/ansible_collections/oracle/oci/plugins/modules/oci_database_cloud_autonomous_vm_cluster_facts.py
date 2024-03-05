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
module: oci_database_cloud_autonomous_vm_cluster_facts
short_description: Fetches details about one or multiple CloudAutonomousVmCluster resources in Oracle Cloud Infrastructure
description:
    - Fetches details about one or multiple CloudAutonomousVmCluster resources in Oracle Cloud Infrastructure
    - Lists Autonomous Exadata VM clusters in the Oracle cloud. For Exadata Cloud@Customer systems, see
      L(ListAutonomousVmClusters,https://docs.cloud.oracle.com/en-us/iaas/api/#/en/database/latest/AutonomousVmCluster/ListAutonomousVmClusters).
    - If I(cloud_autonomous_vm_cluster_id) is specified, the details of a single CloudAutonomousVmCluster will be returned.
version_added: "2.9.0"
author: Oracle (@oracle)
options:
    cloud_autonomous_vm_cluster_id:
        description:
            - The Cloud VM cluster L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm).
            - Required to get a specific cloud_autonomous_vm_cluster.
        type: str
        aliases: ["id"]
    compartment_id:
        description:
            - The compartment L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm).
            - Required to list multiple cloud_autonomous_vm_clusters.
        type: str
    cloud_exadata_infrastructure_id:
        description:
            - If provided, filters the results for the specified cloud Exadata infrastructure.
        type: str
    sort_by:
        description:
            - The field to sort by.  You can provide one sort order (`sortOrder`).  Default order for TIMECREATED is descending.  Default order for DISPLAYNAME
              is ascending. The DISPLAYNAME sort order is case sensitive.
        type: str
        choices:
            - "TIMECREATED"
            - "DISPLAYNAME"
    sort_order:
        description:
            - The sort order to use, either ascending (`ASC`) or descending (`DESC`).
        type: str
        choices:
            - "ASC"
            - "DESC"
    lifecycle_state:
        description:
            - A filter to return only resources that match the given lifecycle state exactly.
        type: str
        choices:
            - "PROVISIONING"
            - "AVAILABLE"
            - "UPDATING"
            - "TERMINATING"
            - "TERMINATED"
            - "FAILED"
            - "MAINTENANCE_IN_PROGRESS"
    availability_domain:
        description:
            - A filter to return only resources that match the given availability domain exactly.
        type: str
    display_name:
        description:
            - A filter to return only resources that match the entire display name given. The match is not case sensitive.
        type: str
        aliases: ["name"]
extends_documentation_fragment: [ oracle.oci.oracle ]
"""

EXAMPLES = """
- name: Get a specific cloud_autonomous_vm_cluster
  oci_database_cloud_autonomous_vm_cluster_facts:
    # required
    cloud_autonomous_vm_cluster_id: "ocid1.cloudautonomousvmcluster.oc1..xxxxxxEXAMPLExxxxxx"

- name: List cloud_autonomous_vm_clusters
  oci_database_cloud_autonomous_vm_cluster_facts:
    # required
    compartment_id: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"

    # optional
    cloud_exadata_infrastructure_id: "ocid1.cloudexadatainfrastructure.oc1..xxxxxxEXAMPLExxxxxx"
    sort_by: TIMECREATED
    sort_order: ASC
    lifecycle_state: PROVISIONING
    availability_domain: Uocm:PHX-AD-1
    display_name: display_name_example

"""

RETURN = """
cloud_autonomous_vm_clusters:
    description:
        - List of CloudAutonomousVmCluster resources
    returned: on success
    type: complex
    contains:
        id:
            description:
                - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the Cloud Autonomous VM cluster.
            returned: on success
            type: str
            sample: "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx"
        compartment_id:
            description:
                - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the compartment.
            returned: on success
            type: str
            sample: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
        description:
            description:
                - User defined description of the cloud Autonomous VM cluster.
            returned: on success
            type: str
            sample: description_example
        availability_domain:
            description:
                - The name of the availability domain that the cloud Autonomous VM cluster is located in.
            returned: on success
            type: str
            sample: Uocm:PHX-AD-1
        subnet_id:
            description:
                - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the subnet the cloud Autonomous VM Cluster is associated
                  with.
                - "**Subnet Restrictions:**
                  - For Exadata and virtual machine 2-node RAC DB systems, do not use a subnet that overlaps with 192.168.128.0/20."
                - These subnets are used by the Oracle Clusterware private interconnect on the database instance.
                  Specifying an overlapping subnet will cause the private interconnect to malfunction.
                  This restriction applies to both the client subnet and backup subnet.
            returned: on success
            type: str
            sample: "ocid1.subnet.oc1..xxxxxxEXAMPLExxxxxx"
        nsg_ids:
            description:
                - "The list of L(OCIDs,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) for the network security groups (NSGs) to which
                  this resource belongs. Setting this to an empty list removes all resources from all NSGs. For more information about NSGs, see L(Security
                  Rules,https://docs.cloud.oracle.com/Content/Network/Concepts/securityrules.htm).
                  **NsgIds restrictions:**
                  - A network security group (NSG) is optional for Autonomous Databases with private access. The nsgIds list can be empty."
            returned: on success
            type: list
            sample: []
        last_update_history_entry_id:
            description:
                - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the last maintenance update history. This value is
                  updated when a maintenance update starts.
            returned: on success
            type: str
            sample: "ocid1.lastupdatehistoryentry.oc1..xxxxxxEXAMPLExxxxxx"
        lifecycle_state:
            description:
                - The current state of the cloud Autonomous VM cluster.
            returned: on success
            type: str
            sample: PROVISIONING
        display_name:
            description:
                - The user-friendly name for the cloud Autonomous VM cluster. The name does not need to be unique.
            returned: on success
            type: str
            sample: display_name_example
        time_created:
            description:
                - The date and time that the cloud Autonomous VM cluster was created.
            returned: on success
            type: str
            sample: "2013-10-20T19:20:30+01:00"
        time_updated:
            description:
                - The last date and time that the cloud Autonomous VM cluster was updated.
            returned: on success
            type: str
            sample: "2013-10-20T19:20:30+01:00"
        cluster_time_zone:
            description:
                - The time zone of the Cloud Autonomous VM Cluster.
            returned: on success
            type: str
            sample: cluster_time_zone_example
        lifecycle_details:
            description:
                - Additional information about the current lifecycle state.
            returned: on success
            type: str
            sample: lifecycle_details_example
        hostname:
            description:
                - The hostname for the cloud Autonomous VM cluster.
            returned: on success
            type: str
            sample: hostname_example
        domain:
            description:
                - The domain name for the cloud Autonomous VM cluster.
            returned: on success
            type: str
            sample: domain_example
        cloud_exadata_infrastructure_id:
            description:
                - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the cloud Exadata infrastructure.
            returned: on success
            type: str
            sample: "ocid1.cloudexadatainfrastructure.oc1..xxxxxxEXAMPLExxxxxx"
        shape:
            description:
                - The model name of the Exadata hardware running the cloud Autonomous VM cluster.
            returned: on success
            type: str
            sample: shape_example
        node_count:
            description:
                - The number of database servers in the cloud VM cluster.
            returned: on success
            type: int
            sample: 56
        data_storage_size_in_tbs:
            description:
                - The total data storage allocated, in terabytes (TB).
            returned: on success
            type: float
            sample: 1.2
        data_storage_size_in_gbs:
            description:
                - The total data storage allocated, in gigabytes (GB).
            returned: on success
            type: float
            sample: 1.2
        cpu_core_count:
            description:
                - The number of CPU cores on the cloud Autonomous VM cluster.
            returned: on success
            type: int
            sample: 56
        ocpu_count:
            description:
                - The number of CPU cores on the cloud Autonomous VM cluster. Only 1 decimal place is allowed for the fractional part.
            returned: on success
            type: float
            sample: 3.4
        compute_model:
            description:
                - The compute model of the Cloud Autonomous VM Cluster. See L(Compute Models in Autonomous Database on Dedicated Exadata
                  Infrastructure,https://docs.oracle.com/en/cloud/paas/autonomous-database/dedicated/adbak) for more details.
            returned: on success
            type: str
            sample: ECPU
        is_mtls_enabled_vm_cluster:
            description:
                - Enable mutual TLS(mTLS) authentication for database at time of provisioning a VMCluster. This is applicable to database TLS Certificates only.
                  Default is TLS
            returned: on success
            type: bool
            sample: true
        cpu_core_count_per_node:
            description:
                - The number of CPU cores enabled per VM cluster node.
            returned: on success
            type: int
            sample: 56
        memory_size_in_gbs:
            description:
                - The memory allocated in GBs.
            returned: on success
            type: int
            sample: 56
        license_model:
            description:
                - The Oracle license model that applies to the Oracle Autonomous Database. Bring your own license (BYOL) allows you to apply your current on-
                  premises Oracle software licenses to equivalent, highly automated Oracle PaaS and IaaS services in the cloud.
                  License Included allows you to subscribe to new Oracle Database software licenses and the Database service.
                  Note that when provisioning an Autonomous Database on L(dedicated Exadata infrastructure,https://docs.oracle.com/en/cloud/paas/autonomous-
                  database/index.html), this attribute must be null because the attribute is already set at the
                  Autonomous Exadata Infrastructure level. When using L(shared Exadata infrastructure,https://docs.oracle.com/en/cloud/paas/autonomous-
                  database/index.html), if a value is not specified, the system will supply the value of `BRING_YOUR_OWN_LICENSE`.
                - "This cannot be updated in parallel with any of the following: cpuCoreCount, computeCount, maxCpuCoreCount, dataStorageSizeInTBs,
                  adminPassword, isMTLSConnectionRequired, dbWorkload, privateEndpointLabel, nsgIds, dbVersion, dbName, scheduledOperations, dbToolsDetails, or
                  isFreeTier."
            returned: on success
            type: str
            sample: LICENSE_INCLUDED
        last_maintenance_run_id:
            description:
                - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the last maintenance run.
            returned: on success
            type: str
            sample: "ocid1.lastmaintenancerun.oc1..xxxxxxEXAMPLExxxxxx"
        next_maintenance_run_id:
            description:
                - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the next maintenance run.
            returned: on success
            type: str
            sample: "ocid1.nextmaintenancerun.oc1..xxxxxxEXAMPLExxxxxx"
        maintenance_window:
            description:
                - ""
            returned: on success
            type: complex
            contains:
                preference:
                    description:
                        - The maintenance window scheduling preference.
                    returned: on success
                    type: str
                    sample: NO_PREFERENCE
                patching_mode:
                    description:
                        - "Cloud Exadata infrastructure node patching method, either \\"ROLLING\\" or \\"NONROLLING\\". Default value is ROLLING."
                        - "*IMPORTANT*: Non-rolling infrastructure patching involves system down time. See L(Oracle-Managed Infrastructure Maintenance
                          Updates,https://docs.cloud.oracle.com/iaas/Content/Database/Concepts/examaintenance.htm#Oracle) for more information."
                    returned: on success
                    type: str
                    sample: ROLLING
                is_custom_action_timeout_enabled:
                    description:
                        - If true, enables the configuration of a custom action timeout (waiting period) between database server patching operations.
                    returned: on success
                    type: bool
                    sample: true
                custom_action_timeout_in_mins:
                    description:
                        - Determines the amount of time the system will wait before the start of each database server patching operation.
                          Custom action timeout is in minutes and valid value is between 15 to 120 (inclusive).
                    returned: on success
                    type: int
                    sample: 56
                is_monthly_patching_enabled:
                    description:
                        - If true, enables the monthly patching option.
                    returned: on success
                    type: bool
                    sample: true
                months:
                    description:
                        - Months during the year when maintenance should be performed.
                    returned: on success
                    type: complex
                    contains:
                        name:
                            description:
                                - Name of the month of the year.
                            returned: on success
                            type: str
                            sample: JANUARY
                weeks_of_month:
                    description:
                        - Weeks during the month when maintenance should be performed. Weeks start on the 1st, 8th, 15th, and 22nd days of the month, and have a
                          duration of 7 days. Weeks start and end based on calendar dates, not days of the week.
                          For example, to allow maintenance during the 2nd week of the month (from the 8th day to the 14th day of the month), use the value 2.
                          Maintenance cannot be scheduled for the fifth week of months that contain more than 28 days.
                          Note that this parameter works in conjunction with the  daysOfWeek and hoursOfDay parameters to allow you to specify specific days of
                          the week and hours that maintenance will be performed.
                    returned: on success
                    type: list
                    sample: []
                days_of_week:
                    description:
                        - Days during the week when maintenance should be performed.
                    returned: on success
                    type: complex
                    contains:
                        name:
                            description:
                                - Name of the day of the week.
                            returned: on success
                            type: str
                            sample: MONDAY
                hours_of_day:
                    description:
                        - "The window of hours during the day when maintenance should be performed. The window is a 4 hour slot. Valid values are
                          - 0 - represents time slot 0:00 - 3:59 UTC - 4 - represents time slot 4:00 - 7:59 UTC - 8 - represents time slot 8:00 - 11:59 UTC - 12
                            - represents time slot 12:00 - 15:59 UTC - 16 - represents time slot 16:00 - 19:59 UTC - 20 - represents time slot 20:00 - 23:59
                            UTC"
                    returned: on success
                    type: list
                    sample: []
                lead_time_in_weeks:
                    description:
                        - Lead time window allows user to set a lead time to prepare for a down time. The lead time is in weeks and valid value is between 1 to
                          4.
                    returned: on success
                    type: int
                    sample: 56
        scan_listener_port_tls:
            description:
                - The SCAN Listenenr TLS port. Default is 2484.
            returned: on success
            type: int
            sample: 56
        scan_listener_port_non_tls:
            description:
                - The SCAN Listener Non TLS port. Default is 1521.
            returned: on success
            type: int
            sample: 56
        freeform_tags:
            description:
                - Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace.
                  For more information, see L(Resource Tags,https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm).
                - "Example: `{\\"Department\\": \\"Finance\\"}`"
            returned: on success
            type: dict
            sample: {'Department': 'Finance'}
        defined_tags:
            description:
                - Defined tags for this resource. Each key is predefined and scoped to a namespace.
                  For more information, see L(Resource Tags,https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm).
            returned: on success
            type: dict
            sample: {'Operations': {'CostCenter': 'US'}}
        time_database_ssl_certificate_expires:
            description:
                - The date and time of Database SSL certificate expiration.
            returned: on success
            type: str
            sample: "2013-10-20T19:20:30+01:00"
        time_ords_certificate_expires:
            description:
                - The date and time of ORDS certificate expiration.
            returned: on success
            type: str
            sample: "2013-10-20T19:20:30+01:00"
        available_cpus:
            description:
                - CPU cores available for allocation to Autonomous Databases.
            returned: on success
            type: float
            sample: 3.4
        reclaimable_cpus:
            description:
                - "For Autonomous Databases on Dedicated Exadata Infrastructure:
                  - These are the CPUs that continue to be included in the count of CPUs available to the Autonomous Container Database even after one of its
                    Autonomous Database is terminated or scaled down. You can release them to the available CPUs at its parent Autonomous VM Cluster level by
                    restarting the Autonomous Container Database.
                  - The CPU type (OCPUs or ECPUs) is determined by the parent Autonomous Exadata VM Cluster's compute model. See L(Compute Models in Autonomous
                    Database on Dedicated Exadata Infrastructure,https://docs.oracle.com/en/cloud/paas/autonomous-database/dedicated/adbak) for more details."
            returned: on success
            type: float
            sample: 3.4
        available_container_databases:
            description:
                - The number of Autonomous Container Databases that can be created with the currently available local storage.
            returned: on success
            type: int
            sample: 56
        total_container_databases:
            description:
                - The total number of Autonomous Container Databases that can be created with the allocated local storage.
            returned: on success
            type: int
            sample: 56
        available_autonomous_data_storage_size_in_tbs:
            description:
                - The data disk group size available for Autonomous Databases, in TBs.
            returned: on success
            type: float
            sample: 1.2
        autonomous_data_storage_size_in_tbs:
            description:
                - The data disk group size allocated for Autonomous Databases, in TBs.
            returned: on success
            type: float
            sample: 1.2
        db_node_storage_size_in_gbs:
            description:
                - The local node storage allocated in GBs.
            returned: on success
            type: int
            sample: 56
        memory_per_oracle_compute_unit_in_gbs:
            description:
                - The amount of memory (in GBs) enabled per OCPU or ECPU. See L(Compute Models in Autonomous Database on Dedicated Exadata
                  Infrastructure,https://docs.oracle.com/en/cloud/paas/autonomous-database/dedicated/adbak) for more details.
            returned: on success
            type: int
            sample: 56
        db_servers:
            description:
                - The list of L(OCIDs,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the Db servers.
            returned: on success
            type: list
            sample: []
    sample: [{
        "id": "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx",
        "compartment_id": "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx",
        "description": "description_example",
        "availability_domain": "Uocm:PHX-AD-1",
        "subnet_id": "ocid1.subnet.oc1..xxxxxxEXAMPLExxxxxx",
        "nsg_ids": [],
        "last_update_history_entry_id": "ocid1.lastupdatehistoryentry.oc1..xxxxxxEXAMPLExxxxxx",
        "lifecycle_state": "PROVISIONING",
        "display_name": "display_name_example",
        "time_created": "2013-10-20T19:20:30+01:00",
        "time_updated": "2013-10-20T19:20:30+01:00",
        "cluster_time_zone": "cluster_time_zone_example",
        "lifecycle_details": "lifecycle_details_example",
        "hostname": "hostname_example",
        "domain": "domain_example",
        "cloud_exadata_infrastructure_id": "ocid1.cloudexadatainfrastructure.oc1..xxxxxxEXAMPLExxxxxx",
        "shape": "shape_example",
        "node_count": 56,
        "data_storage_size_in_tbs": 1.2,
        "data_storage_size_in_gbs": 1.2,
        "cpu_core_count": 56,
        "ocpu_count": 3.4,
        "compute_model": "ECPU",
        "is_mtls_enabled_vm_cluster": true,
        "cpu_core_count_per_node": 56,
        "memory_size_in_gbs": 56,
        "license_model": "LICENSE_INCLUDED",
        "last_maintenance_run_id": "ocid1.lastmaintenancerun.oc1..xxxxxxEXAMPLExxxxxx",
        "next_maintenance_run_id": "ocid1.nextmaintenancerun.oc1..xxxxxxEXAMPLExxxxxx",
        "maintenance_window": {
            "preference": "NO_PREFERENCE",
            "patching_mode": "ROLLING",
            "is_custom_action_timeout_enabled": true,
            "custom_action_timeout_in_mins": 56,
            "is_monthly_patching_enabled": true,
            "months": [{
                "name": "JANUARY"
            }],
            "weeks_of_month": [],
            "days_of_week": [{
                "name": "MONDAY"
            }],
            "hours_of_day": [],
            "lead_time_in_weeks": 56
        },
        "scan_listener_port_tls": 56,
        "scan_listener_port_non_tls": 56,
        "freeform_tags": {'Department': 'Finance'},
        "defined_tags": {'Operations': {'CostCenter': 'US'}},
        "time_database_ssl_certificate_expires": "2013-10-20T19:20:30+01:00",
        "time_ords_certificate_expires": "2013-10-20T19:20:30+01:00",
        "available_cpus": 3.4,
        "reclaimable_cpus": 3.4,
        "available_container_databases": 56,
        "total_container_databases": 56,
        "available_autonomous_data_storage_size_in_tbs": 1.2,
        "autonomous_data_storage_size_in_tbs": 1.2,
        "db_node_storage_size_in_gbs": 56,
        "memory_per_oracle_compute_unit_in_gbs": 56,
        "db_servers": []
    }]
"""

from ansible_collections.oracle.oci.plugins.module_utils import oci_common_utils
from ansible_collections.oracle.oci.plugins.module_utils.oci_resource_utils import (
    OCIResourceFactsHelperBase,
    get_custom_class,
    OCIAnsibleModule,
)

try:
    from oci.database import DatabaseClient

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


class CloudAutonomousVmClusterFactsHelperGen(OCIResourceFactsHelperBase):
    """Supported operations: get, list"""

    def get_required_params_for_get(self):
        return [
            "cloud_autonomous_vm_cluster_id",
        ]

    def get_required_params_for_list(self):
        return [
            "compartment_id",
        ]

    def get_resource(self):
        return oci_common_utils.call_with_backoff(
            self.client.get_cloud_autonomous_vm_cluster,
            cloud_autonomous_vm_cluster_id=self.module.params.get(
                "cloud_autonomous_vm_cluster_id"
            ),
        )

    def list_resources(self):
        optional_list_method_params = [
            "cloud_exadata_infrastructure_id",
            "sort_by",
            "sort_order",
            "lifecycle_state",
            "availability_domain",
            "display_name",
        ]
        optional_kwargs = dict(
            (param, self.module.params[param])
            for param in optional_list_method_params
            if self.module.params.get(param) is not None
        )
        return oci_common_utils.list_all_resources(
            self.client.list_cloud_autonomous_vm_clusters,
            compartment_id=self.module.params.get("compartment_id"),
            **optional_kwargs
        )


CloudAutonomousVmClusterFactsHelperCustom = get_custom_class(
    "CloudAutonomousVmClusterFactsHelperCustom"
)


class ResourceFactsHelper(
    CloudAutonomousVmClusterFactsHelperCustom, CloudAutonomousVmClusterFactsHelperGen
):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec()
    module_args.update(
        dict(
            cloud_autonomous_vm_cluster_id=dict(aliases=["id"], type="str"),
            compartment_id=dict(type="str"),
            cloud_exadata_infrastructure_id=dict(type="str"),
            sort_by=dict(type="str", choices=["TIMECREATED", "DISPLAYNAME"]),
            sort_order=dict(type="str", choices=["ASC", "DESC"]),
            lifecycle_state=dict(
                type="str",
                choices=[
                    "PROVISIONING",
                    "AVAILABLE",
                    "UPDATING",
                    "TERMINATING",
                    "TERMINATED",
                    "FAILED",
                    "MAINTENANCE_IN_PROGRESS",
                ],
            ),
            availability_domain=dict(type="str"),
            display_name=dict(aliases=["name"], type="str"),
        )
    )

    module = OCIAnsibleModule(argument_spec=module_args)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_facts_helper = ResourceFactsHelper(
        module=module,
        resource_type="cloud_autonomous_vm_cluster",
        service_client_class=DatabaseClient,
        namespace="database",
    )

    result = []

    if resource_facts_helper.is_get():
        result = [resource_facts_helper.get()]
    elif resource_facts_helper.is_list():
        result = resource_facts_helper.list()
    else:
        resource_facts_helper.fail()

    module.exit_json(cloud_autonomous_vm_clusters=result)


if __name__ == "__main__":
    main()
