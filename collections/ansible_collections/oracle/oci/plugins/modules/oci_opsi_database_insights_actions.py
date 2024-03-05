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
module: oci_opsi_database_insights_actions
description: >-
    Due to size constraints we have not included the documentation in the module. Please check L(here,
    https://docs.oracle.com/en-us/iaas/tools/oci-ansible-collection/latest/collections/oracle/oci/oci_opsi_database_insights_actions_module.html)
    for the module documentation.
author: Oracle (@oracle)
"""


from ansible_collections.oracle.oci.plugins.module_utils import (
    oci_common_utils,
    oci_wait_utils,
)
from ansible_collections.oracle.oci.plugins.module_utils.oci_resource_utils import (
    OCIActionsHelperBase,
    OCIAnsibleModule,
    get_custom_class,
)

try:
    from oci.opsi import OperationsInsightsClient
    from oci.opsi.models import ChangeAutonomousDatabaseInsightAdvancedFeaturesDetails
    from oci.opsi.models import ChangeDatabaseInsightCompartmentDetails
    from oci.opsi.models import ChangePeComanagedDatabaseInsightDetails
    from oci.opsi.models import EnableAutonomousDatabaseInsightAdvancedFeaturesDetails
    from oci.opsi.models import EnableDatabaseInsightDetails
    from oci.opsi.models import IngestAddmReportsDetails
    from oci.opsi.models import IngestDatabaseConfigurationDetails
    from oci.opsi.models import IngestSqlBucketDetails
    from oci.opsi.models import IngestSqlPlanLinesDetails
    from oci.opsi.models import IngestSqlStatsDetails
    from oci.opsi.models import IngestSqlTextDetails

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


class DatabaseInsightsActionsHelperGen(OCIActionsHelperBase):
    """
    Supported actions:
        change_autonomous_database_insight_advanced_features
        change
        change_pe_comanaged
        disable_autonomous_database_insight_advanced_features
        disable
        enable_autonomous_database_insight_advanced_features
        enable
        ingest_addm_reports
        ingest_database_configuration
        ingest_sql_bucket
        ingest_sql_plan_lines
        ingest_sql_stats
        ingest_sql_text
    """

    def get_get_fn(self):
        return self.client.get_database_insight

    def get_resource(self):
        return oci_common_utils.call_with_backoff(
            self.client.get_database_insight,
            database_insight_id=self.module.params.get("database_insight_id"),
        )

    def change_autonomous_database_insight_advanced_features(self):
        action_details = oci_common_utils.convert_input_data_to_model_class(
            self.module.params, ChangeAutonomousDatabaseInsightAdvancedFeaturesDetails
        )
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.change_autonomous_database_insight_advanced_features,
            call_fn_args=(),
            call_fn_kwargs=dict(
                change_autonomous_database_insight_advanced_features_details=action_details,
                database_insight_id=self.module.params.get("database_insight_id"),
            ),
            waiter_type=oci_wait_utils.WORK_REQUEST_WAITER_KEY,
            operation="{0}_{1}".format(
                self.module.params.get("action").upper(),
                oci_common_utils.ACTION_OPERATION_KEY,
            ),
            waiter_client=self.get_waiter_client(),
            resource_helper=self,
            wait_for_states=oci_common_utils.get_work_request_completed_states(),
        )

    def change(self):
        action_details = oci_common_utils.convert_input_data_to_model_class(
            self.module.params, ChangeDatabaseInsightCompartmentDetails
        )
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.change_database_insight_compartment,
            call_fn_args=(),
            call_fn_kwargs=dict(
                database_insight_id=self.module.params.get("database_insight_id"),
                change_database_insight_compartment_details=action_details,
            ),
            waiter_type=oci_wait_utils.WORK_REQUEST_WAITER_KEY,
            operation="{0}_{1}".format(
                self.module.params.get("action").upper(),
                oci_common_utils.ACTION_OPERATION_KEY,
            ),
            waiter_client=self.get_waiter_client(),
            resource_helper=self,
            wait_for_states=oci_common_utils.get_work_request_completed_states(),
        )

    def change_pe_comanaged(self):
        action_details = oci_common_utils.convert_input_data_to_model_class(
            self.module.params, ChangePeComanagedDatabaseInsightDetails
        )
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.change_pe_comanaged_database_insight,
            call_fn_args=(),
            call_fn_kwargs=dict(
                database_insight_id=self.module.params.get("database_insight_id"),
                change_pe_comanaged_database_insight_details=action_details,
            ),
            waiter_type=oci_wait_utils.WORK_REQUEST_WAITER_KEY,
            operation="{0}_{1}".format(
                self.module.params.get("action").upper(),
                oci_common_utils.ACTION_OPERATION_KEY,
            ),
            waiter_client=self.get_waiter_client(),
            resource_helper=self,
            wait_for_states=oci_common_utils.get_work_request_completed_states(),
        )

    def disable_autonomous_database_insight_advanced_features(self):
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.disable_autonomous_database_insight_advanced_features,
            call_fn_args=(),
            call_fn_kwargs=dict(
                database_insight_id=self.module.params.get("database_insight_id"),
            ),
            waiter_type=oci_wait_utils.WORK_REQUEST_WAITER_KEY,
            operation="{0}_{1}".format(
                self.module.params.get("action").upper(),
                oci_common_utils.ACTION_OPERATION_KEY,
            ),
            waiter_client=self.get_waiter_client(),
            resource_helper=self,
            wait_for_states=oci_common_utils.get_work_request_completed_states(),
        )

    def disable(self):
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.disable_database_insight,
            call_fn_args=(),
            call_fn_kwargs=dict(
                database_insight_id=self.module.params.get("database_insight_id"),
            ),
            waiter_type=oci_wait_utils.WORK_REQUEST_WAITER_KEY,
            operation="{0}_{1}".format(
                self.module.params.get("action").upper(),
                oci_common_utils.ACTION_OPERATION_KEY,
            ),
            waiter_client=self.get_waiter_client(),
            resource_helper=self,
            wait_for_states=oci_common_utils.get_work_request_completed_states(),
        )

    def enable_autonomous_database_insight_advanced_features(self):
        action_details = oci_common_utils.convert_input_data_to_model_class(
            self.module.params, EnableAutonomousDatabaseInsightAdvancedFeaturesDetails
        )
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.enable_autonomous_database_insight_advanced_features,
            call_fn_args=(),
            call_fn_kwargs=dict(
                enable_autonomous_database_insight_advanced_features_details=action_details,
                database_insight_id=self.module.params.get("database_insight_id"),
            ),
            waiter_type=oci_wait_utils.WORK_REQUEST_WAITER_KEY,
            operation="{0}_{1}".format(
                self.module.params.get("action").upper(),
                oci_common_utils.ACTION_OPERATION_KEY,
            ),
            waiter_client=self.get_waiter_client(),
            resource_helper=self,
            wait_for_states=oci_common_utils.get_work_request_completed_states(),
        )

    def enable(self):
        action_details = oci_common_utils.convert_input_data_to_model_class(
            self.module.params, EnableDatabaseInsightDetails
        )
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.enable_database_insight,
            call_fn_args=(),
            call_fn_kwargs=dict(
                enable_database_insight_details=action_details,
                database_insight_id=self.module.params.get("database_insight_id"),
            ),
            waiter_type=oci_wait_utils.WORK_REQUEST_WAITER_KEY,
            operation="{0}_{1}".format(
                self.module.params.get("action").upper(),
                oci_common_utils.ACTION_OPERATION_KEY,
            ),
            waiter_client=self.get_waiter_client(),
            resource_helper=self,
            wait_for_states=oci_common_utils.get_work_request_completed_states(),
        )

    def ingest_addm_reports(self):
        action_details = oci_common_utils.convert_input_data_to_model_class(
            self.module.params, IngestAddmReportsDetails
        )
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.ingest_addm_reports,
            call_fn_args=(),
            call_fn_kwargs=dict(
                ingest_addm_reports_details=action_details,
                database_id=self.module.params.get("database_id"),
                id=self.module.params.get("id"),
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

    def ingest_database_configuration(self):
        action_details = oci_common_utils.convert_input_data_to_model_class(
            self.module.params, IngestDatabaseConfigurationDetails
        )
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.ingest_database_configuration,
            call_fn_args=(),
            call_fn_kwargs=dict(
                ingest_database_configuration_details=action_details,
                database_id=self.module.params.get("database_id"),
                id=self.module.params.get("id"),
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

    def ingest_sql_bucket(self):
        action_details = oci_common_utils.convert_input_data_to_model_class(
            self.module.params, IngestSqlBucketDetails
        )
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.ingest_sql_bucket,
            call_fn_args=(),
            call_fn_kwargs=dict(
                ingest_sql_bucket_details=action_details,
                compartment_id=self.module.params.get("compartment_id"),
                database_id=self.module.params.get("database_id"),
                id=self.module.params.get("id"),
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

    def ingest_sql_plan_lines(self):
        action_details = oci_common_utils.convert_input_data_to_model_class(
            self.module.params, IngestSqlPlanLinesDetails
        )
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.ingest_sql_plan_lines,
            call_fn_args=(),
            call_fn_kwargs=dict(
                ingest_sql_plan_lines_details=action_details,
                compartment_id=self.module.params.get("compartment_id"),
                database_id=self.module.params.get("database_id"),
                id=self.module.params.get("id"),
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

    def ingest_sql_stats(self):
        action_details = oci_common_utils.convert_input_data_to_model_class(
            self.module.params, IngestSqlStatsDetails
        )
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.ingest_sql_stats,
            call_fn_args=(),
            call_fn_kwargs=dict(
                ingest_sql_stats_details=action_details,
                database_id=self.module.params.get("database_id"),
                id=self.module.params.get("id"),
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

    def ingest_sql_text(self):
        action_details = oci_common_utils.convert_input_data_to_model_class(
            self.module.params, IngestSqlTextDetails
        )
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.ingest_sql_text,
            call_fn_args=(),
            call_fn_kwargs=dict(
                ingest_sql_text_details=action_details,
                compartment_id=self.module.params.get("compartment_id"),
                database_id=self.module.params.get("database_id"),
                id=self.module.params.get("id"),
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


DatabaseInsightsActionsHelperCustom = get_custom_class(
    "DatabaseInsightsActionsHelperCustom"
)


class ResourceHelper(
    DatabaseInsightsActionsHelperCustom, DatabaseInsightsActionsHelperGen
):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec(
        supports_create=False, supports_wait=True
    )
    module_args.update(
        dict(
            entity_source=dict(
                type="str",
                choices=["EM_MANAGED_EXTERNAL_DATABASE", "PE_COMANAGED_DATABASE"],
            ),
            opsi_private_endpoint_id=dict(type="str"),
            service_name=dict(type="str"),
            credential_details=dict(
                type="dict",
                options=dict(
                    credential_source_name=dict(type="str", required=True),
                    credential_type=dict(
                        type="str",
                        required=True,
                        choices=["CREDENTIALS_BY_SOURCE", "CREDENTIALS_BY_VAULT"],
                    ),
                    user_name=dict(type="str"),
                    password_secret_id=dict(type="str"),
                    wallet_secret_id=dict(type="str"),
                    role=dict(type="str", choices=["NORMAL"]),
                ),
            ),
            connection_details=dict(
                type="dict",
                options=dict(
                    host_name=dict(type="str"),
                    port=dict(type="int"),
                    hosts=dict(
                        type="list",
                        elements="dict",
                        options=dict(host_ip=dict(type="str"), port=dict(type="int")),
                    ),
                    protocol=dict(type="str", choices=["TCP", "TCPS"]),
                    service_name=dict(type="str"),
                ),
            ),
            freeform_tags=dict(type="dict"),
            defined_tags=dict(type="dict"),
            system_tags=dict(type="dict"),
            database_insight_id=dict(type="str"),
            items=dict(
                type="list",
                elements="dict",
                options=dict(
                    time_interval_start=dict(type="str"),
                    time_interval_end=dict(type="str"),
                    task_identifier=dict(type="str"),
                    database_identifier=dict(type="str"),
                    snapshot_interval_start=dict(type="str"),
                    snapshot_interval_end=dict(type="str"),
                    addm_report=dict(type="str"),
                    num_cp_us=dict(type="int"),
                    num_cpu_cores=dict(type="int"),
                    num_cpu_sockets=dict(type="int"),
                    physical_memory_bytes=dict(type="float"),
                    host_name=dict(type="str"),
                    cpu_count=dict(type="int"),
                    host_memory_capacity=dict(type="float"),
                    db_external_instance_version=dict(type="str"),
                    parallel=dict(type="str"),
                    instance_role=dict(type="str"),
                    logins=dict(type="str"),
                    database_status=dict(type="str"),
                    status=dict(type="str"),
                    edition=dict(type="str"),
                    startup_time=dict(type="str"),
                    instance_number=dict(type="int"),
                    parameter_name=dict(type="str"),
                    parameter_value=dict(type="str"),
                    snapshot_id=dict(type="int"),
                    is_changed=dict(type="str"),
                    is_default=dict(type="str"),
                    metric_name=dict(
                        type="str",
                        choices=[
                            "DB_OS_CONFIG_INSTANCE",
                            "DB_EXTERNAL_INSTANCE",
                            "DB_PARAMETERS",
                            "DB_EXTERNAL_PROPERTIES",
                        ],
                    ),
                    name=dict(type="str"),
                    log_mode=dict(type="str"),
                    cdb=dict(type="str"),
                    open_mode=dict(type="str"),
                    database_role=dict(type="str"),
                    guard_status=dict(type="str"),
                    platform_name=dict(type="str"),
                    control_file_type=dict(type="str"),
                    switchover_status=dict(type="str"),
                    created=dict(type="str"),
                    database_type=dict(type="str"),
                    bucket_id=dict(type="str"),
                    executions_count=dict(type="int"),
                    cpu_time_in_sec=dict(type="float"),
                    io_time_in_sec=dict(type="float"),
                    other_wait_time_in_sec=dict(type="float"),
                    total_time_in_sec=dict(type="float"),
                    plan_hash=dict(type="int"),
                    operation=dict(type="str"),
                    remark=dict(type="str"),
                    options=dict(type="str"),
                    object_node=dict(type="str"),
                    object_owner=dict(type="str"),
                    object_name=dict(type="str"),
                    object_alias=dict(type="str"),
                    object_instance=dict(type="int"),
                    object_type=dict(type="str"),
                    optimizer=dict(type="str"),
                    search_columns=dict(type="int"),
                    identifier=dict(type="int"),
                    parent_identifier=dict(type="int"),
                    depth=dict(type="int"),
                    position=dict(type="int"),
                    cost=dict(type="int"),
                    cardinality=dict(type="int"),
                    bytes=dict(type="int"),
                    other=dict(type="str"),
                    other_tag=dict(type="str"),
                    partition_start=dict(type="str"),
                    partition_stop=dict(type="str"),
                    partition_identifier=dict(type="int"),
                    distribution=dict(type="str"),
                    cpu_cost=dict(type="int"),
                    io_cost=dict(type="int"),
                    temp_space=dict(type="int"),
                    access_predicates=dict(type="str"),
                    filter_predicates=dict(type="str"),
                    projection=dict(type="str"),
                    qblock_name=dict(type="str"),
                    elapsed_time_in_sec=dict(type="float"),
                    other_xml=dict(type="str"),
                    plan_hash_value=dict(type="int"),
                    instance_name=dict(type="str"),
                    last_active_time=dict(type="str"),
                    parse_calls=dict(type="int"),
                    disk_reads=dict(type="int"),
                    direct_reads=dict(type="int"),
                    direct_writes=dict(type="int"),
                    buffer_gets=dict(type="int"),
                    rows_processed=dict(type="int"),
                    serializable_aborts=dict(type="int"),
                    fetches=dict(type="int"),
                    executions=dict(type="int"),
                    avoided_executions=dict(type="int"),
                    end_of_fetch_count=dict(type="int"),
                    loads=dict(type="int"),
                    version_count=dict(type="int"),
                    invalidations=dict(type="int"),
                    obsolete_count=dict(type="int"),
                    px_servers_executions=dict(type="int"),
                    cpu_time_in_us=dict(type="int"),
                    elapsed_time_in_us=dict(type="int"),
                    avg_hard_parse_time_in_us=dict(type="int"),
                    concurrency_wait_time_in_us=dict(type="int"),
                    application_wait_time_in_us=dict(type="int"),
                    cluster_wait_time_in_us=dict(type="int"),
                    user_io_wait_time_in_us=dict(type="int"),
                    plsql_exec_time_in_us=dict(type="int"),
                    java_exec_time_in_us=dict(type="int"),
                    sorts=dict(type="int"),
                    sharable_mem=dict(type="int"),
                    total_sharable_mem=dict(type="int"),
                    type_check_mem=dict(type="int"),
                    io_cell_offload_eligible_bytes=dict(type="int"),
                    io_interconnect_bytes=dict(type="int"),
                    physical_read_requests=dict(type="int"),
                    physical_read_bytes=dict(type="int"),
                    physical_write_requests=dict(type="int"),
                    physical_write_bytes=dict(type="int"),
                    io_cell_uncompressed_bytes=dict(type="int"),
                    io_cell_offload_returned_bytes=dict(type="int"),
                    child_number=dict(type="int"),
                    command_type=dict(type="int"),
                    users_opening=dict(type="int"),
                    users_executing=dict(type="int"),
                    optimizer_cost=dict(type="int"),
                    full_plan_hash_value=dict(type="str"),
                    module=dict(type="str"),
                    service=dict(type="str"),
                    action=dict(type="str"),
                    sql_profile=dict(type="str"),
                    sql_patch=dict(type="str"),
                    sql_plan_baseline=dict(type="str"),
                    delta_execution_count=dict(type="int"),
                    delta_cpu_time=dict(type="int"),
                    delta_io_bytes=dict(type="int"),
                    delta_cpu_rank=dict(type="int"),
                    delta_execs_rank=dict(type="int"),
                    sharable_mem_rank=dict(type="int"),
                    delta_io_rank=dict(type="int"),
                    harmonic_sum=dict(type="int"),
                    wt_harmonic_sum=dict(type="int"),
                    total_sql_count=dict(type="int"),
                    version=dict(type="float"),
                    sql_identifier=dict(type="str"),
                    time_collected=dict(type="str"),
                    sql_command=dict(type="str"),
                    exact_matching_signature=dict(type="str"),
                    force_matching_signature=dict(type="str"),
                    sql_full_text=dict(type="str"),
                ),
            ),
            compartment_id=dict(type="str"),
            database_id=dict(type="str"),
            id=dict(type="str"),
            action=dict(
                type="str",
                required=True,
                choices=[
                    "change_autonomous_database_insight_advanced_features",
                    "change",
                    "change_pe_comanaged",
                    "disable_autonomous_database_insight_advanced_features",
                    "disable",
                    "enable_autonomous_database_insight_advanced_features",
                    "enable",
                    "ingest_addm_reports",
                    "ingest_database_configuration",
                    "ingest_sql_bucket",
                    "ingest_sql_plan_lines",
                    "ingest_sql_stats",
                    "ingest_sql_text",
                ],
            ),
        )
    )

    module = OCIAnsibleModule(argument_spec=module_args, supports_check_mode=True)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_helper = ResourceHelper(
        module=module,
        resource_type="database_insights",
        service_client_class=OperationsInsightsClient,
        namespace="opsi",
    )

    result = resource_helper.perform_action(module.params.get("action"))

    module.exit_json(**result)


if __name__ == "__main__":
    main()
