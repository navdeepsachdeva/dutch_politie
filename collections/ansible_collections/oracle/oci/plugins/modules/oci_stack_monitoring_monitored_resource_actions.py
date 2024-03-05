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
module: oci_stack_monitoring_monitored_resource_actions
description: >-
    Due to size constraints we have not included the documentation in the module. Please check L(here,
    https://docs.oracle.com/en-us/iaas/tools/oci-ansible-collection/latest/collections/oracle/oci/oci_stack_monitoring_monitored_resource_actions_module.html)
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
    from oci.stack_monitoring import StackMonitoringClient
    from oci.stack_monitoring.models import AssociateMonitoredResourcesDetails
    from oci.stack_monitoring.models import ChangeMonitoredResourceCompartmentDetails
    from oci.stack_monitoring.models import DisassociateMonitoredResourcesDetails
    from oci.stack_monitoring.models import SearchMonitoredResourceAssociationsDetails
    from oci.stack_monitoring.models import SearchMonitoredResourceMembersDetails
    from oci.stack_monitoring.models import SearchMonitoredResourcesDetails
    from oci.stack_monitoring.models import UpdateAndPropagateTagsDetails

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


class MonitoredResourceActionsHelperGen(OCIActionsHelperBase):
    """
    Supported actions:
        associate
        change_compartment
        disable_external_database
        disassociate
        search_monitored_resource_associations
        search_monitored_resource_members
        search
        update_and_propagate_tags
    """

    @staticmethod
    def get_module_resource_id_param():
        return "monitored_resource_id"

    def get_module_resource_id(self):
        return self.module.params.get("monitored_resource_id")

    def get_get_fn(self):
        return self.client.get_monitored_resource

    def get_resource(self):
        return oci_common_utils.call_with_backoff(
            self.client.get_monitored_resource,
            monitored_resource_id=self.module.params.get("monitored_resource_id"),
        )

    def associate(self):
        action_details = oci_common_utils.convert_input_data_to_model_class(
            self.module.params, AssociateMonitoredResourcesDetails
        )
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.associate_monitored_resources,
            call_fn_args=(),
            call_fn_kwargs=dict(associate_monitored_resources_details=action_details,),
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

    def change_compartment(self):
        action_details = oci_common_utils.convert_input_data_to_model_class(
            self.module.params, ChangeMonitoredResourceCompartmentDetails
        )
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.change_monitored_resource_compartment,
            call_fn_args=(),
            call_fn_kwargs=dict(
                monitored_resource_id=self.module.params.get("monitored_resource_id"),
                change_monitored_resource_compartment_details=action_details,
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

    def disable_external_database(self):
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.disable_external_database,
            call_fn_args=(),
            call_fn_kwargs=dict(
                monitored_resource_id=self.module.params.get("monitored_resource_id"),
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

    def disassociate(self):
        action_details = oci_common_utils.convert_input_data_to_model_class(
            self.module.params, DisassociateMonitoredResourcesDetails
        )
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.disassociate_monitored_resources,
            call_fn_args=(),
            call_fn_kwargs=dict(
                disassociate_monitored_resources_details=action_details,
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

    def search_monitored_resource_associations(self):
        action_details = oci_common_utils.convert_input_data_to_model_class(
            self.module.params, SearchMonitoredResourceAssociationsDetails
        )
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.search_monitored_resource_associations,
            call_fn_args=(),
            call_fn_kwargs=dict(
                search_monitored_resource_associations_details=action_details,
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

    def search_monitored_resource_members(self):
        action_details = oci_common_utils.convert_input_data_to_model_class(
            self.module.params, SearchMonitoredResourceMembersDetails
        )
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.search_monitored_resource_members,
            call_fn_args=(),
            call_fn_kwargs=dict(
                monitored_resource_id=self.module.params.get("monitored_resource_id"),
                search_monitored_resource_members_details=action_details,
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

    def search(self):
        action_details = oci_common_utils.convert_input_data_to_model_class(
            self.module.params, SearchMonitoredResourcesDetails
        )
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.search_monitored_resources,
            call_fn_args=(),
            call_fn_kwargs=dict(
                search_monitored_resources_details=action_details,
                fields=self.module.params.get("fields"),
                exclude_fields=self.module.params.get("exclude_fields"),
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

    def update_and_propagate_tags(self):
        action_details = oci_common_utils.convert_input_data_to_model_class(
            self.module.params, UpdateAndPropagateTagsDetails
        )
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.update_and_propagate_tags,
            call_fn_args=(),
            call_fn_kwargs=dict(
                monitored_resource_id=self.module.params.get("monitored_resource_id"),
                update_and_propagate_tags_details=action_details,
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


MonitoredResourceActionsHelperCustom = get_custom_class(
    "MonitoredResourceActionsHelperCustom"
)


class ResourceHelper(
    MonitoredResourceActionsHelperCustom, MonitoredResourceActionsHelperGen
):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec(
        supports_create=False, supports_wait=True
    )
    module_args.update(
        dict(
            source_resource_id=dict(type="str"),
            source_resource_name=dict(type="str"),
            source_resource_type=dict(type="str"),
            destination_resource_name=dict(type="str"),
            destination_resource_type=dict(type="str"),
            association_type=dict(type="str"),
            destination_resource_id=dict(type="str"),
            limit_level=dict(type="int"),
            compartment_id=dict(type="str"),
            name=dict(type="str"),
            name_contains=dict(type="str"),
            type=dict(type="str"),
            host_name=dict(type="str"),
            external_id=dict(type="str"),
            host_name_contains=dict(type="str"),
            management_agent_id=dict(type="str"),
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
            time_created_greater_than_or_equal_to=dict(type="str"),
            time_created_less_than=dict(type="str"),
            time_updated_greater_than_or_equal_to=dict(type="str"),
            time_updated_less_than=dict(type="str"),
            resource_time_zone=dict(type="str"),
            sort_order=dict(type="str", choices=["ASC", "DESC"]),
            sort_by=dict(
                type="str",
                choices=[
                    "TIME_CREATED",
                    "ASSOC_TYPE",
                    "resourceName",
                    "resourceType",
                    "sourceResourceType",
                    "RESOURCE_NAME",
                ],
            ),
            property_equals=dict(type="dict"),
            fields=dict(type="list", elements="str"),
            exclude_fields=dict(type="list", elements="str"),
            monitored_resource_id=dict(aliases=["id"], type="str"),
            freeform_tags=dict(type="dict"),
            defined_tags=dict(type="dict"),
            association_types=dict(type="list", elements="str"),
            action=dict(
                type="str",
                required=True,
                choices=[
                    "associate",
                    "change_compartment",
                    "disable_external_database",
                    "disassociate",
                    "search_monitored_resource_associations",
                    "search_monitored_resource_members",
                    "search",
                    "update_and_propagate_tags",
                ],
            ),
        )
    )

    module = OCIAnsibleModule(argument_spec=module_args, supports_check_mode=True)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_helper = ResourceHelper(
        module=module,
        resource_type="monitored_resource",
        service_client_class=StackMonitoringClient,
        namespace="stack_monitoring",
    )

    result = resource_helper.perform_action(module.params.get("action"))

    module.exit_json(**result)


if __name__ == "__main__":
    main()
