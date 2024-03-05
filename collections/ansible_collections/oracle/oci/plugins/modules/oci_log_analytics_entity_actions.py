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
module: oci_log_analytics_entity_actions
description: >-
    Due to size constraints we have not included the documentation in the module. Please check L(here,
    https://docs.oracle.com/en-us/iaas/tools/oci-ansible-collection/latest/collections/oracle/oci/oci_log_analytics_entity_actions_module.html)
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
    from oci.log_analytics import LogAnalyticsClient
    from oci.log_analytics.models import AddEntityAssociationDetails
    from oci.log_analytics.models import ChangeLogAnalyticsEntityCompartmentDetails
    from oci.log_analytics.models import RemoveEntityAssociationsDetails

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


class LogAnalyticsEntityActionsHelperGen(OCIActionsHelperBase):
    """
    Supported actions:
        add_entity_association
        change_compartment
        remove_entity_associations
    """

    @staticmethod
    def get_module_resource_id_param():
        return "log_analytics_entity_id"

    def get_module_resource_id(self):
        return self.module.params.get("log_analytics_entity_id")

    def get_get_fn(self):
        return self.client.get_log_analytics_entity

    def get_resource(self):
        return oci_common_utils.call_with_backoff(
            self.client.get_log_analytics_entity,
            namespace_name=self.module.params.get("namespace_name"),
            log_analytics_entity_id=self.module.params.get("log_analytics_entity_id"),
        )

    def add_entity_association(self):
        action_details = oci_common_utils.convert_input_data_to_model_class(
            self.module.params, AddEntityAssociationDetails
        )
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.add_entity_association,
            call_fn_args=(),
            call_fn_kwargs=dict(
                namespace_name=self.module.params.get("namespace_name"),
                log_analytics_entity_id=self.module.params.get(
                    "log_analytics_entity_id"
                ),
                add_entity_association_details=action_details,
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

    def change_compartment(self):
        action_details = oci_common_utils.convert_input_data_to_model_class(
            self.module.params, ChangeLogAnalyticsEntityCompartmentDetails
        )
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.change_log_analytics_entity_compartment,
            call_fn_args=(),
            call_fn_kwargs=dict(
                namespace_name=self.module.params.get("namespace_name"),
                log_analytics_entity_id=self.module.params.get(
                    "log_analytics_entity_id"
                ),
                change_log_analytics_entity_compartment_details=action_details,
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

    def remove_entity_associations(self):
        action_details = oci_common_utils.convert_input_data_to_model_class(
            self.module.params, RemoveEntityAssociationsDetails
        )
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.remove_entity_associations,
            call_fn_args=(),
            call_fn_kwargs=dict(
                namespace_name=self.module.params.get("namespace_name"),
                log_analytics_entity_id=self.module.params.get(
                    "log_analytics_entity_id"
                ),
                remove_entity_associations_details=action_details,
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


LogAnalyticsEntityActionsHelperCustom = get_custom_class(
    "LogAnalyticsEntityActionsHelperCustom"
)


class ResourceHelper(
    LogAnalyticsEntityActionsHelperCustom, LogAnalyticsEntityActionsHelperGen
):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec(
        supports_create=False, supports_wait=False
    )
    module_args.update(
        dict(
            compartment_id=dict(type="str"),
            namespace_name=dict(type="str", required=True),
            log_analytics_entity_id=dict(aliases=["id"], type="str", required=True),
            association_entities=dict(type="list", elements="str"),
            action=dict(
                type="str",
                required=True,
                choices=[
                    "add_entity_association",
                    "change_compartment",
                    "remove_entity_associations",
                ],
            ),
        )
    )

    module = OCIAnsibleModule(argument_spec=module_args, supports_check_mode=True)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_helper = ResourceHelper(
        module=module,
        resource_type="log_analytics_entity",
        service_client_class=LogAnalyticsClient,
        namespace="log_analytics",
    )

    result = resource_helper.perform_action(module.params.get("action"))

    module.exit_json(**result)


if __name__ == "__main__":
    main()
