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
module: oci_opsi_data_objects_actions
description: >-
    Due to size constraints we have not included the documentation in the module. Please check L(here,
    https://docs.oracle.com/en-us/iaas/tools/oci-ansible-collection/latest/collections/oracle/oci/oci_opsi_data_objects_actions_module.html)
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
    from oci.opsi.models import QueryOpsiDataObjectDataDetails

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


class OpsiDataObjectsActionsHelperGen(OCIActionsHelperBase):
    """
    Supported actions:
        query
    """

    def get_get_fn(self):
        return self.client.get_opsi_data_object

    def get_resource(self):
        return oci_common_utils.call_with_backoff(
            self.client.get_opsi_data_object,
            compartment_id=self.module.params.get("compartment_id"),
            opsi_data_object_identifier=self.module.params.get(
                "opsi_data_object_identifier"
            ),
        )

    def query(self):
        action_details = oci_common_utils.convert_input_data_to_model_class(
            self.module.params, QueryOpsiDataObjectDataDetails
        )
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.query_opsi_data_object_data,
            call_fn_args=(),
            call_fn_kwargs=dict(
                compartment_id=self.module.params.get("compartment_id"),
                query_opsi_data_object_data_details=action_details,
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


OpsiDataObjectsActionsHelperCustom = get_custom_class(
    "OpsiDataObjectsActionsHelperCustom"
)


class ResourceHelper(
    OpsiDataObjectsActionsHelperCustom, OpsiDataObjectsActionsHelperGen
):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec(
        supports_create=False, supports_wait=False
    )
    module_args.update(
        dict(
            compartment_id=dict(type="str", required=True),
            data_object_identifier=dict(type="str"),
            query=dict(
                type="dict",
                required=True,
                options=dict(
                    query_type=dict(
                        type="str", required=True, choices=["TEMPLATIZED_QUERY"]
                    ),
                    select_list=dict(type="list", elements="str"),
                    where_conditions_list=dict(type="list", elements="str"),
                    group_by_list=dict(type="list", elements="str"),
                    having_conditions_list=dict(type="list", elements="str"),
                    order_by_list=dict(type="list", elements="str"),
                    time_filters=dict(
                        type="dict",
                        options=dict(
                            time_period=dict(type="str"),
                            time_start=dict(type="str"),
                            time_end=dict(type="str"),
                        ),
                    ),
                ),
            ),
            resource_filters=dict(
                type="dict",
                options=dict(
                    defined_tag_equals=dict(type="list", elements="str"),
                    freeform_tag_equals=dict(type="list", elements="str"),
                    defined_tag_exists=dict(type="list", elements="str"),
                    freeform_tag_exists=dict(type="list", elements="str"),
                    compartment_id_in_subtree=dict(type="bool"),
                ),
            ),
            action=dict(type="str", required=True, choices=["query"]),
        )
    )

    module = OCIAnsibleModule(argument_spec=module_args, supports_check_mode=True)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_helper = ResourceHelper(
        module=module,
        resource_type="opsi_data_objects",
        service_client_class=OperationsInsightsClient,
        namespace="opsi",
    )

    result = resource_helper.perform_action(module.params.get("action"))

    module.exit_json(**result)


if __name__ == "__main__":
    main()
