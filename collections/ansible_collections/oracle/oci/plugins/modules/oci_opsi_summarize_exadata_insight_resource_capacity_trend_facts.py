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
module: oci_opsi_summarize_exadata_insight_resource_capacity_trend_facts
description: >-
    Due to size constraints we have not included the documentation in the module. Please check L(here,
    https://docs.oracle.com/en-us/iaas/tools/oci-ansible-collection/latest/collections/oracle/oci/oci_opsi_summarize_exadata_insight_resource_capacity_trend_facts_module.html)
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


class SummarizeExadataInsightResourceCapacityTrendFactsHelperGen(
    OCIResourceFactsHelperBase
):
    """Supported operations: list"""

    def get_required_params_for_list(self):
        return [
            "resource_type",
            "resource_metric",
            "exadata_insight_id",
        ]

    def list_resources(self):
        optional_list_method_params = [
            "compartment_id",
            "analysis_time_interval",
            "time_interval_start",
            "time_interval_end",
            "database_insight_id",
            "host_insight_id",
            "storage_server_name",
            "exadata_type",
            "cdb_name",
            "host_name",
            "sort_order",
            "sort_by",
            "name",
        ]
        optional_kwargs = dict(
            (param, self.module.params[param])
            for param in optional_list_method_params
            if self.module.params.get(param) is not None
        )
        return oci_common_utils.list_all_resources(
            self.client.summarize_exadata_insight_resource_capacity_trend,
            resource_type=self.module.params.get("resource_type"),
            resource_metric=self.module.params.get("resource_metric"),
            exadata_insight_id=self.module.params.get("exadata_insight_id"),
            **optional_kwargs
        )


SummarizeExadataInsightResourceCapacityTrendFactsHelperCustom = get_custom_class(
    "SummarizeExadataInsightResourceCapacityTrendFactsHelperCustom"
)


class ResourceFactsHelper(
    SummarizeExadataInsightResourceCapacityTrendFactsHelperCustom,
    SummarizeExadataInsightResourceCapacityTrendFactsHelperGen,
):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec()
    module_args.update(
        dict(
            resource_type=dict(type="str", required=True),
            resource_metric=dict(type="str", required=True),
            exadata_insight_id=dict(type="str", required=True),
            compartment_id=dict(type="str"),
            analysis_time_interval=dict(type="str"),
            time_interval_start=dict(type="str"),
            time_interval_end=dict(type="str"),
            database_insight_id=dict(type="list", elements="str"),
            host_insight_id=dict(type="list", elements="str"),
            storage_server_name=dict(type="list", elements="str"),
            exadata_type=dict(type="list", elements="str"),
            cdb_name=dict(type="list", elements="str"),
            host_name=dict(type="list", elements="str"),
            sort_order=dict(type="str", choices=["ASC", "DESC"]),
            sort_by=dict(type="str", choices=["id", "name"]),
            name=dict(type="str"),
        )
    )

    module = OCIAnsibleModule(argument_spec=module_args)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_facts_helper = ResourceFactsHelper(
        module=module,
        resource_type="summarize_exadata_insight_resource_capacity_trend",
        service_client_class=OperationsInsightsClient,
        namespace="opsi",
    )

    result = []

    if resource_facts_helper.is_list():
        result = resource_facts_helper.list()
    else:
        resource_facts_helper.fail()

    module.exit_json(summarize_exadata_insight_resource_capacity_trends=result)


if __name__ == "__main__":
    main()
