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
module: oci_analytics_private_access_channel
description: >-
    Due to size constraints we have not included the documentation in the module. Please check L(here,
    https://docs.oracle.com/en-us/iaas/tools/oci-ansible-collection/latest/collections/oracle/oci/oci_analytics_private_access_channel_module.html)
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
    from oci.analytics import AnalyticsClient
    from oci.analytics.models import CreatePrivateAccessChannelDetails
    from oci.analytics.models import UpdatePrivateAccessChannelDetails

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


class PrivateAccessChannelHelperGen(OCIResourceHelperBase):
    """Supported operations: create, update, get and delete"""

    def get_default_module_wait_timeout(self):
        return 7200

    def get_possible_entity_types(self):
        return super(
            PrivateAccessChannelHelperGen, self
        ).get_possible_entity_types() + [
            "privateaccesschannel",
            "privateaccesschannels",
            "analyticsprivateaccesschannel",
            "analyticsprivateaccesschannels",
            "privateaccesschannelresource",
            "privateaccesschannelsresource",
            "analytics",
        ]

    def get_module_resource_id_param(self):
        return "analytics_instance_id"

    def get_module_resource_id(self):
        return self.module.params.get("analytics_instance_id")

    def get_get_fn(self):
        return self.client.get_private_access_channel

    def get_resource(self):
        return oci_common_utils.call_with_backoff(
            self.client.get_private_access_channel,
            private_access_channel_key=self.module.params.get(
                "private_access_channel_key"
            ),
            analytics_instance_id=self.module.params.get("analytics_instance_id"),
        )

    def get_create_model_class(self):
        return CreatePrivateAccessChannelDetails

    def create_resource(self):
        create_details = self.get_create_model()
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.create_private_access_channel,
            call_fn_args=(),
            call_fn_kwargs=dict(
                analytics_instance_id=self.module.params.get("analytics_instance_id"),
                create_private_access_channel_details=create_details,
            ),
            waiter_type=oci_wait_utils.WORK_REQUEST_WAITER_KEY,
            operation=oci_common_utils.CREATE_OPERATION_KEY,
            waiter_client=self.get_waiter_client(),
            resource_helper=self,
            wait_for_states=oci_common_utils.get_work_request_completed_states(),
        )

    def get_update_model_class(self):
        return UpdatePrivateAccessChannelDetails

    def update_resource(self):
        update_details = self.get_update_model()
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.update_private_access_channel,
            call_fn_args=(),
            call_fn_kwargs=dict(
                private_access_channel_key=self.module.params.get(
                    "private_access_channel_key"
                ),
                analytics_instance_id=self.module.params.get("analytics_instance_id"),
                update_private_access_channel_details=update_details,
            ),
            waiter_type=oci_wait_utils.WORK_REQUEST_WAITER_KEY,
            operation=oci_common_utils.UPDATE_OPERATION_KEY,
            waiter_client=self.get_waiter_client(),
            resource_helper=self,
            wait_for_states=oci_common_utils.get_work_request_completed_states(),
        )

    def delete_resource(self):
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.delete_private_access_channel,
            call_fn_args=(),
            call_fn_kwargs=dict(
                private_access_channel_key=self.module.params.get(
                    "private_access_channel_key"
                ),
                analytics_instance_id=self.module.params.get("analytics_instance_id"),
            ),
            waiter_type=oci_wait_utils.WORK_REQUEST_WAITER_KEY,
            operation=oci_common_utils.DELETE_OPERATION_KEY,
            waiter_client=self.get_waiter_client(),
            resource_helper=self,
            wait_for_states=oci_common_utils.get_work_request_completed_states(),
        )


PrivateAccessChannelHelperCustom = get_custom_class("PrivateAccessChannelHelperCustom")


class ResourceHelper(PrivateAccessChannelHelperCustom, PrivateAccessChannelHelperGen):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec(
        supports_create=True, supports_wait=True
    )
    module_args.update(
        dict(
            display_name=dict(aliases=["name"], type="str"),
            vcn_id=dict(type="str"),
            subnet_id=dict(type="str"),
            private_source_dns_zones=dict(
                type="list",
                elements="dict",
                options=dict(
                    dns_zone=dict(type="str", required=True),
                    description=dict(type="str"),
                ),
            ),
            private_source_scan_hosts=dict(
                type="list",
                elements="dict",
                options=dict(
                    scan_hostname=dict(type="str", required=True),
                    scan_port=dict(type="int", required=True),
                    description=dict(type="str"),
                ),
            ),
            network_security_group_ids=dict(type="list", elements="str"),
            private_access_channel_key=dict(type="str", no_log=True),
            analytics_instance_id=dict(aliases=["id"], type="str", required=True),
            state=dict(type="str", default="present", choices=["present", "absent"]),
        )
    )

    module = OCIAnsibleModule(argument_spec=module_args, supports_check_mode=True)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_helper = ResourceHelper(
        module=module,
        resource_type="private_access_channel",
        service_client_class=AnalyticsClient,
        namespace="analytics",
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
