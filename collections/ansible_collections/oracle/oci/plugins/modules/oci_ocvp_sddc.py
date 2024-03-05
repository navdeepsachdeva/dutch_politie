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
module: oci_ocvp_sddc
description: >-
    Due to size constraints we have not included the documentation in the module. Please check L(here,
    https://docs.oracle.com/en-us/iaas/tools/oci-ansible-collection/latest/collections/oracle/oci/oci_ocvp_sddc_module.html)
    for the module documentation.
author: Oracle (@oracle)
"""


from ansible_collections.oracle.oci.plugins.module_utils import (
    oci_common_utils,
    oci_wait_utils,
    oci_config_utils,
)
from ansible_collections.oracle.oci.plugins.module_utils.oci_resource_utils import (
    OCIResourceHelperBase,
    get_custom_class,
    OCIAnsibleModule,
)

try:
    from oci.ocvp import WorkRequestClient
    from oci.ocvp import SddcClient
    from oci.ocvp.models import CreateSddcDetails
    from oci.ocvp.models import UpdateSddcDetails

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


class SddcHelperGen(OCIResourceHelperBase):
    """Supported operations: create, update, get, list and delete"""

    def get_waiter_client(self):
        return oci_config_utils.create_service_client(self.module, WorkRequestClient)

    def get_default_module_wait_timeout(self):
        return 21600

    def get_possible_entity_types(self):
        return super(SddcHelperGen, self).get_possible_entity_types() + [
            "vmwaresddc",
            "vmwaresddcs",
            "ocvpvmwaresddc",
            "ocvpvmwaresddcs",
            "vmwaresddcresource",
            "vmwaresddcsresource",
            "sddc",
            "sddcs",
            "ocvpsddc",
            "ocvpsddcs",
            "sddcresource",
            "sddcsresource",
            "ocvp",
        ]

    def get_module_resource_id_param(self):
        return "sddc_id"

    def get_module_resource_id(self):
        return self.module.params.get("sddc_id")

    def get_get_fn(self):
        return self.client.get_sddc

    def get_get_model_from_summary_model(self, summary_model):
        return oci_common_utils.call_with_backoff(
            self.client.get_sddc, sddc_id=summary_model.id,
        ).data

    def get_resource(self):
        return oci_common_utils.call_with_backoff(
            self.client.get_sddc, sddc_id=self.module.params.get("sddc_id"),
        )

    def get_required_kwargs_for_list(self):
        required_list_method_params = [
            "compartment_id",
        ]

        return dict(
            (param, self.module.params[param]) for param in required_list_method_params
        )

    def get_optional_kwargs_for_list(self):
        optional_list_method_params = ["compute_availability_domain", "display_name"]

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
        return oci_common_utils.list_all_resources(self.client.list_sddcs, **kwargs)

    def get_create_model_class(self):
        return CreateSddcDetails

    def create_resource(self):
        create_details = self.get_create_model()
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.create_sddc,
            call_fn_args=(),
            call_fn_kwargs=dict(create_sddc_details=create_details,),
            waiter_type=oci_wait_utils.WORK_REQUEST_WAITER_KEY,
            operation=oci_common_utils.CREATE_OPERATION_KEY,
            waiter_client=self.get_waiter_client(),
            resource_helper=self,
            wait_for_states=oci_common_utils.get_work_request_completed_states(),
        )

    def get_update_model_class(self):
        return UpdateSddcDetails

    def update_resource(self):
        update_details = self.get_update_model()
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.update_sddc,
            call_fn_args=(),
            call_fn_kwargs=dict(
                sddc_id=self.module.params.get("sddc_id"),
                update_sddc_details=update_details,
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
            call_fn=self.client.delete_sddc,
            call_fn_args=(),
            call_fn_kwargs=dict(sddc_id=self.module.params.get("sddc_id"),),
            waiter_type=oci_wait_utils.WORK_REQUEST_WAITER_KEY,
            operation=oci_common_utils.DELETE_OPERATION_KEY,
            waiter_client=self.get_waiter_client(),
            resource_helper=self,
            wait_for_states=oci_common_utils.get_work_request_completed_states(),
        )


SddcHelperCustom = get_custom_class("SddcHelperCustom")


class ResourceHelper(SddcHelperCustom, SddcHelperGen):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec(
        supports_create=True, supports_wait=True
    )
    module_args.update(
        dict(
            compute_availability_domain=dict(type="str"),
            compartment_id=dict(type="str"),
            instance_display_name_prefix=dict(type="str"),
            esxi_hosts_count=dict(type="int"),
            initial_sku=dict(
                type="str", choices=["HOUR", "MONTH", "ONE_YEAR", "THREE_YEARS"]
            ),
            is_hcx_enabled=dict(type="bool"),
            is_hcx_enterprise_enabled=dict(type="bool"),
            is_single_host_sddc=dict(type="bool"),
            workload_network_cidr=dict(type="str"),
            provisioning_subnet_id=dict(type="str"),
            initial_host_shape_name=dict(type="str"),
            initial_host_ocpu_count=dict(type="float"),
            is_shielded_instance_enabled=dict(type="bool"),
            capacity_reservation_id=dict(type="str"),
            datastores=dict(
                type="list",
                elements="dict",
                options=dict(
                    block_volume_ids=dict(type="list", elements="str", required=True),
                    datastore_type=dict(
                        type="str", required=True, choices=["MANAGEMENT", "WORKLOAD"]
                    ),
                ),
            ),
            display_name=dict(aliases=["name"], type="str"),
            vmware_software_version=dict(type="str"),
            ssh_authorized_keys=dict(type="str", no_log=True),
            vsphere_vlan_id=dict(type="str"),
            vmotion_vlan_id=dict(type="str"),
            vsan_vlan_id=dict(type="str"),
            nsx_v_tep_vlan_id=dict(type="str"),
            nsx_edge_v_tep_vlan_id=dict(type="str"),
            nsx_edge_uplink1_vlan_id=dict(type="str"),
            nsx_edge_uplink2_vlan_id=dict(type="str"),
            replication_vlan_id=dict(type="str"),
            provisioning_vlan_id=dict(type="str"),
            hcx_vlan_id=dict(type="str"),
            freeform_tags=dict(type="dict"),
            defined_tags=dict(type="dict"),
            sddc_id=dict(aliases=["id"], type="str"),
            state=dict(type="str", default="present", choices=["present", "absent"]),
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
