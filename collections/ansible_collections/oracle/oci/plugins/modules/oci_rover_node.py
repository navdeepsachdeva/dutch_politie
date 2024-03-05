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
module: oci_rover_node
description: >-
    Due to size constraints we have not included the documentation in the module. Please check L(here,
    https://docs.oracle.com/en-us/iaas/tools/oci-ansible-collection/latest/collections/oracle/oci/oci_rover_node_module.html)
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
    from oci.rover import RoverNodeClient
    from oci.rover.models import CreateRoverNodeDetails
    from oci.rover.models import UpdateRoverNodeDetails

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


class RoverNodeHelperGen(OCIResourceHelperBase):
    """Supported operations: create, update, get, list and delete"""

    def get_possible_entity_types(self):
        return super(RoverNodeHelperGen, self).get_possible_entity_types() + [
            "rovernode",
            "rovernodes",
            "roverrovernode",
            "roverrovernodes",
            "rovernoderesource",
            "rovernodesresource",
            "rover",
        ]

    def get_module_resource_id_param(self):
        return "rover_node_id"

    def get_module_resource_id(self):
        return self.module.params.get("rover_node_id")

    def get_get_fn(self):
        return self.client.get_rover_node

    def get_get_model_from_summary_model(self, summary_model):
        return oci_common_utils.call_with_backoff(
            self.client.get_rover_node, rover_node_id=summary_model.id,
        ).data

    def get_resource(self):
        return oci_common_utils.call_with_backoff(
            self.client.get_rover_node,
            rover_node_id=self.module.params.get("rover_node_id"),
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
            ["display_name"]
            if self._use_name_as_identifier()
            else ["display_name", "shape", "lifecycle_state"]
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
        return oci_common_utils.list_all_resources(
            self.client.list_rover_nodes, **kwargs
        )

    def get_create_model_class(self):
        return CreateRoverNodeDetails

    def create_resource(self):
        create_details = self.get_create_model()
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.create_rover_node,
            call_fn_args=(),
            call_fn_kwargs=dict(create_rover_node_details=create_details,),
            waiter_type=oci_wait_utils.LIFECYCLE_STATE_WAITER_KEY,
            operation=oci_common_utils.CREATE_OPERATION_KEY,
            waiter_client=self.get_waiter_client(),
            resource_helper=self,
            wait_for_states=self.get_wait_for_states_for_operation(
                oci_common_utils.CREATE_OPERATION_KEY,
            ),
        )

    def get_update_model_class(self):
        return UpdateRoverNodeDetails

    def update_resource(self):
        update_details = self.get_update_model()
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.update_rover_node,
            call_fn_args=(),
            call_fn_kwargs=dict(
                rover_node_id=self.module.params.get("rover_node_id"),
                update_rover_node_details=update_details,
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
            call_fn=self.client.delete_rover_node,
            call_fn_args=(),
            call_fn_kwargs=dict(rover_node_id=self.module.params.get("rover_node_id"),),
            waiter_type=oci_wait_utils.LIFECYCLE_STATE_WAITER_KEY,
            operation=oci_common_utils.DELETE_OPERATION_KEY,
            waiter_client=self.get_waiter_client(),
            resource_helper=self,
            wait_for_states=self.get_wait_for_states_for_operation(
                oci_common_utils.DELETE_OPERATION_KEY,
            ),
        )


RoverNodeHelperCustom = get_custom_class("RoverNodeHelperCustom")


class ResourceHelper(RoverNodeHelperCustom, RoverNodeHelperGen):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec(
        supports_create=True, supports_wait=True
    )
    module_args.update(
        dict(
            compartment_id=dict(type="str"),
            master_key_id=dict(type="str"),
            display_name=dict(aliases=["name"], type="str"),
            shape=dict(type="str"),
            serial_number=dict(type="str"),
            customer_shipping_address=dict(
                type="dict",
                options=dict(
                    addressee=dict(type="str", required=True),
                    care_of=dict(type="str"),
                    address1=dict(type="str", required=True),
                    address2=dict(type="str"),
                    address3=dict(type="str"),
                    address4=dict(type="str"),
                    city_or_locality=dict(type="str", required=True),
                    state_or_region=dict(type="str", required=True),
                    zipcode=dict(type="str", required=True),
                    country=dict(type="str", required=True),
                    phone_number=dict(type="str", required=True),
                    email=dict(type="str"),
                ),
            ),
            node_workloads=dict(
                type="list",
                elements="dict",
                options=dict(
                    name=dict(type="str"),
                    compartment_id=dict(type="str", required=True),
                    id=dict(type="str", required=True),
                    size=dict(type="str"),
                    object_count=dict(type="str"),
                    prefix=dict(type="str"),
                    range_start=dict(type="str"),
                    range_end=dict(type="str"),
                    workload_type=dict(type="str", required=True),
                    work_request_id=dict(type="str"),
                ),
            ),
            super_user_password=dict(type="str", no_log=True),
            unlock_passphrase=dict(type="str", no_log=True),
            point_of_contact=dict(type="str"),
            point_of_contact_phone_number=dict(type="str"),
            oracle_shipping_tracking_url=dict(type="str"),
            shipping_preference=dict(
                type="str", choices=["ORACLE_SHIPPED", "CUSTOMER_PICKUP"]
            ),
            shipping_vendor=dict(type="str"),
            time_pickup_expected=dict(type="str"),
            lifecycle_state=dict(
                type="str",
                choices=[
                    "CREATING",
                    "UPDATING",
                    "ACTIVE",
                    "DELETING",
                    "DELETED",
                    "FAILED",
                ],
            ),
            enclosure_type=dict(type="str", choices=["RUGGADIZED", "NON_RUGGADIZED"]),
            lifecycle_state_details=dict(type="str"),
            time_return_window_starts=dict(type="str"),
            time_return_window_ends=dict(type="str"),
            is_import_requested=dict(type="bool"),
            import_compartment_id=dict(type="str"),
            import_file_bucket=dict(type="str"),
            data_validation_code=dict(type="str"),
            public_key=dict(type="str"),
            freeform_tags=dict(type="dict"),
            defined_tags=dict(type="dict"),
            system_tags=dict(type="dict"),
            rover_node_id=dict(aliases=["id"], type="str"),
            state=dict(type="str", default="present", choices=["present", "absent"]),
        )
    )

    module = OCIAnsibleModule(argument_spec=module_args, supports_check_mode=True)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_helper = ResourceHelper(
        module=module,
        resource_type="rover_node",
        service_client_class=RoverNodeClient,
        namespace="rover",
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
