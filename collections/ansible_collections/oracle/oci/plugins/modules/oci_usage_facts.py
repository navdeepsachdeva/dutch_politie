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
module: oci_usage_facts
description: >-
    Due to size constraints we have not included the documentation in the module. Please check L(here,
    https://docs.oracle.com/en-us/iaas/tools/oci-ansible-collection/latest/collections/oracle/oci/oci_usage_facts_module.html)
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
    from oci.usage_api import UsageapiClient
    from oci.usage_api.models import RequestSummarizedUsagesDetails

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


class UsageFactsHelperGen(OCIResourceFactsHelperBase):
    """Supported operations: list"""

    def get_required_params_for_list(self):
        return [
            "tenant_id",
            "time_usage_started",
            "time_usage_ended",
            "granularity",
        ]

    def list_resources(self):
        optional_list_method_params = []
        optional_kwargs = dict(
            (param, self.module.params[param])
            for param in optional_list_method_params
            if self.module.params.get(param) is not None
        )
        return oci_common_utils.list_all_resources(
            self.client.request_summarized_usages,
            request_summarized_usages_details=oci_common_utils.convert_input_data_to_model_class(
                self.module.params, RequestSummarizedUsagesDetails
            ),
            **optional_kwargs
        )


UsageFactsHelperCustom = get_custom_class("UsageFactsHelperCustom")


class ResourceFactsHelper(UsageFactsHelperCustom, UsageFactsHelperGen):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec()
    module_args.update(
        dict(
            tenant_id=dict(type="str", required=True),
            time_usage_started=dict(type="str", required=True),
            time_usage_ended=dict(type="str", required=True),
            granularity=dict(
                type="str",
                required=True,
                choices=["HOURLY", "DAILY", "MONTHLY", "TOTAL"],
            ),
            is_aggregate_by_time=dict(type="bool"),
            forecast=dict(
                type="dict",
                options=dict(
                    forecast_type=dict(type="str", choices=["BASIC"]),
                    time_forecast_started=dict(type="str"),
                    time_forecast_ended=dict(type="str", required=True),
                ),
            ),
            query_type=dict(
                type="str",
                choices=["USAGE", "COST", "CREDIT", "EXPIREDCREDIT", "ALLCREDIT"],
            ),
            group_by=dict(type="list", elements="str"),
            group_by_tag=dict(
                type="list",
                elements="dict",
                options=dict(
                    namespace=dict(type="str"),
                    key=dict(type="str", no_log=True),
                    value=dict(type="str"),
                ),
            ),
            compartment_depth=dict(type="float"),
            filter=dict(
                type="dict",
                options=dict(
                    operator=dict(type="str", choices=["AND", "NOT", "OR"]),
                    dimensions=dict(
                        type="list",
                        elements="dict",
                        options=dict(
                            key=dict(type="str", required=True, no_log=True),
                            value=dict(type="str", required=True),
                        ),
                    ),
                    tags=dict(
                        type="list",
                        elements="dict",
                        options=dict(
                            namespace=dict(type="str"),
                            key=dict(type="str", no_log=True),
                            value=dict(type="str"),
                        ),
                    ),
                    filters=dict(
                        type="list",
                        elements="dict",
                        options=dict(
                            operator=dict(type="str", choices=["AND", "NOT", "OR"]),
                            dimensions=dict(type="list", elements="dict"),
                            tags=dict(type="list", elements="dict"),
                            filters=dict(type="list", elements="dict"),
                        ),
                    ),
                ),
            ),
        )
    )

    module = OCIAnsibleModule(argument_spec=module_args)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_facts_helper = ResourceFactsHelper(
        module=module,
        resource_type="usage",
        service_client_class=UsageapiClient,
        namespace="usage_api",
    )

    result = []

    if resource_facts_helper.is_list():
        result = resource_facts_helper.list()
    else:
        resource_facts_helper.fail()

    module.exit_json(usages=result)


if __name__ == "__main__":
    main()
