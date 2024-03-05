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
module: oci_apm_control_plane_data_keys_actions
description: >-
    Due to size constraints we have not included the documentation in the module. Please check L(here,
    https://docs.oracle.com/en-us/iaas/tools/oci-ansible-collection/latest/collections/oracle/oci/oci_apm_control_plane_data_keys_actions_module.html)
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
    from oci.apm_control_plane import ApmDomainClient
    from oci.apm_control_plane.models import GenerateDataKeyDetails
    from oci.apm_control_plane.models import RemoveDataKeyDetails

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


class DataKeysActionsHelperGen(OCIActionsHelperBase):
    """
    Supported actions:
        generate
        remove
    """

    @staticmethod
    def get_module_resource_id_param():
        return "apm_domain_id"

    def get_module_resource_id(self):
        return self.module.params.get("apm_domain_id")

    def generate(self):
        action_details = []
        if self.module.params.get("generate_data_keys_list_details"):
            for action_details_item in self.module.params.get(
                "generate_data_keys_list_details"
            ):
                action_details.append(
                    oci_common_utils.convert_input_data_to_model_class(
                        action_details_item, GenerateDataKeyDetails
                    )
                )
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.generate_data_keys,
            call_fn_args=(),
            call_fn_kwargs=dict(
                generate_data_keys_list_details=action_details,
                apm_domain_id=self.module.params.get("apm_domain_id"),
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

    def remove(self):
        action_details = []
        if self.module.params.get("remove_data_keys_list_details"):
            for action_details_item in self.module.params.get(
                "remove_data_keys_list_details"
            ):
                action_details.append(
                    oci_common_utils.convert_input_data_to_model_class(
                        action_details_item, RemoveDataKeyDetails
                    )
                )
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.remove_data_keys,
            call_fn_args=(),
            call_fn_kwargs=dict(
                apm_domain_id=self.module.params.get("apm_domain_id"),
                remove_data_keys_list_details=action_details,
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


DataKeysActionsHelperCustom = get_custom_class("DataKeysActionsHelperCustom")


class ResourceHelper(DataKeysActionsHelperCustom, DataKeysActionsHelperGen):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec(
        supports_create=False, supports_wait=True
    )
    module_args.update(
        dict(
            generate_data_keys_list_details=dict(
                type="list",
                elements="dict",
                no_log=False,
                options=dict(
                    name=dict(type="str", required=True),
                    type=dict(type="str", required=True, choices=["PRIVATE", "PUBLIC"]),
                ),
            ),
            apm_domain_id=dict(aliases=["id"], type="str", required=True),
            remove_data_keys_list_details=dict(
                type="list",
                elements="dict",
                no_log=False,
                options=dict(name=dict(type="str", required=True)),
            ),
            action=dict(type="str", required=True, choices=["generate", "remove"]),
        )
    )

    module = OCIAnsibleModule(argument_spec=module_args, supports_check_mode=True)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_helper = ResourceHelper(
        module=module,
        resource_type="data_keys",
        service_client_class=ApmDomainClient,
        namespace="apm_control_plane",
    )

    result = resource_helper.perform_action(module.params.get("action"))

    module.exit_json(**result)


if __name__ == "__main__":
    main()
