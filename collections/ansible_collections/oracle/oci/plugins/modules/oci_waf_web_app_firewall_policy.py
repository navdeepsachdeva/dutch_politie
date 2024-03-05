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
module: oci_waf_web_app_firewall_policy
description: >-
    Due to size constraints we have not included the documentation in the module. Please check L(here,
    https://docs.oracle.com/en-us/iaas/tools/oci-ansible-collection/latest/collections/oracle/oci/oci_waf_web_app_firewall_policy_module.html)
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
    from oci.waf import WafClient
    from oci.waf.models import CreateWebAppFirewallPolicyDetails
    from oci.waf.models import UpdateWebAppFirewallPolicyDetails

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


class WebAppFirewallPolicyHelperGen(OCIResourceHelperBase):
    """Supported operations: create, update, get, list and delete"""

    def get_possible_entity_types(self):
        return super(
            WebAppFirewallPolicyHelperGen, self
        ).get_possible_entity_types() + [
            "webappfirewallpolicy",
            "webappfirewallpolicies",
            "wafwebappfirewallpolicy",
            "wafwebappfirewallpolicies",
            "webappfirewallpolicyresource",
            "webappfirewallpoliciesresource",
            "waf",
        ]

    def get_module_resource_id_param(self):
        return "web_app_firewall_policy_id"

    def get_module_resource_id(self):
        return self.module.params.get("web_app_firewall_policy_id")

    def get_get_fn(self):
        return self.client.get_web_app_firewall_policy

    def get_get_model_from_summary_model(self, summary_model):
        return oci_common_utils.call_with_backoff(
            self.client.get_web_app_firewall_policy,
            web_app_firewall_policy_id=summary_model.id,
        ).data

    def get_resource(self):
        return oci_common_utils.call_with_backoff(
            self.client.get_web_app_firewall_policy,
            web_app_firewall_policy_id=self.module.params.get(
                "web_app_firewall_policy_id"
            ),
        )

    def get_required_kwargs_for_list(self):
        required_list_method_params = [
            "compartment_id",
        ]

        return dict(
            (param, self.module.params[param]) for param in required_list_method_params
        )

    def get_optional_kwargs_for_list(self):
        optional_list_method_params = ["display_name"]

        return dict(
            (param, self.module.params[param])
            for param in optional_list_method_params
            if self.module.params.get(param) is not None
            and (
                self._use_name_as_identifier()
                or (
                    not self.module.params.get("key_by")
                    or param in self.module.params.get("key_by")
                )
            )
        )

    def list_resources(self):

        required_kwargs = self.get_required_kwargs_for_list()
        optional_kwargs = self.get_optional_kwargs_for_list()
        kwargs = oci_common_utils.merge_dicts(required_kwargs, optional_kwargs)
        return oci_common_utils.list_all_resources(
            self.client.list_web_app_firewall_policies, **kwargs
        )

    def get_create_model_class(self):
        return CreateWebAppFirewallPolicyDetails

    def create_resource(self):
        create_details = self.get_create_model()
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.create_web_app_firewall_policy,
            call_fn_args=(),
            call_fn_kwargs=dict(create_web_app_firewall_policy_details=create_details,),
            waiter_type=oci_wait_utils.WORK_REQUEST_WAITER_KEY,
            operation=oci_common_utils.CREATE_OPERATION_KEY,
            waiter_client=self.get_waiter_client(),
            resource_helper=self,
            wait_for_states=oci_common_utils.get_work_request_completed_states(),
        )

    def get_update_model_class(self):
        return UpdateWebAppFirewallPolicyDetails

    def update_resource(self):
        update_details = self.get_update_model()
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.update_web_app_firewall_policy,
            call_fn_args=(),
            call_fn_kwargs=dict(
                web_app_firewall_policy_id=self.module.params.get(
                    "web_app_firewall_policy_id"
                ),
                update_web_app_firewall_policy_details=update_details,
            ),
            waiter_type=oci_wait_utils.WORK_REQUEST_WAITER_KEY,
            operation=oci_common_utils.UPDATE_OPERATION_KEY,
            waiter_client=self.get_waiter_client(),
            resource_helper=self,
            wait_for_states=oci_common_utils.get_work_request_completed_states(),
        )

    def delete_resource(self):
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.delete_web_app_firewall_policy,
            call_fn_args=(),
            call_fn_kwargs=dict(
                web_app_firewall_policy_id=self.module.params.get(
                    "web_app_firewall_policy_id"
                ),
            ),
            waiter_type=oci_wait_utils.WORK_REQUEST_WAITER_KEY,
            operation=oci_common_utils.DELETE_OPERATION_KEY,
            waiter_client=self.get_waiter_client(),
            resource_helper=self,
            wait_for_states=oci_common_utils.get_work_request_completed_states(),
        )


