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
module: oci_mysql_channel
description: >-
    Due to size constraints we have not included the documentation in the module. Please check L(here,
    https://docs.oracle.com/en-us/iaas/tools/oci-ansible-collection/latest/collections/oracle/oci/oci_mysql_channel_module.html)
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
    from oci.mysql import WorkRequestsClient
    from oci.mysql import ChannelsClient
    from oci.mysql.models import CreateChannelDetails
    from oci.mysql.models import UpdateChannelDetails

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


class MysqlChannelHelperGen(OCIResourceHelperBase):
    """Supported operations: create, update, get, list and delete"""

    def get_waiter_client(self):
        return oci_config_utils.create_service_client(self.module, WorkRequestsClient)

    def get_possible_entity_types(self):
        return super(MysqlChannelHelperGen, self).get_possible_entity_types() + [
            "channel",
            "channels",
            "mysqlchannel",
            "mysqlchannels",
            "channelresource",
            "channelsresource",
            "mysql",
        ]

    def get_module_resource_id_param(self):
        return "channel_id"

    def get_module_resource_id(self):
        return self.module.params.get("channel_id")

    def get_get_fn(self):
        return self.client.get_channel

    def get_get_model_from_summary_model(self, summary_model):
        return oci_common_utils.call_with_backoff(
            self.client.get_channel, channel_id=summary_model.id,
        ).data

    def get_resource(self):
        return oci_common_utils.call_with_backoff(
            self.client.get_channel, channel_id=self.module.params.get("channel_id"),
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
            ["channel_id", "display_name"]
            if self._use_name_as_identifier()
            else ["channel_id", "display_name", "is_enabled"]
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
        return oci_common_utils.list_all_resources(self.client.list_channels, **kwargs)

    def get_create_model_class(self):
        return CreateChannelDetails

    def get_exclude_attributes(self):
        return ["source.password"]

    def create_resource(self):
        create_details = self.get_create_model()
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.create_channel,
            call_fn_args=(),
            call_fn_kwargs=dict(create_channel_details=create_details,),
            waiter_type=oci_wait_utils.WORK_REQUEST_WAITER_KEY,
            operation=oci_common_utils.CREATE_OPERATION_KEY,
            waiter_client=self.get_waiter_client(),
            resource_helper=self,
            wait_for_states=oci_common_utils.get_work_request_completed_states(),
        )

    def get_update_model_class(self):
        return UpdateChannelDetails

    def update_resource(self):
        update_details = self.get_update_model()
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.update_channel,
            call_fn_args=(),
            call_fn_kwargs=dict(
                channel_id=self.module.params.get("channel_id"),
                update_channel_details=update_details,
            ),
            waiter_type=oci_wait_utils.WORK_REQUEST_WAITER_KEY,
            operation=oci_common_utils.UPDATE_OPERATION_KEY,
            waiter_client=self.get_waiter_client(),
            resource_helper=self,
            wait_for_states=oci_common_utils.get_work_request_completed_states(),
        )

    def delete_resource(self):
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.delete_channel,
            call_fn_args=(),
            call_fn_kwargs=dict(channel_id=self.module.params.get("channel_id"),),
            waiter_type=oci_wait_utils.WORK_REQUEST_WAITER_KEY,
            operation=oci_common_utils.DELETE_OPERATION_KEY,
            waiter_client=self.get_waiter_client(),
            resource_helper=self,
            wait_for_states=oci_common_utils.get_work_request_completed_states(),
        )


MysqlChannelHelperCustom = get_custom_class("MysqlChannelHelperCustom")


class ResourceHelper(MysqlChannelHelperCustom, MysqlChannelHelperGen):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec(
        supports_create=True, supports_wait=True
    )
    module_args.update(
        dict(
            compartment_id=dict(type="str"),
            source=dict(
                type="dict",
                options=dict(
                    source_type=dict(type="str", required=True, choices=["MYSQL"]),
                    hostname=dict(type="str"),
                    port=dict(type="int"),
                    username=dict(type="str"),
                    password=dict(type="str", no_log=True),
                    ssl_mode=dict(type="str"),
                    ssl_ca_certificate=dict(
                        type="dict",
                        options=dict(
                            certificate_type=dict(
                                type="str", required=True, choices=["PEM"]
                            ),
                            contents=dict(type="str", required=True),
                        ),
                    ),
                    anonymous_transactions_handling=dict(
                        type="dict",
                        options=dict(
                            uuid=dict(type="str"),
                            policy=dict(
                                type="str",
                                required=True,
                                choices=[
                                    "ERROR_ON_ANONYMOUS",
                                    "ASSIGN_MANUAL_UUID",
                                    "ASSIGN_TARGET_UUID",
                                ],
                            ),
                            last_configured_log_filename=dict(type="str"),
                            last_configured_log_offset=dict(type="int"),
                        ),
                    ),
                ),
            ),
            target=dict(
                type="dict",
                options=dict(
                    db_system_id=dict(type="str"),
                    target_type=dict(type="str", required=True, choices=["DBSYSTEM"]),
                    channel_name=dict(type="str"),
                    applier_username=dict(type="str"),
                    filters=dict(
                        type="list",
                        elements="dict",
                        options=dict(
                            type=dict(
                                type="str",
                                required=True,
                                choices=[
                                    "REPLICATE_DO_DB",
                                    "REPLICATE_IGNORE_DB",
                                    "REPLICATE_DO_TABLE",
                                    "REPLICATE_IGNORE_TABLE",
                                    "REPLICATE_WILD_DO_TABLE",
                                    "REPLICATE_WILD_IGNORE_TABLE",
                                    "REPLICATE_REWRITE_DB",
                                ],
                            ),
                            value=dict(type="str", required=True),
                        ),
                    ),
                    tables_without_primary_key_handling=dict(type="str", no_log=True),
                    delay_in_seconds=dict(type="int"),
                ),
            ),
            display_name=dict(aliases=["name"], type="str"),
            is_enabled=dict(type="bool"),
            description=dict(type="str"),
            freeform_tags=dict(type="dict"),
            defined_tags=dict(type="dict"),
            channel_id=dict(aliases=["id"], type="str"),
            state=dict(type="str", default="present", choices=["present", "absent"]),
        )
    )

    module = OCIAnsibleModule(argument_spec=module_args, supports_check_mode=True)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_helper = ResourceHelper(
        module=module,
        resource_type="channel",
        service_client_class=ChannelsClient,
        namespace="mysql",
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
