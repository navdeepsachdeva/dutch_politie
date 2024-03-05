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
module: oci_cloud_migrations_target_asset
description: >-
    Due to size constraints we have not included the documentation in the module. Please check L(here,
    https://docs.oracle.com/en-us/iaas/tools/oci-ansible-collection/latest/collections/oracle/oci/oci_cloud_migrations_target_asset_module.html)
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
    from oci.cloud_migrations import MigrationClient
    from oci.cloud_migrations.models import CreateTargetAssetDetails
    from oci.cloud_migrations.models import UpdateTargetAssetDetails

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


class TargetAssetHelperGen(OCIResourceHelperBase):
    """Supported operations: create, update, get, list and delete"""

    def get_possible_entity_types(self):
        return super(TargetAssetHelperGen, self).get_possible_entity_types() + [
            "ocmtargetasset",
            "ocmtargetassets",
            "cloudMigrationsocmtargetasset",
            "cloudMigrationsocmtargetassets",
            "ocmtargetassetresource",
            "ocmtargetassetsresource",
            "targetasset",
            "targetassets",
            "cloudMigrationstargetasset",
            "cloudMigrationstargetassets",
            "targetassetresource",
            "targetassetsresource",
            "cloudmigrations",
        ]

    def get_module_resource_id_param(self):
        return "target_asset_id"

    def get_module_resource_id(self):
        return self.module.params.get("target_asset_id")

    def get_get_fn(self):
        return self.client.get_target_asset

    def get_get_model_from_summary_model(self, summary_model):
        return oci_common_utils.call_with_backoff(
            self.client.get_target_asset, target_asset_id=summary_model.id,
        ).data

    def get_resource(self):
        return oci_common_utils.call_with_backoff(
            self.client.get_target_asset,
            target_asset_id=self.module.params.get("target_asset_id"),
        )

    def get_required_kwargs_for_list(self):
        return dict()

    def get_optional_kwargs_for_list(self):
        optional_list_method_params = ["migration_plan_id", "target_asset_id"]

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
            self.client.list_target_assets, **kwargs
        )

    def get_create_model_class(self):
        return CreateTargetAssetDetails

    def create_resource(self):
        create_details = self.get_create_model()
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.create_target_asset,
            call_fn_args=(),
            call_fn_kwargs=dict(create_target_asset_details=create_details,),
            waiter_type=oci_wait_utils.WORK_REQUEST_WAITER_KEY,
            operation=oci_common_utils.CREATE_OPERATION_KEY,
            waiter_client=self.get_waiter_client(),
            resource_helper=self,
            wait_for_states=oci_common_utils.get_work_request_completed_states(),
        )

    def get_update_model_class(self):
        return UpdateTargetAssetDetails

    def update_resource(self):
        update_details = self.get_update_model()
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.update_target_asset,
            call_fn_args=(),
            call_fn_kwargs=dict(
                target_asset_id=self.module.params.get("target_asset_id"),
                update_target_asset_details=update_details,
            ),
            waiter_type=oci_wait_utils.WORK_REQUEST_WAITER_KEY,
            operation=oci_common_utils.UPDATE_OPERATION_KEY,
            waiter_client=self.get_waiter_client(),
            resource_helper=self,
            wait_for_states=oci_common_utils.get_work_request_completed_states(),
        )

    def delete_resource(self):
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.delete_target_asset,
            call_fn_args=(),
            call_fn_kwargs=dict(
                target_asset_id=self.module.params.get("target_asset_id"),
            ),
            waiter_type=oci_wait_utils.WORK_REQUEST_WAITER_KEY,
            operation=oci_common_utils.DELETE_OPERATION_KEY,
            waiter_client=self.get_waiter_client(),
            resource_helper=self,
            wait_for_states=oci_common_utils.get_work_request_completed_states(),
        )


TargetAssetHelperCustom = get_custom_class("TargetAssetHelperCustom")


