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
module: oci_data_catalog_catalog_actions
description: >-
    Due to size constraints we have not included the documentation in the module. Please check L(here,
    https://docs.oracle.com/en-us/iaas/tools/oci-ansible-collection/latest/collections/oracle/oci/oci_data_catalog_catalog_actions_module.html)
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
    from oci.data_catalog import DataCatalogClient
    from oci.data_catalog.models import AttachCatalogPrivateEndpointDetails
    from oci.data_catalog.models import ChangeCatalogCompartmentDetails
    from oci.data_catalog.models import DetachCatalogPrivateEndpointDetails

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


class DataCatalogCatalogActionsHelperGen(OCIActionsHelperBase):
    """
    Supported actions:
        attach_catalog_private_endpoint
        change_compartment
        detach_catalog_private_endpoint
        object_stats
        users
    """

    @staticmethod
    def get_module_resource_id_param():
        return "catalog_id"

    def get_module_resource_id(self):
        return self.module.params.get("catalog_id")

    def get_get_fn(self):
        return self.client.get_catalog

    def get_resource(self):
        return oci_common_utils.call_with_backoff(
            self.client.get_catalog, catalog_id=self.module.params.get("catalog_id"),
        )

    def attach_catalog_private_endpoint(self):
        action_details = oci_common_utils.convert_input_data_to_model_class(
            self.module.params, AttachCatalogPrivateEndpointDetails
        )
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.attach_catalog_private_endpoint,
            call_fn_args=(),
            call_fn_kwargs=dict(
                attach_catalog_private_endpoint_details=action_details,
                catalog_id=self.module.params.get("catalog_id"),
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

    def change_compartment(self):
        action_details = oci_common_utils.convert_input_data_to_model_class(
            self.module.params, ChangeCatalogCompartmentDetails
        )
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.change_catalog_compartment,
            call_fn_args=(),
            call_fn_kwargs=dict(
                change_catalog_compartment_details=action_details,
                catalog_id=self.module.params.get("catalog_id"),
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

    def detach_catalog_private_endpoint(self):
        action_details = oci_common_utils.convert_input_data_to_model_class(
            self.module.params, DetachCatalogPrivateEndpointDetails
        )
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.detach_catalog_private_endpoint,
            call_fn_args=(),
            call_fn_kwargs=dict(
                detach_catalog_private_endpoint_details=action_details,
                catalog_id=self.module.params.get("catalog_id"),
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

    def object_stats(self):
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.object_stats,
            call_fn_args=(),
            call_fn_kwargs=dict(
                catalog_id=self.module.params.get("catalog_id"),
                sort_by=self.module.params.get("sort_by"),
                sort_order=self.module.params.get("sort_order"),
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

    def users(self):
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.users,
            call_fn_args=(),
            call_fn_kwargs=dict(
                catalog_id=self.module.params.get("catalog_id"),
                sort_by=self.module.params.get("sort_by"),
                sort_order=self.module.params.get("sort_order"),
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


DataCatalogCatalogActionsHelperCustom = get_custom_class(
    "DataCatalogCatalogActionsHelperCustom"
)


class ResourceHelper(
    DataCatalogCatalogActionsHelperCustom, DataCatalogCatalogActionsHelperGen
):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec(
        supports_create=False, supports_wait=True
    )
    module_args.update(
        dict(
            compartment_id=dict(type="str"),
            catalog_private_endpoint_id=dict(type="str"),
            catalog_id=dict(aliases=["id"], type="str", required=True),
            sort_by=dict(type="str", choices=["TIMECREATED", "DISPLAYNAME"]),
            sort_order=dict(type="str", choices=["ASC", "DESC"]),
            action=dict(
                type="str",
                required=True,
                choices=[
                    "attach_catalog_private_endpoint",
                    "change_compartment",
                    "detach_catalog_private_endpoint",
                    "object_stats",
                    "users",
                ],
            ),
        )
    )

    module = OCIAnsibleModule(argument_spec=module_args, supports_check_mode=True)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_helper = ResourceHelper(
        module=module,
        resource_type="catalog",
        service_client_class=DataCatalogClient,
        namespace="data_catalog",
    )

    result = resource_helper.perform_action(module.params.get("action"))

    module.exit_json(**result)


if __name__ == "__main__":
    main()
