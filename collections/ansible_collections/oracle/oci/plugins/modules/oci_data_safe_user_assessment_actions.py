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
module: oci_data_safe_user_assessment_actions
description: >-
    Due to size constraints we have not included the documentation in the module. Please check L(here,
    https://docs.oracle.com/en-us/iaas/tools/oci-ansible-collection/latest/collections/oracle/oci/oci_data_safe_user_assessment_actions_module.html)
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
    from oci.data_safe import DataSafeClient
    from oci.data_safe.models import ChangeUserAssessmentCompartmentDetails
    from oci.data_safe.models import UserAssessmentBaseLineDetails

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


class DataSafeUserAssessmentActionsHelperGen(OCIActionsHelperBase):
    """
    Supported actions:
        change_compartment
        set_user_assessment_baseline
        unset_user_assessment_baseline
    """

    @staticmethod
    def get_module_resource_id_param():
        return "user_assessment_id"

    def get_module_resource_id(self):
        return self.module.params.get("user_assessment_id")

    def get_get_fn(self):
        return self.client.get_user_assessment

    def get_resource(self):
        return oci_common_utils.call_with_backoff(
            self.client.get_user_assessment,
            user_assessment_id=self.module.params.get("user_assessment_id"),
        )

    def change_compartment(self):
        action_details = oci_common_utils.convert_input_data_to_model_class(
            self.module.params, ChangeUserAssessmentCompartmentDetails
        )
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.change_user_assessment_compartment,
            call_fn_args=(),
            call_fn_kwargs=dict(
                user_assessment_id=self.module.params.get("user_assessment_id"),
                change_user_assessment_compartment_details=action_details,
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

    def set_user_assessment_baseline(self):
        action_details = oci_common_utils.convert_input_data_to_model_class(
            self.module.params, UserAssessmentBaseLineDetails
        )
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.set_user_assessment_baseline,
            call_fn_args=(),
            call_fn_kwargs=dict(
                user_assessment_id=self.module.params.get("user_assessment_id"),
                base_line_details=action_details,
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

    def unset_user_assessment_baseline(self):
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.unset_user_assessment_baseline,
            call_fn_args=(),
            call_fn_kwargs=dict(
                user_assessment_id=self.module.params.get("user_assessment_id"),
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


DataSafeUserAssessmentActionsHelperCustom = get_custom_class(
    "DataSafeUserAssessmentActionsHelperCustom"
)


class ResourceHelper(
    DataSafeUserAssessmentActionsHelperCustom, DataSafeUserAssessmentActionsHelperGen
):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec(
        supports_create=False, supports_wait=True
    )
    module_args.update(
        dict(
            compartment_id=dict(type="str"),
            assessment_ids=dict(type="list", elements="str"),
            user_assessment_id=dict(aliases=["id"], type="str", required=True),
            action=dict(
                type="str",
                required=True,
                choices=[
                    "change_compartment",
                    "set_user_assessment_baseline",
                    "unset_user_assessment_baseline",
                ],
            ),
        )
    )

    module = OCIAnsibleModule(argument_spec=module_args, supports_check_mode=True)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_helper = ResourceHelper(
        module=module,
        resource_type="user_assessment",
        service_client_class=DataSafeClient,
        namespace="data_safe",
    )

    result = resource_helper.perform_action(module.params.get("action"))

    module.exit_json(**result)


if __name__ == "__main__":
    main()
