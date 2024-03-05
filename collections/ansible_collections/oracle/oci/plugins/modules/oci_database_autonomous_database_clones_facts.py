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
module: oci_database_autonomous_database_clones_facts
short_description: Fetches details about one or multiple AutonomousDatabaseClones resources in Oracle Cloud Infrastructure
description:
    - Fetches details about one or multiple AutonomousDatabaseClones resources in Oracle Cloud Infrastructure
    - Lists the Autonomous Database clones for the specified Autonomous Database.
version_added: "2.9.0"
author: Oracle (@oracle)
options:
    compartment_id:
        description:
            - The compartment L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm).
        type: str
        required: true
    autonomous_database_id:
        description:
            - The database L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm).
        type: str
        required: true
    sort_order:
        description:
            - The sort order to use, either ascending (`ASC`) or descending (`DESC`).
        type: str
        choices:
            - "ASC"
            - "DESC"
    display_name:
        description:
            - A filter to return only resources that match the entire display name given. The match is not case sensitive.
        type: str
        aliases: ["name"]
    lifecycle_state:
        description:
            - A filter to return only resources that match the given lifecycle state exactly.
        type: str
        choices:
            - "PROVISIONING"
            - "AVAILABLE"
            - "STOPPING"
            - "STOPPED"
            - "STARTING"
            - "TERMINATING"
            - "TERMINATED"
            - "UNAVAILABLE"
            - "RESTORE_IN_PROGRESS"
            - "RESTORE_FAILED"
            - "BACKUP_IN_PROGRESS"
            - "SCALE_IN_PROGRESS"
            - "AVAILABLE_NEEDS_ATTENTION"
            - "UPDATING"
            - "MAINTENANCE_IN_PROGRESS"
            - "RESTARTING"
            - "RECREATING"
            - "ROLE_CHANGE_IN_PROGRESS"
            - "UPGRADING"
            - "INACCESSIBLE"
            - "STANDBY"
    sort_by:
        description:
            - The field to sort by.  You can provide one sort order (`sortOrder`).  Default order for TIMECREATED is descending.  Default order for DISPLAYNAME
              is ascending. The DISPLAYNAME sort order is case sensitive.
            - "**Note:** If you do not include the availability domain filter, the resources are grouped by availability domain, then sorted."
        type: str
        choices:
            - "NONE"
            - "TIMECREATED"
            - "DISPLAYNAME"
    clone_type:
        description:
            - A filter to return only resources that match the given clone type exactly.
        type: str
        choices:
            - "REFRESHABLE_CLONE"
extends_documentation_fragment: [ oracle.oci.oracle ]
"""

EXAMPLES = """
- name: List autonomous_database_clones
  oci_database_autonomous_database_clones_facts:
    # required
    compartment_id: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
    autonomous_database_id: "ocid1.autonomousdatabase.oc1..xxxxxxEXAMPLExxxxxx"

    # optional
    sort_order: ASC
    display_name: display_name_example
    lifecycle_state: PROVISIONING
    sort_by: NONE
    clone_type: REFRESHABLE_CLONE

