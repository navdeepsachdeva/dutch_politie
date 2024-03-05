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
module: oci_key_management_vault_actions
description: >-
    Due to size constraints we have not included the documentation in the module. Please check L(here,
    https://docs.oracle.com/en-us/iaas/tools/oci-ansible-collection/latest/collections/oracle/oci/oci_key_management_vault_actions_module.html)
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
    from oci.key_management import KmsVaultClient
    from oci.key_management.models import ChangeVaultCompartmentDetails
    from oci.key_management.models import CreateVaultReplicaDetails
    from oci.key_management.models import DeleteVaultReplicaDetails
    from oci.key_management.models import ScheduleVaultDeletionDetails

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


class VaultActionsHelperGen(OCIActionsHelperBase):
    """
    Supported actions:
        cancel_vault_deletion
        change_compartment
        create_vault_replica
        delete_vault_replica
        schedule_vault_deletion
    """

    def get_default_module_wait_timeout(self):
        return 2400

    @staticmethod
    def get_module_resource_id_param():
        return "vault_id"

    def get_module_resource_id(self):
        return self.module.params.get("vault_id")

    def get_get_fn(self):
        return self.client.get_vault

    def get_resource(self):
        return oci_common_utils.call_with_backoff(
            self.client.get_vault, vault_id=self.module.params.get("vault_id"),
        )

    def cancel_vault_deletion(self):
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.cancel_vault_deletion,
            call_fn_args=(),
            call_fn_kwargs=dict(vault_id=self.module.params.get("vault_id"),),
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

    def change_compartment(self):
        action_details = oci_common_utils.convert_input_data_to_model_class(
            self.module.params, ChangeVaultCompartmentDetails
        )
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.change_vault_compartment,
            call_fn_args=(),
            call_fn_kwargs=dict(
                vault_id=self.module.params.get("vault_id"),
                change_vault_compartment_details=action_details,
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

    def create_vault_replica(self):
        action_details = oci_common_utils.convert_input_data_to_model_class(
            self.module.params, CreateVaultReplicaDetails
        )
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.create_vault_replica,
            call_fn_args=(),
            call_fn_kwargs=dict(
                vault_id=self.module.params.get("vault_id"),
                create_vault_replica_details=action_details,
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

    def delete_vault_replica(self):
        action_details = oci_common_utils.convert_input_data_to_model_class(
            self.module.params, DeleteVaultReplicaDetails
        )
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.delete_vault_replica,
            call_fn_args=(),
            call_fn_kwargs=dict(
                vault_id=self.module.params.get("vault_id"),
                delete_vault_replica_details=action_details,
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

    def schedule_vault_deletion(self):
        action_details = oci_common_utils.convert_input_data_to_model_class(
            self.module.params, ScheduleVaultDeletionDetails
        )
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.schedule_vault_deletion,
            call_fn_args=(),
            call_fn_kwargs=dict(
                vault_id=self.module.params.get("vault_id"),
                schedule_vault_deletion_details=action_details,
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


VaultActionsHelperCustom = get_custom_class("VaultActionsHelperCustom")


class ResourceHelper(VaultActionsHelperCustom, VaultActionsHelperGen):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec(
        supports_create=False, supports_wait=True
    )
    module_args.update(
        dict(
            compartment_id=dict(type="str"),
            replica_region=dict(type="str"),
            vault_id=dict(aliases=["id"], type="str", required=True),
            time_of_deletion=dict(type="str"),
            action=dict(
                type="str",
                required=True,
                choices=[
                    "cancel_vault_deletion",
                    "change_compartment",
                    "create_vault_replica",
                    "delete_vault_replica",
                    "schedule_vault_deletion",
                ],
            ),
        )
    )

    module = OCIAnsibleModule(argument_spec=module_args, supports_check_mode=True)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_helper = ResourceHelper(
        module=module,
        resource_type="vault",
        service_client_class=KmsVaultClient,
        namespace="key_management",
    )

    result = resource_helper.perform_action(module.params.get("action"))

    module.exit_json(**result)


if __name__ == "__main__":
    main()
