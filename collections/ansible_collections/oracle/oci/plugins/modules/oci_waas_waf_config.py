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
module: oci_waas_waf_config
description: >-
    Due to size constraints we have not included the documentation in the module. Please check L(here,
    https://docs.oracle.com/en-us/iaas/tools/oci-ansible-collection/latest/collections/oracle/oci/oci_waas_waf_config_module.html)
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
    from oci.waas.models import WafConfig

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


class WafConfigHelperGen(OCIResourceHelperBase):
    """Supported operations: update and get"""

    def get_default_module_wait_timeout(self):
        return 7200

    def get_possible_entity_types(self):
        return super(WafConfigHelperGen, self).get_possible_entity_types() + [
            "wafconfig",
            "wafconfigs",
            "waaswafconfig",
            "waaswafconfigs",
            "wafconfigresource",
            "wafconfigsresource",
            "waas",
        ]

    def get_module_resource_id_param(self):
        return "waas_policy_id"

    def get_module_resource_id(self):
        return self.module.params.get("waas_policy_id")

    def get_get_fn(self):
        return self.client.get_waf_config

    def get_resource(self):
        return oci_common_utils.call_with_backoff(
            self.client.get_waf_config,
            waas_policy_id=self.module.params.get("waas_policy_id"),
        )

    def get_update_model_class(self):
        return WafConfig

    def update_resource(self):
        update_details = self.get_update_model()
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.update_waf_config,
            call_fn_args=(),
            call_fn_kwargs=dict(
                waas_policy_id=self.module.params.get("waas_policy_id"),
                update_waf_config_details=update_details,
            ),
            waiter_type=oci_wait_utils.WORK_REQUEST_WAITER_KEY,
            operation=oci_common_utils.UPDATE_OPERATION_KEY,
            waiter_client=self.get_waiter_client(),
            resource_helper=self,
            wait_for_states=oci_common_utils.get_work_request_completed_states(),
        )


WafConfigHelperCustom = get_custom_class("WafConfigHelperCustom")


