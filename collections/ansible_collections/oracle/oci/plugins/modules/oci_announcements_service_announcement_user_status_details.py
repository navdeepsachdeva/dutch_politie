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
module: oci_announcements_service_announcement_user_status_details
description: >-
    Due to size constraints we have not included the documentation in the module. Please check L(here,
    https://docs.oracle.com/en-us/iaas/tools/oci-ansible-collection/latest/collections/oracle/oci/oci_announcements_service_announcement_user_status_details_module.html)
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
    from oci.announcements_service import AnnouncementClient
    from oci.announcements_service.models import AnnouncementUserStatusDetails

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


class AnnouncementUserStatusDetailsHelperGen(OCIResourceHelperBase):
    """Supported operations: update and get"""

    def get_possible_entity_types(self):
        return super(
            AnnouncementUserStatusDetailsHelperGen, self
        ).get_possible_entity_types() + [
            "announcementuserstatusdetails",
            "announcementuserstatusdetail",
            "announcementsServiceannouncementuserstatusdetails",
            "announcementsServiceannouncementuserstatusdetail",
            "announcementuserstatusdetailsresource",
            "announcementuserstatusdetailresource",
            "userstatus",
            "userstatuses",
            "announcementsServiceuserstatus",
            "announcementsServiceuserstatuses",
            "userstatusresource",
            "userstatusesresource",
            "announcementsservice",
        ]

    def get_module_resource_id_param(self):
        return "announcement_id"

    def get_module_resource_id(self):
        return self.module.params.get("announcement_id")

    def get_get_fn(self):
        return self.client.get_announcement_user_status

    def get_resource(self):
        return oci_common_utils.call_with_backoff(
            self.client.get_announcement_user_status,
            announcement_id=self.module.params.get("announcement_id"),
        )

    def get_update_model_class(self):
        return AnnouncementUserStatusDetails

    def update_resource(self):
        update_details = self.get_update_model()
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.update_announcement_user_status,
            call_fn_args=(),
            call_fn_kwargs=dict(
                announcement_id=self.module.params.get("announcement_id"),
                status_details=update_details,
            ),
            waiter_type=oci_wait_utils.NONE_WAITER_KEY,
            operation=oci_common_utils.UPDATE_OPERATION_KEY,
            waiter_client=self.get_waiter_client(),
            resource_helper=self,
            wait_for_states=self.get_wait_for_states_for_operation(
                oci_common_utils.UPDATE_OPERATION_KEY,
            ),
        )


AnnouncementUserStatusDetailsHelperCustom = get_custom_class(
    "AnnouncementUserStatusDetailsHelperCustom"
)


class ResourceHelper(
    AnnouncementUserStatusDetailsHelperCustom, AnnouncementUserStatusDetailsHelperGen
):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec(
        supports_create=False, supports_wait=False
    )
    module_args.update(
        dict(
            announcement_id=dict(aliases=["id"], type="str", required=True),
            user_status_announcement_id=dict(type="str", required=True),
            user_id=dict(type="str", required=True),
            time_acknowledged=dict(type="str"),
            state=dict(type="str", default="present", choices=["present"]),
        )
    )

    module = OCIAnsibleModule(argument_spec=module_args, supports_check_mode=True)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_helper = ResourceHelper(
        module=module,
        resource_type="announcement_user_status_details",
        service_client_class=AnnouncementClient,
        namespace="announcements_service",
    )

    result = dict(changed=False)

    if resource_helper.is_update():
        result = resource_helper.update()

    module.exit_json(**result)


if __name__ == "__main__":
    main()
