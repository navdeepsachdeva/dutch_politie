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
module: oci_waas_human_interaction_challenge
description: >-
    Due to size constraints we have not included the documentation in the module. Please check L(here,
    https://docs.oracle.com/en-us/iaas/tools/oci-ansible-collection/latest/collections/oracle/oci/oci_waas_human_interaction_challenge_module.html)
    for the module documentation.
author: Oracle (@oracle)
"""


from ansible_collections.oracle.oci.plugins.module_utils import (
    oci_common_utils,
    oci_wait_utils,
)
from ansible_collections.oracle.oci.plugins.module_utils.oci_resource_utils import (
    OCIResourceHelperBase,
    get_custom_class,
    OCIAnsibleModule,
)

try:
    from oci.waas import WaasClient
    from oci.waas.models import HumanInteractionChallenge

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


class HumanInteractionChallengeHelperGen(OCIResourceHelperBase):
    """Supported operations: update and get"""

    def get_possible_entity_types(self):
        return super(
            HumanInteractionChallengeHelperGen, self
        ).get_possible_entity_types() + [
            "humaninteractionchallenge",
            "humaninteractionchallenges",
            "waashumaninteractionchallenge",
            "waashumaninteractionchallenges",
            "humaninteractionchallengeresource",
            "humaninteractionchallengesresource",
            "waas",
        ]

    def get_module_resource_id_param(self):
        return "waas_policy_id"

    def get_module_resource_id(self):
        return self.module.params.get("waas_policy_id")

    def get_get_fn(self):
        return self.client.get_human_interaction_challenge

    def get_resource(self):
        return oci_common_utils.call_with_backoff(
            self.client.get_human_interaction_challenge,
            waas_policy_id=self.module.params.get("waas_policy_id"),
        )

    def get_update_model_class(self):
        return HumanInteractionChallenge

    def update_resource(self):
        update_details = self.get_update_model()
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.update_human_interaction_challenge,
            call_fn_args=(),
            call_fn_kwargs=dict(
                waas_policy_id=self.module.params.get("waas_policy_id"),
                update_human_interaction_challenge_details=update_details,
            ),
            waiter_type=oci_wait_utils.WORK_REQUEST_WAITER_KEY,
            operation=oci_common_utils.UPDATE_OPERATION_KEY,
            waiter_client=self.get_waiter_client(),
            resource_helper=self,
            wait_for_states=oci_common_utils.get_work_request_completed_states(),
        )


HumanInteractionChallengeHelperCustom = get_custom_class(
    "HumanInteractionChallengeHelperCustom"
)


class ResourceHelper(
    HumanInteractionChallengeHelperCustom, HumanInteractionChallengeHelperGen
):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec(
        supports_create=False, supports_wait=True
    )
    module_args.update(
        dict(
            waas_policy_id=dict(aliases=["id"], type="str", required=True),
            is_enabled=dict(type="bool", required=True),
            action=dict(type="str", choices=["DETECT", "BLOCK"]),
            failure_threshold=dict(type="int"),
            action_expiration_in_seconds=dict(type="int"),
            failure_threshold_expiration_in_seconds=dict(type="int"),
            interaction_threshold=dict(type="int"),
            recording_period_in_seconds=dict(type="int"),
            set_http_header=dict(
                type="dict",
                options=dict(
                    name=dict(type="str", required=True),
                    value=dict(type="str", required=True),
                ),
            ),
            challenge_settings=dict(
                type="dict",
                options=dict(
                    block_action=dict(
                        type="str",
                        choices=[
                            "SET_RESPONSE_CODE",
                            "SHOW_ERROR_PAGE",
                            "SHOW_CAPTCHA",
                        ],
                    ),
                    block_response_code=dict(type="int"),
                    block_error_page_message=dict(type="str"),
                    block_error_page_description=dict(type="str"),
                    block_error_page_code=dict(type="str"),
                    captcha_title=dict(type="str"),
                    captcha_header=dict(type="str"),
                    captcha_footer=dict(type="str"),
                    captcha_submit_label=dict(type="str"),
                ),
            ),
            is_nat_enabled=dict(type="bool"),
            state=dict(type="str", default="present", choices=["present"]),
        )
    )

    module = OCIAnsibleModule(argument_spec=module_args, supports_check_mode=True)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_helper = ResourceHelper(
        module=module,
        resource_type="human_interaction_challenge",
        service_client_class=WaasClient,
        namespace="waas",
    )

    result = dict(changed=False)

    if resource_helper.is_update():
        result = resource_helper.update()

    module.exit_json(**result)


if __name__ == "__main__":
    main()
