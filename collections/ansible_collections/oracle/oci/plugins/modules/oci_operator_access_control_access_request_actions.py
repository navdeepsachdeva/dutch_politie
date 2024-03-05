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
module: oci_operator_access_control_access_request_actions
description: >-
    Due to size constraints we have not included the documentation in the module. Please check L(here,
    https://docs.oracle.com/en-us/iaas/tools/oci-ansible-collection/latest/collections/oracle/oci/oci_operator_access_control_access_request_actions_module.html)
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
    from oci.operator_access_control import AccessRequestsClient
    from oci.operator_access_control.models import ApproveAccessRequestDetails
    from oci.operator_access_control.models import InteractionRequestDetails
    from oci.operator_access_control.models import RejectAccessRequestDetails
    from oci.operator_access_control.models import ReviewAccessRequestDetails
    from oci.operator_access_control.models import RevokeAccessRequestDetails

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


class AccessRequestActionsHelperGen(OCIActionsHelperBase):
    """
    Supported actions:
        approve
        interaction_request
        reject
        review
        revoke
    """

    @staticmethod
    def get_module_resource_id_param():
        return "access_request_id"

    def get_module_resource_id(self):
        return self.module.params.get("access_request_id")

    def get_get_fn(self):
        return self.client.get_access_request

    def get_resource(self):
        return oci_common_utils.call_with_backoff(
            self.client.get_access_request,
            access_request_id=self.module.params.get("access_request_id"),
        )

    def approve(self):
        action_details = oci_common_utils.convert_input_data_to_model_class(
            self.module.params, ApproveAccessRequestDetails
        )
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.approve_access_request,
            call_fn_args=(),
            call_fn_kwargs=dict(
                access_request_id=self.module.params.get("access_request_id"),
                approve_access_request_details=action_details,
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

    def interaction_request(self):
        action_details = oci_common_utils.convert_input_data_to_model_class(
            self.module.params, InteractionRequestDetails
        )
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.interaction_request,
            call_fn_args=(),
            call_fn_kwargs=dict(
                access_request_id=self.module.params.get("access_request_id"),
                interaction_request_details=action_details,
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

    def reject(self):
        action_details = oci_common_utils.convert_input_data_to_model_class(
            self.module.params, RejectAccessRequestDetails
        )
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.reject_access_request,
            call_fn_args=(),
            call_fn_kwargs=dict(
                access_request_id=self.module.params.get("access_request_id"),
                reject_access_request_details=action_details,
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

    def review(self):
        action_details = oci_common_utils.convert_input_data_to_model_class(
            self.module.params, ReviewAccessRequestDetails
        )
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.review_access_request,
            call_fn_args=(),
            call_fn_kwargs=dict(
                access_request_id=self.module.params.get("access_request_id"),
                review_access_request_details=action_details,
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

    def revoke(self):
        action_details = oci_common_utils.convert_input_data_to_model_class(
            self.module.params, RevokeAccessRequestDetails
        )
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.revoke_access_request,
            call_fn_args=(),
            call_fn_kwargs=dict(
                access_request_id=self.module.params.get("access_request_id"),
                revoke_access_request_details=action_details,
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


AccessRequestActionsHelperCustom = get_custom_class("AccessRequestActionsHelperCustom")


class ResourceHelper(AccessRequestActionsHelperCustom, AccessRequestActionsHelperGen):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec(
        supports_create=False, supports_wait=True
    )
    module_args.update(
        dict(
            audit_type=dict(type="list", elements="str"),
            additional_message=dict(type="str"),
            time_of_user_creation=dict(type="str"),
            more_info_details=dict(type="str"),
            access_request_id=dict(aliases=["id"], type="str", required=True),
            approver_comment=dict(type="str"),
            action=dict(
                type="str",
                required=True,
                choices=[
                    "approve",
                    "interaction_request",
                    "reject",
                    "review",
                    "revoke",
                ],
            ),
        )
    )

    module = OCIAnsibleModule(argument_spec=module_args, supports_check_mode=True)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_helper = ResourceHelper(
        module=module,
        resource_type="access_request",
        service_client_class=AccessRequestsClient,
        namespace="operator_access_control",
    )

    result = resource_helper.perform_action(module.params.get("action"))

    module.exit_json(**result)


if __name__ == "__main__":
    main()
