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
module: oci_waas_protection_rules_facts
description: >-
    Due to size constraints we have not included the documentation in the module. Please check L(here,
    https://docs.oracle.com/en-us/iaas/tools/oci-ansible-collection/latest/collections/oracle/oci/oci_waas_protection_rules_facts_module.html)
    for the module documentation.
author: Oracle (@oracle)
"""


from ansible_collections.oracle.oci.plugins.module_utils import oci_common_utils
from ansible_collections.oracle.oci.plugins.module_utils.oci_resource_utils import (
    OCIResourceFactsHelperBase,
    get_custom_class,
    OCIAnsibleModule,
)

try:
    from oci.waas import WaasClient

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


class ProtectionRulesFactsHelperGen(OCIResourceFactsHelperBase):
    """Supported operations: get, list"""

    def get_required_params_for_get(self):
        return [
            "waas_policy_id",
            "protection_rule_key",
        ]

    def get_required_params_for_list(self):
        return [
            "waas_policy_id",
        ]

    def get_resource(self):
        return oci_common_utils.get_default_response_from_resource(
            oci_common_utils.list_all_resources(
                self.client.get_protection_rule,
                waas_policy_id=self.module.params.get("waas_policy_id"),
                protection_rule_key=self.module.params.get("protection_rule_key"),
            )
        )

    def list_resources(self):
        optional_list_method_params = [
            "mod_security_rule_id",
            "action",
            "name",
        ]
        optional_kwargs = dict(
            (param, self.module.params[param])
            for param in optional_list_method_params
            if self.module.params.get(param) is not None
        )
        return oci_common_utils.list_all_resources(
            self.client.list_protection_rules,
            waas_policy_id=self.module.params.get("waas_policy_id"),
            **optional_kwargs
        )


ProtectionRulesFactsHelperCustom = get_custom_class("ProtectionRulesFactsHelperCustom")


class ResourceFactsHelper(
    ProtectionRulesFactsHelperCustom, ProtectionRulesFactsHelperGen
):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec()
    module_args.update(
        dict(
            protection_rule_key=dict(type="str", no_log=True),
            waas_policy_id=dict(type="str", required=True),
            mod_security_rule_id=dict(type="list", elements="str"),
            action=dict(
                type="list", elements="str", choices=["OFF", "DETECT", "BLOCK"]
            ),
            name=dict(type="str"),
        )
    )

    module = OCIAnsibleModule(argument_spec=module_args)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_facts_helper = ResourceFactsHelper(
        module=module,
        resource_type="protection_rules",
        service_client_class=WaasClient,
        namespace="waas",
    )

    result = []

    if resource_facts_helper.is_get():
        result = [resource_facts_helper.get()]
    elif resource_facts_helper.is_list():
        result = resource_facts_helper.list()
    else:
        resource_facts_helper.fail()

    module.exit_json(protection_rules=result)


if __name__ == "__main__":
    main()
