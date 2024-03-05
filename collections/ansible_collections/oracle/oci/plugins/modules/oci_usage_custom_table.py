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
module: oci_usage_custom_table
description: >-
    Due to size constraints we have not included the documentation in the module. Please check L(here,
    https://docs.oracle.com/en-us/iaas/tools/oci-ansible-collection/latest/collections/oracle/oci/oci_usage_custom_table_module.html)
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
    from oci.usage_api import UsageapiClient
    from oci.usage_api.models import CreateCustomTableDetails
    from oci.usage_api.models import UpdateCustomTableDetails

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


class CustomTableHelperGen(OCIResourceHelperBase):
    """Supported operations: create, update, get, list and delete"""

    def get_possible_entity_types(self):
        return super(CustomTableHelperGen, self).get_possible_entity_types() + [
            "customtable",
            "customtables",
            "usageApicustomtable",
            "usageApicustomtables",
            "customtableresource",
            "customtablesresource",
            "usageapi",
        ]

    def get_module_resource_id_param(self):
        return "custom_table_id"

    def get_module_resource_id(self):
        return self.module.params.get("custom_table_id")

    def get_get_fn(self):
        return self.client.get_custom_table

    def get_get_model_from_summary_model(self, summary_model):
        return oci_common_utils.call_with_backoff(
            self.client.get_custom_table, custom_table_id=summary_model.id,
        ).data

    def get_resource(self):
        return oci_common_utils.call_with_backoff(
            self.client.get_custom_table,
            custom_table_id=self.module.params.get("custom_table_id"),
        )

    def get_required_kwargs_for_list(self):
        required_list_method_params = [
            "compartment_id",
            "saved_report_id",
        ]

        return dict(
            (param, self.module.params[param]) for param in required_list_method_params
        )

    def get_optional_kwargs_for_list(self):
        return dict()

    def list_resources(self):

        required_kwargs = self.get_required_kwargs_for_list()
        optional_kwargs = self.get_optional_kwargs_for_list()
        kwargs = oci_common_utils.merge_dicts(required_kwargs, optional_kwargs)
        return oci_common_utils.list_all_resources(
            self.client.list_custom_tables, **kwargs
        )

    def get_create_model_class(self):
        return CreateCustomTableDetails

    def create_resource(self):
        create_details = self.get_create_model()
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.create_custom_table,
            call_fn_args=(),
            call_fn_kwargs=dict(create_custom_table_details=create_details,),
            waiter_type=oci_wait_utils.NONE_WAITER_KEY,
            operation=oci_common_utils.CREATE_OPERATION_KEY,
            waiter_client=self.get_waiter_client(),
            resource_helper=self,
            wait_for_states=self.get_wait_for_states_for_operation(
                oci_common_utils.CREATE_OPERATION_KEY,
            ),
        )

    def get_update_model_class(self):
        return UpdateCustomTableDetails

    def update_resource(self):
        update_details = self.get_update_model()
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.update_custom_table,
            call_fn_args=(),
            call_fn_kwargs=dict(
                update_custom_table_details=update_details,
                custom_table_id=self.module.params.get("custom_table_id"),
            ),
            waiter_type=oci_wait_utils.NONE_WAITER_KEY,
            operation=oci_common_utils.UPDATE_OPERATION_KEY,
            waiter_client=self.get_waiter_client(),
            resource_helper=self,
            wait_for_states=self.get_wait_for_states_for_operation(
                oci_common_utils.UPDATE_OPERATION_KEY,
            ),
        )

    def delete_resource(self):
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.delete_custom_table,
            call_fn_args=(),
            call_fn_kwargs=dict(
                custom_table_id=self.module.params.get("custom_table_id"),
            ),
            waiter_type=oci_wait_utils.NONE_WAITER_KEY,
            operation=oci_common_utils.DELETE_OPERATION_KEY,
            waiter_client=self.get_waiter_client(),
            resource_helper=self,
            wait_for_states=self.get_wait_for_states_for_operation(
                oci_common_utils.DELETE_OPERATION_KEY,
            ),
        )


CustomTableHelperCustom = get_custom_class("CustomTableHelperCustom")


class ResourceHelper(CustomTableHelperCustom, CustomTableHelperGen):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec(
        supports_create=True, supports_wait=False
    )
    module_args.update(
        dict(
            compartment_id=dict(type="str"),
            saved_report_id=dict(type="str"),
            saved_custom_table=dict(
                type="dict",
                options=dict(
                    display_name=dict(aliases=["name"], type="str", required=True),
                    row_group_by=dict(type="list", elements="str"),
                    column_group_by=dict(type="list", elements="str"),
                    group_by_tag=dict(
                        type="list",
                        elements="dict",
                        options=dict(
                            namespace=dict(type="str"),
                            key=dict(type="str", no_log=True),
                            value=dict(type="str"),
                        ),
                    ),
                    compartment_depth=dict(type="float"),
                    version=dict(type="float"),
                ),
            ),
            custom_table_id=dict(aliases=["id"], type="str"),
            state=dict(type="str", default="present", choices=["present", "absent"]),
        )
    )

    module = OCIAnsibleModule(argument_spec=module_args, supports_check_mode=True)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_helper = ResourceHelper(
        module=module,
        resource_type="custom_table",
        service_client_class=UsageapiClient,
        namespace="usage_api",
    )

    result = dict(changed=False)

    if resource_helper.is_delete():
        result = resource_helper.delete()
    elif resource_helper.is_update():
        result = resource_helper.update()
    elif resource_helper.is_create():
        result = resource_helper.create()

    module.exit_json(**result)


if __name__ == "__main__":
    main()
