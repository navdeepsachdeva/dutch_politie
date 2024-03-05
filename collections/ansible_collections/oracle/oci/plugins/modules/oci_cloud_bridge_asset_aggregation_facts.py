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
module: oci_cloud_bridge_asset_aggregation_facts
description: >-
    Due to size constraints we have not included the documentation in the module. Please check L(here,
    https://docs.oracle.com/en-us/iaas/tools/oci-ansible-collection/latest/collections/oracle/oci/oci_cloud_bridge_asset_aggregation_facts_module.html)
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
    from oci.cloud_bridge import InventoryClient

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


class AssetAggregationFactsHelperGen(OCIResourceFactsHelperBase):
    """Supported operations: list"""

    def get_required_params_for_list(self):
        return [
            "compartment_id",
            "aggregation_properties",
        ]

    def list_resources(self):
        optional_list_method_params = [
            "lifecycle_state",
            "source_key",
            "external_asset_key",
            "asset_type",
            "sort_order",
            "group_by",
            "inventory_id",
        ]
        optional_kwargs = dict(
            (param, self.module.params[param])
            for param in optional_list_method_params
            if self.module.params.get(param) is not None
        )
        return oci_common_utils.list_all_resources(
            self.client.analyze_assets,
            compartment_id=self.module.params.get("compartment_id"),
            aggregation_properties=self.module.params.get("aggregation_properties"),
            **optional_kwargs
        )


AssetAggregationFactsHelperCustom = get_custom_class(
    "AssetAggregationFactsHelperCustom"
)


class ResourceFactsHelper(
    AssetAggregationFactsHelperCustom, AssetAggregationFactsHelperGen
):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec()
    module_args.update(
        dict(
            compartment_id=dict(type="str", required=True),
            aggregation_properties=dict(type="list", elements="str", required=True),
            lifecycle_state=dict(type="str", choices=["ACTIVE", "DELETED"]),
            source_key=dict(type="str", no_log=True),
            external_asset_key=dict(type="str", no_log=True),
            asset_type=dict(type="str", choices=["VMWARE_VM", "VM"]),
            sort_order=dict(type="str", choices=["ASC", "DESC"]),
            group_by=dict(type="list", elements="str"),
            inventory_id=dict(type="str"),
        )
    )

    module = OCIAnsibleModule(argument_spec=module_args)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_facts_helper = ResourceFactsHelper(
        module=module,
        resource_type="asset_aggregation",
        service_client_class=InventoryClient,
        namespace="cloud_bridge",
    )

    result = []

    if resource_facts_helper.is_list():
        result = resource_facts_helper.list()
    else:
        resource_facts_helper.fail()

    module.exit_json(asset_aggregations=result)


if __name__ == "__main__":
    main()
