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
module: oci_mysql_configuration
description: >-
    Due to size constraints we have not included the documentation in the module. Please check L(here,
    https://docs.oracle.com/en-us/iaas/tools/oci-ansible-collection/latest/collections/oracle/oci/oci_mysql_configuration_module.html)
    for the module documentation.
author: Oracle (@oracle)
"""


from ansible_collections.oracle.oci.plugins.module_utils import (
    oci_common_utils,
    oci_wait_utils,
    oci_config_utils,
)
from ansible_collections.oracle.oci.plugins.module_utils.oci_resource_utils import (
    OCIResourceHelperBase,
    get_custom_class,
    OCIAnsibleModule,
)

try:
    from oci.mysql import WorkRequestsClient
    from oci.mysql import MysqlaasClient
    from oci.mysql.models import CreateConfigurationDetails
    from oci.mysql.models import UpdateConfigurationDetails

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


class MysqlConfigurationHelperGen(OCIResourceHelperBase):
    """Supported operations: create, update, get, list and delete"""

    def get_waiter_client(self):
        return oci_config_utils.create_service_client(self.module, WorkRequestsClient)

    def get_possible_entity_types(self):
        return super(MysqlConfigurationHelperGen, self).get_possible_entity_types() + [
            "configuration",
            "configurations",
            "mysqlconfiguration",
            "mysqlconfigurations",
            "configurationresource",
            "configurationsresource",
            "mysql",
        ]

    def get_module_resource_id_param(self):
        return "configuration_id"

    def get_module_resource_id(self):
        return self.module.params.get("configuration_id")

    def get_get_fn(self):
        return self.client.get_configuration

    def get_get_model_from_summary_model(self, summary_model):
        return oci_common_utils.call_with_backoff(
            self.client.get_configuration, configuration_id=summary_model.id,
        ).data

    def get_resource(self):
        return oci_common_utils.call_with_backoff(
            self.client.get_configuration,
            configuration_id=self.module.params.get("configuration_id"),
        )

    def get_required_kwargs_for_list(self):
        required_list_method_params = [
            "compartment_id",
        ]

        return dict(
            (param, self.module.params[param]) for param in required_list_method_params
        )

    def get_optional_kwargs_for_list(self):
        optional_list_method_params = ["configuration_id", "display_name", "shape_name"]

        return dict(
            (param, self.module.params[param])
            for param in optional_list_method_params
            if self.module.params.get(param) is not None
            and (
                self._use_name_as_identifier()
                or (
                    not self.module.params.get("key_by")
                    or param in self.module.params.get("key_by")
                )
            )
        )

    def list_resources(self):

        required_kwargs = self.get_required_kwargs_for_list()
        optional_kwargs = self.get_optional_kwargs_for_list()
        kwargs = oci_common_utils.merge_dicts(required_kwargs, optional_kwargs)
        return oci_common_utils.list_all_resources(
            self.client.list_configurations, **kwargs
        )

    def get_create_model_class(self):
        return CreateConfigurationDetails

    def create_resource(self):
        create_details = self.get_create_model()
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.create_configuration,
            call_fn_args=(),
            call_fn_kwargs=dict(create_configuration_details=create_details,),
            waiter_type=oci_wait_utils.WORK_REQUEST_WAITER_KEY,
            operation=oci_common_utils.CREATE_OPERATION_KEY,
            waiter_client=self.get_waiter_client(),
            resource_helper=self,
            wait_for_states=oci_common_utils.get_work_request_completed_states(),
        )

    def get_update_model_class(self):
        return UpdateConfigurationDetails

    def update_resource(self):
        update_details = self.get_update_model()
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.update_configuration,
            call_fn_args=(),
            call_fn_kwargs=dict(
                configuration_id=self.module.params.get("configuration_id"),
                update_configuration_details=update_details,
            ),
            waiter_type=oci_wait_utils.LIFECYCLE_STATE_WAITER_KEY,
            operation=oci_common_utils.UPDATE_OPERATION_KEY,
            waiter_client=self.get_waiter_client(),
            resource_helper=self,
            wait_for_states=self.get_wait_for_states_for_operation(
                oci_common_utils.UPDATE_OPERATION_KEY,
            ),
        )

    def delete_resource(self):
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.delete_configuration,
            call_fn_args=(),
            call_fn_kwargs=dict(
                configuration_id=self.module.params.get("configuration_id"),
            ),
            waiter_type=oci_wait_utils.LIFECYCLE_STATE_WAITER_KEY,
            operation=oci_common_utils.DELETE_OPERATION_KEY,
            waiter_client=self.get_waiter_client(),
            resource_helper=self,
            wait_for_states=self.get_wait_for_states_for_operation(
                oci_common_utils.DELETE_OPERATION_KEY,
            ),
        )


MysqlConfigurationHelperCustom = get_custom_class("MysqlConfigurationHelperCustom")


class ResourceHelper(MysqlConfigurationHelperCustom, MysqlConfigurationHelperGen):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec(
        supports_create=True, supports_wait=True
    )
    module_args.update(
        dict(
            compartment_id=dict(type="str"),
            shape_name=dict(type="str"),
            init_variables=dict(
                type="dict",
                options=dict(
                    lower_case_table_names=dict(
                        type="str",
                        choices=["CASE_SENSITIVE", "CASE_INSENSITIVE_LOWERCASE"],
                    )
                ),
            ),
            variables=dict(
                type="dict",
                options=dict(
                    completion_type=dict(
                        type="str", choices=["NO_CHAIN", "CHAIN", "RELEASE"]
                    ),
                    big_tables=dict(type="bool"),
                    connection_memory_chunk_size=dict(type="int"),
                    connection_memory_limit=dict(type="int"),
                    default_authentication_plugin=dict(
                        type="str",
                        choices=[
                            "mysql_native_password",
                            "sha256_password",
                            "caching_sha2_password",
                        ],
                    ),
                    global_connection_memory_limit=dict(type="int"),
                    global_connection_memory_tracking=dict(type="bool"),
                    transaction_isolation=dict(
                        type="str",
                        choices=[
                            "READ-UNCOMMITTED",
                            "READ-COMMITED",
                            "READ-COMMITTED",
                            "REPEATABLE-READ",
                            "SERIALIZABLE",
                        ],
                    ),
                    innodb_ft_server_stopword_table=dict(type="str"),
                    mandatory_roles=dict(type="str"),
                    autocommit=dict(type="bool"),
                    foreign_key_checks=dict(type="bool", no_log=True),
                    group_replication_consistency=dict(
                        type="str",
                        choices=[
                            "EVENTUAL",
                            "BEFORE_ON_PRIMARY_FAILOVER",
                            "BEFORE",
                            "AFTER",
                            "BEFORE_AND_AFTER",
                        ],
                    ),
                    innodb_ft_enable_stopword=dict(type="bool"),
                    innodb_log_writer_threads=dict(type="bool"),
                    local_infile=dict(type="bool"),
                    mysql_firewall_mode=dict(type="bool"),
                    mysqlx_enable_hello_notice=dict(type="bool"),
                    sql_require_primary_key=dict(type="bool", no_log=True),
                    sql_warnings=dict(type="bool"),
                    binlog_expire_logs_seconds=dict(type="int"),
                    binlog_row_metadata=dict(type="str", choices=["FULL", "MINIMAL"]),
                    binlog_row_value_options=dict(type="str"),
                    binlog_transaction_compression=dict(type="bool"),
                    innodb_buffer_pool_size=dict(type="int"),
                    innodb_ft_result_cache_limit=dict(type="int"),
                    max_binlog_cache_size=dict(type="int"),
                    max_connect_errors=dict(type="int"),
                    max_heap_table_size=dict(type="int"),
                    max_connections=dict(type="int"),
                    max_prepared_stmt_count=dict(type="int"),
                    connect_timeout=dict(type="int"),
                    cte_max_recursion_depth=dict(type="int"),
                    generated_random_password_length=dict(type="int", no_log=True),
                    information_schema_stats_expiry=dict(type="int"),
                    innodb_buffer_pool_dump_pct=dict(type="int"),
                    innodb_buffer_pool_instances=dict(type="int"),
                    innodb_ddl_buffer_size=dict(type="int"),
                    innodb_ddl_threads=dict(type="int"),
                    innodb_ft_max_token_size=dict(type="int", no_log=True),
                    innodb_ft_min_token_size=dict(type="int", no_log=True),
                    innodb_ft_num_word_optimize=dict(type="int"),
                    innodb_lock_wait_timeout=dict(type="int"),
                    innodb_max_purge_lag=dict(type="int"),
                    innodb_max_purge_lag_delay=dict(type="int"),
                    interactive_timeout=dict(type="int"),
                    innodb_stats_persistent_sample_pages=dict(type="int"),
                    innodb_stats_transient_sample_pages=dict(type="int"),
                    max_allowed_packet=dict(type="int"),
                    max_execution_time=dict(type="int"),
                    mysqlx_connect_timeout=dict(type="int"),
                    mysqlx_document_id_unique_prefix=dict(type="int"),
                    mysqlx_idle_worker_thread_timeout=dict(type="int"),
                    mysqlx_interactive_timeout=dict(type="int"),
                    mysqlx_max_allowed_packet=dict(type="int"),
                    mysqlx_min_worker_threads=dict(type="int"),
                    mysqlx_read_timeout=dict(type="int"),
                    mysqlx_wait_timeout=dict(type="int"),
                    mysqlx_write_timeout=dict(type="int"),
                    net_read_timeout=dict(type="int"),
                    net_write_timeout=dict(type="int"),
                    parser_max_mem_size=dict(type="int"),
                    query_alloc_block_size=dict(type="int"),
                    query_prealloc_size=dict(type="int"),
                    regexp_time_limit=dict(type="int"),
                    sql_mode=dict(type="str"),
                    tmp_table_size=dict(type="int"),
                    mysqlx_deflate_default_compression_level=dict(type="int"),
                    mysqlx_deflate_max_client_compression_level=dict(type="int"),
                    mysqlx_lz4_max_client_compression_level=dict(type="int"),
                    mysqlx_lz4_default_compression_level=dict(type="int"),
                    mysqlx_zstd_max_client_compression_level=dict(type="int"),
                    mysqlx_zstd_default_compression_level=dict(type="int"),
                    mysql_zstd_default_compression_level=dict(type="int"),
                    sort_buffer_size=dict(type="int"),
                    wait_timeout=dict(type="int"),
                    thread_pool_dedicated_listeners=dict(type="bool"),
                    thread_pool_max_transactions_limit=dict(type="int"),
                    time_zone=dict(type="str"),
                ),
            ),
            parent_configuration_id=dict(type="str"),
            description=dict(type="str"),
            display_name=dict(aliases=["name"], type="str"),
            freeform_tags=dict(type="dict"),
            defined_tags=dict(type="dict"),
            configuration_id=dict(aliases=["id"], type="str"),
            state=dict(type="str", default="present", choices=["present", "absent"]),
        )
    )

    module = OCIAnsibleModule(argument_spec=module_args, supports_check_mode=True)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_helper = ResourceHelper(
        module=module,
        resource_type="configuration",
        service_client_class=MysqlaasClient,
        namespace="mysql",
    )

    result = dict(changed=False)

    if resource_helper.is_delete_using_name():
        result = resource_helper.delete_using_name()
    elif resource_helper.is_delete():
        result = resource_helper.delete()
    elif resource_helper.is_update_using_name():
        result = resource_helper.update_using_name()
    elif resource_helper.is_update():
        result = resource_helper.update()
    elif resource_helper.is_create():
        result = resource_helper.create()

    module.exit_json(**result)


if __name__ == "__main__":
    main()
