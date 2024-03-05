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
module: oci_bds_metastore_configuration_actions
description: >-
    Due to size constraints we have not included the documentation in the module. Please check L(here,
    https://docs.oracle.com/en-us/iaas/tools/oci-ansible-collection/latest/collections/oracle/oci/oci_bds_metastore_configuration_actions_module.html)
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
    from oci.bds.models import ActivateBdsMetastoreConfigurationDetails
    from oci.bds.models import TestBdsMetastoreConfigurationDetails

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


class BdsMetastoreConfigurationActionsHelperGen(OCIActionsHelperBase):
    """
    Supported actions:
        activate
        test
    """

    @staticmethod
    def get_module_resource_id_param():
        return "metastore_config_id"

    def get_module_resource_id(self):
        return self.module.params.get("metastore_config_id")

    def get_get_fn(self):
        return self.client.get_bds_metastore_configuration

    def get_resource(self):
        return oci_common_utils.call_with_backoff(
            self.client.get_bds_metastore_configuration,
            bds_instance_id=self.module.params.get("bds_instance_id"),
            metastore_config_id=self.module.params.get("metastore_config_id"),
        )

    def activate(self):
        action_details = oci_common_utils.convert_input_data_to_model_class(
            self.module.params, ActivateBdsMetastoreConfigurationDetails
        )
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.activate_bds_metastore_configuration,
            call_fn_args=(),
            call_fn_kwargs=dict(
                bds_instance_id=self.module.params.get("bds_instance_id"),
                metastore_config_id=self.module.params.get("metastore_config_id"),
                activate_bds_metastore_configuration_details=action_details,
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

    def test(self):
        action_details = oci_common_utils.convert_input_data_to_model_class(
            self.module.params, TestBdsMetastoreConfigurationDetails
        )
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.test_bds_metastore_configuration,
            call_fn_args=(),
            call_fn_kwargs=dict(
                bds_instance_id=self.module.params.get("bds_instance_id"),
                metastore_config_id=self.module.params.get("metastore_config_id"),
                test_bds_metastore_configuration_details=action_details,
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


BdsMetastoreConfigurationActionsHelperCustom = get_custom_class(
    "BdsMetastoreConfigurationActionsHelperCustom"
)


class ResourceHelper(
    BdsMetastoreConfigurationActionsHelperCustom,
    BdsMetastoreConfigurationActionsHelperGen,
):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec(
        supports_create=False, supports_wait=True
    )
    module_args.update(
        dict(
            bds_api_key_passphrase=dict(type="str", no_log=True),
            bds_instance_id=dict(type="str", required=True),
            metastore_config_id=dict(aliases=["id"], type="str", required=True),
            cluster_admin_password=dict(type="str", required=True, no_log=True),
            action=dict(type="str", required=True, choices=["activate", "test"]),
        )
    )

    module = OCIAnsibleModule(argument_spec=module_args, supports_check_mode=True)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_helper = ResourceHelper(
        module=module,
        resource_type="bds_metastore_configuration",
        service_client_class=BdsClient,
        namespace="bds",
    )

    result = resource_helper.perform_action(module.params.get("action"))

    module.exit_json(**result)


if __name__ == "__main__":
    main()
