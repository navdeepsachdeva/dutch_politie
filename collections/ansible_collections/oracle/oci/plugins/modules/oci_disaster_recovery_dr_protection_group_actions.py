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
module: oci_disaster_recovery_dr_protection_group_actions
description: >-
    Due to size constraints we have not included the documentation in the module. Please check L(here,
    https://docs.oracle.com/en-us/iaas/tools/oci-ansible-collection/latest/collections/oracle/oci/oci_disaster_recovery_dr_protection_group_actions_module.html)
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
    from oci.disaster_recovery import DisasterRecoveryClient
    from oci.disaster_recovery.models import AssociateDrProtectionGroupDetails
    from oci.disaster_recovery.models import ChangeDrProtectionGroupCompartmentDetails
    from oci.disaster_recovery.models import DisassociateDrProtectionGroupDetails
    from oci.disaster_recovery.models import UpdateDrProtectionGroupRoleDetails

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


class DrProtectionGroupActionsHelperGen(OCIActionsHelperBase):
    """
    Supported actions:
        associate
        change_compartment
        disassociate
        update_dr_protection_group_role
    """

    @staticmethod
    def get_module_resource_id_param():
        return "dr_protection_group_id"

    def get_module_resource_id(self):
        return self.module.params.get("dr_protection_group_id")

    def get_get_fn(self):
        return self.client.get_dr_protection_group

    def get_resource(self):
        return oci_common_utils.call_with_backoff(
            self.client.get_dr_protection_group,
            dr_protection_group_id=self.module.params.get("dr_protection_group_id"),
        )

    def associate(self):
        action_details = oci_common_utils.convert_input_data_to_model_class(
            self.module.params, AssociateDrProtectionGroupDetails
        )
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.associate_dr_protection_group,
            call_fn_args=(),
            call_fn_kwargs=dict(
                associate_dr_protection_group_details=action_details,
                dr_protection_group_id=self.module.params.get("dr_protection_group_id"),
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

    def change_compartment(self):
        action_details = oci_common_utils.convert_input_data_to_model_class(
            self.module.params, ChangeDrProtectionGroupCompartmentDetails
        )
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.change_dr_protection_group_compartment,
            call_fn_args=(),
            call_fn_kwargs=dict(
                change_dr_protection_group_compartment_details=action_details,
                dr_protection_group_id=self.module.params.get("dr_protection_group_id"),
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

    def disassociate(self):
        action_details = oci_common_utils.convert_input_data_to_model_class(
            self.module.params, DisassociateDrProtectionGroupDetails
        )
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.disassociate_dr_protection_group,
            call_fn_args=(),
            call_fn_kwargs=dict(
                disassociate_dr_protection_group_details=action_details,
                dr_protection_group_id=self.module.params.get("dr_protection_group_id"),
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

    def update_dr_protection_group_role(self):
        action_details = oci_common_utils.convert_input_data_to_model_class(
            self.module.params, UpdateDrProtectionGroupRoleDetails
        )
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.update_dr_protection_group_role,
            call_fn_args=(),
            call_fn_kwargs=dict(
                update_dr_protection_group_role_details=action_details,
                dr_protection_group_id=self.module.params.get("dr_protection_group_id"),
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


DrProtectionGroupActionsHelperCustom = get_custom_class(
    "DrProtectionGroupActionsHelperCustom"
)


class ResourceHelper(
    DrProtectionGroupActionsHelperCustom, DrProtectionGroupActionsHelperGen
):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec(
        supports_create=False, supports_wait=True
    )
    module_args.update(
        dict(
            peer_id=dict(type="str"),
            peer_region=dict(type="str"),
            compartment_id=dict(type="str"),
            type=dict(type="str", choices=["DEFAULT"]),
            role=dict(type="str", choices=["PRIMARY", "STANDBY", "UNCONFIGURED"]),
            dr_protection_group_id=dict(aliases=["id"], type="str", required=True),
            action=dict(
                type="str",
                required=True,
                choices=[
                    "associate",
                    "change_compartment",
                    "disassociate",
                    "update_dr_protection_group_role",
                ],
            ),
        )
    )

    module = OCIAnsibleModule(argument_spec=module_args, supports_check_mode=True)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_helper = ResourceHelper(
        module=module,
        resource_type="dr_protection_group",
        service_client_class=DisasterRecoveryClient,
        namespace="disaster_recovery",
    )

    result = resource_helper.perform_action(module.params.get("action"))

    module.exit_json(**result)


if __name__ == "__main__":
    main()
