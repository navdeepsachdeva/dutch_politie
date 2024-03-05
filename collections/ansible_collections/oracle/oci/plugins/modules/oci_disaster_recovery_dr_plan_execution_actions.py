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
module: oci_disaster_recovery_dr_plan_execution_actions
description: >-
    Due to size constraints we have not included the documentation in the module. Please check L(here,
    https://docs.oracle.com/en-us/iaas/tools/oci-ansible-collection/latest/collections/oracle/oci/oci_disaster_recovery_dr_plan_execution_actions_module.html)
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
    from oci.disaster_recovery.models import CancelDrPlanExecutionDetails
    from oci.disaster_recovery.models import IgnoreDrPlanExecutionDetails
    from oci.disaster_recovery.models import PauseDrPlanExecutionDetails
    from oci.disaster_recovery.models import ResumeDrPlanExecutionDetails
    from oci.disaster_recovery.models import RetryDrPlanExecutionDetails

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


class DrPlanExecutionActionsHelperGen(OCIActionsHelperBase):
    """
    Supported actions:
        cancel
        ignore
        pause
        resume
        retry
    """

    @staticmethod
    def get_module_resource_id_param():
        return "dr_plan_execution_id"

    def get_module_resource_id(self):
        return self.module.params.get("dr_plan_execution_id")

    def get_get_fn(self):
        return self.client.get_dr_plan_execution

    def get_resource(self):
        return oci_common_utils.call_with_backoff(
            self.client.get_dr_plan_execution,
            dr_plan_execution_id=self.module.params.get("dr_plan_execution_id"),
        )

    def cancel(self):
        action_details = oci_common_utils.convert_input_data_to_model_class(
            self.module.params, CancelDrPlanExecutionDetails
        )
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.cancel_dr_plan_execution,
            call_fn_args=(),
            call_fn_kwargs=dict(
                cancel_dr_plan_execution_details=action_details,
                dr_plan_execution_id=self.module.params.get("dr_plan_execution_id"),
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

    def ignore(self):
        action_details = oci_common_utils.convert_input_data_to_model_class(
            self.module.params, IgnoreDrPlanExecutionDetails
        )
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.ignore_dr_plan_execution,
            call_fn_args=(),
            call_fn_kwargs=dict(
                ignore_dr_plan_execution_details=action_details,
                dr_plan_execution_id=self.module.params.get("dr_plan_execution_id"),
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

    def pause(self):
        action_details = oci_common_utils.convert_input_data_to_model_class(
            self.module.params, PauseDrPlanExecutionDetails
        )
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.pause_dr_plan_execution,
            call_fn_args=(),
            call_fn_kwargs=dict(
                pause_dr_plan_execution_details=action_details,
                dr_plan_execution_id=self.module.params.get("dr_plan_execution_id"),
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

    def resume(self):
        action_details = oci_common_utils.convert_input_data_to_model_class(
            self.module.params, ResumeDrPlanExecutionDetails
        )
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.resume_dr_plan_execution,
            call_fn_args=(),
            call_fn_kwargs=dict(
                resume_dr_plan_execution_details=action_details,
                dr_plan_execution_id=self.module.params.get("dr_plan_execution_id"),
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

    def retry(self):
        action_details = oci_common_utils.convert_input_data_to_model_class(
            self.module.params, RetryDrPlanExecutionDetails
        )
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.retry_dr_plan_execution,
            call_fn_args=(),
            call_fn_kwargs=dict(
                retry_dr_plan_execution_details=action_details,
                dr_plan_execution_id=self.module.params.get("dr_plan_execution_id"),
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


DrPlanExecutionActionsHelperCustom = get_custom_class(
    "DrPlanExecutionActionsHelperCustom"
)


class ResourceHelper(
    DrPlanExecutionActionsHelperCustom, DrPlanExecutionActionsHelperGen
):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec(
        supports_create=False, supports_wait=True
    )
    module_args.update(
        dict(
            action_type=dict(type="str", choices=["CANCEL", "PAUSE", "RESUME"]),
            group_id=dict(type="str"),
            step_id=dict(type="str"),
            dr_plan_execution_id=dict(aliases=["id"], type="str", required=True),
            action=dict(
                type="str",
                required=True,
                choices=["cancel", "ignore", "pause", "resume", "retry"],
            ),
        )
    )

    module = OCIAnsibleModule(argument_spec=module_args, supports_check_mode=True)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_helper = ResourceHelper(
        module=module,
        resource_type="dr_plan_execution",
        service_client_class=DisasterRecoveryClient,
        namespace="disaster_recovery",
    )

    result = resource_helper.perform_action(module.params.get("action"))

    module.exit_json(**result)


if __name__ == "__main__":
    main()
