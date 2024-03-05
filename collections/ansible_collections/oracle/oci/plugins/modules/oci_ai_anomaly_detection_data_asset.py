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
module: oci_ai_anomaly_detection_data_asset
description: >-
    Due to size constraints we have not included the documentation in the module. Please check L(here,
    https://docs.oracle.com/en-us/iaas/tools/oci-ansible-collection/latest/collections/oracle/oci/oci_ai_anomaly_detection_data_asset_module.html)
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
    from oci.ai_anomaly_detection import AnomalyDetectionClient
    from oci.ai_anomaly_detection.models import CreateDataAssetDetails
    from oci.ai_anomaly_detection.models import UpdateDataAssetDetails

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


class DataAssetHelperGen(OCIResourceHelperBase):
    """Supported operations: create, update, get, list and delete"""

    def get_possible_entity_types(self):
        return super(DataAssetHelperGen, self).get_possible_entity_types() + [
            "dataasset",
            "dataassets",
            "aiAnomalyDetectiondataasset",
            "aiAnomalyDetectiondataassets",
            "dataassetresource",
            "dataassetsresource",
            "aianomalydetection",
        ]

    def get_module_resource_id_param(self):
        return "data_asset_id"

    def get_module_resource_id(self):
        return self.module.params.get("data_asset_id")

    def get_get_fn(self):
        return self.client.get_data_asset

    def get_get_model_from_summary_model(self, summary_model):
        return oci_common_utils.call_with_backoff(
            self.client.get_data_asset, data_asset_id=summary_model.id,
        ).data

    def get_resource(self):
        return oci_common_utils.call_with_backoff(
            self.client.get_data_asset,
            data_asset_id=self.module.params.get("data_asset_id"),
        )

    def get_required_kwargs_for_list(self):
        required_list_method_params = [
            "compartment_id",
        ]

        return dict(
            (param, self.module.params[param]) for param in required_list_method_params
        )

    def get_optional_kwargs_for_list(self):
        optional_list_method_params = ["project_id", "display_name"]

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
            self.client.list_data_assets, **kwargs
        )

    def get_create_model_class(self):
        return CreateDataAssetDetails

    def create_resource(self):
        create_details = self.get_create_model()
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.create_data_asset,
            call_fn_args=(),
            call_fn_kwargs=dict(create_data_asset_details=create_details,),
            waiter_type=oci_wait_utils.LIFECYCLE_STATE_WAITER_KEY,
            operation=oci_common_utils.CREATE_OPERATION_KEY,
            waiter_client=self.get_waiter_client(),
            resource_helper=self,
            wait_for_states=self.get_wait_for_states_for_operation(
                oci_common_utils.CREATE_OPERATION_KEY,
            ),
        )

    def get_update_model_class(self):
        return UpdateDataAssetDetails

    def update_resource(self):
        update_details = self.get_update_model()
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.update_data_asset,
            call_fn_args=(),
            call_fn_kwargs=dict(
                data_asset_id=self.module.params.get("data_asset_id"),
                update_data_asset_details=update_details,
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
            call_fn=self.client.delete_data_asset,
            call_fn_args=(),
            call_fn_kwargs=dict(data_asset_id=self.module.params.get("data_asset_id"),),
            waiter_type=oci_wait_utils.LIFECYCLE_STATE_WAITER_KEY,
            operation=oci_common_utils.DELETE_OPERATION_KEY,
            waiter_client=self.get_waiter_client(),
            resource_helper=self,
            wait_for_states=self.get_wait_for_states_for_operation(
                oci_common_utils.DELETE_OPERATION_KEY,
            ),
        )


DataAssetHelperCustom = get_custom_class("DataAssetHelperCustom")


class ResourceHelper(DataAssetHelperCustom, DataAssetHelperGen):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec(
        supports_create=True, supports_wait=True
    )
    module_args.update(
        dict(
            compartment_id=dict(type="str"),
            project_id=dict(type="str"),
            data_source_details=dict(
                type="dict",
                options=dict(
                    namespace=dict(type="str"),
                    bucket_name=dict(type="str"),
                    object_name=dict(type="str"),
                    version_specific_details=dict(
                        type="dict",
                        options=dict(
                            database_name=dict(type="str"),
                            retention_policy_name=dict(type="str"),
                            influx_version=dict(
                                type="str", required=True, choices=["V_1_8", "V_2_0"]
                            ),
                            bucket_name=dict(type="str"),
                            organization_name=dict(type="str"),
                        ),
                    ),
                    user_name=dict(type="str"),
                    password_secret_id=dict(type="str"),
                    measurement_name=dict(type="str"),
                    url=dict(type="str"),
                    data_source_type=dict(
                        type="str",
                        required=True,
                        choices=["ORACLE_OBJECT_STORAGE", "INFLUX", "ORACLE_ATP"],
                    ),
                    wallet_password_secret_id=dict(type="str"),
                    atp_user_name=dict(type="str"),
                    atp_password_secret_id=dict(type="str"),
                    cwallet_file_secret_id=dict(type="str"),
                    ewallet_file_secret_id=dict(type="str"),
                    key_store_file_secret_id=dict(type="str"),
                    ojdbc_file_secret_id=dict(type="str"),
                    tnsnames_file_secret_id=dict(type="str"),
                    truststore_file_secret_id=dict(type="str"),
                    database_name=dict(type="str"),
                    table_name=dict(type="str"),
                ),
            ),
            private_endpoint_id=dict(type="str"),
            display_name=dict(aliases=["name"], type="str"),
            description=dict(type="str"),
            freeform_tags=dict(type="dict"),
            defined_tags=dict(type="dict"),
            data_asset_id=dict(aliases=["id"], type="str"),
            state=dict(type="str", default="present", choices=["present", "absent"]),
        )
    )

    module = OCIAnsibleModule(argument_spec=module_args, supports_check_mode=True)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_helper = ResourceHelper(
        module=module,
        resource_type="data_asset",
        service_client_class=AnomalyDetectionClient,
        namespace="ai_anomaly_detection",
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
