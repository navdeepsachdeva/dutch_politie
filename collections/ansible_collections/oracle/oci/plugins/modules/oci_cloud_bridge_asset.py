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
module: oci_cloud_bridge_asset
description: >-
    Due to size constraints we have not included the documentation in the module. Please check L(here,
    https://docs.oracle.com/en-us/iaas/tools/oci-ansible-collection/latest/collections/oracle/oci/oci_cloud_bridge_asset_module.html)
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
    from oci.cloud_bridge import InventoryClient
    from oci.cloud_bridge.models import CreateAssetDetails
    from oci.cloud_bridge.models import UpdateAssetDetails

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


class AssetHelperGen(OCIResourceHelperBase):
    """Supported operations: create, update, get, list and delete"""

    def get_possible_entity_types(self):
        return super(AssetHelperGen, self).get_possible_entity_types() + [
            "ocbinventoryasset",
            "ocbinventoryassets",
            "cloudBridgeocbinventoryasset",
            "cloudBridgeocbinventoryassets",
            "ocbinventoryassetresource",
            "ocbinventoryassetsresource",
            "asset",
            "assets",
            "cloudBridgeasset",
            "cloudBridgeassets",
            "assetresource",
            "assetsresource",
            "cloudbridge",
        ]

    def get_module_resource_id_param(self):
        return "asset_id"

    def get_module_resource_id(self):
        return self.module.params.get("asset_id")

    def get_get_fn(self):
        return self.client.get_asset

    def get_get_model_from_summary_model(self, summary_model):
        return oci_common_utils.call_with_backoff(
            self.client.get_asset, asset_id=summary_model.id,
        ).data

    def get_resource(self):
        return oci_common_utils.call_with_backoff(
            self.client.get_asset, asset_id=self.module.params.get("asset_id"),
        )

    def get_required_kwargs_for_list(self):
        required_list_method_params = [
            "compartment_id",
        ]

        return dict(
            (param, self.module.params[param]) for param in required_list_method_params
        )

    def get_optional_kwargs_for_list(self):
        optional_list_method_params = (
            [
                "source_key",
                "external_asset_key",
                "asset_id",
                "display_name",
                "inventory_id",
            ]
            if self._use_name_as_identifier()
            else [
                "source_key",
                "external_asset_key",
                "asset_type",
                "asset_id",
                "display_name",
                "inventory_id",
            ]
        )

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
        return oci_common_utils.list_all_resources(self.client.list_assets, **kwargs)

    def get_create_model_class(self):
        return CreateAssetDetails

    def create_resource(self):
        create_details = self.get_create_model()
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.create_asset,
            call_fn_args=(),
            call_fn_kwargs=dict(create_asset_details=create_details,),
            waiter_type=oci_wait_utils.LIFECYCLE_STATE_WAITER_KEY,
            operation=oci_common_utils.CREATE_OPERATION_KEY,
            waiter_client=self.get_waiter_client(),
            resource_helper=self,
            wait_for_states=self.get_wait_for_states_for_operation(
                oci_common_utils.CREATE_OPERATION_KEY,
            ),
        )

    def get_update_model_class(self):
        return UpdateAssetDetails

    def update_resource(self):
        update_details = self.get_update_model()
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.update_asset,
            call_fn_args=(),
            call_fn_kwargs=dict(
                asset_id=self.module.params.get("asset_id"),
                update_asset_details=update_details,
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
            call_fn=self.client.delete_asset,
            call_fn_args=(),
            call_fn_kwargs=dict(asset_id=self.module.params.get("asset_id"),),
            waiter_type=oci_wait_utils.LIFECYCLE_STATE_WAITER_KEY,
            operation=oci_common_utils.DELETE_OPERATION_KEY,
            waiter_client=self.get_waiter_client(),
            resource_helper=self,
            wait_for_states=self.get_wait_for_states_for_operation(
                oci_common_utils.DELETE_OPERATION_KEY,
            ),
        )


AssetHelperCustom = get_custom_class("AssetHelperCustom")


