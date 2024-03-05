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
module: oci_bds_api_key_actions
description: >-
    Due to size constraints we have not included the documentation in the module. Please check L(here,
    https://docs.oracle.com/en-us/iaas/tools/oci-ansible-collection/latest/collections/oracle/oci/oci_bds_api_key_actions_module.html)
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
    from oci.bds import BdsClient
    from oci.bds.models import TestBdsObjectStorageConnectionDetails

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


class BdsApiKeyActionsHelperGen(OCIActionsHelperBase):
    """
    Supported actions:
        test_bds_object_storage_connection
    """

    @staticmethod
    def get_module_resource_id_param():
        return "api_key_id"

    def get_module_resource_id(self):
        return self.module.params.get("api_key_id")

    def get_get_fn(self):
        return self.client.get_bds_api_key

    def get_resource(self):
        return oci_common_utils.call_with_backoff(
            self.client.get_bds_api_key,
            bds_instance_id=self.module.params.get("bds_instance_id"),
            api_key_id=self.module.params.get("api_key_id"),
        )

    def test_bds_object_storage_connection(self):
        action_details = oci_common_utils.convert_input_data_to_model_class(
            self.module.params, TestBdsObjectStorageConnectionDetails
        )
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.test_bds_object_storage_connection,
            call_fn_args=(),
            call_fn_kwargs=dict(
                bds_instance_id=self.module.params.get("bds_instance_id"),
                api_key_id=self.module.params.get("api_key_id"),
                test_bds_object_storage_connection_details=action_details,
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


BdsApiKeyActionsHelperCustom = get_custom_class("BdsApiKeyActionsHelperCustom")


class ResourceHelper(BdsApiKeyActionsHelperCustom, BdsApiKeyActionsHelperGen):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec(
        supports_create=False, supports_wait=True
    )
    module_args.update(
        dict(
            bds_instance_id=dict(type="str", required=True),
            api_key_id=dict(aliases=["id"], type="str", required=True),
            object_storage_uri=dict(type="str", required=True),
            passphrase=dict(type="str", required=True, no_log=True),
            object_storage_region=dict(type="str"),
            action=dict(
                type="str",
                required=True,
                choices=["test_bds_object_storage_connection"],
            ),
        )
    )

    module = OCIAnsibleModule(argument_spec=module_args, supports_check_mode=True)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_helper = ResourceHelper(
        module=module,
        resource_type="bds_api_key",
        service_client_class=BdsClient,
        namespace="bds",
    )

    result = resource_helper.perform_action(module.params.get("action"))

    module.exit_json(**result)


if __name__ == "__main__":
    main()
