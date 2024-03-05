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
module: oci_golden_gate_deployment_upgrade_actions
description: >-
    Due to size constraints we have not included the documentation in the module. Please check L(here,
    https://docs.oracle.com/en-us/iaas/tools/oci-ansible-collection/latest/collections/oracle/oci/oci_golden_gate_deployment_upgrade_actions_module.html)
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
    from oci.golden_gate import GoldenGateClient
    from oci.golden_gate.models import CancelDeploymentUpgradeDetails
    from oci.golden_gate.models import CancelSnoozeDeploymentUpgradeDetails
    from oci.golden_gate.models import RescheduleDeploymentUpgradeDetails
    from oci.golden_gate.models import RollbackDeploymentUpgradeDetails
    from oci.golden_gate.models import SnoozeDeploymentUpgradeDetails
    from oci.golden_gate.models import UpgradeDeploymentUpgradeDetails

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


class DeploymentUpgradeActionsHelperGen(OCIActionsHelperBase):
    """
    Supported actions:
        cancel
        cancel_snooze
        reschedule
        rollback
        snooze
        upgrade
    """

    @staticmethod
    def get_module_resource_id_param():
        return "deployment_upgrade_id"

    def get_module_resource_id(self):
        return self.module.params.get("deployment_upgrade_id")

    def get_get_fn(self):
        return self.client.get_deployment_upgrade

    def get_resource(self):
        return oci_common_utils.call_with_backoff(
            self.client.get_deployment_upgrade,
            deployment_upgrade_id=self.module.params.get("deployment_upgrade_id"),
        )

    def cancel(self):
        action_details = oci_common_utils.convert_input_data_to_model_class(
            self.module.params, CancelDeploymentUpgradeDetails
        )
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.cancel_deployment_upgrade,
            call_fn_args=(),
            call_fn_kwargs=dict(
                deployment_upgrade_id=self.module.params.get("deployment_upgrade_id"),
                cancel_deployment_upgrade_details=action_details,
            ),
            waiter_type=oci_wait_utils.LIFECYCLE_STATE_WAITER_KEY,
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

    def cancel_snooze(self):
        action_details = oci_common_utils.convert_input_data_to_model_class(
            self.module.params, CancelSnoozeDeploymentUpgradeDetails
        )
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.cancel_snooze_deployment_upgrade,
            call_fn_args=(),
            call_fn_kwargs=dict(
                deployment_upgrade_id=self.module.params.get("deployment_upgrade_id"),
                cancel_snooze_deployment_upgrade_details=action_details,
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

    def reschedule(self):
        action_details = oci_common_utils.convert_input_data_to_model_class(
            self.module.params, RescheduleDeploymentUpgradeDetails
        )
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.reschedule_deployment_upgrade,
            call_fn_args=(),
            call_fn_kwargs=dict(
                deployment_upgrade_id=self.module.params.get("deployment_upgrade_id"),
                reschedule_deployment_upgrade_details=action_details,
            ),
            waiter_type=oci_wait_utils.LIFECYCLE_STATE_WAITER_KEY,
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

    def rollback(self):
        action_details = oci_common_utils.convert_input_data_to_model_class(
            self.module.params, RollbackDeploymentUpgradeDetails
        )
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.rollback_deployment_upgrade,
            call_fn_args=(),
            call_fn_kwargs=dict(
                deployment_upgrade_id=self.module.params.get("deployment_upgrade_id"),
                rollback_deployment_upgrade_details=action_details,
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

    def snooze(self):
        action_details = oci_common_utils.convert_input_data_to_model_class(
            self.module.params, SnoozeDeploymentUpgradeDetails
        )
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.snooze_deployment_upgrade,
            call_fn_args=(),
            call_fn_kwargs=dict(
                deployment_upgrade_id=self.module.params.get("deployment_upgrade_id"),
                snooze_deployment_upgrade_details=action_details,
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

    def upgrade(self):
        action_details = oci_common_utils.convert_input_data_to_model_class(
            self.module.params, UpgradeDeploymentUpgradeDetails
        )
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.upgrade_deployment_upgrade,
            call_fn_args=(),
            call_fn_kwargs=dict(
                deployment_upgrade_id=self.module.params.get("deployment_upgrade_id"),
                upgrade_deployment_upgrade_details=action_details,
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


DeploymentUpgradeActionsHelperCustom = get_custom_class(
    "DeploymentUpgradeActionsHelperCustom"
)


class ResourceHelper(
    DeploymentUpgradeActionsHelperCustom, DeploymentUpgradeActionsHelperGen
):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec(
        supports_create=False, supports_wait=True
    )
    module_args.update(
        dict(
            time_schedule=dict(type="str"),
            deployment_upgrade_id=dict(aliases=["id"], type="str", required=True),
            type=dict(
                type="str", required=True, choices=["DEFAULT", "RESCHEDULE_TO_DATE"]
            ),
            action=dict(
                type="str",
                required=True,
                choices=[
                    "cancel",
                    "cancel_snooze",
                    "reschedule",
                    "rollback",
                    "snooze",
                    "upgrade",
                ],
            ),
        )
    )

    module = OCIAnsibleModule(argument_spec=module_args, supports_check_mode=True)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_helper = ResourceHelper(
        module=module,
        resource_type="deployment_upgrade",
        service_client_class=GoldenGateClient,
        namespace="golden_gate",
    )

    result = resource_helper.perform_action(module.params.get("action"))

    module.exit_json(**result)


if __name__ == "__main__":
    main()
