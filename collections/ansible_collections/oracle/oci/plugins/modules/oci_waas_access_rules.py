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
module: oci_waas_access_rules
description: >-
    Due to size constraints we have not included the documentation in the module. Please check L(here,
    https://docs.oracle.com/en-us/iaas/tools/oci-ansible-collection/latest/collections/oracle/oci/oci_waas_access_rules_module.html)
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
    from oci.waas.models import AccessRule

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


class AccessRulesHelperGen(OCIResourceHelperBase):
    """Supported operations: update and list"""

    def get_default_module_wait_timeout(self):
        return 7200

    def get_possible_entity_types(self):
        return super(AccessRulesHelperGen, self).get_possible_entity_types() + [
            "accessrules",
            "accessrule",
            "waasaccessrules",
            "waasaccessrule",
            "accessrulesresource",
            "accessruleresource",
            "waas",
        ]

    def get_module_resource_id_param(self):
        return "waas_policy_id"

    def get_module_resource_id(self):
        return self.module.params.get("waas_policy_id")

    def get_resource(self):
        resources = self.list_resources()
        for resource in resources:
            if self.get_module_resource_id() == resource.id:
                return oci_common_utils.get_default_response_from_resource(resource)

        oci_common_utils.raise_does_not_exist_service_error()

    def get_required_kwargs_for_list(self):
        required_list_method_params = [
            "waas_policy_id",
        ]

        return dict(
            (param, self.module.params[param]) for param in required_list_method_params
        )

    def get_optional_kwargs_for_list(self):
        return dict()

    def list_resources(self):

        required_kwargs = self.get_required_kwargs_for_list()
        optional_kwargs = self.get_optional_kwargs_for_list()
        kwargs = oci_common_utils.merge_dicts(required_kwargs, optional_kwargs)
        return oci_common_utils.list_all_resources(
            self.client.list_access_rules, **kwargs
        )

    def get_update_model_class(self):
        return AccessRule

    def get_update_model(self):
        if self.module.params.get("access_rules"):
            return [
                oci_common_utils.convert_input_data_to_model_class(
                    resource, self.get_update_model_class()
                )
                for resource in self.module.params["access_rules"]
            ]
        return []

    def update_resource(self):
        update_details = self.get_update_model()
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.update_access_rules,
            call_fn_args=(),
            call_fn_kwargs=dict(
                waas_policy_id=self.module.params.get("waas_policy_id"),
                access_rules=update_details,
            ),
            waiter_type=oci_wait_utils.WORK_REQUEST_WAITER_KEY,
            operation=oci_common_utils.UPDATE_OPERATION_KEY,
            waiter_client=self.get_waiter_client(),
            resource_helper=self,
            wait_for_states=oci_common_utils.get_work_request_completed_states(),
        )


AccessRulesHelperCustom = get_custom_class("AccessRulesHelperCustom")


class ResourceHelper(AccessRulesHelperCustom, AccessRulesHelperGen):
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
                required=True,
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
            state=dict(type="str", default="present", choices=["present"]),
        )
    )

    module = OCIAnsibleModule(argument_spec=module_args, supports_check_mode=True)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_helper = ResourceHelper(
        module=module,
        resource_type="access_rules",
        service_client_class=WaasClient,
        namespace="waas",
    )

    result = dict(changed=False)

    if resource_helper.is_update():
        result = resource_helper.update()

    module.exit_json(**result)


if __name__ == "__main__":
    main()
