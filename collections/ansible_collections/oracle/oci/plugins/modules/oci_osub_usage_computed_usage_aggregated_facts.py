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
module: oci_osub_usage_computed_usage_aggregated_facts
description: >-
    Due to size constraints we have not included the documentation in the module. Please check L(here,
    https://docs.oracle.com/en-us/iaas/tools/oci-ansible-collection/latest/collections/oracle/oci/oci_osub_usage_computed_usage_aggregated_facts_module.html)
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
    from oci.osub_usage import ComputedUsageClient

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


class ComputedUsageAggregatedFactsHelperGen(OCIResourceFactsHelperBase):
    """Supported operations: list"""

    def get_required_params_for_list(self):
        return [
            "compartment_id",
            "subscription_id",
            "time_from",
            "time_to",
        ]

    def list_resources(self):
        optional_list_method_params = [
            "parent_product",
            "grouping",
            "x_one_origin_region",
        ]
        optional_kwargs = dict(
            (param, self.module.params[param])
            for param in optional_list_method_params
            if self.module.params.get(param) is not None
        )
        return oci_common_utils.list_all_resources(
            self.client.list_computed_usage_aggregateds,
            compartment_id=self.module.params.get("compartment_id"),
            subscription_id=self.module.params.get("subscription_id"),
            time_from=self.module.params.get("time_from"),
            time_to=self.module.params.get("time_to"),
            **optional_kwargs
        )


ComputedUsageAggregatedFactsHelperCustom = get_custom_class(
    "ComputedUsageAggregatedFactsHelperCustom"
)


class ResourceFactsHelper(
    ComputedUsageAggregatedFactsHelperCustom, ComputedUsageAggregatedFactsHelperGen
):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec()
    module_args.update(
        dict(
            compartment_id=dict(type="str", required=True),
            subscription_id=dict(type="str", required=True),
            time_from=dict(type="str", required=True),
            time_to=dict(type="str", required=True),
            parent_product=dict(type="str"),
            grouping=dict(type="str", choices=["HOURLY", "DAILY", "MONTHLY", "NONE"]),
            x_one_origin_region=dict(type="str"),
        )
    )

    module = OCIAnsibleModule(argument_spec=module_args)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_facts_helper = ResourceFactsHelper(
        module=module,
        resource_type="computed_usage_aggregated",
        service_client_class=ComputedUsageClient,
        namespace="osub_usage",
    )

    result = []

    if resource_facts_helper.is_list():
        result = resource_facts_helper.list()
    else:
        resource_facts_helper.fail()

    module.exit_json(computed_usage_aggregateds=result)


if __name__ == "__main__":
    main()
