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
module: oci_oda_channel
description: >-
    Due to size constraints we have not included the documentation in the module. Please check L(here,
    https://docs.oracle.com/en-us/iaas/tools/oci-ansible-collection/latest/collections/oracle/oci/oci_oda_channel_module.html)
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
    from oci.oda import ManagementClient
    from oci.oda.models import CreateChannelDetails
    from oci.oda.models import UpdateChannelDetails

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


class ChannelHelperGen(OCIResourceHelperBase):
    """Supported operations: create, update, get, list and delete"""

    def get_possible_entity_types(self):
        return super(ChannelHelperGen, self).get_possible_entity_types() + [
            "channel",
            "channels",
            "odachannel",
            "odachannels",
            "channelresource",
            "channelsresource",
            "oda",
        ]

    def get_module_resource_id_param(self):
        return "channel_id"

    def get_module_resource_id(self):
        return self.module.params.get("channel_id")

    def get_get_fn(self):
        return self.client.get_channel

    def get_get_model_from_summary_model(self, summary_model):
        return oci_common_utils.call_with_backoff(
            self.client.get_channel,
            channel_id=summary_model.id,
            oda_instance_id=self.module.params.get("oda_instance_id"),
        ).data

    def get_resource(self):
        return oci_common_utils.call_with_backoff(
            self.client.get_channel,
            oda_instance_id=self.module.params.get("oda_instance_id"),
            channel_id=self.module.params.get("channel_id"),
        )

    def get_required_kwargs_for_list(self):
        required_list_method_params = [
            "oda_instance_id",
        ]

        return dict(
            (param, self.module.params[param]) for param in required_list_method_params
        )

    def get_optional_kwargs_for_list(self):
        optional_list_method_params = (
            ["name"] if self._use_name_as_identifier() else ["name", "type"]
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
        return [
            "page_access_token",
            "password",
            "signing_secret",
            "client_secret",
            "auth_token",
            "app_secret",
            "msa_app_password",
        ]

    def create_resource(self):
        create_details = self.get_create_model()
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.create_channel,
            call_fn_args=(),
            call_fn_kwargs=dict(
                oda_instance_id=self.module.params.get("oda_instance_id"),
                create_channel_details=create_details,
            ),
            waiter_type=oci_wait_utils.NONE_WAITER_KEY,
            operation=oci_common_utils.CREATE_OPERATION_KEY,
            waiter_client=self.get_waiter_client(),
            resource_helper=self,
            wait_for_states=self.get_wait_for_states_for_operation(
                oci_common_utils.CREATE_OPERATION_KEY,
            ),
        )

    def get_update_model_class(self):
        return UpdateChannelDetails

    def update_resource(self):
        update_details = self.get_update_model()
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.update_channel,
            call_fn_args=(),
            call_fn_kwargs=dict(
                oda_instance_id=self.module.params.get("oda_instance_id"),
                channel_id=self.module.params.get("channel_id"),
                update_channel_details=update_details,
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
            call_fn=self.client.delete_channel,
            call_fn_args=(),
            call_fn_kwargs=dict(
                oda_instance_id=self.module.params.get("oda_instance_id"),
                channel_id=self.module.params.get("channel_id"),
            ),
            waiter_type=oci_wait_utils.NONE_WAITER_KEY,
            operation=oci_common_utils.DELETE_OPERATION_KEY,
            waiter_client=self.get_waiter_client(),
            resource_helper=self,
            wait_for_states=self.get_wait_for_states_for_operation(
                oci_common_utils.DELETE_OPERATION_KEY,
            ),
        )


ChannelHelperCustom = get_custom_class("ChannelHelperCustom")


class ResourceHelper(ChannelHelperCustom, ChannelHelperGen):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec(
        supports_create=True, supports_wait=True
    )
    module_args.update(
        dict(
            name=dict(type="str"),
            host=dict(type="str"),
            port=dict(type="str"),
            total_session_count=dict(type="int"),
            channel_service=dict(type="str", choices=["OSVC", "FUSION"]),
            authentication_provider_name=dict(type="str"),
            inbound_message_topic=dict(type="str"),
            outbound_message_topic=dict(type="str"),
            bootstrap_servers=dict(type="str"),
            security_protocol=dict(type="str"),
            sasl_mechanism=dict(type="str"),
            tenancy_name=dict(type="str"),
            stream_pool_id=dict(type="str"),
            event_sink_bot_ids=dict(type="list", elements="str"),
            allowed_domains=dict(type="str"),
            max_token_expiration_time_in_minutes=dict(type="int", no_log=True),
            is_client_authentication_enabled=dict(type="bool"),
            client_id=dict(type="str"),
            auth_success_url=dict(type="str"),
            auth_error_url=dict(type="str"),
            signing_secret=dict(type="str", no_log=True),
            client_secret=dict(type="str", no_log=True),
            domain_name=dict(type="str"),
            host_name_prefix=dict(type="str"),
            user_name=dict(type="str"),
            password=dict(type="str", no_log=True),
            client_type=dict(type="str", choices=["WSDL", "REST"]),
            account_sid=dict(type="str"),
            phone_number=dict(type="str"),
            auth_token=dict(type="str", no_log=True),
            is_mms_enabled=dict(type="bool"),
            original_connectors_url=dict(type="str"),
            payload_version=dict(type="str", choices=["1.0", "1.1"]),
            outbound_url=dict(type="str"),
            is_authenticated_user_id=dict(type="bool"),
            app_secret=dict(type="str", no_log=True),
            page_access_token=dict(type="str", no_log=True),
            description=dict(type="str"),
            type=dict(
                type="str",
                choices=[
                    "MSTEAMS",
                    "WEB",
                    "FACEBOOK",
                    "APPLICATION",
                    "SERVICECLOUD",
                    "SLACK",
                    "OSVC",
                    "APPEVENT",
                    "OSS",
                    "CORTANA",
                    "ANDROID",
                    "TWILIO",
                    "WEBHOOK",
                    "IOS",
                ],
            ),
            session_expiry_duration_in_milliseconds=dict(type="int"),
            freeform_tags=dict(type="dict"),
            defined_tags=dict(type="dict"),
            msa_app_id=dict(type="str"),
            msa_app_password=dict(type="str", no_log=True),
            bot_id=dict(type="str"),
            oda_instance_id=dict(type="str", required=True),
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
        service_client_class=ManagementClient,
        namespace="oda",
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