class ResourceHelper(TargetAssetHelperCustom, TargetAssetHelperGen):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec(
        supports_create=True, supports_wait=True
    )
    module_args.update(
        dict(
            migration_plan_id=dict(type="str"),
            type=dict(type="str", choices=["INSTANCE"]),
            is_excluded_from_execution=dict(type="bool"),
            preferred_shape_type=dict(type="str"),
            block_volumes_performance=dict(type="int"),
            ms_license=dict(type="str"),
            user_spec=dict(
                type="dict",
                options=dict(
                    availability_domain=dict(type="str"),
                    capacity_reservation_id=dict(type="str"),
                    compartment_id=dict(type="str"),
                    create_vnic_details=dict(
                        type="dict",
                        options=dict(
                            assign_public_ip=dict(type="bool"),
                            assign_private_dns_record=dict(type="bool"),
                            defined_tags=dict(type="dict"),
                            display_name=dict(aliases=["name"], type="str"),
                            freeform_tags=dict(type="dict"),
                            hostname_label=dict(type="str"),
                            nsg_ids=dict(type="list", elements="str"),
                            private_ip=dict(type="str"),
                            skip_source_dest_check=dict(type="bool"),
                            subnet_id=dict(type="str"),
                            vlan_id=dict(type="str"),
                        ),
                    ),
                    dedicated_vm_host_id=dict(type="str"),
                    defined_tags=dict(type="dict"),
                    display_name=dict(aliases=["name"], type="str"),
                    fault_domain=dict(type="str"),
                    freeform_tags=dict(type="dict"),
                    hostname_label=dict(type="str"),
                    ipxe_script=dict(type="str"),
                    instance_options=dict(
                        type="dict",
                        options=dict(
                            are_legacy_imds_endpoints_disabled=dict(type="bool")
                        ),
                    ),
                    preemptible_instance_config=dict(
                        type="dict",
                        options=dict(
                            preemption_action=dict(
                                type="dict",
                                required=True,
                                options=dict(
                                    type=dict(
                                        type="str", required=True, choices=["TERMINATE"]
                                    ),
                                    preserve_boot_volume=dict(type="bool"),
                                ),
                            )
                        ),
                    ),
                    agent_config=dict(
                        type="dict",
                        options=dict(
                            is_monitoring_disabled=dict(type="bool"),
                            is_management_disabled=dict(type="bool"),
                            are_all_plugins_disabled=dict(type="bool"),
                            plugins_config=dict(
                                type="list",
                                elements="dict",
                                options=dict(
                                    name=dict(type="str", required=True),
                                    desired_state=dict(
                                        type="str",
                                        required=True,
                                        choices=["ENABLED", "DISABLED"],
                                    ),
                                ),
                            ),
                        ),
                    ),
                    shape=dict(type="str"),
                    shape_config=dict(
                        type="dict",
                        options=dict(
                            ocpus=dict(type="float"),
                            memory_in_gbs=dict(type="float"),
                            baseline_ocpu_utilization=dict(
                                type="str",
                                choices=[
                                    "BASELINE_1_8",
                                    "BASELINE_1_2",
                                    "BASELINE_1_1",
                                ],
                            ),
                        ),
                    ),
                    source_details=dict(
                        type="dict",
                        options=dict(
                            boot_volume_size_in_gbs=dict(type="int"),
                            image_id=dict(type="str"),
                            kms_key_id=dict(type="str"),
                            boot_volume_vpus_per_gb=dict(type="int"),
                            source_type=dict(
                                type="str",
                                required=True,
                                choices=["image", "bootVolume"],
                            ),
                            boot_volume_id=dict(type="str"),
                        ),
                    ),
                    is_pv_encryption_in_transit_enabled=dict(type="bool"),
                ),
            ),
            target_asset_id=dict(aliases=["id"], type="str"),
            state=dict(type="str", default="present", choices=["present", "absent"]),
        )
    )

    module = OCIAnsibleModule(argument_spec=module_args, supports_check_mode=True)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_helper = ResourceHelper(
        module=module,
        resource_type="target_asset",
        service_client_class=MigrationClient,
        namespace="cloud_migrations",
    )

    result = dict(changed=False)

    if resource_helper.is_delete():
        result = resource_helper.delete()
    elif resource_helper.is_update():
        result = resource_helper.update()
    elif resource_helper.is_create():
        result = resource_helper.create()

    module.exit_json(**result)


if __name__ == "__main__":
    main()