"""

RETURN = """
autonomous_database_clones:
    description:
        - List of AutonomousDatabaseClones resources
    returned: on success
    type: complex
    contains:
        id:
            description:
                - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the Autonomous Database.
            returned: on success
            type: str
            sample: "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx"
        compartment_id:
            description:
                - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the compartment.
            returned: on success
            type: str
            sample: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
        lifecycle_state:
            description:
                - The current state of the Autonomous Database.
            returned: on success
            type: str
            sample: PROVISIONING
        lifecycle_details:
            description:
                - Information about the current lifecycle state.
            returned: on success
            type: str
            sample: lifecycle_details_example
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
        kms_key_lifecycle_details:
            description:
                - KMS key lifecycle details.
            returned: on success
            type: str
            sample: kms_key_lifecycle_details_example
        kms_key_version_id:
            description:
                - The OCID of the key container version that is used in database transparent data encryption (TDE) operations KMS Key can have multiple key
                  versions. If none is specified, the current key version (latest) of the Key Id is used for the operation.
            returned: on success
            type: str
            sample: "ocid1.kmskeyversion.oc1..xxxxxxEXAMPLExxxxxx"
        db_name:
            description:
                - The database name.
            returned: on success
            type: str
            sample: db_name_example
        character_set:
            description:
                - "The character set for the autonomous database.  The default is AL32UTF8. Allowed values are:"
                - AL32UTF8, AR8ADOS710, AR8ADOS720, AR8APTEC715, AR8ARABICMACS, AR8ASMO8X, AR8ISO8859P6, AR8MSWIN1256, AR8MUSSAD768, AR8NAFITHA711,
                  AR8NAFITHA721, AR8SAKHR706, AR8SAKHR707, AZ8ISO8859P9E, BG8MSWIN, BG8PC437S, BLT8CP921, BLT8ISO8859P13, BLT8MSWIN1257, BLT8PC775, BN8BSCII,
                  CDN8PC863, CEL8ISO8859P14, CL8ISO8859P5, CL8ISOIR111, CL8KOI8R, CL8KOI8U, CL8MACCYRILLICS, CL8MSWIN1251, EE8ISO8859P2, EE8MACCES,
                  EE8MACCROATIANS, EE8MSWIN1250, EE8PC852, EL8DEC, EL8ISO8859P7, EL8MACGREEKS, EL8MSWIN1253, EL8PC437S, EL8PC851, EL8PC869, ET8MSWIN923,
                  HU8ABMOD, HU8CWI2, IN8ISCII, IS8PC861, IW8ISO8859P8, IW8MACHEBREWS, IW8MSWIN1255, IW8PC1507, JA16EUC, JA16EUCTILDE, JA16SJIS, JA16SJISTILDE,
                  JA16VMS, KO16KSC5601, KO16KSCCS, KO16MSWIN949, LA8ISO6937, LA8PASSPORT, LT8MSWIN921, LT8PC772, LT8PC774, LV8PC1117, LV8PC8LR, LV8RST104090,
                  N8PC865, NE8ISO8859P10, NEE8ISO8859P4, RU8BESTA, RU8PC855, RU8PC866, SE8ISO8859P3, TH8MACTHAIS, TH8TISASCII, TR8DEC, TR8MACTURKISHS,
                  TR8MSWIN1254, TR8PC857, US7ASCII, US8PC437, UTF8, VN8MSWIN1258, VN8VN3, WE8DEC, WE8DG, WE8ISO8859P1, WE8ISO8859P15, WE8ISO8859P9,
                  WE8MACROMAN8S, WE8MSWIN1252, WE8NCR4970, WE8NEXTSTEP, WE8PC850, WE8PC858, WE8PC860, WE8ROMAN8, ZHS16CGB231280, ZHS16GBK, ZHT16BIG5, ZHT16CCDC,
                  ZHT16DBT, ZHT16HKSCS, ZHT16MSWIN950, ZHT32EUC, ZHT32SOPS, ZHT32TRIS
            returned: on success
            type: str
            sample: character_set_example
        ncharacter_set:
            description:
                - "The national character set for the autonomous database.  The default is AL16UTF16. Allowed values are:
                  AL16UTF16 or UTF8."
            returned: on success
            type: str
            sample: ncharacter_set_example
        in_memory_percentage:
            description:
                - The percentage of the System Global Area(SGA) assigned to In-Memory tables in Autonomous Database.
            returned: on success
            type: int
            sample: 56
        in_memory_area_in_gbs:
            description:
                - The area assigned to In-Memory tables in Autonomous Database.
            returned: on success
            type: int
            sample: 56
        next_long_term_backup_time_stamp:
            description:
                - The date and time when the next long-term backup would be created.
            returned: on success
            type: str
            sample: "2013-10-20T19:20:30+01:00"
        long_term_backup_schedule:
            description:
                - ""
            returned: on success
            type: complex
            contains:
                repeat_cadence:
                    description:
                        - The frequency of the long-term backup schedule
                    returned: on success
                    type: str
                    sample: ONE_TIME
                time_of_backup:
                    description:
                        - The timestamp for the long-term backup schedule. For a MONTHLY cadence, months having fewer days than the provided date will have the
                          backup taken on the last day of that month.
                    returned: on success
                    type: str
                    sample: "2013-10-20T19:20:30+01:00"
                retention_period_in_days:
                    description:
                        - Retention period, in days, for long-term backups
                    returned: on success
                    type: int
                    sample: 56
                is_disabled:
                    description:
                        - Indicates if the long-term backup schedule should be deleted. The default value is `FALSE`.
                    returned: on success
                    type: bool
                    sample: true
        is_free_tier:
            description:
                - Indicates if this is an Always Free resource. The default value is false. Note that Always Free Autonomous Databases have 1 CPU and 20GB of
                  memory. For Always Free databases, memory and CPU cannot be scaled.
                - "This cannot be updated in parallel with any of the following: licenseModel, dbEdition, cpuCoreCount, computeCount, computeModel,
                  adminPassword, whitelistedIps, isMTLSConnectionRequired, openMode, permissionLevel, privateEndpointLabel, nsgIds, dbVersion, isRefreshable,
                  dbName, scheduledOperations, dbToolsDetails, or isLocalDataGuardEnabled"
            returned: on success
            type: bool
            sample: true
        system_tags:
            description:
                - System tags for this resource. Each key is predefined and scoped to a namespace.
                  For more information, see L(Resource Tags,https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm).
            returned: on success
            type: dict
            sample: {}
        time_reclamation_of_free_autonomous_database:
            description:
                - The date and time the Always Free database will be stopped because of inactivity. If this time is reached without any database activity, the
                  database will automatically be put into the STOPPED state.
            returned: on success
            type: str
            sample: "2013-10-20T19:20:30+01:00"
        time_deletion_of_free_autonomous_database:
            description:
                - The date and time the Always Free database will be automatically deleted because of inactivity. If the database is in the STOPPED state and
                  without activity until this time, it will be deleted.
            returned: on success
            type: str
            sample: "2013-10-20T19:20:30+01:00"
        backup_config:
            description:
                - ""
            returned: on success
            type: complex
            contains:
                manual_backup_bucket_name:
                    description:
                        - Name of L(Object Storage,https://docs.cloud.oracle.com/Content/Object/Concepts/objectstorageoverview.htm) bucket to use for storing
                          manual backups.
                    returned: on success
                    type: str
                    sample: manual_backup_bucket_name_example
                manual_backup_type:
                    description:
                        - The manual backup destination type.
                    returned: on success
                    type: str
                    sample: NONE
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
        cpu_core_count:
            description:
                - The number of OCPU cores to be made available to the database. When the ECPU is selected, the value for cpuCoreCount is 0. For Autonomous
                  Databases on dedicated Exadata infrastructure, the maximum number of cores is determined by the infrastructure shape. See L(Characteristics of
                  Infrastructure Shapes,https://www.oracle.com/pls/topic/lookup?ctx=en/cloud/paas/autonomous-database&id=ATPFG-
                  GUID-B0F033C1-CC5A-42F0-B2E7-3CECFEDA1FD1) for shape details.
                - "**Note:** This parameter cannot be used with the `ocpuCount` parameter."
            returned: on success
            type: int
            sample: 56
        local_adg_auto_failover_max_data_loss_limit:
            description:
                - Parameter that allows users to select an acceptable maximum data loss limit in seconds, up to which Automatic Failover will be triggered when
                  necessary for a Local Autonomous Data Guard
            returned: on success
            type: int
            sample: 56
        compute_model:
            description:
                - The compute model of the Autonomous Database. This is required if using the `computeCount` parameter. If using `cpuCoreCount` then it is an
                  error to specify `computeModel` to a non-null value.
            returned: on success
            type: str
            sample: ECPU
        compute_count:
            description:
                - The compute amount available to the database. Minimum and maximum values depend on the compute model and whether the database is on Shared or
                  Dedicated infrastructure.
                  For an Autonomous Database on Shared infrastructure, the 'ECPU' compute model requires values in multiples of two. Required when using the
                  `computeModel` parameter. When using `cpuCoreCount` parameter, it is an error to specify computeCount to a non-null value.
            returned: on success
            type: float
            sample: 3.4
        backup_retention_period_in_days:
            description:
                - Retention period, in days, for long-term backups
            returned: on success
            type: int
            sample: 56
        total_backup_storage_size_in_gbs:
            description:
                - The backup storage to the database.
            returned: on success
            type: float
            sample: 1.2
        ocpu_count:
            description:
                - The number of OCPU cores to be made available to the database.
                - "The following points apply:
                  - For Autonomous Databases on dedicated Exadata infrastructure, to provision less than 1 core, enter a fractional value in an increment of
                    0.1. For example, you can provision 0.3 or 0.4 cores, but not 0.35 cores. (Note that fractional OCPU values are not supported for Autonomous
                    Databasese on shared Exadata infrastructure.)
                  - To provision 1 or more cores, you must enter an integer between 1 and the maximum number of cores available for the infrastructure shape.
                    For example, you can provision 2 cores or 3 cores, but not 2.5 cores. This applies to Autonomous Databases on both shared and dedicated
                    Exadata infrastructure."
                - For Autonomous Databases on dedicated Exadata infrastructure, the maximum number of cores is determined by the infrastructure shape. See
                  L(Characteristics of Infrastructure Shapes,https://www.oracle.com/pls/topic/lookup?ctx=en/cloud/paas/autonomous-database&id=ATPFG-
                  GUID-B0F033C1-CC5A-42F0-B2E7-3CECFEDA1FD1) for shape details.
                - "**Note:** This parameter cannot be used with the `cpuCoreCount` parameter."
            returned: on success
            type: float
            sample: 3.4
        provisionable_cpus:
            description:
                - An array of CPU values that an Autonomous Database can be scaled to.
            returned: on success
            type: list
            sample: []
        data_storage_size_in_tbs:
            description:
                - The quantity of data in the database, in terabytes.
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
        data_storage_size_in_gbs:
            description:
                - The quantity of data in the database, in gigabytes.
            returned: on success
            type: int
            sample: 56
        used_data_storage_size_in_gbs:
            description:
                - The storage space consumed by Autonomous Database in GBs.
            returned: on success
            type: int
            sample: 56
        infrastructure_type:
            description:
                - The infrastructure type this resource belongs to.
            returned: on success
            type: str
            sample: CLOUD
        is_dedicated:
            description:
                - True if the database uses L(dedicated Exadata infrastructure,https://docs.oracle.com/en/cloud/paas/autonomous-database/index.html).
            returned: on success
            type: bool
            sample: true
        autonomous_container_database_id:
            description:
                - The Autonomous Container Database L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm).
            returned: on success
            type: str
            sample: "ocid1.autonomouscontainerdatabase.oc1..xxxxxxEXAMPLExxxxxx"
        time_created:
            description:
                - The date and time the Autonomous Database was created.
            returned: on success
            type: str
            sample: "2013-10-20T19:20:30+01:00"
        display_name:
            description:
                - The user-friendly name for the Autonomous Database. The name does not have to be unique.
            returned: on success
            type: str
            sample: display_name_example
        service_console_url:
            description:
                - The URL of the Service Console for the Autonomous Database.
            returned: on success
            type: str
            sample: service_console_url_example
        connection_strings:
            description:
                - The connection string used to connect to the Autonomous Database. The username for the Service Console is ADMIN. Use the password you entered
                  when creating the Autonomous Database for the password value.
            returned: on success
            type: complex
            contains:
                high:
                    description:
                        - The High database service provides the highest level of resources to each SQL statement resulting in the highest performance, but
                          supports the fewest number of concurrent SQL statements.
                    returned: on success
                    type: str
                    sample: high_example
                medium:
                    description:
                        - The Medium database service provides a lower level of resources to each SQL statement potentially resulting a lower level of
                          performance, but supports more concurrent SQL statements.
                    returned: on success
                    type: str
                    sample: medium_example
                low:
                    description:
                        - The Low database service provides the least level of resources to each SQL statement, but supports the most number of concurrent SQL
                          statements.
                    returned: on success
                    type: str
                    sample: low_example
                dedicated:
                    description:
                        - The database service provides the least level of resources to each SQL statement, but supports the most number of concurrent SQL
                          statements.
                    returned: on success
                    type: str
                    sample: dedicated_example
                all_connection_strings:
                    description:
                        - Returns all connection strings that can be used to connect to the Autonomous Database.
                          For more information, please see L(Predefined Database Service Names for Autonomous Transaction
                          Processing,https://docs.oracle.com/en/cloud/paas/atp-cloud/atpug/connect-predefined.html#GUID-9747539B-FD46-44F1-8FF8-F5AC650F15BE)
                    returned: on success
                    type: dict
                    sample: {}
                profiles:
                    description:
                        - A list of connection string profiles to allow clients to group, filter and select connection string values based on structured
                          metadata.
                    returned: on success
                    type: complex
                    contains:
                        display_name:
                            description:
                                - A user-friendly name for the connection.
                            returned: on success
                            type: str
                            sample: display_name_example
                        value:
                            description:
                                - Connection string value.
                            returned: on success
                            type: str
                            sample: value_example
                        consumer_group:
                            description:
                                - Consumer group used by the connection.
                            returned: on success
                            type: str
                            sample: HIGH
                        protocol:
                            description:
                                - Protocol used by the connection.
                            returned: on success
                            type: str
                            sample: TCP
                        tls_authentication:
                            description:
                                - Specifies whether the TLS handshake is using one-way (`SERVER`) or mutual (`MUTUAL`) authentication.
                            returned: on success
                            type: str
                            sample: SERVER
                        host_format:
                            description:
                                - Host format used in connection string.
                            returned: on success
                            type: str
                            sample: FQDN
                        session_mode:
                            description:
                                - Specifies whether the listener performs a direct hand-off of the session, or redirects the session. In RAC deployments where
                                  SCAN is used, sessions are redirected to a Node VIP. Use `DIRECT` for direct hand-offs. Use `REDIRECT` to redirect the
                                  session.
                            returned: on success
                            type: str
                            sample: DIRECT
                        syntax_format:
                            description:
                                - Specifies whether the connection string is using the long (`LONG`), Easy Connect (`EZCONNECT`), or Easy Connect Plus
                                  (`EZCONNECTPLUS`) format.
                                  Autonomous Databases on shared Exadata infrastructure always use the long format.
                            returned: on success
                            type: str
                            sample: LONG
        connection_urls:
            description:
                - ""
            returned: on success
            type: complex
            contains:
                sql_dev_web_url:
                    description:
                        - Oracle SQL Developer Web URL.
                    returned: on success
                    type: str
                    sample: sql_dev_web_url_example
                apex_url:
                    description:
                        - Oracle Application Express (APEX) URL.
                    returned: on success
                    type: str
                    sample: apex_url_example
                machine_learning_user_management_url:
                    description:
                        - Oracle Machine Learning user management URL.
                    returned: on success
                    type: str
                    sample: machine_learning_user_management_url_example
                graph_studio_url:
                    description:
                        - The URL of the Graph Studio for the Autonomous Database.
                    returned: on success
                    type: str
                    sample: graph_studio_url_example
                mongo_db_url:
                    description:
                        - The URL of the MongoDB API for the Autonomous Database.
                    returned: on success
                    type: str
                    sample: mongo_db_url_example
                machine_learning_notebook_url:
                    description:
                        - The URL of the Oracle Machine Learning (OML) Notebook for the Autonomous Database.
                    returned: on success
                    type: str
                    sample: machine_learning_notebook_url_example
                ords_url:
                    description:
                        - The Oracle REST Data Services (ORDS) URL of the Web Access for the Autonomous Database.
                    returned: on success
                    type: str
                    sample: ords_url_example
                database_transforms_url:
                    description:
                        - The URL of the Database Transforms for the Autonomous Database.
                    returned: on success
                    type: str
                    sample: database_transforms_url_example
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
        used_data_storage_size_in_tbs:
            description:
                - The amount of storage that has been used, in terabytes.
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
        subnet_id:
            description:
                - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the subnet the resource is associated with.
                - "**Subnet Restrictions:**
                  - For bare metal DB systems and for single node virtual machine DB systems, do not use a subnet that overlaps with 192.168.16.16/28.
                  - For Exadata and virtual machine 2-node RAC systems, do not use a subnet that overlaps with 192.168.128.0/20.
                  - For Autonomous Database, setting this will disable public secure access to the database."
                - These subnets are used by the Oracle Clusterware private interconnect on the database instance.
                  Specifying an overlapping subnet will cause the private interconnect to malfunction.
                  This restriction applies to both the client subnet and the backup subnet.
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
        private_endpoint:
            description:
                - The private endpoint for the resource.
            returned: on success
            type: str
            sample: private_endpoint_example
        private_endpoint_label:
            description:
                - The resource's private endpoint label. Setting this to an empty string, after the creation of the private endpoint database, changes the
                  private endpoint database to a public endpoint database.
                - "This setting cannot be updated in parallel with any of the following: licenseModel, dbEdition, cpuCoreCount, computeCount, computeModel,
                  adminPassword, whitelistedIps, isMTLSConnectionRequired, dbWorkload, dbVersion, isRefreshable, dbName, scheduledOperations, dbToolsDetails, or
                  isFreeTier."
            returned: on success
            type: str
            sample: private_endpoint_label_example
        private_endpoint_ip:
            description:
                - The private endpoint Ip address for the resource.
            returned: on success
            type: str
            sample: private_endpoint_ip_example
        db_version:
            description:
                - A valid Oracle Database version for Autonomous Database.
            returned: on success
            type: str
            sample: db_version_example
        is_preview:
            description:
                - Indicates if the Autonomous Database version is a preview version.
            returned: on success
            type: bool
            sample: true
        db_workload:
            description:
                - "The Autonomous Database workload type. The following values are valid:"
                - "- OLTP - indicates an Autonomous Transaction Processing database
                  - DW - indicates an Autonomous Data Warehouse database
                  - AJD - indicates an Autonomous JSON Database
                  - APEX - indicates an Autonomous Database with the Oracle APEX Application Development workload type."
                - "This cannot be updated in parallel with any of the following: licenseModel, dbEdition, cpuCoreCount, computeCount, computeModel,
                  adminPassword, whitelistedIps, isMTLSConnectionRequired, privateEndpointLabel, nsgIds, dbVersion, isRefreshable, dbName, scheduledOperations,
                  dbToolsDetails, isLocalDataGuardEnabled, or isFreeTier."
            returned: on success
            type: str
            sample: OLTP
        is_access_control_enabled:
            description:
                - Indicates if the database-level access control is enabled.
                  If disabled, database access is defined by the network security rules.
                  If enabled, database access is restricted to the IP addresses defined by the rules specified with the `whitelistedIps` property. While
                  specifying `whitelistedIps` rules is optional,
                   if database-level access control is enabled and no rules are specified, the database will become inaccessible. The rules can be added later
                   using the `UpdateAutonomousDatabase` API operation or edit option in console.
                  When creating a database clone, the desired access control setting should be specified. By default, database-level access control will be
                  disabled for the clone.
                - This property is applicable only to Autonomous Databases on the Exadata Cloud@Customer platform.
            returned: on success
            type: bool
            sample: true
        whitelisted_ips:
            description:
                - The client IP access control list (ACL). This feature is available for autonomous databases on L(shared Exadata
                  infrastructure,https://docs.oracle.com/en/cloud/paas/autonomous-database/index.html) and on Exadata Cloud@Customer.
                  Only clients connecting from an IP address included in the ACL may access the Autonomous Database instance.
                - "For shared Exadata infrastructure, this is an array of CIDR (Classless Inter-Domain Routing) notations for a subnet or VCN OCID.
                  Use a semicolon (;) as a deliminator between the VCN-specific subnets or IPs.
                  Example: `[\\"1.1.1.1\\",\\"1.1.1.0/24\\",\\"ocid1.vcn.oc1.sea.<unique_id>\\",\\"ocid1.vcn.oc1.sea.<unique_id1>;1.1.1.1\\",\\"ocid1.vcn.oc1.se
                  a.<unique_id2>;1.1.0.0/16\\"]`
                  For Exadata Cloud@Customer, this is an array of IP addresses or CIDR (Classless Inter-Domain Routing) notations.
                  Example: `[\\"1.1.1.1\\",\\"1.1.1.0/24\\",\\"1.1.2.25\\"]`"
                - For an update operation, if you want to delete all the IPs in the ACL, use an array with a single empty string entry.
                - "This cannot be updated in parallel with any of the following: licenseModel, dbEdition, cpuCoreCount, computeCount, computeModel,
                  adminPassword, isMTLSConnectionRequired, openMode, permissionLevel, dbWorkload, dbVersion, isRefreshable, dbName, scheduledOperations,
                  dbToolsDetails, isLocalDataGuardEnabled, or isFreeTier."
            returned: on success
            type: list
            sample: []
        are_primary_whitelisted_ips_used:
            description:
                - This field will be null if the Autonomous Database is not Data Guard enabled or Access Control is disabled.
                  It's value would be `TRUE` if Autonomous Database is Data Guard enabled and Access Control is enabled and if the Autonomous Database uses
                  primary IP access control list (ACL) for standby.
                  It's value would be `FALSE` if Autonomous Database is Data Guard enabled and Access Control is enabled and if the Autonomous Database uses
                  different IP access control list (ACL) for standby compared to primary.
            returned: on success
            type: bool
            sample: true
        standby_whitelisted_ips:
            description:
                - The client IP access control list (ACL). This feature is available for autonomous databases on L(shared Exadata
                  infrastructure,https://docs.oracle.com/en/cloud/paas/autonomous-database/index.html) and on Exadata Cloud@Customer.
                  Only clients connecting from an IP address included in the ACL may access the Autonomous Database instance.
                - "For shared Exadata infrastructure, this is an array of CIDR (Classless Inter-Domain Routing) notations for a subnet or VCN OCID.
                  Use a semicolon (;) as a deliminator between the VCN-specific subnets or IPs.
                  Example: `[\\"1.1.1.1\\",\\"1.1.1.0/24\\",\\"ocid1.vcn.oc1.sea.<unique_id>\\",\\"ocid1.vcn.oc1.sea.<unique_id1>;1.1.1.1\\",\\"ocid1.vcn.oc1.se
                  a.<unique_id2>;1.1.0.0/16\\"]`
                  For Exadata Cloud@Customer, this is an array of IP addresses or CIDR (Classless Inter-Domain Routing) notations.
                  Example: `[\\"1.1.1.1\\",\\"1.1.1.0/24\\",\\"1.1.2.25\\"]`"
                - For an update operation, if you want to delete all the IPs in the ACL, use an array with a single empty string entry.
                - "This cannot be updated in parallel with any of the following: licenseModel, dbEdition, cpuCoreCount, computeCount, computeModel,
                  adminPassword, isMTLSConnectionRequired, openMode, permissionLevel, dbWorkload, dbVersion, isRefreshable, dbName, scheduledOperations,
                  dbToolsDetails, isLocalDataGuardEnabled, or isFreeTier."
            returned: on success
            type: list
            sample: []
        apex_details:
            description:
                - Information about Oracle APEX Application Development.
            returned: on success
            type: complex
            contains:
                apex_version:
                    description:
                        - The Oracle APEX Application Development version.
                    returned: on success
                    type: str
                    sample: apex_version_example
                ords_version:
                    description:
                        - The Oracle REST Data Services (ORDS) version.
                    returned: on success
                    type: str
                    sample: ords_version_example
        is_auto_scaling_enabled:
            description:
                - Indicates if auto scaling is enabled for the Autonomous Database CPU core count.
            returned: on success
            type: bool
            sample: true
        data_safe_status:
            description:
                - Status of the Data Safe registration for this Autonomous Database.
            returned: on success
            type: str
            sample: REGISTERING
        operations_insights_status:
            description:
                - Status of Operations Insights for this Autonomous Database.
            returned: on success
            type: str
            sample: ENABLING
        database_management_status:
            description:
                - Status of Database Management for this Autonomous Database.
            returned: on success
            type: str
            sample: ENABLING
        time_maintenance_begin:
            description:
                - The date and time when maintenance will begin.
            returned: on success
            type: str
            sample: "2013-10-20T19:20:30+01:00"
        time_maintenance_end:
            description:
                - The date and time when maintenance will end.
            returned: on success
            type: str
            sample: "2013-10-20T19:20:30+01:00"
        is_refreshable_clone:
            description:
                - Indicates if the Autonomous Database is a refreshable clone.
                - "This cannot be updated in parallel with any of the following: cpuCoreCount, computeCount, computeModel, adminPassword, whitelistedIps,
                  openMode, permissionLevel, dbWorkload, privateEndpointLabel, nsgIds, dbVersion, dbName, scheduledOperations, dbToolsDetails,
                  isLocalDataGuardEnabled, or isFreeTier."
            returned: on success
            type: bool
            sample: true
        time_of_last_refresh:
            description:
                - The date and time when last refresh happened.
            returned: on success
            type: str
            sample: "2013-10-20T19:20:30+01:00"
        time_of_last_refresh_point:
            description:
                - The refresh point timestamp (UTC). The refresh point is the time to which the database was most recently refreshed. Data created after the
                  refresh point is not included in the refresh.
            returned: on success
            type: str
            sample: "2013-10-20T19:20:30+01:00"
        time_of_next_refresh:
            description:
                - The date and time of next refresh.
            returned: on success
            type: str
            sample: "2013-10-20T19:20:30+01:00"
        open_mode:
            description:
                - Indicates the Autonomous Database mode. The database can be opened in `READ_ONLY` or `READ_WRITE` mode.
                - "This cannot be updated in parallel with any of the following: cpuCoreCount, computeCount, computeModel, adminPassword, whitelistedIps,
                  isMTLSConnectionRequired, dbVersion, isRefreshable, dbName, scheduledOperations, dbToolsDetails, or isFreeTier."
            returned: on success
            type: str
            sample: READ_ONLY
        refreshable_status:
            description:
                - The refresh status of the clone. REFRESHING indicates that the clone is currently being refreshed with data from the source Autonomous
                  Database.
            returned: on success
            type: str
            sample: REFRESHING
        refreshable_mode:
            description:
                - The refresh mode of the clone. AUTOMATIC indicates that the clone is automatically being refreshed with data from the source Autonomous
                  Database.
            returned: on success
            type: str
            sample: AUTOMATIC
        source_id:
            description:
                - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the source Autonomous Database that was cloned to create
                  the current Autonomous Database.
            returned: on success
            type: str
            sample: "ocid1.source.oc1..xxxxxxEXAMPLExxxxxx"
        permission_level:
            description:
                - The Autonomous Database permission level. Restricted mode allows access only by admin users.
                - "This cannot be updated in parallel with any of the following: cpuCoreCount, computeCount, computeModel, adminPassword, whitelistedIps,
                  isMTLSConnectionRequired, nsgIds, dbVersion, isRefreshable, dbName, scheduledOperations, dbToolsDetails, or isFreeTier."
            returned: on success
            type: str
            sample: RESTRICTED
        time_of_last_switchover:
            description:
                - The timestamp of the last switchover operation for the Autonomous Database.
            returned: on success
            type: str
            sample: "2013-10-20T19:20:30+01:00"
        time_of_last_failover:
            description:
                - The timestamp of the last failover operation.
            returned: on success
            type: str
            sample: "2013-10-20T19:20:30+01:00"
        is_data_guard_enabled:
            description:
                - "**Deprecated.** Indicates whether the Autonomous Database has local (in-region) Data Guard enabled. Not applicable to cross-region Autonomous
                  Data Guard associations, or to Autonomous Databases using dedicated Exadata infrastructure or Exadata Cloud@Customer infrastructure."
            returned: on success
            type: bool
            sample: true
        failed_data_recovery_in_seconds:
            description:
                - Indicates the number of seconds of data loss for a Data Guard failover.
            returned: on success
            type: int
            sample: 56
        standby_db:
            description:
                - "**Deprecated** Autonomous Data Guard standby database details."
            returned: on success
            type: complex
            contains:
                lag_time_in_seconds:
                    description:
                        - The amount of time, in seconds, that the data of the standby database lags the data of the primary database. Can be used to determine
                          the potential data loss in the event of a failover.
                    returned: on success
                    type: int
                    sample: 56
                lifecycle_state:
                    description:
                        - The current state of the Autonomous Database.
                    returned: on success
                    type: str
                    sample: PROVISIONING
                lifecycle_details:
                    description:
                        - Additional information about the current lifecycle state.
                    returned: on success
                    type: str
                    sample: lifecycle_details_example
                time_data_guard_role_changed:
                    description:
                        - The date and time the Autonomous Data Guard role was switched for the standby Autonomous Database.
                    returned: on success
                    type: str
                    sample: "2013-10-20T19:20:30+01:00"
                time_disaster_recovery_role_changed:
                    description:
                        - The date and time the Disaster Recovery role was switched for the standby Autonomous Database.
                    returned: on success
                    type: str
                    sample: "2013-10-20T19:20:30+01:00"
        is_local_data_guard_enabled:
            description:
                - Indicates whether the Autonomous Database has local (in-region) Data Guard enabled. Not applicable to cross-region Autonomous Data Guard
                  associations, or to Autonomous Databases using dedicated Exadata infrastructure or Exadata Cloud@Customer infrastructure.
            returned: on success
            type: bool
            sample: true
        is_remote_data_guard_enabled:
            description:
                - Indicates whether the Autonomous Database has Cross Region Data Guard enabled. Not applicable to Autonomous Databases using dedicated Exadata
                  infrastructure or Exadata Cloud@Customer infrastructure.
            returned: on success
            type: bool
            sample: true
        local_standby_db:
            description:
                - ""
            returned: on success
            type: complex
            contains:
                lag_time_in_seconds:
                    description:
                        - The amount of time, in seconds, that the data of the standby database lags the data of the primary database. Can be used to determine
                          the potential data loss in the event of a failover.
                    returned: on success
                    type: int
                    sample: 56
                lifecycle_state:
                    description:
                        - The current state of the Autonomous Database.
                    returned: on success
                    type: str
                    sample: PROVISIONING
                lifecycle_details:
                    description:
                        - Additional information about the current lifecycle state.
                    returned: on success
                    type: str
                    sample: lifecycle_details_example
                time_data_guard_role_changed:
                    description:
                        - The date and time the Autonomous Data Guard role was switched for the standby Autonomous Database.
                    returned: on success
                    type: str
                    sample: "2013-10-20T19:20:30+01:00"
                time_disaster_recovery_role_changed:
                    description:
                        - The date and time the Disaster Recovery role was switched for the standby Autonomous Database.
                    returned: on success
                    type: str
                    sample: "2013-10-20T19:20:30+01:00"
        role:
            description:
                - The Data Guard role of the Autonomous Container Database or Autonomous Database, if Autonomous Data Guard is enabled.
            returned: on success
            type: str
            sample: PRIMARY
        available_upgrade_versions:
            description:
                - List of Oracle Database versions available for a database upgrade. If there are no version upgrades available, this list is empty.
            returned: on success
            type: list
            sample: []
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
        supported_regions_to_clone_to:
            description:
                - The list of regions that support the creation of an Autonomous Database clone or an Autonomous Data Guard standby database.
            returned: on success
            type: list
            sample: []
        customer_contacts:
            description:
                - Customer Contacts.
            returned: on success
            type: complex
            contains:
                email:
                    description:
                        - The email address used by Oracle to send notifications regarding databases and infrastructure.
                    returned: on success
                    type: str
                    sample: email_example
        time_local_data_guard_enabled:
            description:
                - The date and time that Autonomous Data Guard was enabled for an Autonomous Database where the standby was provisioned in the same region as
                  the primary database.
            returned: on success
            type: str
            sample: "2013-10-20T19:20:30+01:00"
        dataguard_region_type:
            description:
                - "The Autonomous Data Guard region type of the Autonomous Database. For Autonomous Databases on shared Exadata infrastructure, Data Guard
                  associations have designated primary and standby regions, and these region types do not change when the database changes roles. The standby
                  regions in Data Guard associations can be the same region designated as the primary region, or they can be remote regions. Certain database
                  administrative operations may be available only in the primary region of the Data Guard association, and cannot be performed when the database
                  using the \\"primary\\" role is operating in a remote Data Guard standby region."
            returned: on success
            type: str
            sample: PRIMARY_DG_REGION
        time_data_guard_role_changed:
            description:
                - "The date and time the Autonomous Data Guard role was switched for the Autonomous Database. For databases that have standbys in both the
                  primary Data Guard region and a remote Data Guard standby region, this is the latest timestamp of either the database using the \\"primary\\"
                  role in the primary Data Guard region, or database located in the remote Data Guard standby region."
            returned: on success
            type: str
            sample: "2013-10-20T19:20:30+01:00"
        peer_db_ids:
            description:
                - The list of L(OCIDs,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of standby databases located in Autonomous Data
                  Guard remote regions that are associated with the source database. Note that for shared Exadata infrastructure, standby databases located in
                  the same region as the source primary database do not have OCIDs.
            returned: on success
            type: list
            sample: []
        is_mtls_connection_required:
            description:
                - Specifies if the Autonomous Database requires mTLS connections.
                - "This may not be updated in parallel with any of the following: licenseModel, databaseEdition, cpuCoreCount, computeCount, maxCpuCoreCount,
                  dataStorageSizeInTBs, whitelistedIps, openMode, permissionLevel, db-workload, privateEndpointLabel, nsgIds, customerContacts, dbVersion,
                  scheduledOperations, dbToolsDetails, isLocalDataGuardEnabled, or isFreeTier."
                - "Service Change: The default value of the isMTLSConnectionRequired attribute will change from true to false on July 1, 2023 in the following
                  APIs:
                  - CreateAutonomousDatabase
                  - GetAutonomousDatabase
                  - UpdateAutonomousDatabase
                  Details: Prior to the July 1, 2023 change, the isMTLSConnectionRequired attribute default value was true. This applies to Autonomous Databases
                  on shared Exadata infrastructure.
                  Does this impact me? If you use or maintain custom scripts or Terraform scripts referencing the CreateAutonomousDatabase,
                  GetAutonomousDatabase, or UpdateAutonomousDatabase APIs, you want to check, and possibly modify, the scripts for the changed default value of
                  the attribute. Should you choose not to leave your scripts unchanged, the API calls containing this attribute will continue to work, but the
                  default value will switch from true to false.
                  How do I make this change? Using either OCI SDKs or command line tools, update your custom scripts to explicitly set the
                  isMTLSConnectionRequired attribute to true."
            returned: on success
            type: bool
            sample: true
        time_of_joining_resource_pool:
            description:
                - The time the member joined the resource pool.
            returned: on success
            type: str
            sample: "2013-10-20T19:20:30+01:00"
        resource_pool_leader_id:
            description:
                - The unique identifier for leader autonomous database OCID L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm).
            returned: on success
            type: str
            sample: "ocid1.resourcepoolleader.oc1..xxxxxxEXAMPLExxxxxx"
        resource_pool_summary:
            description:
                - ""
            returned: on success
            type: complex
            contains:
                pool_size:
                    description:
                        - Resource pool size.
                    returned: on success
                    type: int
                    sample: 56
        is_reconnect_clone_enabled:
            description:
                - Indicates if the refreshable clone can be reconnected to its source database.
            returned: on success
            type: bool
            sample: true
        time_until_reconnect_clone_enabled:
            description:
                - The time and date as an RFC3339 formatted string, e.g., 2022-01-01T12:00:00.000Z, to set the limit for a refreshable clone to be reconnected
                  to its source database.
            returned: on success
            type: str
            sample: "2013-10-20T19:20:30+01:00"
        autonomous_maintenance_schedule_type:
            description:
                - The maintenance schedule type of the Autonomous Database on shared Exadata infrastructure. The EARLY maintenance schedule of this Autonomous
                  Database
                  follows a schedule that applies patches prior to the REGULAR schedule.The REGULAR maintenance schedule of this Autonomous Database follows the
                  normal cycle.
            returned: on success
            type: str
            sample: EARLY
        scheduled_operations:
            description:
                - The list of scheduled operations.
                - "This cannot be updated in parallel with any of the following: licenseModel, dbEdition, cpuCoreCount, computeCount, computeModel,
                  whitelistedIps, isMTLSConnectionRequired, openMode, permissionLevel, dbWorkload, privateEndpointLabel, nsgIds, dbVersion, isRefreshable,
                  dbName, dbToolsDetails, isLocalDataGuardEnabled, or isFreeTier."
            returned: on success
            type: complex
            contains:
                day_of_week:
                    description:
                        - ""
                    returned: on success
                    type: complex
                    contains:
                        name:
                            description:
                                - Name of the day of the week.
                            returned: on success
                            type: str
                            sample: MONDAY
                scheduled_start_time:
                    description:
                        - "auto start time. value must be of ISO-8601 format \\"HH:mm\\""
                    returned: on success
                    type: str
                    sample: scheduled_start_time_example
                scheduled_stop_time:
                    description:
                        - "auto stop time. value must be of ISO-8601 format \\"HH:mm\\""
                    returned: on success
                    type: str
                    sample: scheduled_stop_time_example
        is_auto_scaling_for_storage_enabled:
            description:
                - Indicates if auto scaling is enabled for the Autonomous Database storage. The default value is `FALSE`.
            returned: on success
            type: bool
            sample: true
        allocated_storage_size_in_tbs:
            description:
                - The amount of storage currently allocated for the database tables and billed for, rounded up. When auto-scaling is not enabled, this value is
                  equal to the `dataStorageSizeInTBs` value. You can compare this value to the `actualUsedDataStorageSizeInTBs` value to determine if a manual
                  shrink operation is appropriate for your allocated storage.
                - "**Note:** Auto-scaling does not automatically decrease allocated storage when data is deleted from the database."
            returned: on success
            type: float
            sample: 1.2
        actual_used_data_storage_size_in_tbs:
            description:
                - The current amount of storage in use for user and system data, in terabytes (TB).
            returned: on success
            type: float
            sample: 1.2
        max_cpu_core_count:
            description:
                - The number of Max OCPU cores to be made available to the autonomous database with auto scaling of cpu enabled.
            returned: on success
            type: int
            sample: 56
        database_edition:
            description:
                - The Oracle Database Edition that applies to the Autonomous databases.
            returned: on success
            type: str
            sample: STANDARD_EDITION
        db_tools_details:
            description:
                - The list of database tools details.
                - "This cannot be updated in parallel with any of the following: licenseModel, dbEdition, cpuCoreCount, computeCount, computeModel,
                  whitelistedIps, isMTLSConnectionRequired, openMode, permissionLevel, dbWorkload, privateEndpointLabel, nsgIds, dbVersion, isRefreshable,
                  dbName, scheduledOperations, isLocalDataGuardEnabled, or isFreeTier."
            returned: on success
            type: complex
            contains:
                name:
                    description:
                        - Name of database tool.
                    returned: on success
                    type: str
                    sample: APEX
                is_enabled:
                    description:
                        - Indicates whether tool is enabled.
                    returned: on success
                    type: bool
                    sample: true
                compute_count:
                    description:
                        - Compute used by database tools.
                    returned: on success
                    type: float
                    sample: 3.4
                max_idle_time_in_minutes:
                    description:
                        - The max idle time, in minutes, after which the VM used by database tools will be terminated.
                    returned: on success
                    type: int
                    sample: 56
        local_disaster_recovery_type:
            description:
                - Indicates the local disaster recovery (DR) type of the Shared Autonomous Database.
                  Autonomous Data Guard (ADG) DR type provides business critical DR with a faster recovery time objective (RTO) during failover or switchover.
                  Backup-based DR type provides lower cost DR with a slower RTO during failover or switchover.
            returned: on success
            type: str
            sample: local_disaster_recovery_type_example
        disaster_recovery_region_type:
            description:
                - The disaster recovery (DR) region type of the Autonomous Database. For Shared Autonomous Databases, DR associations have designated primary
                  and standby regions. These region types do not change when the database changes roles. The standby region in DR associations can be the same
                  region as the primary region, or they can be in a remote regions. Some database administration operations may be available only in the primary
                  region of the DR association, and cannot be performed when the database using the primary role is operating in a remote region.
            returned: on success
            type: str
            sample: PRIMARY
        time_disaster_recovery_role_changed:
            description:
                - The date and time the Disaster Recovery role was switched for the standby Autonomous Database.
            returned: on success
            type: str
            sample: "2013-10-20T19:20:30+01:00"
        remote_disaster_recovery_configuration:
            description:
                - ""
            returned: on success
            type: complex
            contains:
                disaster_recovery_type:
                    description:
                        - Indicates the disaster recovery (DR) type of the Shared Autonomous Database.
                          Autonomous Data Guard (ADG) DR type provides business critical DR with a faster recovery time objective (RTO) during failover or
                          switchover.
                          Backup-based DR type provides lower cost DR with a slower RTO during failover or switchover.
                    returned: on success
                    type: str
                    sample: ADG
                time_snapshot_standby_enabled_till:
                    description:
                        - Time and date stored as an RFC 3339 formatted timestamp string. For example, 2022-01-01T12:00:00.000Z would set a limit for the
                          snapshot standby to be converted back to a cross-region standby database.
                    returned: on success
                    type: str
                    sample: "2013-10-20T19:20:30+01:00"
                is_snapshot_standby:
                    description:
                        - Indicates if user wants to convert to a snapshot standby. For example, true would set a standby database to snapshot standby database.
                          False would set a snapshot standby database back to regular standby database.
                    returned: on success
                    type: bool
                    sample: true
    sample: [{
        "id": "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx",
        "compartment_id": "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx",
        "lifecycle_state": "PROVISIONING",
        "lifecycle_details": "lifecycle_details_example",
        "kms_key_id": "ocid1.kmskey.oc1..xxxxxxEXAMPLExxxxxx",
        "vault_id": "ocid1.vault.oc1..xxxxxxEXAMPLExxxxxx",
        "kms_key_lifecycle_details": "kms_key_lifecycle_details_example",
        "kms_key_version_id": "ocid1.kmskeyversion.oc1..xxxxxxEXAMPLExxxxxx",
        "db_name": "db_name_example",
        "character_set": "character_set_example",
        "ncharacter_set": "ncharacter_set_example",
        "in_memory_percentage": 56,
        "in_memory_area_in_gbs": 56,
        "next_long_term_backup_time_stamp": "2013-10-20T19:20:30+01:00",
        "long_term_backup_schedule": {
            "repeat_cadence": "ONE_TIME",
            "time_of_backup": "2013-10-20T19:20:30+01:00",
            "retention_period_in_days": 56,
            "is_disabled": true
        },
        "is_free_tier": true,
        "system_tags": {},
        "time_reclamation_of_free_autonomous_database": "2013-10-20T19:20:30+01:00",
        "time_deletion_of_free_autonomous_database": "2013-10-20T19:20:30+01:00",
        "backup_config": {
            "manual_backup_bucket_name": "manual_backup_bucket_name_example",
            "manual_backup_type": "NONE"
        },
        "key_history_entry": [{
            "id": "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx",
            "kms_key_version_id": "ocid1.kmskeyversion.oc1..xxxxxxEXAMPLExxxxxx",
            "vault_id": "ocid1.vault.oc1..xxxxxxEXAMPLExxxxxx",
            "time_activated": "2013-10-20T19:20:30+01:00"
        }],
        "cpu_core_count": 56,
        "local_adg_auto_failover_max_data_loss_limit": 56,
        "compute_model": "ECPU",
        "compute_count": 3.4,
        "backup_retention_period_in_days": 56,
        "total_backup_storage_size_in_gbs": 1.2,
        "ocpu_count": 3.4,
        "provisionable_cpus": [],
        "data_storage_size_in_tbs": 56,
        "memory_per_oracle_compute_unit_in_gbs": 56,
        "data_storage_size_in_gbs": 56,
        "used_data_storage_size_in_gbs": 56,
        "infrastructure_type": "CLOUD",
        "is_dedicated": true,
        "autonomous_container_database_id": "ocid1.autonomouscontainerdatabase.oc1..xxxxxxEXAMPLExxxxxx",
        "time_created": "2013-10-20T19:20:30+01:00",
        "display_name": "display_name_example",
        "service_console_url": "service_console_url_example",
        "connection_strings": {
            "high": "high_example",
            "medium": "medium_example",
            "low": "low_example",
            "dedicated": "dedicated_example",
            "all_connection_strings": {},
            "profiles": [{
                "display_name": "display_name_example",
                "value": "value_example",
                "consumer_group": "HIGH",
                "protocol": "TCP",
                "tls_authentication": "SERVER",
                "host_format": "FQDN",
                "session_mode": "DIRECT",
                "syntax_format": "LONG"
            }]
        },
        "connection_urls": {
            "sql_dev_web_url": "sql_dev_web_url_example",
            "apex_url": "apex_url_example",
            "machine_learning_user_management_url": "machine_learning_user_management_url_example",
            "graph_studio_url": "graph_studio_url_example",
            "mongo_db_url": "mongo_db_url_example",
            "machine_learning_notebook_url": "machine_learning_notebook_url_example",
            "ords_url": "ords_url_example",
            "database_transforms_url": "database_transforms_url_example"
        },
        "license_model": "LICENSE_INCLUDED",
        "used_data_storage_size_in_tbs": 56,
        "freeform_tags": {'Department': 'Finance'},
        "defined_tags": {'Operations': {'CostCenter': 'US'}},
        "subnet_id": "ocid1.subnet.oc1..xxxxxxEXAMPLExxxxxx",
        "nsg_ids": [],
        "private_endpoint": "private_endpoint_example",
        "private_endpoint_label": "private_endpoint_label_example",
        "private_endpoint_ip": "private_endpoint_ip_example",
        "db_version": "db_version_example",
        "is_preview": true,
        "db_workload": "OLTP",
        "is_access_control_enabled": true,
        "whitelisted_ips": [],
        "are_primary_whitelisted_ips_used": true,
        "standby_whitelisted_ips": [],
        "apex_details": {
            "apex_version": "apex_version_example",
            "ords_version": "ords_version_example"
        },
        "is_auto_scaling_enabled": true,
        "data_safe_status": "REGISTERING",
        "operations_insights_status": "ENABLING",
        "database_management_status": "ENABLING",
        "time_maintenance_begin": "2013-10-20T19:20:30+01:00",
        "time_maintenance_end": "2013-10-20T19:20:30+01:00",
        "is_refreshable_clone": true,
        "time_of_last_refresh": "2013-10-20T19:20:30+01:00",
        "time_of_last_refresh_point": "2013-10-20T19:20:30+01:00",
        "time_of_next_refresh": "2013-10-20T19:20:30+01:00",
        "open_mode": "READ_ONLY",
        "refreshable_status": "REFRESHING",
        "refreshable_mode": "AUTOMATIC",
        "source_id": "ocid1.source.oc1..xxxxxxEXAMPLExxxxxx",
        "permission_level": "RESTRICTED",
        "time_of_last_switchover": "2013-10-20T19:20:30+01:00",
        "time_of_last_failover": "2013-10-20T19:20:30+01:00",
        "is_data_guard_enabled": true,
        "failed_data_recovery_in_seconds": 56,
        "standby_db": {
            "lag_time_in_seconds": 56,
            "lifecycle_state": "PROVISIONING",
            "lifecycle_details": "lifecycle_details_example",
            "time_data_guard_role_changed": "2013-10-20T19:20:30+01:00",
            "time_disaster_recovery_role_changed": "2013-10-20T19:20:30+01:00"
        },
        "is_local_data_guard_enabled": true,
        "is_remote_data_guard_enabled": true,
        "local_standby_db": {
            "lag_time_in_seconds": 56,
            "lifecycle_state": "PROVISIONING",
            "lifecycle_details": "lifecycle_details_example",
            "time_data_guard_role_changed": "2013-10-20T19:20:30+01:00",
            "time_disaster_recovery_role_changed": "2013-10-20T19:20:30+01:00"
        },
        "role": "PRIMARY",
        "available_upgrade_versions": [],
        "key_store_id": "ocid1.keystore.oc1..xxxxxxEXAMPLExxxxxx",
        "key_store_wallet_name": "key_store_wallet_name_example",
        "supported_regions_to_clone_to": [],
        "customer_contacts": [{
            "email": "email_example"
        }],
        "time_local_data_guard_enabled": "2013-10-20T19:20:30+01:00",
        "dataguard_region_type": "PRIMARY_DG_REGION",
        "time_data_guard_role_changed": "2013-10-20T19:20:30+01:00",
        "peer_db_ids": [],
        "is_mtls_connection_required": true,
        "time_of_joining_resource_pool": "2013-10-20T19:20:30+01:00",
        "resource_pool_leader_id": "ocid1.resourcepoolleader.oc1..xxxxxxEXAMPLExxxxxx",
        "resource_pool_summary": {
            "pool_size": 56
        },
        "is_reconnect_clone_enabled": true,
        "time_until_reconnect_clone_enabled": "2013-10-20T19:20:30+01:00",
        "autonomous_maintenance_schedule_type": "EARLY",
        "scheduled_operations": [{
            "day_of_week": {
                "name": "MONDAY"
            },
            "scheduled_start_time": "scheduled_start_time_example",
            "scheduled_stop_time": "scheduled_stop_time_example"
        }],
        "is_auto_scaling_for_storage_enabled": true,
        "allocated_storage_size_in_tbs": 1.2,
        "actual_used_data_storage_size_in_tbs": 1.2,
        "max_cpu_core_count": 56,
        "database_edition": "STANDARD_EDITION",
        "db_tools_details": [{
            "name": "APEX",
            "is_enabled": true,
            "compute_count": 3.4,
            "max_idle_time_in_minutes": 56
        }],
        "local_disaster_recovery_type": "local_disaster_recovery_type_example",
        "disaster_recovery_region_type": "PRIMARY",
        "time_disaster_recovery_role_changed": "2013-10-20T19:20:30+01:00",
        "remote_disaster_recovery_configuration": {
            "disaster_recovery_type": "ADG",
            "time_snapshot_standby_enabled_till": "2013-10-20T19:20:30+01:00",
            "is_snapshot_standby": true
        }
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


class AutonomousDatabaseClonesFactsHelperGen(OCIResourceFactsHelperBase):
    """Supported operations: list"""

    def get_required_params_for_list(self):
        return [
            "compartment_id",
            "autonomous_database_id",
        ]

    def list_resources(self):
        optional_list_method_params = [
            "sort_order",
            "display_name",
            "lifecycle_state",
            "sort_by",
            "clone_type",
        ]
        optional_kwargs = dict(
            (param, self.module.params[param])
            for param in optional_list_method_params
            if self.module.params.get(param) is not None
        )
        return oci_common_utils.list_all_resources(
            self.client.list_autonomous_database_clones,
            compartment_id=self.module.params.get("compartment_id"),
            autonomous_database_id=self.module.params.get("autonomous_database_id"),
            **optional_kwargs
        )


AutonomousDatabaseClonesFactsHelperCustom = get_custom_class(
    "AutonomousDatabaseClonesFactsHelperCustom"
)


class ResourceFactsHelper(
    AutonomousDatabaseClonesFactsHelperCustom, AutonomousDatabaseClonesFactsHelperGen
):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec()
    module_args.update(
        dict(
            compartment_id=dict(type="str", required=True),
            autonomous_database_id=dict(type="str", required=True),
            sort_order=dict(type="str", choices=["ASC", "DESC"]),
            display_name=dict(aliases=["name"], type="str"),
            lifecycle_state=dict(
                type="str",
                choices=[
                    "PROVISIONING",
                    "AVAILABLE",
                    "STOPPING",
                    "STOPPED",
                    "STARTING",
                    "TERMINATING",
                    "TERMINATED",
                    "UNAVAILABLE",
                    "RESTORE_IN_PROGRESS",
                    "RESTORE_FAILED",
                    "BACKUP_IN_PROGRESS",
                    "SCALE_IN_PROGRESS",
                    "AVAILABLE_NEEDS_ATTENTION",
                    "UPDATING",
                    "MAINTENANCE_IN_PROGRESS",
                    "RESTARTING",
                    "RECREATING",
                    "ROLE_CHANGE_IN_PROGRESS",
                    "UPGRADING",
                    "INACCESSIBLE",
                    "STANDBY",
                ],
            ),
            sort_by=dict(type="str", choices=["NONE", "TIMECREATED", "DISPLAYNAME"]),
            clone_type=dict(type="str", choices=["REFRESHABLE_CLONE"]),
        )
    )

    module = OCIAnsibleModule(argument_spec=module_args)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_facts_helper = ResourceFactsHelper(
        module=module,
        resource_type="autonomous_database_clones",
        service_client_class=DatabaseClient,
        namespace="database",
    )

    result = []

    if resource_facts_helper.is_list():
        result = resource_facts_helper.list()
    else:
        resource_facts_helper.fail()

    module.exit_json(autonomous_database_clones=result)


if __name__ == "__main__":
    main()
