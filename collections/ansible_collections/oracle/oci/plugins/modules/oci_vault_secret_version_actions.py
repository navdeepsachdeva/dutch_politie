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
module: oci_vault_secret_version_actions
description: >-
    Due to size constraints we have not included the documentation in the module. Please check L(here,
    https://docs.oracle.com/en-us/iaas/tools/oci-ansible-collection/latest/collections/oracle/oci/oci_vault_secret_version_actions_module.html)
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
    from oci.vault import VaultsClient
    from oci.vault.models import ScheduleSecretVersionDeletionDetails

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


class SecretVersionActionsHelperGen(OCIActionsHelperBase):
    """
    Supported actions:
        cancel_secret_version_deletion
        schedule_secret_version_deletion
    """

    @staticmethod
    def get_module_resource_id_param():
        return "secret_version_number"

    def get_module_resource_id(self):
        return self.module.params.get("secret_version_number")

    def get_get_fn(self):
        return self.client.get_secret_version

    def get_resource(self):
        return oci_common_utils.call_with_backoff(
            self.client.get_secret_version,
            secret_id=self.module.params.get("secret_id"),
            secret_version_number=self.module.params.get("secret_version_number"),
        )

    def cancel_secret_version_deletion(self):
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.cancel_secret_version_deletion,
            call_fn_args=(),
            call_fn_kwargs=dict(
                secret_id=self.module.params.get("secret_id"),
                secret_version_number=self.module.params.get("secret_version_number"),
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

    def schedule_secret_version_deletion(self):
        action_details = oci_common_utils.convert_input_data_to_model_class(
            self.module.params, ScheduleSecretVersionDeletionDetails
        )
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.schedule_secret_version_deletion,
            call_fn_args=(),
            call_fn_kwargs=dict(
                secret_id=self.module.params.get("secret_id"),
                secret_version_number=self.module.params.get("secret_version_number"),
                schedule_secret_version_deletion_details=action_details,
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


SecretVersionActionsHelperCustom = get_custom_class("SecretVersionActionsHelperCustom")


class ResourceHelper(SecretVersionActionsHelperCustom, SecretVersionActionsHelperGen):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec(
        supports_create=False, supports_wait=False
    )
    module_args.update(
        dict(
            secret_id=dict(type="str", required=True),
            secret_version_number=dict(type="int", required=True, no_log=True),
            time_of_deletion=dict(type="str"),
            action=dict(
                type="str",
                required=True,
                choices=[
                    "cancel_secret_version_deletion",
                    "schedule_secret_version_deletion",
                ],
            ),
        )
    )

    module = OCIAnsibleModule(argument_spec=module_args, supports_check_mode=True)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_helper = ResourceHelper(
        module=module,
        resource_type="secret_version",
        service_client_class=VaultsClient,
        namespace="vault",
    )

    result = resource_helper.perform_action(module.params.get("action"))

    module.exit_json(**result)


if __name__ == "__main__":
    main()
