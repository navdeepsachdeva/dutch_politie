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
module: oci_dts_transfer_appliance_facts
description: >-
    Due to size constraints we have not included the documentation in the module. Please check L(here,
    https://docs.oracle.com/en-us/iaas/tools/oci-ansible-collection/latest/collections/oracle/oci/oci_dts_transfer_appliance_facts_module.html)
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
    from oci.dts import TransferApplianceClient

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


class TransferApplianceFactsHelperGen(OCIResourceFactsHelperBase):
    """Supported operations: get, list"""

    def get_required_params_for_get(self):
        return [
            "id",
            "transfer_appliance_label",
        ]

    def get_required_params_for_list(self):
        return [
            "id",
        ]

    def get_resource(self):
        return oci_common_utils.call_with_backoff(
            self.client.get_transfer_appliance,
            id=self.module.params.get("id"),
            transfer_appliance_label=self.module.params.get("transfer_appliance_label"),
        )

    def list_resources(self):
        optional_list_method_params = [
            "lifecycle_state",
        ]
        optional_kwargs = dict(
            (param, self.module.params[param])
            for param in optional_list_method_params
            if self.module.params.get(param) is not None
        )
        return oci_common_utils.list_all_resources(
            self.client.list_transfer_appliances,
            id=self.module.params.get("id"),
            **optional_kwargs
        )


TransferApplianceFactsHelperCustom = get_custom_class(
    "TransferApplianceFactsHelperCustom"
)


class ResourceFactsHelper(
    TransferApplianceFactsHelperCustom, TransferApplianceFactsHelperGen
):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec()
    module_args.update(
        dict(
            transfer_appliance_label=dict(type="str"),
            id=dict(type="str", required=True),
            lifecycle_state=dict(
                type="str",
                choices=[
                    "REQUESTED",
                    "ORACLE_PREPARING",
                    "SHIPPING",
                    "DELIVERED",
                    "PREPARING",
                    "FINALIZED",
                    "RETURN_LABEL_REQUESTED",
                    "RETURN_LABEL_GENERATING",
                    "RETURN_LABEL_AVAILABLE",
                    "RETURN_DELAYED",
                    "RETURN_SHIPPED",
                    "RETURN_SHIPPED_CANCELLED",
                    "ORACLE_RECEIVED",
                    "ORACLE_RECEIVED_CANCELLED",
                    "PROCESSING",
                    "COMPLETE",
                    "CUSTOMER_NEVER_RECEIVED",
                    "ORACLE_NEVER_RECEIVED",
                    "CUSTOMER_LOST",
                    "CANCELLED",
                    "DELETED",
                    "REJECTED",
                    "ERROR",
                ],
            ),
        )
    )

    module = OCIAnsibleModule(argument_spec=module_args)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_facts_helper = ResourceFactsHelper(
        module=module,
        resource_type="transfer_appliance",
        service_client_class=TransferApplianceClient,
        namespace="dts",
    )

    result = []

    if resource_facts_helper.is_get():
        result = [resource_facts_helper.get()]
    elif resource_facts_helper.is_list():
        result = resource_facts_helper.list()
    else:
        resource_facts_helper.fail()

    module.exit_json(transfer_appliances=result)


if __name__ == "__main__":
    main()
