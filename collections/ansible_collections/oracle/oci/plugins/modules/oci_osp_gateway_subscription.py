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
module: oci_osp_gateway_subscription
description: >-
    Due to size constraints we have not included the documentation in the module. Please check L(here,
    https://docs.oracle.com/en-us/iaas/tools/oci-ansible-collection/latest/collections/oracle/oci/oci_osp_gateway_subscription_module.html)
    for the module documentation.
author: Oracle (@oracle)
"""


from ansible_collections.oracle.oci.plugins.module_utils import (
    oci_common_utils,
    oci_wait_utils,
)
from ansible_collections.oracle.oci.plugins.module_utils.oci_resource_utils import (
    OCIResourceHelperBase,
    get_custom_class,
    OCIAnsibleModule,
)

try:
    from oci.osp_gateway import SubscriptionServiceClient
    from oci.osp_gateway.models import UpdateSubscriptionDetails

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


class SubscriptionHelperGen(OCIResourceHelperBase):
    """Supported operations: update, get and list"""

    def get_possible_entity_types(self):
        return super(SubscriptionHelperGen, self).get_possible_entity_types() + [
            "subscription",
            "subscriptions",
            "ospGatewaysubscription",
            "ospGatewaysubscriptions",
            "subscriptionresource",
            "subscriptionsresource",
            "ospgateway",
        ]

    def get_module_resource_id_param(self):
        return "subscription_id"

    def get_module_resource_id(self):
        return self.module.params.get("subscription_id")

    def get_get_fn(self):
        return self.client.get_subscription

    def get_resource(self):
        return oci_common_utils.call_with_backoff(
            self.client.get_subscription,
            subscription_id=self.module.params.get("subscription_id"),
            osp_home_region=self.module.params.get("osp_home_region"),
            compartment_id=self.module.params.get("compartment_id"),
        )

    def get_required_kwargs_for_list(self):
        required_list_method_params = [
            "osp_home_region",
            "compartment_id",
        ]

        return dict(
            (param, self.module.params[param]) for param in required_list_method_params
        )

    def get_optional_kwargs_for_list(self):
        return dict()

    def list_resources(self):

        required_kwargs = self.get_required_kwargs_for_list()
        optional_kwargs = self.get_optional_kwargs_for_list()
        kwargs = oci_common_utils.merge_dicts(required_kwargs, optional_kwargs)
        return oci_common_utils.list_all_resources(
            self.client.list_subscriptions, **kwargs
        )

    def get_update_model_class(self):
        return UpdateSubscriptionDetails

    def update_resource(self):
        update_details = self.get_update_model()
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.update_subscription,
            call_fn_args=(),
            call_fn_kwargs=dict(
                subscription_id=self.module.params.get("subscription_id"),
                osp_home_region=self.module.params.get("osp_home_region"),
                compartment_id=self.module.params.get("compartment_id"),
                update_subscription_details=update_details,
            ),
            waiter_type=oci_wait_utils.NONE_WAITER_KEY,
            operation=oci_common_utils.UPDATE_OPERATION_KEY,
            waiter_client=self.get_waiter_client(),
            resource_helper=self,
            wait_for_states=self.get_wait_for_states_for_operation(
                oci_common_utils.UPDATE_OPERATION_KEY,
            ),
        )


SubscriptionHelperCustom = get_custom_class("SubscriptionHelperCustom")


class ResourceHelper(SubscriptionHelperCustom, SubscriptionHelperGen):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec(
        supports_create=False, supports_wait=False
    )
    module_args.update(
        dict(
            subscription_id=dict(aliases=["id"], type="str", required=True),
            osp_home_region=dict(type="str", required=True),
            compartment_id=dict(type="str", required=True),
            subscription=dict(
                type="dict",
                required=True,
                options=dict(
                    id=dict(type="str"),
                    subscription_plan_number=dict(type="str", required=True),
                    plan_type=dict(type="str", choices=["FREE_TIER", "PAYG"]),
                    time_start=dict(type="str"),
                    ship_to_cust_acct_site_id=dict(type="str"),
                    ship_to_cust_acct_role_id=dict(type="str"),
                    bill_to_cust_account_id=dict(type="str"),
                    is_intent_to_pay=dict(type="bool"),
                    currency_code=dict(type="str"),
                    gsi_org_code=dict(type="str"),
                    language_code=dict(type="str"),
                    organization_id=dict(type="str"),
                    upgrade_state=dict(
                        type="str", choices=["PROMO", "SUBMITTED", "ERROR", "UPGRADED"]
                    ),
                    upgrade_state_details=dict(
                        type="str", choices=["TAX_ERROR", "UPGRADE_ERROR"]
                    ),
                    account_type=dict(
                        type="str",
                        choices=["PERSONAL", "CORPORATE", "CORPORATE_SUBMITTED"],
                    ),
                    tax_info=dict(
                        type="dict",
                        options=dict(
                            tax_payer_id=dict(type="str"),
                            tax_reg_number=dict(type="str"),
                            no_tax_reason_code=dict(type="str"),
                            no_tax_reason_code_details=dict(type="str"),
                            tax_cnpj=dict(type="str"),
                        ),
                    ),
                    payment_options=dict(
                        type="list",
                        elements="dict",
                        options=dict(
                            credit_card_type=dict(
                                type="str",
                                choices=[
                                    "VISA",
                                    "AMEX",
                                    "MASTERCARD",
                                    "DISCOVER",
                                    "JCB",
                                    "DINER",
                                    "ELO",
                                ],
                            ),
                            last_digits=dict(type="str"),
                            name_on_card=dict(type="str"),
                            time_expiration=dict(type="str"),
                            wallet_instrument_id=dict(type="str"),
                            wallet_transaction_id=dict(type="str"),
                            payment_method=dict(
                                type="str",
                                required=True,
                                choices=["CREDIT_CARD", "PAYPAL"],
                            ),
                            email_address=dict(type="str"),
                            first_name=dict(type="str"),
                            last_name=dict(type="str"),
                            ext_billing_agreement_id=dict(type="str"),
                        ),
                    ),
                    payment_gateway=dict(
                        type="dict",
                        options=dict(
                            merchant_defined_data=dict(
                                type="dict",
                                options=dict(
                                    promo_type=dict(type="str"),
                                    cloud_account_name=dict(type="str"),
                                ),
                            )
                        ),
                    ),
                    billing_address=dict(
                        type="dict",
                        options=dict(
                            address_key=dict(type="str", no_log=True),
                            line1=dict(type="str"),
                            line2=dict(type="str"),
                            line3=dict(type="str"),
                            line4=dict(type="str"),
                            street_name=dict(type="str"),
                            street_number=dict(type="str"),
                            city=dict(type="str"),
                            county=dict(type="str"),
                            country=dict(type="str"),
                            province=dict(type="str"),
                            postal_code=dict(type="str"),
                            state=dict(type="str"),
                            email_address=dict(type="str"),
                            company_name=dict(type="str"),
                            first_name=dict(type="str"),
                            middle_name=dict(type="str"),
                            last_name=dict(type="str"),
                            phone_country_code=dict(type="str"),
                            phone_number=dict(type="str"),
                            job_title=dict(type="str"),
                            department_name=dict(type="str"),
                            internal_number=dict(type="str"),
                            contributor_class=dict(type="str"),
                            state_inscription=dict(type="str"),
                            municipal_inscription=dict(type="str"),
                        ),
                    ),
                    time_plan_upgrade=dict(type="str"),
                    time_personal_to_corporate_conv=dict(type="str"),
                ),
            ),
            email=dict(type="str", required=True),
            state=dict(type="str", default="present", choices=["present"]),
        )
    )

    module = OCIAnsibleModule(argument_spec=module_args, supports_check_mode=True)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_helper = ResourceHelper(
        module=module,
        resource_type="subscription",
        service_client_class=SubscriptionServiceClient,
        namespace="osp_gateway",
    )

    result = dict(changed=False)

    if resource_helper.is_update():
        result = resource_helper.update()

    module.exit_json(**result)


if __name__ == "__main__":
    main()
