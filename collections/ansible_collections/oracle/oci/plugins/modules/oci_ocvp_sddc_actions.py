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
module: oci_ocvp_sddc_actions
description: >-
    Due to size constraints we have not included the documentation in the module. Please check L(here,
    https://docs.oracle.com/en-us/iaas/tools/oci-ansible-collection/latest/collections/oracle/oci/oci_ocvp_sddc_actions_module.html)
    for the module documentation.
author: Oracle (@oracle)
"""


from ansible_collections.oracle.oci.plugins.module_utils import (
    oci_common_utils,
    oci_wait_utils,
    oci_config_utils,
)
from ansible_collections.oracle.oci.plugins.module_utils.oci_resource_utils import (
    OCIActionsHelperBase,
    OCIAnsibleModule,
    get_custom_class,
)

try:
    from oci.ocvp import WorkRequestClient
    from oci.ocvp import SddcClient
    from oci.ocvp.models import ChangeSddcCompartmentDetails
    from oci.ocvp.models import DowngradeHcxDetails

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


class SddcActionsHelperGen(OCIActionsHelperBase):
    """
    Supported actions:
        cancel_downgrade_hcx
        change_compartment
        downgrade_hcx
        refresh_hcx_license_status
        upgrade_hcx
    """

    def get_waiter_client(self):
        return oci_config_utils.create_service_client(self.module, WorkRequestClient)

    @staticmethod
    def get_module_resource_id_param():
        return "sddc_id"

    def get_module_resource_id(self):
        return self.module.params.get("sddc_id")

    def get_get_fn(self):
        return self.client.get_sddc

    def get_resource(self):
        return oci_common_utils.call_with_backoff(
            self.client.get_sddc, sddc_id=self.module.params.get("sddc_id"),
        )

    def cancel_downgrade_hcx(self):
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.cancel_downgrade_hcx,
            call_fn_args=(),
            call_fn_kwargs=dict(sddc_id=self.module.params.get("sddc_id"),),
            waiter_type=oci_wait_utils.WORK_REQUEST_WAITER_KEY,
            operation="{0}_{1}".format(
                self.module.params.get("action").upper(),
                oci_common_utils.ACTION_OPERATION_KEY,
            ),
            waiter_client=self.get_waiter_client(),
            resource_helper=self,
            wait_for_states=oci_common_utils.get_work_request_completed_states(),
        )

    def change_compartment(self):
        action_details = oci_common_utils.convert_input_data_to_model_class(
            self.module.params, ChangeSddcCompartmentDetails
        )
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.change_sddc_compartment,
            call_fn_args=(),
            call_fn_kwargs=dict(
                sddc_id=self.module.params.get("sddc_id"),
                change_sddc_compartment_details=action_details,
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

    def downgrade_hcx(self):
        action_details = oci_common_utils.convert_input_data_to_model_class(
            self.module.params, DowngradeHcxDetails
        )
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.downgrade_hcx,
            call_fn_args=(),
            call_fn_kwargs=dict(
                downgrade_hcx_details=action_details,
                sddc_id=self.module.params.get("sddc_id"),
            ),
            waiter_type=oci_wait_utils.WORK_REQUEST_WAITER_KEY,
            operation="{0}_{1}".format(
                self.module.params.get("action").upper(),
                oci_common_utils.ACTION_OPERATION_KEY,
            ),
            waiter_client=self.get_waiter_client(),
            resource_helper=self,
            wait_for_states=oci_common_utils.get_work_request_completed_states(),
        )

    def refresh_hcx_license_status(self):
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.refresh_hcx_license_status,
            call_fn_args=(),
            call_fn_kwargs=dict(sddc_id=self.module.params.get("sddc_id"),),
            waiter_type=oci_wait_utils.WORK_REQUEST_WAITER_KEY,
            operation="{0}_{1}".format(
                self.module.params.get("action").upper(),
                oci_common_utils.ACTION_OPERATION_KEY,
            ),
            waiter_client=self.get_waiter_client(),
            resource_helper=self,
            wait_for_states=oci_common_utils.get_work_request_completed_states(),
        )

    def upgrade_hcx(self):
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.upgrade_hcx,
            call_fn_args=(),
            call_fn_kwargs=dict(sddc_id=self.module.params.get("sddc_id"),),
            waiter_type=oci_wait_utils.WORK_REQUEST_WAITER_KEY,
            operation="{0}_{1}".format(
                self.module.params.get("action").upper(),
                oci_common_utils.ACTION_OPERATION_KEY,
            ),
            waiter_client=self.get_waiter_client(),
            resource_helper=self,
            wait_for_states=oci_common_utils.get_work_request_completed_states(),
        )


SddcActionsHelperCustom = get_custom_class("SddcActionsHelperCustom")


class ResourceHelper(SddcActionsHelperCustom, SddcActionsHelperGen):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec(
        supports_create=False, supports_wait=True
    )
    module_args.update(
        dict(
            compartment_id=dict(type="str"),
            reserving_hcx_on_premise_license_keys=dict(
                type="list", elements="str", no_log=True
            ),
            sddc_id=dict(aliases=["id"], type="str", required=True),
            action=dict(
                type="str",
                required=True,
                choices=[
                    "cancel_downgrade_hcx",
                    "change_compartment",
                    "downgrade_hcx",
                    "refresh_hcx_license_status",
                    "upgrade_hcx",
                ],
            ),
        )
    )

    module = OCIAnsibleModule(argument_spec=module_args, supports_check_mode=True)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_helper = ResourceHelper(
        module=module,
        resource_type="sddc",
        service_client_class=SddcClient,
        namespace="ocvp",
    )

    result = resource_helper.perform_action(module.params.get("action"))

    module.exit_json(**result)


if __name__ == "__main__":
    main()
