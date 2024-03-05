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
module: oci_limits_quota_actions
description: >-
    Due to size constraints we have not included the documentation in the module. Please check L(here,
    https://docs.oracle.com/en-us/iaas/tools/oci-ansible-collection/latest/collections/oracle/oci/oci_limits_quota_actions_module.html)
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
    from oci.limits import QuotasClient
    from oci.limits.models import AddLockDetails
    from oci.limits.models import RemoveLockDetails

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


class QuotaActionsHelperGen(OCIActionsHelperBase):
    """
    Supported actions:
        add_quota_lock
        remove_quota_lock
    """

    @staticmethod
    def get_module_resource_id_param():
        return "quota_id"

    def get_module_resource_id(self):
        return self.module.params.get("quota_id")

    def get_get_fn(self):
        return self.client.get_quota

    def get_resource(self):
        return oci_common_utils.call_with_backoff(
            self.client.get_quota, quota_id=self.module.params.get("quota_id"),
        )

    def add_quota_lock(self):
        action_details = oci_common_utils.convert_input_data_to_model_class(
            self.module.params, AddLockDetails
        )
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.add_quota_lock,
            call_fn_args=(),
            call_fn_kwargs=dict(
                quota_id=self.module.params.get("quota_id"),
                add_lock_details=action_details,
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

    def remove_quota_lock(self):
        action_details = oci_common_utils.convert_input_data_to_model_class(
            self.module.params, RemoveLockDetails
        )
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.remove_quota_lock,
            call_fn_args=(),
            call_fn_kwargs=dict(
                quota_id=self.module.params.get("quota_id"),
                remove_lock_details=action_details,
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


QuotaActionsHelperCustom = get_custom_class("QuotaActionsHelperCustom")


class ResourceHelper(QuotaActionsHelperCustom, QuotaActionsHelperGen):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec(
        supports_create=False, supports_wait=True
    )
    module_args.update(
        dict(
            related_resource_id=dict(type="str"),
            msg=dict(aliases=["message"], type="str"),
            quota_id=dict(aliases=["id"], type="str", required=True),
            type=dict(type="str", required=True, choices=["FULL", "DELETE"]),
            action=dict(
                type="str",
                required=True,
                choices=["add_quota_lock", "remove_quota_lock"],
            ),
        )
    )

    module = OCIAnsibleModule(argument_spec=module_args, supports_check_mode=True)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_helper = ResourceHelper(
        module=module,
        resource_type="quota",
        service_client_class=QuotasClient,
        namespace="limits",
    )

    result = resource_helper.perform_action(module.params.get("action"))

    module.exit_json(**result)


if __name__ == "__main__":
    main()
