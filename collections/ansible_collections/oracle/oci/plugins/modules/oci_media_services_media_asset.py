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
module: oci_media_services_media_asset
description: >-
    Due to size constraints we have not included the documentation in the module. Please check L(here,
    https://docs.oracle.com/en-us/iaas/tools/oci-ansible-collection/latest/collections/oracle/oci/oci_media_services_media_asset_module.html)
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
    from oci.media_services.models import CreateMediaAssetDetails
    from oci.media_services.models import UpdateMediaAssetDetails

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


class MediaAssetHelperGen(OCIResourceHelperBase):
    """Supported operations: create, update, get, list and delete"""

    def get_possible_entity_types(self):
        return super(MediaAssetHelperGen, self).get_possible_entity_types() + [
            "mediaasset",
            "mediaassets",
            "mediaServicesmediaasset",
            "mediaServicesmediaassets",
            "mediaassetresource",
            "mediaassetsresource",
            "mediaservices",
        ]

    def get_module_resource_id_param(self):
        return "media_asset_id"

    def get_module_resource_id(self):
        return self.module.params.get("media_asset_id")

    def get_get_fn(self):
        return self.client.get_media_asset

    def get_get_model_from_summary_model(self, summary_model):
        return oci_common_utils.call_with_backoff(
            self.client.get_media_asset, media_asset_id=summary_model.id,
        ).data

    def get_resource(self):
        return oci_common_utils.call_with_backoff(
            self.client.get_media_asset,
            media_asset_id=self.module.params.get("media_asset_id"),
        )

    def get_required_kwargs_for_list(self):
        return dict()

    def get_optional_kwargs_for_list(self):
        optional_list_method_params = (
            [
                "compartment_id",
                "display_name",
                "bucket_name",
                "object_name",
                "media_workflow_job_id",
                "source_media_workflow_id",
                "source_media_workflow_version",
            ]
            if self._use_name_as_identifier()
            else [
                "compartment_id",
                "display_name",
                "parent_media_asset_id",
                "master_media_asset_id",
                "type",
                "bucket_name",
                "object_name",
                "media_workflow_job_id",
                "source_media_workflow_id",
                "source_media_workflow_version",
            ]
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
            self.client.list_media_assets, **kwargs
        )

    def get_create_model_class(self):
        return CreateMediaAssetDetails

    def create_resource(self):
        create_details = self.get_create_model()
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.create_media_asset,
            call_fn_args=(),
            call_fn_kwargs=dict(create_media_asset_details=create_details,),
            waiter_type=oci_wait_utils.LIFECYCLE_STATE_WAITER_KEY,
            operation=oci_common_utils.CREATE_OPERATION_KEY,
            waiter_client=self.get_waiter_client(),
            resource_helper=self,
            wait_for_states=self.get_wait_for_states_for_operation(
                oci_common_utils.CREATE_OPERATION_KEY,
            ),
        )

    def get_update_model_class(self):
        return UpdateMediaAssetDetails

    def update_resource(self):
        update_details = self.get_update_model()
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.update_media_asset,
            call_fn_args=(),
            call_fn_kwargs=dict(
                media_asset_id=self.module.params.get("media_asset_id"),
                update_media_asset_details=update_details,
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
        optional_enum_params = [
            "delete_mode",
        ]
        optional_enum_kwargs = dict(
            (param, self.module.params[param])
            for param in optional_enum_params
            if self.module.params.get(param) is not None
        )
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.delete_media_asset,
            call_fn_args=(),
            call_fn_kwargs=dict(
                media_asset_id=self.module.params.get("media_asset_id"),
                **optional_enum_kwargs
            ),
            waiter_type=oci_wait_utils.LIFECYCLE_STATE_WAITER_KEY,
            operation=oci_common_utils.DELETE_OPERATION_KEY,
            waiter_client=self.get_waiter_client(),
            resource_helper=self,
            wait_for_states=self.get_wait_for_states_for_operation(
                oci_common_utils.DELETE_OPERATION_KEY,
            ),
        )


MediaAssetHelperCustom = get_custom_class("MediaAssetHelperCustom")


class ResourceHelper(MediaAssetHelperCustom, MediaAssetHelperGen):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec(
        supports_create=True, supports_wait=True
    )
    module_args.update(
        dict(
            source_media_workflow_id=dict(type="str"),
            media_workflow_job_id=dict(type="str"),
            source_media_workflow_version=dict(type="int"),
            compartment_id=dict(type="str"),
            bucket_name=dict(type="str"),
            namespace_name=dict(type="str"),
            object_name=dict(type="str"),
            object_etag=dict(type="str"),
            segment_range_start_index=dict(type="int"),
            segment_range_end_index=dict(type="int"),
            display_name=dict(aliases=["name"], type="str"),
            type=dict(
                type="str",
                choices=[
                    "AUDIO",
                    "VIDEO",
                    "PLAYLIST",
                    "IMAGE",
                    "CAPTION_FILE",
                    "UNKNOWN",
                ],
            ),
            parent_media_asset_id=dict(type="str"),
            master_media_asset_id=dict(type="str"),
            metadata=dict(
                type="list",
                elements="dict",
                options=dict(metadata=dict(type="str", required=True)),
            ),
            media_asset_tags=dict(
                type="list",
                elements="dict",
                options=dict(
                    type=dict(type="str", choices=["USER", "SYSTEM"]),
                    value=dict(type="str", required=True),
                ),
            ),
            freeform_tags=dict(type="dict"),
            defined_tags=dict(type="dict"),
            media_asset_id=dict(aliases=["id"], type="str"),
            delete_mode=dict(
                type="str", choices=["DELETE_CHILDREN", "DELETE_DERIVATIONS"]
            ),
            state=dict(type="str", default="present", choices=["present", "absent"]),
        )
    )

    module = OCIAnsibleModule(argument_spec=module_args, supports_check_mode=True)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_helper = ResourceHelper(
        module=module,
        resource_type="media_asset",
        service_client_class=MediaServicesClient,
        namespace="media_services",
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
