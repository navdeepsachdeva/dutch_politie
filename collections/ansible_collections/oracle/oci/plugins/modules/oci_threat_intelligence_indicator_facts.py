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
module: oci_threat_intelligence_indicator_facts
description: >-
    Due to size constraints we have not included the documentation in the module. Please check L(here,
    https://docs.oracle.com/en-us/iaas/tools/oci-ansible-collection/latest/collections/oracle/oci/oci_threat_intelligence_indicator_facts_module.html)
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
    from oci.threat_intelligence import ThreatintelClient

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


class IndicatorFactsHelperGen(OCIResourceFactsHelperBase):
    """Supported operations: get, list"""

    def get_required_params_for_get(self):
        return [
            "indicator_id",
            "compartment_id",
        ]

    def get_required_params_for_list(self):
        return [
            "compartment_id",
        ]

    def get_resource(self):
        return oci_common_utils.call_with_backoff(
            self.client.get_indicator,
            indicator_id=self.module.params.get("indicator_id"),
            compartment_id=self.module.params.get("compartment_id"),
        )

    def list_resources(self):
        optional_list_method_params = [
            "threat_type_name",
            "type",
            "value",
            "confidence_greater_than_or_equal_to",
            "time_updated_greater_than_or_equal_to",
            "time_updated_less_than",
            "time_last_seen_greater_than_or_equal_to",
            "time_last_seen_less_than",
            "time_created_greater_than_or_equal_to",
            "time_created_less_than",
            "sort_order",
            "sort_by",
        ]
        optional_kwargs = dict(
            (param, self.module.params[param])
            for param in optional_list_method_params
            if self.module.params.get(param) is not None
        )
        return oci_common_utils.list_all_resources(
            self.client.list_indicators,
            compartment_id=self.module.params.get("compartment_id"),
            **optional_kwargs
        )


IndicatorFactsHelperCustom = get_custom_class("IndicatorFactsHelperCustom")


class ResourceFactsHelper(IndicatorFactsHelperCustom, IndicatorFactsHelperGen):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec()
    module_args.update(
        dict(
            indicator_id=dict(aliases=["id"], type="str"),
            compartment_id=dict(type="str", required=True),
            threat_type_name=dict(type="list", elements="str"),
            type=dict(
                type="str",
                choices=[
                    "DOMAIN_NAME",
                    "FILE_NAME",
                    "MD5_HASH",
                    "SHA1_HASH",
                    "SHA256_HASH",
                    "IP_ADDRESS",
                    "URL",
                ],
            ),
            value=dict(type="str"),
            confidence_greater_than_or_equal_to=dict(type="int"),
            time_updated_greater_than_or_equal_to=dict(type="str"),
            time_updated_less_than=dict(type="str"),
            time_last_seen_greater_than_or_equal_to=dict(type="str"),
            time_last_seen_less_than=dict(type="str"),
            time_created_greater_than_or_equal_to=dict(type="str"),
            time_created_less_than=dict(type="str"),
            sort_order=dict(type="str", choices=["ASC", "DESC"]),
            sort_by=dict(
                type="str",
                choices=["confidence", "timeCreated", "timeUpdated", "timeLastSeen"],
            ),
        )
    )

    module = OCIAnsibleModule(argument_spec=module_args)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_facts_helper = ResourceFactsHelper(
        module=module,
        resource_type="indicator",
        service_client_class=ThreatintelClient,
        namespace="threat_intelligence",
    )

    result = []

    if resource_facts_helper.is_get():
        result = [resource_facts_helper.get()]
    elif resource_facts_helper.is_list():
        result = resource_facts_helper.list()
    else:
        resource_facts_helper.fail()

    module.exit_json(indicators=result)


if __name__ == "__main__":
    main()
