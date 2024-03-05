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
module: oci_osp_gateway_invoice_facts
description: >-
    Due to size constraints we have not included the documentation in the module. Please check L(here,
    https://docs.oracle.com/en-us/iaas/tools/oci-ansible-collection/latest/collections/oracle/oci/oci_osp_gateway_invoice_facts_module.html)
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
    from oci.osp_gateway import InvoiceServiceClient

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


class InvoiceFactsHelperGen(OCIResourceFactsHelperBase):
    """Supported operations: get, list"""

    def get_required_params_for_get(self):
        return [
            "osp_home_region",
            "compartment_id",
            "internal_invoice_id",
        ]

    def get_required_params_for_list(self):
        return [
            "osp_home_region",
            "compartment_id",
        ]

    def get_resource(self):
        return oci_common_utils.call_with_backoff(
            self.client.get_invoice,
            osp_home_region=self.module.params.get("osp_home_region"),
            compartment_id=self.module.params.get("compartment_id"),
            internal_invoice_id=self.module.params.get("internal_invoice_id"),
        )

    def list_resources(self):
        optional_list_method_params = [
            "invoice_id",
            "type",
            "search_text",
            "time_invoice_start",
            "time_invoice_end",
            "time_payment_start",
            "time_payment_end",
            "status",
            "sort_by",
            "sort_order",
        ]
        optional_kwargs = dict(
            (param, self.module.params[param])
            for param in optional_list_method_params
            if self.module.params.get(param) is not None
        )
        return oci_common_utils.list_all_resources(
            self.client.list_invoices,
            osp_home_region=self.module.params.get("osp_home_region"),
            compartment_id=self.module.params.get("compartment_id"),
            **optional_kwargs
        )


InvoiceFactsHelperCustom = get_custom_class("InvoiceFactsHelperCustom")


class ResourceFactsHelper(InvoiceFactsHelperCustom, InvoiceFactsHelperGen):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec()
    module_args.update(
        dict(
            internal_invoice_id=dict(aliases=["id"], type="str"),
            osp_home_region=dict(type="str", required=True),
            compartment_id=dict(type="str", required=True),
            invoice_id=dict(type="str"),
            type=dict(
                type="list",
                elements="str",
                choices=[
                    "HARDWARE",
                    "SUBSCRIPTION",
                    "SUPPORT",
                    "LICENSE",
                    "EDUCATION",
                    "CONSULTING",
                    "SERVICE",
                    "USAGE",
                ],
            ),
            search_text=dict(type="str"),
            time_invoice_start=dict(type="str"),
            time_invoice_end=dict(type="str"),
            time_payment_start=dict(type="str"),
            time_payment_end=dict(type="str"),
            status=dict(
                type="list",
                elements="str",
                choices=["OPEN", "PAST_DUE", "PAYMENT_SUBMITTED", "CLOSED"],
            ),
            sort_by=dict(
                type="str",
                choices=[
                    "INVOICE_NO",
                    "REF_NO",
                    "STATUS",
                    "TYPE",
                    "INVOICE_DATE",
                    "DUE_DATE",
                    "PAYM_REF",
                    "TOTAL_AMOUNT",
                    "BALANCE_DUE",
                ],
            ),
            sort_order=dict(type="str", choices=["ASC", "DESC"]),
        )
    )

    module = OCIAnsibleModule(argument_spec=module_args)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_facts_helper = ResourceFactsHelper(
        module=module,
        resource_type="invoice",
        service_client_class=InvoiceServiceClient,
        namespace="osp_gateway",
    )

    result = []

    if resource_facts_helper.is_get():
        result = [resource_facts_helper.get()]
    elif resource_facts_helper.is_list():
        result = resource_facts_helper.list()
    else:
        resource_facts_helper.fail()

    module.exit_json(invoices=result)


if __name__ == "__main__":
    main()
