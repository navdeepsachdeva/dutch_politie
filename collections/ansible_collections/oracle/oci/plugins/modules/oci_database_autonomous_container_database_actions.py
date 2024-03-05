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
module: oci_database_autonomous_container_database_actions
short_description: Perform actions on an AutonomousContainerDatabase resource in Oracle Cloud Infrastructure
description:
    - Perform actions on an AutonomousContainerDatabase resource in Oracle Cloud Infrastructure
    - For I(action=change_compartment), move the Autonomous Container Database and its dependent resources to the specified compartment.
      For more information about moving Autonomous Container Databases, see
      L(Moving Database Resources to a Different Compartment,https://docs.cloud.oracle.com/Content/Database/Concepts/databaseoverview.htm#moveRes).
    - For I(action=change_dataguard_role), switch the Autonomous Container Database role between Standby and Snapshot Standby.
      For more information about changing Autonomous Container Databases Dataguard Role, see
      L(Convert Physical Standby to Snapshot Standby,https://docs.oracle.com/en/cloud/paas/autonomous-database/dedicated/adbcl/index.html#ADBCL-
      GUID-D3B503F1-0032-4B0D-9F00-ACAE8151AB80) and L(Convert Snapshot Standby to Physical Standby,https://docs.oracle.com/en/cloud/paas/autonomous-
      database/dedicated/adbcl/index.html#ADBCL-GUID-E8D7E0EE-8244-467D-B33A-1BC6F969A0A4).
    - For I(action=restart), rolling restarts the specified Autonomous Container Database.
    - For I(action=rotate_autonomous_container_database_encryption_key), creates a new version of an existing L(Vault
      service,https://docs.cloud.oracle.com/iaas/Content/KeyManagement/Concepts/keyoverview.htm) key.
version_added: "2.9.0"
author: Oracle (@oracle)
options:
    compartment_id:
        description:
            - The L(OCID,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the compartment to move the resource to.
            - Required for I(action=change_compartment).
        type: str
    role:
        description:
            - The Data Guard role of the Autonomous Container Database or Autonomous Database, if Autonomous Data Guard is enabled.
            - Required for I(action=change_dataguard_role).
        type: str
        choices:
            - "PRIMARY"
            - "STANDBY"
            - "DISABLED_STANDBY"
            - "BACKUP_COPY"
            - "SNAPSHOT_STANDBY"
    autonomous_container_database_dataguard_association_id:
        description:
            - The Autonomous Container Database-Autonomous Data Guard association
              L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm).
            - Required for I(action=change_dataguard_role).
        type: str
    connection_strings_type:
        description:
            - type of connection strings when converting database to snapshot mode
            - Applicable only for I(action=change_dataguard_role).
        type: str
        choices:
            - "SNAPSHOT_SERVICES"
            - "PRIMARY_SERVICES"
    autonomous_container_database_id:
        description:
            - The Autonomous Container Database L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm).
        type: str
        aliases: ["id"]
        required: true
    action:
        description:
            - The action to perform on the AutonomousContainerDatabase.
        type: str
        required: true
        choices:
            - "change_compartment"
            - "change_dataguard_role"
            - "restart"
            - "rotate_autonomous_container_database_encryption_key"
extends_documentation_fragment: [ oracle.oci.oracle, oracle.oci.oracle_wait_options ]
"""

EXAMPLES = """
- name: Perform action change_compartment on autonomous_container_database
  oci_database_autonomous_container_database_actions:
    # required
    compartment_id: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
    autonomous_container_database_id: "ocid1.autonomouscontainerdatabase.oc1..xxxxxxEXAMPLExxxxxx"
    action: change_compartment

- name: Perform action change_dataguard_role on autonomous_container_database
  oci_database_autonomous_container_database_actions:
    # required
    role: PRIMARY
    autonomous_container_database_dataguard_association_id: "ocid1.autonomouscontainerdatabasedataguardassociation.oc1..xxxxxxEXAMPLExxxxxx"
    autonomous_container_database_id: "ocid1.autonomouscontainerdatabase.oc1..xxxxxxEXAMPLExxxxxx"
    action: change_dataguard_role

    # optional
    connection_strings_type: SNAPSHOT_SERVICES

- name: Perform action restart on autonomous_container_database
  oci_database_autonomous_container_database_actions:
    # required
    autonomous_container_database_id: "ocid1.autonomouscontainerdatabase.oc1..xxxxxxEXAMPLExxxxxx"
    action: restart

- name: Perform action rotate_autonomous_container_database_encryption_key on autonomous_container_database
  oci_database_autonomous_container_database_actions:
    # required
    autonomous_container_database_id: "ocid1.autonomouscontainerdatabase.oc1..xxxxxxEXAMPLExxxxxx"
    action: rotate_autonomous_container_database_encryption_key

"""

RETURN = """
autonomous_container_database:
    description:
        - Details of the AutonomousContainerDatabase resource acted upon by the current operation
    returned: on success
    type: complex
    contains:
        id:
            description:
                - The OCID of the Autonomous Container Database.
            returned: on success
            type: str
            sample: "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx"
        compartment_id:
            description:
                - The OCID of the compartment.
            returned: on success
            type: str
            sample: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
        display_name:
            description:
                - The user-provided name for the Autonomous Container Database.
            returned: on success
            type: str
            sample: display_name_example
        db_unique_name:
            description:
                - "**Deprecated.** The `DB_UNIQUE_NAME` value is set by Oracle Cloud Infrastructure.  Do not specify a value for this parameter. Specifying a
                  value for this field will cause Terraform operations to fail."
            returned: on success
            type: str
            sample: db_unique_name_example
        db_name:
            description:
                - The Database name for the Autonomous Container Database. The name must be unique within the Cloud Autonomous VM Cluster, starting with an
                  alphabetic character, followed by 1 to 7 alphanumeric characters.
            returned: on success
            type: str
            sample: db_name_example
        service_level_agreement_type:
            description:
                - The service level agreement type of the container database. The default is STANDARD.
            returned: on success
            type: str
            sample: STANDARD
        autonomous_exadata_infrastructure_id:
            description:
                - "**No longer used.** For Autonomous Database on dedicated Exadata infrastructure, the container database is created within a specified
                  `cloudAutonomousVmCluster`."
            returned: on success
            type: str
            sample: "ocid1.autonomousexadatainfrastructure.oc1..xxxxxxEXAMPLExxxxxx"
        autonomous_vm_cluster_id:
            description:
                - The OCID of the Autonomous VM Cluster.
            returned: on success
            type: str
            sample: "ocid1.autonomousvmcluster.oc1..xxxxxxEXAMPLExxxxxx"
        infrastructure_type:
            description:
                - The infrastructure type this resource belongs to.
            returned: on success
            type: str
            sample: CLOUD
        cloud_autonomous_vm_cluster_id:
            description:
                - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the cloud Autonomous Exadata VM Cluster.
            returned: on success
            type: str
            sample: "ocid1.cloudautonomousvmcluster.oc1..xxxxxxEXAMPLExxxxxx"
        kms_key_id:
            description:
                - The OCID of the key container that is used as the master encryption key in database transparent data encryption (TDE) operations.
            returned: on success
            type: str
            sample: "ocid1.kmskey.oc1..xxxxxxEXAMPLExxxxxx"
        vault_id:
            description:
                - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the Oracle Cloud Infrastructure
                  L(vault,https://docs.cloud.oracle.com/Content/KeyManagement/Concepts/keyoverview.htm#concepts).
            returned: on success
            type: str
            sample: "ocid1.vault.oc1..xxxxxxEXAMPLExxxxxx"
        kms_key_version_id:
            description:
                - The OCID of the key container version that is used in database transparent data encryption (TDE) operations KMS Key can have multiple key
                  versions. If none is specified, the current key version (latest) of the Key Id is used for the operation.
            returned: on success
            type: str
            sample: "ocid1.kmskeyversion.oc1..xxxxxxEXAMPLExxxxxx"
        key_history_entry:
            description:
                - Key History Entry.
            returned: on success
            type: complex
            contains:
                id:
                    description:
                        - The id of the Autonomous Database L(Vault,https://docs.cloud.oracle.com/Content/KeyManagement/Concepts/keyoverview.htm#concepts)
                          service key management history entry.
                    returned: on success
                    type: str
                    sample: "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx"
                kms_key_version_id:
                    description:
                        - The OCID of the key container version that is used in database transparent data encryption (TDE) operations KMS Key can have multiple
                          key versions. If none is specified, the current key version (latest) of the Key Id is used for the operation.
                    returned: on success
                    type: str
                    sample: "ocid1.kmskeyversion.oc1..xxxxxxEXAMPLExxxxxx"
                vault_id:
                    description:
                        - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the Oracle Cloud Infrastructure
                          L(vault,https://docs.cloud.oracle.com/Content/KeyManagement/Concepts/keyoverview.htm#concepts).
                    returned: on success
                    type: str
                    sample: "ocid1.vault.oc1..xxxxxxEXAMPLExxxxxx"
                time_activated:
                    description:
                        - The date and time the kms key activated.
                    returned: on success
                    type: str
                    sample: "2013-10-20T19:20:30+01:00"
        lifecycle_state:
            description:
                - The current state of the Autonomous Container Database.
            returned: on success
            type: str
            sample: PROVISIONING
        lifecycle_details:
            description:
                - Additional information about the current lifecycle state.
            returned: on success
            type: str
            sample: lifecycle_details_example
        time_created:
            description:
                - The date and time the Autonomous Container Database was created.
            returned: on success
            type: str
            sample: "2013-10-20T19:20:30+01:00"
        time_snapshot_standby_revert:
            description:
                - The date and time the Autonomous Container Database will be reverted to Standby from Snapshot Standby.
            returned: on success
            type: str
            sample: "2013-10-20T19:20:30+01:00"
        patch_model:
            description:
                - Database patch model preference.
            returned: on success
            type: str
            sample: RELEASE_UPDATES
        patch_id:
            description:
                - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the last patch applied on the system.
            returned: on success
            type: str
            sample: "ocid1.patch.oc1..xxxxxxEXAMPLExxxxxx"
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
        standby_maintenance_buffer_in_days:
            description:
                - The scheduling detail for the quarterly maintenance window of the standby Autonomous Container Database.
                  This value represents the number of days before scheduled maintenance of the primary database.
            returned: on success
            type: int
            sample: 56
        version_preference:
            description:
                - The next maintenance version preference.
            returned: on success
            type: str
            sample: NEXT_RELEASE_UPDATE
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
        role:
            description:
                - The Data Guard role of the Autonomous Container Database or Autonomous Database, if Autonomous Data Guard is enabled.
            returned: on success
            type: str
            sample: PRIMARY
        availability_domain:
            description:
                - The availability domain of the Autonomous Container Database.
            returned: on success
            type: str
            sample: Uocm:PHX-AD-1
        db_version:
            description:
                - Oracle Database version of the Autonomous Container Database.
            returned: on success
            type: str
            sample: db_version_example
        backup_config:
            description:
                - ""
            returned: on success
            type: complex
            contains:
                backup_destination_details:
                    description:
                        - Backup destination details.
                    returned: on success
                    type: complex
                    contains:
                        type:
                            description:
                                - Type of the database backup destination.
                            returned: on success
                            type: str
                            sample: NFS
                        id:
                            description:
                                - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the backup destination.
                            returned: on success
                            type: str
                            sample: "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx"
                        vpc_user:
                            description:
                                - For a RECOVERY_APPLIANCE backup destination, the Virtual Private Catalog (VPC) user that is used to access the Recovery
                                  Appliance.
                            returned: on success
                            type: str
                            sample: vpc_user_example
                        vpc_password:
                            description:
                                - For a RECOVERY_APPLIANCE backup destination, the password for the VPC user that is used to access the Recovery Appliance.
                            returned: on success
                            type: str
                            sample: example-password
                        internet_proxy:
                            description:
                                - Proxy URL to connect to object store.
                            returned: on success
                            type: str
                            sample: internet_proxy_example
                        dbrs_policy_id:
                            description:
                                - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the DBRS policy used for backup.
                            returned: on success
                            type: str
                            sample: "ocid1.dbrspolicy.oc1..xxxxxxEXAMPLExxxxxx"
                recovery_window_in_days:
                    description:
                        - Number of days between the current and the earliest point of recoverability covered by automatic backups.
                          This value applies to automatic backups. After a new automatic backup has been created, Oracle removes old automatic backups that are
                          created before the window.
                          When the value is updated, it is applied to all existing automatic backups.
                    returned: on success
                    type: int
                    sample: 56
        key_store_id:
            description:
                - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the key store.
            returned: on success
            type: str
            sample: "ocid1.keystore.oc1..xxxxxxEXAMPLExxxxxx"
        key_store_wallet_name:
            description:
                - The wallet name for Oracle Key Vault.
            returned: on success
            type: str
            sample: key_store_wallet_name_example
        memory_per_oracle_compute_unit_in_gbs:
            description:
                - The amount of memory (in GBs) enabled per OCPU or ECPU in the Autonomous VM Cluster.See L(Compute
                  Models,https://docs.oracle.com/en/cloud/paas/autonomous-database/dedicated/adbak) for more details.
            returned: on success
            type: int
            sample: 56
        available_cpus:
            description:
                - Sum of CPUs available on the Autonomous VM Cluster + Sum of reclaimable CPUs available in the Autonomous Container Database.<br>
                  For Autonomous Databases on Dedicated Exadata Infrastructure, the CPU type (OCPUs or ECPUs) is determined by the parent Autonomous Exadata VM
                  Cluster's compute model. See L(Compute Models in Autonomous Database on Dedicated Exadata
                  Infrastructure,https://docs.oracle.com/en/cloud/paas/autonomous-database/dedicated/adbak) for more details.
            returned: on success
            type: float
            sample: 3.4
        total_cpus:
            description:
                - The number of CPUs allocated to the Autonomous VM cluster.<br>
                  For Autonomous Databases on Dedicated Exadata Infrastructure, the CPU type (OCPUs or ECPUs) is determined by the parent Autonomous Exadata VM
                  Cluster's compute model. See L(Compute Models in Autonomous Database on Dedicated Exadata
                  Infrastructure,https://docs.oracle.com/en/cloud/paas/autonomous-database/dedicated/adbak) for more details.
            returned: on success
            type: int
            sample: 56
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
        provisionable_cpus:
            description:
                - An array of CPU values that can be used to successfully provision a single Autonomous Database.\\\\
                  For Autonomous Database on Dedicated Exadata Infrastructure, the CPU type (OCPUs or ECPUs) is determined by the parent Autonomous Exadata VM
                  Cluster's compute model. See L(Compute Models in Autonomous Database on Dedicated Exadata
                  Infrastructure,https://docs.oracle.com/en/cloud/paas/autonomous-database/dedicated/adbak) for more details.
            returned: on success
            type: list
            sample: []
        compute_model:
            description:
                - The compute model of the Autonomous VM Cluster. See L(Compute Models in Autonomous Database on Dedicated Exadata
                  Infrastructure,https://docs.oracle.com/en/cloud/paas/autonomous-database/dedicated/adbak) for more details.
            returned: on success
            type: str
            sample: ECPU
    sample: {
        "id": "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx",
        "compartment_id": "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx",
        "display_name": "display_name_example",
        "db_unique_name": "db_unique_name_example",
        "db_name": "db_name_example",
        "service_level_agreement_type": "STANDARD",
        "autonomous_exadata_infrastructure_id": "ocid1.autonomousexadatainfrastructure.oc1..xxxxxxEXAMPLExxxxxx",
        "autonomous_vm_cluster_id": "ocid1.autonomousvmcluster.oc1..xxxxxxEXAMPLExxxxxx",
        "infrastructure_type": "CLOUD",
        "cloud_autonomous_vm_cluster_id": "ocid1.cloudautonomousvmcluster.oc1..xxxxxxEXAMPLExxxxxx",
        "kms_key_id": "ocid1.kmskey.oc1..xxxxxxEXAMPLExxxxxx",
        "vault_id": "ocid1.vault.oc1..xxxxxxEXAMPLExxxxxx",
        "kms_key_version_id": "ocid1.kmskeyversion.oc1..xxxxxxEXAMPLExxxxxx",
        "key_history_entry": [{
            "id": "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx",
            "kms_key_version_id": "ocid1.kmskeyversion.oc1..xxxxxxEXAMPLExxxxxx",
            "vault_id": "ocid1.vault.oc1..xxxxxxEXAMPLExxxxxx",
            "time_activated": "2013-10-20T19:20:30+01:00"
        }],
        "lifecycle_state": "PROVISIONING",
        "lifecycle_details": "lifecycle_details_example",
        "time_created": "2013-10-20T19:20:30+01:00",
        "time_snapshot_standby_revert": "2013-10-20T19:20:30+01:00",
        "patch_model": "RELEASE_UPDATES",
        "patch_id": "ocid1.patch.oc1..xxxxxxEXAMPLExxxxxx",
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
        "standby_maintenance_buffer_in_days": 56,
        "version_preference": "NEXT_RELEASE_UPDATE",
        "freeform_tags": {'Department': 'Finance'},
        "defined_tags": {'Operations': {'CostCenter': 'US'}},
        "role": "PRIMARY",
        "availability_domain": "Uocm:PHX-AD-1",
        "db_version": "db_version_example",
        "backup_config": {
            "backup_destination_details": [{
                "type": "NFS",
                "id": "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx",
                "vpc_user": "vpc_user_example",
                "vpc_password": "example-password",
                "internet_proxy": "internet_proxy_example",
                "dbrs_policy_id": "ocid1.dbrspolicy.oc1..xxxxxxEXAMPLExxxxxx"
            }],
            "recovery_window_in_days": 56
        },
        "key_store_id": "ocid1.keystore.oc1..xxxxxxEXAMPLExxxxxx",
        "key_store_wallet_name": "key_store_wallet_name_example",
        "memory_per_oracle_compute_unit_in_gbs": 56,
        "available_cpus": 3.4,
        "total_cpus": 56,
        "reclaimable_cpus": 3.4,
        "provisionable_cpus": [],
        "compute_model": "ECPU"
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
    from oci.database import DatabaseClient
    from oci.database.models import ChangeCompartmentDetails
    from oci.database.models import ChangeDataguardRoleDetails

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


class AutonomousContainerDatabaseActionsHelperGen(OCIActionsHelperBase):
    """
    Supported actions:
        change_compartment
        change_dataguard_role
        restart
        rotate_autonomous_container_database_encryption_key
    """

    def __init__(self, *args, **kwargs):
        super(AutonomousContainerDatabaseActionsHelperGen, self).__init__(
            *args, **kwargs
        )
        self.work_request_client = oci_config_utils.create_service_client(
            self.module, WorkRequestClient
        )

    @staticmethod
    def get_module_resource_id_param():
        return "autonomous_container_database_id"

    def get_module_resource_id(self):
        return self.module.params.get("autonomous_container_database_id")

    def get_get_fn(self):
        return self.client.get_autonomous_container_database

    def get_resource(self):
        return oci_common_utils.call_with_backoff(
            self.client.get_autonomous_container_database,
            autonomous_container_database_id=self.module.params.get(
                "autonomous_container_database_id"
            ),
        )

    def change_compartment(self):
        action_details = oci_common_utils.convert_input_data_to_model_class(
            self.module.params, ChangeCompartmentDetails
        )
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.change_autonomous_container_database_compartment,
            call_fn_args=(),
            call_fn_kwargs=dict(
                change_compartment_details=action_details,
                autonomous_container_database_id=self.module.params.get(
                    "autonomous_container_database_id"
                ),
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

    def change_dataguard_role(self):
        action_details = oci_common_utils.convert_input_data_to_model_class(
            self.module.params, ChangeDataguardRoleDetails
        )
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.change_dataguard_role,
            call_fn_args=(),
            call_fn_kwargs=dict(
                change_dataguard_role_details=action_details,
                autonomous_container_database_id=self.module.params.get(
                    "autonomous_container_database_id"
                ),
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

    def restart(self):
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.restart_autonomous_container_database,
            call_fn_args=(),
            call_fn_kwargs=dict(
                autonomous_container_database_id=self.module.params.get(
                    "autonomous_container_database_id"
                ),
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

    def rotate_autonomous_container_database_encryption_key(self):
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.rotate_autonomous_container_database_encryption_key,
            call_fn_args=(),
            call_fn_kwargs=dict(
                autonomous_container_database_id=self.module.params.get(
                    "autonomous_container_database_id"
                ),
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


AutonomousContainerDatabaseActionsHelperCustom = get_custom_class(
    "AutonomousContainerDatabaseActionsHelperCustom"
)


class ResourceHelper(
    AutonomousContainerDatabaseActionsHelperCustom,
    AutonomousContainerDatabaseActionsHelperGen,
):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec(
        supports_create=False, supports_wait=True
    )
    module_args.update(
        dict(
            compartment_id=dict(type="str"),
            role=dict(
                type="str",
                choices=[
                    "PRIMARY",
                    "STANDBY",
                    "DISABLED_STANDBY",
                    "BACKUP_COPY",
                    "SNAPSHOT_STANDBY",
                ],
            ),
            autonomous_container_database_dataguard_association_id=dict(type="str"),
            connection_strings_type=dict(
                type="str", choices=["SNAPSHOT_SERVICES", "PRIMARY_SERVICES"]
            ),
            autonomous_container_database_id=dict(
                aliases=["id"], type="str", required=True
            ),
            action=dict(
                type="str",
                required=True,
                choices=[
                    "change_compartment",
                    "change_dataguard_role",
                    "restart",
                    "rotate_autonomous_container_database_encryption_key",
                ],
            ),
        )
    )

    module = OCIAnsibleModule(argument_spec=module_args, supports_check_mode=True)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_helper = ResourceHelper(
        module=module,
        resource_type="autonomous_container_database",
        service_client_class=DatabaseClient,
        namespace="database",
    )

    result = resource_helper.perform_action(module.params.get("action"))

    module.exit_json(**result)


if __name__ == "__main__":
    main()
