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
module: oci_golden_gate_deployment_actions
description: >-
    Due to size constraints we have not included the documentation in the module. Please check L(here,
    https://docs.oracle.com/en-us/iaas/tools/oci-ansible-collection/latest/collections/oracle/oci/oci_golden_gate_deployment_actions_module.html)
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
    from oci.golden_gate.models import ChangeDeploymentCompartmentDetails
    from oci.golden_gate.models import CollectDeploymentDiagnosticDetails
    from oci.golden_gate.models import DeploymentWalletExistsDetails
    from oci.golden_gate.models import ExportDeploymentWalletDetails
    from oci.golden_gate.models import ImportDeploymentWalletDetails
    from oci.golden_gate.models import StartDeploymentDetails
    from oci.golden_gate.models import StopDeploymentDetails
    from oci.golden_gate.models import UpgradeDeploymentDetails

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


class DeploymentActionsHelperGen(OCIActionsHelperBase):
    """
    Supported actions:
        change_compartment
        collect_deployment_diagnostic
        deployment_wallet_exists
        export_deployment_wallet
        import_deployment_wallet
        start
        stop
        upgrade
    """

    @staticmethod
    def get_module_resource_id_param():
        return "deployment_id"

    def get_module_resource_id(self):
        return self.module.params.get("deployment_id")

    def get_get_fn(self):
        return self.client.get_deployment

    def get_resource(self):
        return oci_common_utils.call_with_backoff(
            self.client.get_deployment,
            deployment_id=self.module.params.get("deployment_id"),
        )

    def get_response_field_name(self, action):
        response_fields = dict(
            stop="deployment",
            start="deployment",
            collect_deployment_diagnostic="deployment",
            deployment_wallet_exists="deployment_wallet_exists_response_details",
            export_deployment_wallet="deployment",
            import_deployment_wallet="deployment",
            upgrade="deployment",
            change_compartment="deployment",
        )
        return response_fields.get(action, "deployment")

    def change_compartment(self):
        action_details = oci_common_utils.convert_input_data_to_model_class(
            self.module.params, ChangeDeploymentCompartmentDetails
        )
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.change_deployment_compartment,
            call_fn_args=(),
            call_fn_kwargs=dict(
                deployment_id=self.module.params.get("deployment_id"),
                change_deployment_compartment_details=action_details,
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

    def collect_deployment_diagnostic(self):
        action_details = oci_common_utils.convert_input_data_to_model_class(
            self.module.params, CollectDeploymentDiagnosticDetails
        )
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.collect_deployment_diagnostic,
            call_fn_args=(),
            call_fn_kwargs=dict(
                deployment_id=self.module.params.get("deployment_id"),
                collect_deployment_diagnostic_details=action_details,
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

    def deployment_wallet_exists(self):
        action_details = oci_common_utils.convert_input_data_to_model_class(
            self.module.params, DeploymentWalletExistsDetails
        )
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.deployment_wallet_exists,
            call_fn_args=(),
            call_fn_kwargs=dict(
                deployment_id=self.module.params.get("deployment_id"),
                deployment_wallet_exists_details=action_details,
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

    def export_deployment_wallet(self):
        action_details = oci_common_utils.convert_input_data_to_model_class(
            self.module.params, ExportDeploymentWalletDetails
        )
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.export_deployment_wallet,
            call_fn_args=(),
            call_fn_kwargs=dict(
                deployment_id=self.module.params.get("deployment_id"),
                export_deployment_wallet_details=action_details,
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

    def import_deployment_wallet(self):
        action_details = oci_common_utils.convert_input_data_to_model_class(
            self.module.params, ImportDeploymentWalletDetails
        )
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.import_deployment_wallet,
            call_fn_args=(),
            call_fn_kwargs=dict(
                deployment_id=self.module.params.get("deployment_id"),
                import_deployment_wallet_details=action_details,
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

    def start(self):
        action_details = oci_common_utils.convert_input_data_to_model_class(
            self.module.params, StartDeploymentDetails
        )
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.start_deployment,
            call_fn_args=(),
            call_fn_kwargs=dict(
                deployment_id=self.module.params.get("deployment_id"),
                start_deployment_details=action_details,
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

    def stop(self):
        action_details = oci_common_utils.convert_input_data_to_model_class(
            self.module.params, StopDeploymentDetails
        )
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.stop_deployment,
            call_fn_args=(),
            call_fn_kwargs=dict(
                deployment_id=self.module.params.get("deployment_id"),
                stop_deployment_details=action_details,
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

    def upgrade(self):
        action_details = oci_common_utils.convert_input_data_to_model_class(
            self.module.params, UpgradeDeploymentDetails
        )
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.upgrade_deployment,
            call_fn_args=(),
            call_fn_kwargs=dict(
                deployment_id=self.module.params.get("deployment_id"),
                upgrade_deployment_details=action_details,
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


DeploymentActionsHelperCustom = get_custom_class("DeploymentActionsHelperCustom")


class ResourceHelper(DeploymentActionsHelperCustom, DeploymentActionsHelperGen):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec(
        supports_create=False, supports_wait=True
    )
    module_args.update(
        dict(
            compartment_id=dict(type="str"),
            namespace_name=dict(type="str"),
            bucket_name=dict(type="str"),
            diagnostic_name_prefix=dict(type="str"),
            time_diagnostic_start=dict(type="str"),
            time_diagnostic_end=dict(type="str"),
            secret_name=dict(type="str"),
            vault_id=dict(type="str"),
            new_wallet_secret_id=dict(type="str"),
            wallet_backup_secret_name=dict(type="str"),
            master_encryption_key_id=dict(type="str"),
            description=dict(type="str"),
            deployment_id=dict(aliases=["id"], type="str", required=True),
            ogg_version=dict(type="str"),
            type=dict(
                type="str", choices=["DEFAULT", "SPECIFIC_RELEASE", "CURRENT_RELEASE"]
            ),
            action=dict(
                type="str",
                required=True,
                choices=[
                    "change_compartment",
                    "collect_deployment_diagnostic",
                    "deployment_wallet_exists",
                    "export_deployment_wallet",
                    "import_deployment_wallet",
                    "start",
                    "stop",
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
        resource_type="deployment",
        service_client_class=GoldenGateClient,
        namespace="golden_gate",
    )

    result = resource_helper.perform_action(module.params.get("action"))

    module.exit_json(**result)


if __name__ == "__main__":
    main()
