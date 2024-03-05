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
module: oci_opsi_summarize_host_insights_top_processes_usage_facts
description: >-
    Due to size constraints we have not included the documentation in the module. Please check L(here,
    https://docs.oracle.com/en-us/iaas/tools/oci-ansible-collection/latest/collections/oracle/oci/oci_opsi_summarize_host_insights_top_processes_usage_facts_module.html)
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
    from oci.opsi import OperationsInsightsClient

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


class SummarizeHostInsightsTopProcessesUsageFactsHelperGen(OCIResourceFactsHelperBase):
    """Supported operations: list"""

    def get_required_params_for_list(self):
        return [
            "compartment_id",
            "id",
            "resource_metric",
            "timestamp",
        ]

    def list_resources(self):
        optional_list_method_params = [
            "time_interval_start",
            "time_interval_end",
            "analysis_time_interval",
            "host_type",
            "host_id",
            "statistic",
        ]
        optional_kwargs = dict(
            (param, self.module.params[param])
            for param in optional_list_method_params
            if self.module.params.get(param) is not None
        )
        return oci_common_utils.list_all_resources(
            self.client.summarize_host_insight_top_processes_usage,
            compartment_id=self.module.params.get("compartment_id"),
            id=self.module.params.get("id"),
            resource_metric=self.module.params.get("resource_metric"),
            timestamp=self.module.params.get("timestamp"),
            **optional_kwargs
        )


SummarizeHostInsightsTopProcessesUsageFactsHelperCustom = get_custom_class(
    "SummarizeHostInsightsTopProcessesUsageFactsHelperCustom"
)


class ResourceFactsHelper(
    SummarizeHostInsightsTopProcessesUsageFactsHelperCustom,
    SummarizeHostInsightsTopProcessesUsageFactsHelperGen,
):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec()
    module_args.update(
        dict(
            compartment_id=dict(type="str", required=True),
            id=dict(type="str", required=True),
            resource_metric=dict(type="str", required=True),
            timestamp=dict(type="str", required=True),
            time_interval_start=dict(type="str"),
            time_interval_end=dict(type="str"),
            analysis_time_interval=dict(type="str"),
            host_type=dict(type="list", elements="str"),
            host_id=dict(type="str"),
            statistic=dict(type="str", choices=["AVG", "MAX"]),
        )
    )

    module = OCIAnsibleModule(argument_spec=module_args)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_facts_helper = ResourceFactsHelper(
        module=module,
        resource_type="summarize_host_insights_top_processes_usage",
        service_client_class=OperationsInsightsClient,
        namespace="opsi",
    )

    result = []

    if resource_facts_helper.is_list():
        result = resource_facts_helper.list()
    else:
        resource_facts_helper.fail()

    module.exit_json(summarize_host_insights_top_processes_usages=result)


if __name__ == "__main__":
    main()