WebAppFirewallPolicyHelperCustom = get_custom_class("WebAppFirewallPolicyHelperCustom")


class ResourceHelper(WebAppFirewallPolicyHelperCustom, WebAppFirewallPolicyHelperGen):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec(
        supports_create=True, supports_wait=True
    )
    module_args.update(
        dict(
            compartment_id=dict(type="str"),
            display_name=dict(aliases=["name"], type="str"),
            actions=dict(
                type="list",
                elements="dict",
                options=dict(
                    code=dict(type="int"),
                    headers=dict(
                        type="list",
                        elements="dict",
                        options=dict(
                            name=dict(type="str", required=True),
                            value=dict(type="str", required=True),
                        ),
                    ),
                    body=dict(
                        type="dict",
                        options=dict(
                            type=dict(
                                type="str", required=True, choices=["STATIC_TEXT"]
                            ),
                            text=dict(type="str", required=True),
                        ),
                    ),
                    type=dict(
                        type="str",
                        required=True,
                        choices=["RETURN_HTTP_RESPONSE", "ALLOW", "CHECK"],
                    ),
                    name=dict(type="str", required=True),
                ),
            ),
            request_access_control=dict(
                type="dict",
                options=dict(
                    default_action_name=dict(type="str", required=True),
                    rules=dict(
                        type="list",
                        elements="dict",
                        options=dict(
                            type=dict(
                                type="str",
                                required=True,
                                choices=[
                                    "ACCESS_CONTROL",
                                    "PROTECTION",
                                    "REQUEST_RATE_LIMITING",
                                ],
                            ),
                            name=dict(type="str", required=True),
                            condition_language=dict(type="str", choices=["JMESPATH"]),
                            condition=dict(type="str"),
                            action_name=dict(type="str", required=True),
                        ),
                    ),
                ),
            ),
            request_rate_limiting=dict(
                type="dict",
                options=dict(
                    rules=dict(
                        type="list",
                        elements="dict",
                        options=dict(
                            type=dict(
                                type="str",
                                required=True,
                                choices=[
                                    "ACCESS_CONTROL",
                                    "PROTECTION",
                                    "REQUEST_RATE_LIMITING",
                                ],
                            ),
                            name=dict(type="str", required=True),
                            condition_language=dict(type="str", choices=["JMESPATH"]),
                            condition=dict(type="str"),
                            action_name=dict(type="str", required=True),
                            configurations=dict(
                                type="list",
                                elements="dict",
                                required=True,
                                options=dict(
                                    period_in_seconds=dict(type="int", required=True),
                                    requests_limit=dict(type="int", required=True),
                                    action_duration_in_seconds=dict(type="int"),
                                ),
                            ),
                        ),
                    )
                ),
            ),
            request_protection=dict(
                type="dict",
                options=dict(
                    rules=dict(
                        type="list",
                        elements="dict",
                        options=dict(
                            type=dict(
                                type="str",
                                required=True,
                                choices=[
                                    "ACCESS_CONTROL",
                                    "PROTECTION",
                                    "REQUEST_RATE_LIMITING",
                                ],
                            ),
                            name=dict(type="str", required=True),
                            condition_language=dict(type="str", choices=["JMESPATH"]),
                            condition=dict(type="str"),
                            action_name=dict(type="str", required=True),
                            protection_capabilities=dict(
                                type="list",
                                elements="dict",
                                required=True,
                                options=dict(
                                    key=dict(type="str", required=True, no_log=True),
                                    version=dict(type="int", required=True),
                                    exclusions=dict(
                                        type="dict",
                                        options=dict(
                                            request_cookies=dict(
                                                type="list", elements="str"
                                            ),
                                            args=dict(type="list", elements="str"),
                                        ),
                                    ),
                                    action_name=dict(type="str"),
                                    collaborative_action_threshold=dict(type="int"),
                                    collaborative_weights=dict(
                                        type="list",
                                        elements="dict",
                                        options=dict(
                                            key=dict(
                                                type="str", required=True, no_log=True
                                            ),
                                            weight=dict(type="int", required=True),
                                        ),
                                    ),
                                ),
                            ),
                            protection_capability_settings=dict(
                                type="dict",
                                options=dict(
                                    max_number_of_arguments=dict(type="int"),
                                    max_single_argument_length=dict(type="int"),
                                    max_total_argument_length=dict(type="int"),
                                    max_http_request_headers=dict(type="int"),
                                    max_http_request_header_length=dict(type="int"),
                                    allowed_http_methods=dict(
                                        type="list", elements="str"
                                    ),
                                ),
                            ),
                            is_body_inspection_enabled=dict(type="bool"),
                        ),
                    ),
                    body_inspection_size_limit_in_bytes=dict(type="int"),
                    body_inspection_size_limit_exceeded_action_name=dict(type="str"),
                ),
            ),
            response_access_control=dict(
                type="dict",
                options=dict(
                    rules=dict(
                        type="list",
                        elements="dict",
                        options=dict(
                            type=dict(
                                type="str",
                                required=True,
                                choices=[
                                    "ACCESS_CONTROL",
                                    "PROTECTION",
                                    "REQUEST_RATE_LIMITING",
                                ],
                            ),
                            name=dict(type="str", required=True),
                            condition_language=dict(type="str", choices=["JMESPATH"]),
                            condition=dict(type="str"),
                            action_name=dict(type="str", required=True),
                        ),
                    )
                ),
            ),
            response_protection=dict(
                type="dict",
                options=dict(
                    rules=dict(
                        type="list",
                        elements="dict",
                        options=dict(
                            type=dict(
                                type="str",
                                required=True,
                                choices=[
                                    "ACCESS_CONTROL",
                                    "PROTECTION",
                                    "REQUEST_RATE_LIMITING",
                                ],
                            ),
                            name=dict(type="str", required=True),
                            condition_language=dict(type="str", choices=["JMESPATH"]),
                            condition=dict(type="str"),
                            action_name=dict(type="str", required=True),
                            protection_capabilities=dict(
                                type="list",
                                elements="dict",
                                required=True,
                                options=dict(
                                    key=dict(type="str", required=True, no_log=True),
                                    version=dict(type="int", required=True),
                                    exclusions=dict(
                                        type="dict",
                                        options=dict(
                                            request_cookies=dict(
                                                type="list", elements="str"
                                            ),
                                            args=dict(type="list", elements="str"),
                                        ),
                                    ),
                                    action_name=dict(type="str"),
                                    collaborative_action_threshold=dict(type="int"),
                                    collaborative_weights=dict(
                                        type="list",
                                        elements="dict",
                                        options=dict(
                                            key=dict(
                                                type="str", required=True, no_log=True
                                            ),
                                            weight=dict(type="int", required=True),
                                        ),
                                    ),
                                ),
                            ),
                            protection_capability_settings=dict(
                                type="dict",
                                options=dict(
                                    max_number_of_arguments=dict(type="int"),
                                    max_single_argument_length=dict(type="int"),
                                    max_total_argument_length=dict(type="int"),
                                    max_http_request_headers=dict(type="int"),
                                    max_http_request_header_length=dict(type="int"),
                                    allowed_http_methods=dict(
                                        type="list", elements="str"
                                    ),
                                ),
                            ),
                            is_body_inspection_enabled=dict(type="bool"),
                        ),
                    )
                ),
            ),
            freeform_tags=dict(type="dict"),
            defined_tags=dict(type="dict"),
            system_tags=dict(type="dict"),
            web_app_firewall_policy_id=dict(aliases=["id"], type="str"),
            state=dict(type="str", default="present", choices=["present", "absent"]),
        )
    )

    module = OCIAnsibleModule(argument_spec=module_args, supports_check_mode=True)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_helper = ResourceHelper(
        module=module,
        resource_type="web_app_firewall_policy",
        service_client_class=WafClient,
        namespace="waf",
    )

    result = dict(changed=False)

    if resource_helper.is_delete_using_name():
        result = resource_helper.delete_using_name()
    elif resource_helper.is_delete():
        result = resource_helper.delete()
    elif resource_helper.is_update_using_name():
        result = resource_helper.update_using_name()
    elif resource_helper.is_update():
        result = resource_helper.update()
    elif resource_helper.is_create():
        result = resource_helper.create()

    module.exit_json(**result)


if __name__ == "__main__":
    main()
