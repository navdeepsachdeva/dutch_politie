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
module: oci_waas_protection_rules
description: >-
    Due to size constraints we have not included the documentation in the module. Please check L(here,
    https://docs.oracle.com/en-us/iaas/tools/oci-ansible-collection/latest/collections/oracle/oci/oci_waas_protection_rules_module.html)
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
    from oci.waas.models import ProtectionRuleAction

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


class ProtectionRulesHelperGen(OCIResourceHelperBase):
    """Supported operations: update, get and list"""

    def get_default_module_wait_timeout(self):
        return 7200

    def get_possible_entity_types(self):
        return super(ProtectionRulesHelperGen, self).get_possible_entity_types() + [
            "protectionrules",
            "protectionrule",
            "waasprotectionrules",
            "waasprotectionrule",
            "protectionrulesresource",
            "protectionruleresource",
            "waas",
        ]

    def get_module_resource_id_param(self):
        return "waas_policy_id"

    def get_module_resource_id(self):
        return self.module.params.get("waas_policy_id")

    def get_get_fn(self):
        return self.client.get_protection_rule

    def get_resource(self):
        return oci_common_utils.get_default_response_from_resource(
            oci_common_utils.list_all_resources(
                self.client.get_protection_rule,
                waas_policy_id=self.module.params.get("waas_policy_id"),
                protection_rule_key=self.module.params.get("protection_rule_key"),
            )
        )

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
            self.client.list_protection_rules, **kwargs
        )

    def get_update_model_class(self):
        return ProtectionRuleAction

    def get_update_model(self):
        if self.module.params.get("protection_rules"):
            return [
                oci_common_utils.convert_input_data_to_model_class(
                    resource, self.get_update_model_class()
                )
                for resource in self.module.params["protection_rules"]
            ]
        return []

    def update_resource(self):
        update_details = self.get_update_model()
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.update_protection_rules,
            call_fn_args=(),
            call_fn_kwargs=dict(
                waas_policy_id=self.module.params.get("waas_policy_id"),
                protection_rules=update_details,
            ),
            waiter_type=oci_wait_utils.WORK_REQUEST_WAITER_KEY,
            operation=oci_common_utils.UPDATE_OPERATION_KEY,
            waiter_client=self.get_waiter_client(),
            resource_helper=self,
            wait_for_states=oci_common_utils.get_work_request_completed_states(),
        )


ProtectionRulesHelperCustom = get_custom_class("ProtectionRulesHelperCustom")


class ResourceHelper(ProtectionRulesHelperCustom, ProtectionRulesHelperGen):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec(
        supports_create=False, supports_wait=True
    )
    module_args.update(
        dict(
            waas_policy_id=dict(aliases=["id"], type="str", required=True),
            protection_rules=dict(
                type="list",
                elements="dict",
                required=True,
                options=dict(
                    key=dict(type="str", required=True, no_log=True),
                    action=dict(
                        type="str", required=True, choices=["OFF", "DETECT", "BLOCK"]
                    ),
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
            state=dict(type="str", default="present", choices=["present"]),
        )
    )

    module = OCIAnsibleModule(argument_spec=module_args, supports_check_mode=True)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_helper = ResourceHelper(
        module=module,
        resource_type="protection_rules",
        service_client_class=WaasClient,
        namespace="waas",
    )

    result = dict(changed=False)

    if resource_helper.is_update():
        result = resource_helper.update()

    module.exit_json(**result)


if __name__ == "__main__":
    main()