class ResourceHelper(AssetHelperCustom, AssetHelperGen):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec(
        supports_create=True, supports_wait=True
    )
    module_args.update(
        dict(
            inventory_id=dict(type="str"),
            compartment_id=dict(type="str"),
            source_key=dict(type="str", no_log=True),
            external_asset_key=dict(type="str", no_log=True),
            display_name=dict(aliases=["name"], type="str"),
            asset_type=dict(type="str", choices=["VMWARE_VM", "VM"]),
            asset_source_ids=dict(type="list", elements="str"),
            freeform_tags=dict(type="dict"),
            defined_tags=dict(type="dict"),
            compute=dict(
                type="dict",
                options=dict(
                    primary_ip=dict(type="str"),
                    dns_name=dict(type="str"),
                    description=dict(type="str"),
                    cores_count=dict(type="int"),
                    cpu_model=dict(type="str"),
                    gpu_devices_count=dict(type="int"),
                    gpu_devices=dict(
                        type="list",
                        elements="dict",
                        options=dict(
                            name=dict(type="str"),
                            description=dict(type="str"),
                            cores_count=dict(type="int"),
                            memory_in_mbs=dict(type="int"),
                            manufacturer=dict(type="str"),
                        ),
                    ),
                    threads_per_core_count=dict(type="int"),
                    memory_in_mbs=dict(type="int"),
                    is_pmem_enabled=dict(type="bool"),
                    pmem_in_mbs=dict(type="int"),
                    operating_system=dict(type="str"),
                    operating_system_version=dict(type="str"),
                    host_name=dict(type="str"),
                    power_state=dict(type="str"),
                    guest_state=dict(type="str"),
                    is_tpm_enabled=dict(type="bool"),
                    connected_networks=dict(type="int"),
                    nics_count=dict(type="int"),
                    nics=dict(
                        type="list",
                        elements="dict",
                        options=dict(
                            label=dict(type="str"),
                            switch_name=dict(type="str"),
                            mac_address=dict(type="str"),
                            mac_address_type=dict(type="str"),
                            network_name=dict(type="str"),
                            ip_addresses=dict(type="list", elements="str"),
                        ),
                    ),
                    storage_provisioned_in_mbs=dict(type="int"),
                    disks_count=dict(type="int"),
                    disks=dict(
                        type="list",
                        elements="dict",
                        options=dict(
                            name=dict(type="str"),
                            boot_order=dict(type="int"),
                            uuid=dict(type="str"),
                            uuid_lun=dict(type="str"),
                            size_in_mbs=dict(type="int"),
                            location=dict(type="str"),
                            persistent_mode=dict(type="str"),
                        ),
                    ),
                    firmware=dict(type="str"),
                    latency_sensitivity=dict(type="str"),
                    nvdimms=dict(
                        type="list",
                        elements="dict",
                        options=dict(
                            label=dict(type="str"),
                            unit_number=dict(type="int"),
                            controller_key=dict(type="int", no_log=True),
                        ),
                    ),
                    nvdimm_controller=dict(
                        type="dict",
                        options=dict(
                            label=dict(type="str"), bus_number=dict(type="int")
                        ),
                    ),
                    scsi_controller=dict(
                        type="dict",
                        options=dict(
                            label=dict(type="str"),
                            unit_number=dict(type="int"),
                            shared_bus=dict(type="str"),
                        ),
                    ),
                    hardware_version=dict(type="str"),
                ),
            ),
            vm=dict(
                type="dict",
                options=dict(
                    hypervisor_vendor=dict(type="str"),
                    hypervisor_version=dict(type="str"),
                    hypervisor_host=dict(type="str"),
                ),
            ),
            vmware_vm=dict(
                type="dict",
                options=dict(
                    cluster=dict(type="str"),
                    customer_fields=dict(type="list", elements="str"),
                    customer_tags=dict(
                        type="list",
                        elements="dict",
                        options=dict(
                            name=dict(type="str"), description=dict(type="str")
                        ),
                    ),
                    instance_uuid=dict(type="str"),
                    path=dict(type="str"),
                    vmware_tools_status=dict(type="str"),
                    is_disks_uuid_enabled=dict(type="bool"),
                    is_disks_cbt_enabled=dict(type="bool"),
                    fault_tolerance_state=dict(type="str"),
                    fault_tolerance_bandwidth=dict(type="int"),
                    fault_tolerance_secondary_latency=dict(type="int"),
                ),
            ),
            vmware_v_center=dict(
                type="dict",
                options=dict(
                    vcenter_key=dict(type="str", no_log=True),
                    vcenter_version=dict(type="str"),
                    data_center=dict(type="str"),
                ),
            ),
            asset_id=dict(aliases=["id"], type="str"),
            state=dict(type="str", default="present", choices=["present", "absent"]),
        )
    )

    module = OCIAnsibleModule(argument_spec=module_args, supports_check_mode=True)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_helper = ResourceHelper(
        module=module,
        resource_type="asset",
        service_client_class=InventoryClient,
        namespace="cloud_bridge",
    )

    result = dict(changed=False)

    if resource_helper.is_delete_using_name():
        result = resource_helper.delete_using_name()
    elif resource_helper.is_delete():
        result = resource_helper.delete()
    elif resource_helper.is_update_using_name():
        result = resource_helper.update_using_name()
    elif resource_helper.is_update():
        result = resource_helper.update()
    elif resource_helper.is_create():
        result = resource_helper.create()

    module.exit_json(**result)


if __name__ == "__main__":
    main()
