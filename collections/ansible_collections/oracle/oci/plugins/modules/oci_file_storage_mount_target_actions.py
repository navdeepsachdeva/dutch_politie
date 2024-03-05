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
module: oci_file_storage_mount_target_actions
description: >-
    Due to size constraints we have not included the documentation in the module. Please check L(here,
    https://docs.oracle.com/en-us/iaas/tools/oci-ansible-collection/latest/collections/oracle/oci/oci_file_storage_mount_target_actions_module.html)
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
    from oci.file_storage import FileStorageClient
    from oci.file_storage.models import ChangeMountTargetCompartmentDetails
    from oci.file_storage.models import ValidateKeyTabsDetails

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


class MountTargetActionsHelperGen(OCIActionsHelperBase):
    """
    Supported actions:
        change_compartment
        validate_key_tabs
    """

    def get_get_fn(self):
        return self.client.get_mount_target

    def get_resource(self):
        return oci_common_utils.call_with_backoff(
            self.client.get_mount_target,
            mount_target_id=self.module.params.get("mount_target_id"),
        )

    def change_compartment(self):
        action_details = oci_common_utils.convert_input_data_to_model_class(
            self.module.params, ChangeMountTargetCompartmentDetails
        )
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.change_mount_target_compartment,
            call_fn_args=(),
            call_fn_kwargs=dict(
                mount_target_id=self.module.params.get("mount_target_id"),
                change_mount_target_compartment_details=action_details,
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

    def validate_key_tabs(self):
        action_details = oci_common_utils.convert_input_data_to_model_class(
            self.module.params, ValidateKeyTabsDetails
        )
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.validate_key_tabs,
            call_fn_args=(),
            call_fn_kwargs=dict(validate_key_tabs_details=action_details,),
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


MountTargetActionsHelperCustom = get_custom_class("MountTargetActionsHelperCustom")


class ResourceHelper(MountTargetActionsHelperCustom, MountTargetActionsHelperGen):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec(
        supports_create=False, supports_wait=False
    )
    module_args.update(
        dict(
            compartment_id=dict(type="str"),
            mount_target_id=dict(type="str"),
            key_tab_secret_details=dict(
                type="dict",
                no_log=False,
                options=dict(
                    key_tab_secret_id=dict(type="str", required=True),
                    current_key_tab_secret_version=dict(
                        type="int", required=True, no_log=True
                    ),
                    backup_key_tab_secret_version=dict(type="int", no_log=True),
                ),
            ),
            action=dict(
                type="str",
                required=True,
                choices=["change_compartment", "validate_key_tabs"],
            ),
        )
    )

    module = OCIAnsibleModule(argument_spec=module_args, supports_check_mode=True)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_helper = ResourceHelper(
        module=module,
        resource_type="mount_target",
        service_client_class=FileStorageClient,
        namespace="file_storage",
    )

    result = resource_helper.perform_action(module.params.get("action"))

    module.exit_json(**result)


if __name__ == "__main__":
    main()
