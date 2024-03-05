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
module: oci_os_management_event_content
description: >-
    Due to size constraints we have not included the documentation in the module. Please check L(here,
    https://docs.oracle.com/en-us/iaas/tools/oci-ansible-collection/latest/collections/oracle/oci/oci_os_management_event_content_module.html)
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
    from oci.os_management import EventClient

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


class EventContentHelperGen(OCIResourceHelperBase):
    """Supported operations: get and delete"""

    def get_possible_entity_types(self):
        return super(EventContentHelperGen, self).get_possible_entity_types() + [
            "eventcontent",
            "eventcontents",
            "osManagementeventcontent",
            "osManagementeventcontents",
            "eventcontentresource",
            "eventcontentsresource",
            "content",
            "contents",
            "osManagementcontent",
            "osManagementcontents",
            "contentresource",
            "contentsresource",
            "osmanagement",
        ]

    def get_module_resource_id_param(self):
        return "event_id"

    def get_module_resource_id(self):
        return self.module.params.get("event_id")

    def get_get_fn(self):
        return self.client.get_event_content

    def get_resource(self):
        return oci_common_utils.call_with_backoff(
            self.client.get_event_content,
            managed_instance_id=self.module.params.get("managed_instance_id"),
            event_id=self.module.params.get("event_id"),
            compartment_id=self.module.params.get("compartment_id"),
        )

    def delete_resource(self):
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.delete_event_content,
            call_fn_args=(),
            call_fn_kwargs=dict(
                managed_instance_id=self.module.params.get("managed_instance_id"),
                event_id=self.module.params.get("event_id"),
                compartment_id=self.module.params.get("compartment_id"),
            ),
            waiter_type=oci_wait_utils.NONE_WAITER_KEY,
            operation=oci_common_utils.DELETE_OPERATION_KEY,
            waiter_client=self.get_waiter_client(),
            resource_helper=self,
            wait_for_states=self.get_wait_for_states_for_operation(
                oci_common_utils.DELETE_OPERATION_KEY,
            ),
        )


EventContentHelperCustom = get_custom_class("EventContentHelperCustom")


class ResourceHelper(EventContentHelperCustom, EventContentHelperGen):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec(
        supports_create=False, supports_wait=False
    )
    module_args.update(
        dict(
            managed_instance_id=dict(type="str", required=True),
            event_id=dict(aliases=["id"], type="str", required=True),
            compartment_id=dict(type="str", required=True),
            state=dict(type="str", default="present", choices=["absent"]),
        )
    )

    module = OCIAnsibleModule(argument_spec=module_args, supports_check_mode=True)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_helper = ResourceHelper(
        module=module,
        resource_type="event_content",
        service_client_class=EventClient,
        namespace="os_management",
    )

    result = dict(changed=False)

    if resource_helper.is_delete():
        result = resource_helper.delete()

    module.exit_json(**result)


if __name__ == "__main__":
    main()
