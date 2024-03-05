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
module: oci_loggingingestion_log_entry_actions
description: >-
    Due to size constraints we have not included the documentation in the module. Please check L(here,
    https://docs.oracle.com/en-us/iaas/tools/oci-ansible-collection/latest/collections/oracle/oci/oci_loggingingestion_log_entry_actions_module.html)
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
    from oci.loggingingestion import LoggingClient
    from oci.loggingingestion.models import PutLogsDetails

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


class LogEntryActionsHelperGen(OCIActionsHelperBase):
    """
    Supported actions:
        put_logs
    """

    @staticmethod
    def get_module_resource_id_param():
        return "log_id"

    def get_module_resource_id(self):
        return self.module.params.get("log_id")

    def put_logs(self):
        action_details = oci_common_utils.convert_input_data_to_model_class(
            self.module.params, PutLogsDetails
        )
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.put_logs,
            call_fn_args=(),
            call_fn_kwargs=dict(
                log_id=self.module.params.get("log_id"),
                put_logs_details=action_details,
                timestamp_opc_agent_processing=self.module.params.get(
                    "timestamp_opc_agent_processing"
                ),
                opc_agent_version=self.module.params.get("opc_agent_version"),
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


LogEntryActionsHelperCustom = get_custom_class("LogEntryActionsHelperCustom")


class ResourceHelper(LogEntryActionsHelperCustom, LogEntryActionsHelperGen):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec(
        supports_create=False, supports_wait=False
    )
    module_args.update(
        dict(
            log_id=dict(aliases=["id"], type="str", required=True),
            specversion=dict(type="str", required=True),
            log_entry_batches=dict(
                type="list",
                elements="dict",
                required=True,
                options=dict(
                    entries=dict(
                        type="list",
                        elements="dict",
                        required=True,
                        options=dict(
                            data=dict(type="str", required=True),
                            id=dict(type="str", required=True),
                            time=dict(type="str"),
                        ),
                    ),
                    source=dict(type="str", required=True),
                    type=dict(type="str", required=True),
                    subject=dict(type="str"),
                    defaultlogentrytime=dict(type="str", required=True),
                ),
            ),
            timestamp_opc_agent_processing=dict(type="str"),
            opc_agent_version=dict(type="str"),
            action=dict(type="str", required=True, choices=["put_logs"]),
        )
    )

    module = OCIAnsibleModule(argument_spec=module_args, supports_check_mode=True)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_helper = ResourceHelper(
        module=module,
        resource_type="log_entry",
        service_client_class=LoggingClient,
        namespace="loggingingestion",
    )

    result = resource_helper.perform_action(module.params.get("action"))

    module.exit_json(**result)


if __name__ == "__main__":
    main()
