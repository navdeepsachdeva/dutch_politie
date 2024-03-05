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
module: oci_apm_synthetics_aggregated_network_data_result_actions
description: >-
    Due to size constraints we have not included the documentation in the module. Please check L(here,
    https://docs.oracle.com/en-us/iaas/tools/oci-ansible-collection/latest/collections/oracle/oci/oci_apm_synthetics_aggregated_network_data_result_actions_module.html)
    for the module documentation.
author: Oracle (@oracle)
"""


from ansible_collections.oracle.oci.plugins.module_utils import (
    oci_common_utils,
    oci_wait_utils,
)
from ansible_collections.oracle.oci.plugins.module_utils.oci_resource_utils import (
    OCIActionsHelperBase,
    OCIAnsibleModule,
    get_custom_class,
)

try:
    from oci.apm_synthetics import ApmSyntheticClient
    from oci.apm_synthetics.models import AggregateNetworkDataDetails

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


class AggregatedNetworkDataResultActionsHelperGen(OCIActionsHelperBase):
    """
    Supported actions:
        aggregate_network_data
    """

    @staticmethod
    def get_module_resource_id_param():
        return "monitor_id"

    def get_module_resource_id(self):
        return self.module.params.get("monitor_id")

    def aggregate_network_data(self):
        action_details = oci_common_utils.convert_input_data_to_model_class(
            self.module.params, AggregateNetworkDataDetails
        )
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.aggregate_network_data,
            call_fn_args=(),
            call_fn_kwargs=dict(
                apm_domain_id=self.module.params.get("apm_domain_id"),
                monitor_id=self.module.params.get("monitor_id"),
                aggregate_network_data_details=action_details,
            ),
            waiter_type=oci_wait_utils.NONE_WAITER_KEY,
            operation="{0}_{1}".format(
                self.module.params.get("action").upper(),
                oci_common_utils.ACTION_OPERATION_KEY,
            ),
            waiter_client=self.get_waiter_client(),
            resource_helper=self,
            wait_for_states=self.get_action_desired_states(
                self.module.params.get("action")
            ),
        )


AggregatedNetworkDataResultActionsHelperCustom = get_custom_class(
    "AggregatedNetworkDataResultActionsHelperCustom"
)


class ResourceHelper(
    AggregatedNetworkDataResultActionsHelperCustom,
    AggregatedNetworkDataResultActionsHelperGen,
):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec(
        supports_create=False, supports_wait=False
    )
    module_args.update(
        dict(
            apm_domain_id=dict(type="str", required=True),
            monitor_id=dict(aliases=["id"], type="str", required=True),
            vantage_point_execution_times=dict(
                type="list",
                elements="dict",
                required=True,
                options=dict(
                    name=dict(type="str"), executions=dict(type="list", elements="long")
                ),
            ),
            action=dict(type="str", required=True, choices=["aggregate_network_data"]),
        )
    )

    module = OCIAnsibleModule(argument_spec=module_args, supports_check_mode=True)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_helper = ResourceHelper(
        module=module,
        resource_type="aggregated_network_data_result",
        service_client_class=ApmSyntheticClient,
        namespace="apm_synthetics",
    )

    result = resource_helper.perform_action(module.params.get("action"))

    module.exit_json(**result)


if __name__ == "__main__":
    main()
