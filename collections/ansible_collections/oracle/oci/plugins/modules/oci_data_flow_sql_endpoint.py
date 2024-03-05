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
module: oci_data_flow_sql_endpoint
description: >-
    Due to size constraints we have not included the documentation in the module. Please check L(here,
    https://docs.oracle.com/en-us/iaas/tools/oci-ansible-collection/latest/collections/oracle/oci/oci_data_flow_sql_endpoint_module.html)
    for the module documentation.
author: Oracle (@oracle)
"""


from ansible_collections.oracle.oci.plugins.module_utils import (
    oci_common_utils,
    oci_wait_utils,
)
from ansible_collections.oracle.oci.plugins.module_utils.oci_resource_utils import (
    OCIResourceHelperBase,
    get_custom_class,
    OCIAnsibleModule,
)

try:
    from oci.data_flow import DataFlowClient
    from oci.data_flow.models import CreateSqlEndpointDetails
    from oci.data_flow.models import UpdateSqlEndpointDetails

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


class DataFlowSqlEndpointHelperGen(OCIResourceHelperBase):
    """Supported operations: create, update, get, list and delete"""

    def get_possible_entity_types(self):
        return super(DataFlowSqlEndpointHelperGen, self).get_possible_entity_types() + [
            "dataflowsqlendpoint",
            "dataflowsqlendpoints",
            "dataFlowdataflowsqlendpoint",
            "dataFlowdataflowsqlendpoints",
            "dataflowsqlendpointresource",
            "dataflowsqlendpointsresource",
            "sqlendpoint",
            "sqlendpoints",
            "dataFlowsqlendpoint",
            "dataFlowsqlendpoints",
            "sqlendpointresource",
            "sqlendpointsresource",
            "dataflow",
        ]

    def get_module_resource_id_param(self):
        return "sql_endpoint_id"

    def get_module_resource_id(self):
        return self.module.params.get("sql_endpoint_id")

    def get_get_fn(self):
        return self.client.get_sql_endpoint

    def get_get_model_from_summary_model(self, summary_model):
        return oci_common_utils.call_with_backoff(
            self.client.get_sql_endpoint, sql_endpoint_id=summary_model.id,
        ).data

    def get_resource(self):
        return oci_common_utils.call_with_backoff(
            self.client.get_sql_endpoint,
            sql_endpoint_id=self.module.params.get("sql_endpoint_id"),
        )

    def get_required_kwargs_for_list(self):
        return dict()

    def get_optional_kwargs_for_list(self):
        optional_list_method_params = [
            "compartment_id",
            "sql_endpoint_id",
            "display_name",
        ]

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
            self.client.list_sql_endpoints, **kwargs
        )

    def get_create_model_class(self):
        return CreateSqlEndpointDetails

    def create_resource(self):
        create_details = self.get_create_model()
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.create_sql_endpoint,
            call_fn_args=(),
            call_fn_kwargs=dict(create_sql_endpoint_details=create_details,),
            waiter_type=oci_wait_utils.WORK_REQUEST_WAITER_KEY,
            operation=oci_common_utils.CREATE_OPERATION_KEY,
            waiter_client=self.get_waiter_client(),
            resource_helper=self,
            wait_for_states=oci_common_utils.get_work_request_completed_states(),
        )

    def get_update_model_class(self):
        return UpdateSqlEndpointDetails

    def update_resource(self):
        update_details = self.get_update_model()
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.update_sql_endpoint,
            call_fn_args=(),
            call_fn_kwargs=dict(
                update_sql_endpoint_details=update_details,
                sql_endpoint_id=self.module.params.get("sql_endpoint_id"),
            ),
            waiter_type=oci_wait_utils.WORK_REQUEST_WAITER_KEY,
            operation=oci_common_utils.UPDATE_OPERATION_KEY,
            waiter_client=self.get_waiter_client(),
            resource_helper=self,
            wait_for_states=oci_common_utils.get_work_request_completed_states(),
        )

    def delete_resource(self):
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.delete_sql_endpoint,
            call_fn_args=(),
            call_fn_kwargs=dict(
                sql_endpoint_id=self.module.params.get("sql_endpoint_id"),
            ),
            waiter_type=oci_wait_utils.WORK_REQUEST_WAITER_KEY,
            operation=oci_common_utils.DELETE_OPERATION_KEY,
            waiter_client=self.get_waiter_client(),
            resource_helper=self,
            wait_for_states=oci_common_utils.get_work_request_completed_states(),
        )


DataFlowSqlEndpointHelperCustom = get_custom_class("DataFlowSqlEndpointHelperCustom")


class ResourceHelper(DataFlowSqlEndpointHelperCustom, DataFlowSqlEndpointHelperGen):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec(
        supports_create=True, supports_wait=True
    )
    module_args.update(
        dict(
            compartment_id=dict(type="str"),
            display_name=dict(aliases=["name"], type="str"),
            description=dict(type="str"),
            sql_endpoint_version=dict(type="str"),
            driver_shape=dict(type="str"),
            driver_shape_config=dict(
                type="dict",
                options=dict(
                    ocpus=dict(type="float"), memory_in_gbs=dict(type="float")
                ),
            ),
            executor_shape=dict(type="str"),
            executor_shape_config=dict(
                type="dict",
                options=dict(
                    ocpus=dict(type="float"), memory_in_gbs=dict(type="float")
                ),
            ),
            min_executor_count=dict(type="int"),
            max_executor_count=dict(type="int"),
            metastore_id=dict(type="str"),
            lake_id=dict(type="str"),
            warehouse_bucket_uri=dict(type="str"),
            spark_advanced_configurations=dict(type="dict"),
            network_configuration=dict(
                type="dict",
                options=dict(
                    vcn_id=dict(type="str"),
                    subnet_id=dict(type="str"),
                    host_name_prefix=dict(type="str"),
                    nsg_ids=dict(type="list", elements="str"),
                    private_endpoint_ip=dict(type="str"),
                    network_type=dict(
                        type="str",
                        default="SECURE_ACCESS",
                        choices=["VCN", "SECURE_ACCESS"],
                    ),
                    access_control_rules=dict(
                        type="list",
                        elements="dict",
                        options=dict(
                            ip_notation=dict(
                                type="str",
                                required=True,
                                choices=["IP_ADDRESS", "CIDR", "VCN", "VCN_OCID"],
                            ),
                            value=dict(type="str", required=True),
                            vcn_ips=dict(type="str"),
                        ),
                    ),
                    public_endpoint_ip=dict(type="str"),
                ),
            ),
            defined_tags=dict(type="dict"),
            freeform_tags=dict(type="dict"),
            sql_endpoint_id=dict(aliases=["id"], type="str"),
            state=dict(type="str", default="present", choices=["present", "absent"]),
        )
    )

    module = OCIAnsibleModule(argument_spec=module_args, supports_check_mode=True)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_helper = ResourceHelper(
        module=module,
        resource_type="sql_endpoint",
        service_client_class=DataFlowClient,
        namespace="data_flow",
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
