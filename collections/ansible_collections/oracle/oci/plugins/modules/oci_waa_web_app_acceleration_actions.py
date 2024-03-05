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
module: oci_waa_web_app_acceleration_actions
description: >-
    Due to size constraints we have not included the documentation in the module. Please check L(here,
    https://docs.oracle.com/en-us/iaas/tools/oci-ansible-collection/latest/collections/oracle/oci/oci_waa_web_app_acceleration_actions_module.html)
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
    from oci.waa import WorkRequestClient
    from oci.waa import WaaClient
    from oci.waa.models import ChangeWebAppAccelerationCompartmentDetails
    from oci.waa.models import PurgeWebAppAccelerationCacheDetails

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


class WebAppAccelerationActionsHelperGen(OCIActionsHelperBase):
    """
    Supported actions:
        change_compartment
        purge_web_app_acceleration_cache
    """

    def get_waiter_client(self):
        return oci_config_utils.create_service_client(self.module, WorkRequestClient)

    @staticmethod
    def get_module_resource_id_param():
        return "web_app_acceleration_id"

    def get_module_resource_id(self):
        return self.module.params.get("web_app_acceleration_id")

    def get_get_fn(self):
        return self.client.get_web_app_acceleration

    def get_resource(self):
        return oci_common_utils.call_with_backoff(
            self.client.get_web_app_acceleration,
            web_app_acceleration_id=self.module.params.get("web_app_acceleration_id"),
        )

    def change_compartment(self):
        action_details = oci_common_utils.convert_input_data_to_model_class(
            self.module.params, ChangeWebAppAccelerationCompartmentDetails
        )
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.change_web_app_acceleration_compartment,
            call_fn_args=(),
            call_fn_kwargs=dict(
                web_app_acceleration_id=self.module.params.get(
                    "web_app_acceleration_id"
                ),
                change_web_app_acceleration_compartment_details=action_details,
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

    def purge_web_app_acceleration_cache(self):
        action_details = oci_common_utils.convert_input_data_to_model_class(
            self.module.params, PurgeWebAppAccelerationCacheDetails
        )
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.purge_web_app_acceleration_cache,
            call_fn_args=(),
            call_fn_kwargs=dict(
                web_app_acceleration_id=self.module.params.get(
                    "web_app_acceleration_id"
                ),
                purge_web_app_acceleration_cache_details=action_details,
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


WebAppAccelerationActionsHelperCustom = get_custom_class(
    "WebAppAccelerationActionsHelperCustom"
)


class ResourceHelper(
    WebAppAccelerationActionsHelperCustom, WebAppAccelerationActionsHelperGen
):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec(
        supports_create=False, supports_wait=True
    )
    module_args.update(
        dict(
            compartment_id=dict(type="str"),
            web_app_acceleration_id=dict(aliases=["id"], type="str", required=True),
            purge_type=dict(type="str", choices=["ENTIRE_CACHE"]),
            action=dict(
                type="str",
                required=True,
                choices=["change_compartment", "purge_web_app_acceleration_cache"],
            ),
        )
    )

    module = OCIAnsibleModule(argument_spec=module_args, supports_check_mode=True)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_helper = ResourceHelper(
        module=module,
        resource_type="web_app_acceleration",
        service_client_class=WaaClient,
        namespace="waa",
    )

    result = resource_helper.perform_action(module.params.get("action"))

    module.exit_json(**result)


if __name__ == "__main__":
    main()
