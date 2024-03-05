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
module: oci_jms_fleet_actions
description: >-
    Due to size constraints we have not included the documentation in the module. Please check L(here,
    https://docs.oracle.com/en-us/iaas/tools/oci-ansible-collection/latest/collections/oracle/oci/oci_jms_fleet_actions_module.html)
    for the module documentation.
author: Oracle (@oracle)
"""


from ansible.module_utils._text import to_bytes
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
    from oci.jms import JavaManagementServiceClient
    from oci.jms.models import ChangeFleetCompartmentDetails
    from oci.jms.models import DisableDrsDetails
    from oci.jms.models import EnableDrsDetails
    from oci.jms.models import GenerateAgentDeployScriptDetails
    from oci.jms.models import RequestCryptoAnalysesDetails
    from oci.jms.models import RequestJavaMigrationAnalysesDetails
    from oci.jms.models import RequestJfrRecordingsDetails
    from oci.jms.models import RequestPerformanceTuningAnalysesDetails

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


class FleetActionsHelperGen(OCIActionsHelperBase):
    """
    Supported actions:
        change_compartment
        disable_drs
        enable_drs
        generate_agent_deploy_script
        request_crypto_analyses
        request_java_migration_analyses
        request_jfr_recordings
        request_performance_tuning_analyses
    """

    @staticmethod
    def get_module_resource_id_param():
        return "fleet_id"

    def get_module_resource_id(self):
        return self.module.params.get("fleet_id")

    def get_get_fn(self):
        return self.client.get_fleet

    def get_resource(self):
        return oci_common_utils.call_with_backoff(
            self.client.get_fleet, fleet_id=self.module.params.get("fleet_id"),
        )

    def change_compartment(self):
        action_details = oci_common_utils.convert_input_data_to_model_class(
            self.module.params, ChangeFleetCompartmentDetails
        )
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.change_fleet_compartment,
            call_fn_args=(),
            call_fn_kwargs=dict(
                fleet_id=self.module.params.get("fleet_id"),
                change_fleet_compartment_details=action_details,
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

    def disable_drs(self):
        action_details = oci_common_utils.convert_input_data_to_model_class(
            self.module.params, DisableDrsDetails
        )
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.disable_drs,
            call_fn_args=(),
            call_fn_kwargs=dict(
                fleet_id=self.module.params.get("fleet_id"),
                disable_drs_details=action_details,
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

    def enable_drs(self):
        action_details = oci_common_utils.convert_input_data_to_model_class(
            self.module.params, EnableDrsDetails
        )
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.enable_drs,
            call_fn_args=(),
            call_fn_kwargs=dict(
                fleet_id=self.module.params.get("fleet_id"),
                enable_drs_details=action_details,
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

    def generate_agent_deploy_script(self):
        action_details = oci_common_utils.convert_input_data_to_model_class(
            self.module.params, GenerateAgentDeployScriptDetails
        )
        response = oci_wait_utils.call_and_wait(
            call_fn=self.client.generate_agent_deploy_script,
            call_fn_args=(),
            call_fn_kwargs=dict(
                fleet_id=self.module.params.get("fleet_id"),
                generate_agent_deploy_script_details=action_details,
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
        dest = self.module.params.get("dest")
        chunk_size = oci_common_utils.MEBIBYTE
        with open(to_bytes(dest), "wb") as dest_file:
            for chunk in response.raw.stream(chunk_size, decode_content=True):
                dest_file.write(chunk)
        return None

    def request_crypto_analyses(self):
        action_details = oci_common_utils.convert_input_data_to_model_class(
            self.module.params, RequestCryptoAnalysesDetails
        )
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.request_crypto_analyses,
            call_fn_args=(),
            call_fn_kwargs=dict(
                fleet_id=self.module.params.get("fleet_id"),
                request_crypto_analyses_details=action_details,
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

    def request_java_migration_analyses(self):
        action_details = oci_common_utils.convert_input_data_to_model_class(
            self.module.params, RequestJavaMigrationAnalysesDetails
        )
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.request_java_migration_analyses,
            call_fn_args=(),
            call_fn_kwargs=dict(
                fleet_id=self.module.params.get("fleet_id"),
                request_java_migration_analyses_details=action_details,
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

    def request_jfr_recordings(self):
        action_details = oci_common_utils.convert_input_data_to_model_class(
            self.module.params, RequestJfrRecordingsDetails
        )
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.request_jfr_recordings,
            call_fn_args=(),
            call_fn_kwargs=dict(
                fleet_id=self.module.params.get("fleet_id"),
                request_jfr_recordings_details=action_details,
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

    def request_performance_tuning_analyses(self):
        action_details = oci_common_utils.convert_input_data_to_model_class(
            self.module.params, RequestPerformanceTuningAnalysesDetails
        )
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.request_performance_tuning_analyses,
            call_fn_args=(),
            call_fn_kwargs=dict(
                fleet_id=self.module.params.get("fleet_id"),
                request_performance_tuning_analyses_details=action_details,
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


FleetActionsHelperCustom = get_custom_class("FleetActionsHelperCustom")


class ResourceHelper(FleetActionsHelperCustom, FleetActionsHelperGen):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec(
        supports_create=False, supports_wait=True
    )
    module_args.update(
        dict(
            compartment_id=dict(type="str"),
            manage_drs_details=dict(
                type="dict",
                options=dict(
                    targets=dict(
                        type="list",
                        elements="dict",
                        options=dict(
                            managed_instance_id=dict(type="str", required=True)
                        ),
                    )
                ),
            ),
            dest=dict(type="str"),
            install_key_id=dict(type="str"),
            os_family=dict(
                type="str", choices=["LINUX", "WINDOWS", "MACOS", "UNKNOWN"]
            ),
            is_user_name_enabled=dict(type="bool"),
            jfc_profile_name=dict(type="str"),
            jfc_v1=dict(type="str"),
            jfc_v2=dict(type="str"),
            recording_size_in_mb=dict(type="int"),
            fleet_id=dict(aliases=["id"], type="str", required=True),
            targets=dict(
                type="list",
                elements="dict",
                options=dict(
                    application_key=dict(type="str", no_log=True),
                    jre_key=dict(type="str", no_log=True),
                    managed_instance_id=dict(type="str", required=True),
                    application_installation_key=dict(type="str", no_log=True),
                    source_jdk_version=dict(type="str"),
                    target_jdk_version=dict(type="str"),
                ),
            ),
            recording_duration_in_minutes=dict(type="int"),
            waiting_period_in_minutes=dict(type="int"),
            action=dict(
                type="str",
                required=True,
                choices=[
                    "change_compartment",
                    "disable_drs",
                    "enable_drs",
                    "generate_agent_deploy_script",
                    "request_crypto_analyses",
                    "request_java_migration_analyses",
                    "request_jfr_recordings",
                    "request_performance_tuning_analyses",
                ],
            ),
        )
    )

    module = OCIAnsibleModule(argument_spec=module_args, supports_check_mode=True)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_helper = ResourceHelper(
        module=module,
        resource_type="fleet",
        service_client_class=JavaManagementServiceClient,
        namespace="jms",
    )

    result = resource_helper.perform_action(module.params.get("action"))

    module.exit_json(**result)


if __name__ == "__main__":
    main()