class ResourceHelper(WafConfigHelperCustom, WafConfigHelperGen):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec(
        supports_create=False, supports_wait=True
    )
    module_args.update(
        dict(
            waas_policy_id=dict(aliases=["id"], type="str", required=True),
            access_rules=dict(
                type="list",
                elements="dict",
                options=dict(
                    name=dict(type="str", required=True),
                    criteria=dict(
                        type="list",
                        elements="dict",
                        required=True,
                        options=dict(
                            condition=dict(
                                type="str",
                                required=True,
                                choices=[
                                    "URL_IS",
                                    "URL_IS_NOT",
                                    "URL_STARTS_WITH",
                                    "URL_PART_ENDS_WITH",
                                    "URL_PART_CONTAINS",
                                    "URL_REGEX",
                                    "URL_DOES_NOT_MATCH_REGEX",
                                    "URL_DOES_NOT_START_WITH",
                                    "URL_PART_DOES_NOT_CONTAIN",
                                    "URL_PART_DOES_NOT_END_WITH",
                                    "IP_IS",
                                    "IP_IS_NOT",
                                    "IP_IN_LIST",
                                    "IP_NOT_IN_LIST",
                                    "HTTP_HEADER_CONTAINS",
                                    "HTTP_METHOD_IS",
                                    "HTTP_METHOD_IS_NOT",
                                    "COUNTRY_IS",
                                    "COUNTRY_IS_NOT",
                                    "USER_AGENT_IS",
                                    "USER_AGENT_IS_NOT",
                                ],
                            ),
                            value=dict(type="str", required=True),
                            is_case_sensitive=dict(type="bool"),
                        ),
                    ),
                    action=dict(
                        type="str",
                        required=True,
                        choices=[
                            "ALLOW",
                            "DETECT",
                            "BLOCK",
                            "BYPASS",
                            "REDIRECT",
                            "SHOW_CAPTCHA",
                        ],
                    ),
                    block_action=dict(
                        type="str", choices=["SET_RESPONSE_CODE", "SHOW_ERROR_PAGE"]
                    ),
                    block_response_code=dict(type="int"),
                    block_error_page_message=dict(type="str"),
                    block_error_page_code=dict(type="str"),
                    block_error_page_description=dict(type="str"),
                    bypass_challenges=dict(
                        type="list",
                        elements="str",
                        choices=[
                            "JS_CHALLENGE",
                            "DEVICE_FINGERPRINT_CHALLENGE",
                            "HUMAN_INTERACTION_CHALLENGE",
                            "CAPTCHA",
                        ],
                        no_log=True,
                    ),
                    redirect_url=dict(type="str"),
                    redirect_response_code=dict(
                        type="str", choices=["MOVED_PERMANENTLY", "FOUND"]
                    ),
                    captcha_title=dict(type="str"),
                    captcha_header=dict(type="str"),
                    captcha_footer=dict(type="str"),
                    captcha_submit_label=dict(type="str"),
                    response_header_manipulation=dict(
                        type="list",
                        elements="dict",
                        options=dict(
                            value=dict(type="str"),
                            action=dict(
                                type="str",
                                required=True,
                                choices=[
                                    "EXTEND_HTTP_RESPONSE_HEADER",
                                    "ADD_HTTP_RESPONSE_HEADER",
                                    "REMOVE_HTTP_RESPONSE_HEADER",
                                ],
                            ),
                            header=dict(type="str", required=True),
                        ),
                    ),
                ),
            ),
            address_rate_limiting=dict(
                type="dict",
                options=dict(
                    is_enabled=dict(type="bool", required=True),
                    allowed_rate_per_address=dict(type="int"),
                    max_delayed_count_per_address=dict(type="int"),
                    block_response_code=dict(type="int"),
                ),
            ),
            captchas=dict(
                type="list",
                elements="dict",
                options=dict(
                    url=dict(type="str", required=True),
                    session_expiration_in_seconds=dict(type="int", required=True),
                    title=dict(type="str", required=True),
                    header_text=dict(type="str"),
                    footer_text=dict(type="str"),
                    failure_message=dict(type="str", required=True),
                    submit_label=dict(type="str", required=True),
                ),
            ),
            device_fingerprint_challenge=dict(
                type="dict",
                options=dict(
                    is_enabled=dict(type="bool", required=True),
                    action=dict(type="str", choices=["DETECT", "BLOCK"]),
                    failure_threshold=dict(type="int"),
                    action_expiration_in_seconds=dict(type="int"),
                    failure_threshold_expiration_in_seconds=dict(type="int"),
                    max_address_count=dict(type="int"),
                    max_address_count_expiration_in_seconds=dict(type="int"),
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
                ),
            ),
            good_bots=dict(
                type="list",
                elements="dict",
                options=dict(
                    key=dict(type="str", required=True, no_log=True),
                    name=dict(type="str"),
                    is_enabled=dict(type="bool", required=True),
                    description=dict(type="str"),
                ),
            ),
            human_interaction_challenge=dict(
                type="dict",
                options=dict(
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
                ),
            ),
            js_challenge=dict(
                type="dict",
                options=dict(
                    is_enabled=dict(type="bool", required=True),
                    action=dict(type="str", choices=["DETECT", "BLOCK"]),
                    failure_threshold=dict(type="int"),
                    action_expiration_in_seconds=dict(type="int"),
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
                    are_redirects_challenged=dict(type="bool"),
                    criteria=dict(
                        type="list",
                        elements="dict",
                        options=dict(
                            condition=dict(
                                type="str",
                                required=True,
                                choices=[
                                    "URL_IS",
                                    "URL_IS_NOT",
                                    "URL_STARTS_WITH",
                                    "URL_PART_ENDS_WITH",
                                    "URL_PART_CONTAINS",
                                    "URL_REGEX",
                                    "URL_DOES_NOT_MATCH_REGEX",
                                    "URL_DOES_NOT_START_WITH",
                                    "URL_PART_DOES_NOT_CONTAIN",
                                    "URL_PART_DOES_NOT_END_WITH",
                                    "IP_IS",
                                    "IP_IS_NOT",
                                    "IP_IN_LIST",
                                    "IP_NOT_IN_LIST",
                                    "HTTP_HEADER_CONTAINS",
                                    "HTTP_METHOD_IS",
                                    "HTTP_METHOD_IS_NOT",
                                    "COUNTRY_IS",
                                    "COUNTRY_IS_NOT",
                                    "USER_AGENT_IS",
                                    "USER_AGENT_IS_NOT",
                                ],
                            ),
                            value=dict(type="str", required=True),
                            is_case_sensitive=dict(type="bool"),
                        ),
                    ),
                    is_nat_enabled=dict(type="bool"),
                ),
            ),
            origin=dict(type="str"),
            caching_rules=dict(
                type="list",
                elements="dict",
                options=dict(
                    key=dict(type="str", no_log=True),
                    name=dict(type="str", required=True),
                    action=dict(
                        type="str", required=True, choices=["CACHE", "BYPASS_CACHE"]
                    ),
                    caching_duration=dict(type="str"),
                    is_client_caching_enabled=dict(type="bool"),
                    client_caching_duration=dict(type="str"),
                    criteria=dict(
                        type="list",
                        elements="dict",
                        required=True,
                        options=dict(
                            condition=dict(
                                type="str",
                                required=True,
                                choices=[
                                    "URL_IS",
                                    "URL_STARTS_WITH",
                                    "URL_PART_ENDS_WITH",
                                    "URL_PART_CONTAINS",
                                ],
                            ),
                            value=dict(type="str", required=True),
                        ),
                    ),
                ),
            ),
            custom_protection_rules=dict(
                type="list",
                elements="dict",
                options=dict(
                    id=dict(type="str"),
                    action=dict(type="str", choices=["DETECT", "BLOCK"]),
                    exclusions=dict(
                        type="list",
                        elements="dict",
                        options=dict(
                            target=dict(
                                type="str",
                                choices=[
                                    "REQUEST_COOKIES",
                                    "REQUEST_COOKIE_NAMES",
                                    "ARGS",
                                    "ARGS_NAMES",
                                ],
                            ),
                            exclusions=dict(type="list", elements="str"),
                        ),
                    ),
                ),
            ),
            origin_groups=dict(type="list", elements="str"),
            protection_rules=dict(
                type="list",
                elements="dict",
                options=dict(
                    key=dict(type="str", no_log=True),
                    mod_security_rule_ids=dict(type="list", elements="str"),
                    name=dict(type="str"),
                    description=dict(type="str"),
                    action=dict(type="str", choices=["OFF", "DETECT", "BLOCK"]),
                    labels=dict(type="list", elements="str"),
                    exclusions=dict(
                        type="list",
                        elements="dict",
                        options=dict(
                            target=dict(
                                type="str",
                                choices=[
                                    "REQUEST_COOKIES",
                                    "REQUEST_COOKIE_NAMES",
                                    "ARGS",
                                    "ARGS_NAMES",
                                ],
                            ),
                            exclusions=dict(type="list", elements="str"),
                        ),
                    ),
                ),
            ),
            protection_settings=dict(
                type="dict",
                options=dict(
                    block_action=dict(
                        type="str", choices=["SHOW_ERROR_PAGE", "SET_RESPONSE_CODE"]
                    ),
                    block_response_code=dict(type="int"),
                    block_error_page_message=dict(type="str"),
                    block_error_page_code=dict(type="str"),
                    block_error_page_description=dict(type="str"),
                    max_argument_count=dict(type="int"),
                    max_name_length_per_argument=dict(type="int"),
                    max_total_name_length_of_arguments=dict(type="int"),
                    recommendations_period_in_days=dict(type="int"),
                    is_response_inspected=dict(type="bool"),
                    max_response_size_in_ki_b=dict(type="int"),
                    allowed_http_methods=dict(
                        type="list",
                        elements="str",
                        choices=[
                            "OPTIONS",
                            "GET",
                            "HEAD",
                            "POST",
                            "PUT",
                            "DELETE",
                            "TRACE",
                            "CONNECT",
                            "PATCH",
                            "PROPFIND",
                        ],
                    ),
                    media_types=dict(type="list", elements="str"),
                ),
            ),
            threat_feeds=dict(
                type="list",
                elements="dict",
                options=dict(
                    key=dict(type="str", no_log=True),
                    name=dict(type="str"),
                    action=dict(type="str", choices=["OFF", "DETECT", "BLOCK"]),
                    description=dict(type="str"),
                ),
            ),
            whitelists=dict(
                type="list",
                elements="dict",
                options=dict(
                    name=dict(type="str", required=True),
                    addresses=dict(type="list", elements="str"),
                    address_lists=dict(type="list", elements="str"),
                ),
            ),
            state=dict(type="str", default="present", choices=["present"]),
        )
    )

    module = OCIAnsibleModule(argument_spec=module_args, supports_check_mode=True)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_helper = ResourceHelper(
        module=module,
        resource_type="waf_config",
        service_client_class=WaasClient,
        namespace="waas",
    )

    result = dict(changed=False)

    if resource_helper.is_update():
        result = resource_helper.update()

    module.exit_json(**result)


if __name__ == "__main__":
    main()
