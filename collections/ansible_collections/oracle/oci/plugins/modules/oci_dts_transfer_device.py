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
module: oci_dts_transfer_device
description: >-
    Due to size constraints we have not included the documentation in the module. Please check L(here,
    https://docs.oracle.com/en-us/iaas/tools/oci-ansible-collection/latest/collections/oracle/oci/oci_dts_transfer_device_module.html)
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
    from oci.dts import TransferDeviceClient
    from oci.dts.models import UpdateTransferDeviceDetails

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


class TransferDeviceHelperGen(OCIResourceHelperBase):
    """Supported operations: update, get, list and delete"""

    def get_possible_entity_types(self):
        return super(TransferDeviceHelperGen, self).get_possible_entity_types() + [
            "transferdevice",
            "transferdevices",
            "dtstransferdevice",
            "dtstransferdevices",
            "transferdeviceresource",
            "transferdevicesresource",
            "dts",
        ]

    def get_module_resource_id_param(self):
        return "transfer_device_label"

    def get_module_resource_id(self):
        return self.module.params.get("transfer_device_label")

    def get_get_fn(self):
        return self.client.get_transfer_device

    def get_resource(self):
        return oci_common_utils.call_with_backoff(
            self.client.get_transfer_device,
            id=self.module.params.get("id"),
            transfer_device_label=self.module.params.get("transfer_device_label"),
        )

    def get_required_kwargs_for_list(self):
        required_list_method_params = [
            "id",
        ]

        return dict(
            (param, self.module.params[param]) for param in required_list_method_params
        )

    def get_optional_kwargs_for_list(self):
        optional_list_method_params = ["lifecycle_state"]

        return dict(
            (param, self.module.params[param])
            for param in optional_list_method_params
            if self.module.params.get(param) is not None
            and (
                self._use_name_as_identifier()
                or (
                    not self.module.params.get("key_by")
                    or param in self.module.params.get("key_by")
                )
            )
        )

    def list_resources(self):

        required_kwargs = self.get_required_kwargs_for_list()
        optional_kwargs = self.get_optional_kwargs_for_list()
        kwargs = oci_common_utils.merge_dicts(required_kwargs, optional_kwargs)
        return oci_common_utils.list_all_resources(
            self.client.list_transfer_devices, **kwargs
        )

    def get_update_model_class(self):
        return UpdateTransferDeviceDetails

    def update_resource(self):
        update_details = self.get_update_model()
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.update_transfer_device,
            call_fn_args=(),
            call_fn_kwargs=dict(
                id=self.module.params.get("id"),
                transfer_device_label=self.module.params.get("transfer_device_label"),
                update_transfer_device_details=update_details,
            ),
            waiter_type=oci_wait_utils.LIFECYCLE_STATE_WAITER_KEY,
            operation=oci_common_utils.UPDATE_OPERATION_KEY,
            waiter_client=self.get_waiter_client(),
            resource_helper=self,
            wait_for_states=self.get_wait_for_states_for_operation(
                oci_common_utils.UPDATE_OPERATION_KEY,
            ),
        )

    def delete_resource(self):
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.delete_transfer_device,
            call_fn_args=(),
            call_fn_kwargs=dict(
                id=self.module.params.get("id"),
                transfer_device_label=self.module.params.get("transfer_device_label"),
            ),
            waiter_type=oci_wait_utils.NONE_WAITER_KEY,
            operation=oci_common_utils.DELETE_OPERATION_KEY,
            waiter_client=self.get_waiter_client(),
            resource_helper=self,
            wait_for_states=self.get_wait_for_states_for_operation(
                oci_common_utils.DELETE_OPERATION_KEY,
            ),
        )


TransferDeviceHelperCustom = get_custom_class("TransferDeviceHelperCustom")


class ResourceHelper(TransferDeviceHelperCustom, TransferDeviceHelperGen):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec(
        supports_create=False, supports_wait=True
    )
    module_args.update(
        dict(
            lifecycle_state=dict(
                type="str", choices=["PREPARING", "READY", "CANCELLED"]
            ),
            id=dict(type="str", required=True),
            transfer_device_label=dict(type="str", required=True),
            state=dict(type="str", default="present", choices=["present", "absent"]),
        )
    )

    module = OCIAnsibleModule(argument_spec=module_args, supports_check_mode=True)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_helper = ResourceHelper(
        module=module,
        resource_type="transfer_device",
        service_client_class=TransferDeviceClient,
        namespace="dts",
    )

    result = dict(changed=False)

    if resource_helper.is_delete():
        result = resource_helper.delete()
    elif resource_helper.is_update():
        result = resource_helper.update()

    module.exit_json(**result)


if __name__ == "__main__":
    main()
