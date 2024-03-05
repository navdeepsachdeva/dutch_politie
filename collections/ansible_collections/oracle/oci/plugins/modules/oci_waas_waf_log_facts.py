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
module: oci_waas_waf_log_facts
description: >-
    Due to size constraints we have not included the documentation in the module. Please check L(here,
    https://docs.oracle.com/en-us/iaas/tools/oci-ansible-collection/latest/collections/oracle/oci/oci_waas_waf_log_facts_module.html)
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


class WafLogFactsHelperGen(OCIResourceFactsHelperBase):
    """Supported operations: list"""

    def get_required_params_for_list(self):
        return [
            "waas_policy_id",
        ]

    def list_resources(self):
        optional_list_method_params = [
            "time_observed_greater_than_or_equal_to",
            "time_observed_less_than",
            "text_contains",
            "access_rule_key",
            "action",
            "client_address",
            "country_code",
            "country_name",
            "fingerprint",
            "http_method",
            "incident_key",
            "log_type",
            "origin_address",
            "referrer",
            "request_url",
            "response_code",
            "threat_feed_key",
            "user_agent",
            "protection_rule_key",
        ]
        optional_kwargs = dict(
            (param, self.module.params[param])
            for param in optional_list_method_params
            if self.module.params.get(param) is not None
        )
        return oci_common_utils.list_all_resources(
            self.client.list_waf_logs,
            waas_policy_id=self.module.params.get("waas_policy_id"),
            **optional_kwargs
        )


WafLogFactsHelperCustom = get_custom_class("WafLogFactsHelperCustom")


class ResourceFactsHelper(WafLogFactsHelperCustom, WafLogFactsHelperGen):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec()
    module_args.update(
        dict(
            waas_policy_id=dict(type="str", required=True),
            time_observed_greater_than_or_equal_to=dict(type="str"),
            time_observed_less_than=dict(type="str"),
            text_contains=dict(type="str"),
            access_rule_key=dict(type="list", elements="str", no_log=True),
            action=dict(
                type="list",
                elements="str",
                choices=["BLOCK", "DETECT", "BYPASS", "LOG", "REDIRECTED"],
            ),
            client_address=dict(type="list", elements="str"),
            country_code=dict(type="list", elements="str"),
            country_name=dict(type="list", elements="str"),
            fingerprint=dict(type="list", elements="str"),
            http_method=dict(
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
                ],
            ),
            incident_key=dict(type="list", elements="str", no_log=True),
            log_type=dict(
                type="list",
                elements="str",
                choices=[
                    "ACCESS",
                    "PROTECTION_RULES",
                    "JS_CHALLENGE",
                    "CAPTCHA",
                    "ACCESS_RULES",
                    "THREAT_FEEDS",
                    "HUMAN_INTERACTION_CHALLENGE",
                    "DEVICE_FINGERPRINT_CHALLENGE",
                    "ADDRESS_RATE_LIMITING",
                ],
            ),
            origin_address=dict(type="list", elements="str"),
            referrer=dict(type="list", elements="str"),
            request_url=dict(type="list", elements="str"),
            response_code=dict(type="list", elements="int"),
            threat_feed_key=dict(type="list", elements="str", no_log=True),
            user_agent=dict(type="list", elements="str"),
            protection_rule_key=dict(type="list", elements="str", no_log=True),
        )
    )

    module = OCIAnsibleModule(argument_spec=module_args)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_facts_helper = ResourceFactsHelper(
        module=module,
        resource_type="waf_log",
        service_client_class=WaasClient,
        namespace="waas",
    )

    result = []

    if resource_facts_helper.is_list():
        result = resource_facts_helper.list()
    else:
        resource_facts_helper.fail()

    module.exit_json(waf_logs=result)


if __name__ == "__main__":
    main()
