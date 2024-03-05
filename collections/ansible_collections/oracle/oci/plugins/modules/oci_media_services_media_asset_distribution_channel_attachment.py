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
module: oci_media_services_media_asset_distribution_channel_attachment
description: >-
    Due to size constraints we have not included the documentation in the module. Please check L(here,
    https://docs.oracle.com/en-us/iaas/tools/oci-ansible-collection/latest/collections/oracle/oci/oci_media_services_media_asset_distribution_channel_attachment_module.html)
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
    from oci.media_services import MediaServicesClient

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


class MediaAssetDistributionChannelAttachmentHelperGen(OCIResourceHelperBase):
    """Supported operations: get, list and delete"""

    def get_possible_entity_types(self):
        return super(
            MediaAssetDistributionChannelAttachmentHelperGen, self
        ).get_possible_entity_types() + [
            "mediaassetdistributionchannelattachment",
            "mediaassetdistributionchannelattachments",
            "mediaServicesmediaassetdistributionchannelattachment",
            "mediaServicesmediaassetdistributionchannelattachments",
            "mediaassetdistributionchannelattachmentresource",
            "mediaassetdistributionchannelattachmentsresource",
            "distributionchannelattachment",
            "distributionchannelattachments",
            "mediaServicesdistributionchannelattachment",
            "mediaServicesdistributionchannelattachments",
            "distributionchannelattachmentresource",
            "distributionchannelattachmentsresource",
            "mediaservices",
        ]

    def get_module_resource_id_param(self):
        return "distribution_channel_id"

    def get_module_resource_id(self):
        return self.module.params.get("distribution_channel_id")

    def get_get_fn(self):
        return self.client.get_media_asset_distribution_channel_attachment

    def get_resource(self):
        optional_params = [
            "version",
        ]
        optional_kwargs = dict(
            (param, self.module.params[param])
            for param in optional_params
            if self.module.params.get(param) is not None
        )
        return oci_common_utils.call_with_backoff(
            self.client.get_media_asset_distribution_channel_attachment,
            media_asset_id=self.module.params.get("media_asset_id"),
            distribution_channel_id=self.module.params.get("distribution_channel_id"),
            **optional_kwargs
        )

    def get_required_kwargs_for_list(self):
        required_list_method_params = [
            "media_asset_id",
        ]

        return dict(
            (param, self.module.params[param]) for param in required_list_method_params
        )

    def get_optional_kwargs_for_list(self):
        optional_list_method_params = ["distribution_channel_id"]

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
            self.client.list_media_asset_distribution_channel_attachments, **kwargs
        )

    def delete_resource(self):
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.delete_media_asset_distribution_channel_attachment,
            call_fn_args=(),
            call_fn_kwargs=dict(
                media_asset_id=self.module.params.get("media_asset_id"),
                distribution_channel_id=self.module.params.get(
                    "distribution_channel_id"
                ),
                version=self.module.params.get("version"),
            ),
            waiter_type=oci_wait_utils.NONE_WAITER_KEY,
            operation=oci_common_utils.DELETE_OPERATION_KEY,
            waiter_client=self.get_waiter_client(),
            resource_helper=self,
            wait_for_states=self.get_wait_for_states_for_operation(
                oci_common_utils.DELETE_OPERATION_KEY,
            ),
        )


MediaAssetDistributionChannelAttachmentHelperCustom = get_custom_class(
    "MediaAssetDistributionChannelAttachmentHelperCustom"
)


class ResourceHelper(
    MediaAssetDistributionChannelAttachmentHelperCustom,
    MediaAssetDistributionChannelAttachmentHelperGen,
):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec(
        supports_create=False, supports_wait=False
    )
    module_args.update(
        dict(
            media_asset_id=dict(type="str", required=True),
            distribution_channel_id=dict(aliases=["id"], type="str", required=True),
            version=dict(type="int"),
            state=dict(type="str", default="present", choices=["absent"]),
        )
    )

    module = OCIAnsibleModule(argument_spec=module_args, supports_check_mode=True)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_helper = ResourceHelper(
        module=module,
        resource_type="media_asset_distribution_channel_attachment",
        service_client_class=MediaServicesClient,
        namespace="media_services",
    )

    result = dict(changed=False)

    if resource_helper.is_delete():
        result = resource_helper.delete()

    module.exit_json(**result)


if __name__ == "__main__":
    main()
