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
module: oci_data_catalog_data_asset_actions
description: >-
    Due to size constraints we have not included the documentation in the module. Please check L(here,
    https://docs.oracle.com/en-us/iaas/tools/oci-ansible-collection/latest/collections/oracle/oci/oci_data_catalog_data_asset_actions_module.html)
    for the module documentation.
author: Oracle (@oracle)
"""


from ansible.module_utils._text import to_bytes
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
    from oci.data_catalog import DataCatalogClient
    from oci.data_catalog.models import DataSelectorPatternDetails
    from oci.data_catalog.models import ImportConnectionDetails
    from oci.data_catalog.models import ImportDataAssetDetails
    from oci.data_catalog.models import ParseConnectionDetails
    from oci.data_catalog.models import ExportDataAssetDetails
    from oci.data_catalog.models import ValidateConnectionDetails

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


class DataCatalogDataAssetActionsHelperGen(OCIActionsHelperBase):
    """
    Supported actions:
        add_data_selector_patterns
        import_connection
        import_data_asset
        parse_connection
        remove_data_selector_patterns
        synchronous_export
        validate_connection
    """

    @staticmethod
    def get_module_resource_id_param():
        return "data_asset_key"

    def get_module_resource_id(self):
        return self.module.params.get("data_asset_key")

    def get_get_fn(self):
        return self.client.get_data_asset

    def get_resource(self):
        return oci_common_utils.call_with_backoff(
            self.client.get_data_asset,
            catalog_id=self.module.params.get("catalog_id"),
            data_asset_key=self.module.params.get("data_asset_key"),
        )

    def add_data_selector_patterns(self):
        action_details = oci_common_utils.convert_input_data_to_model_class(
            self.module.params, DataSelectorPatternDetails
        )
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.add_data_selector_patterns,
            call_fn_args=(),
            call_fn_kwargs=dict(
                catalog_id=self.module.params.get("catalog_id"),
                data_asset_key=self.module.params.get("data_asset_key"),
                data_selector_pattern_details=action_details,
            ),
            waiter_type=oci_wait_utils.LIFECYCLE_STATE_WAITER_KEY,
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

    def import_connection(self):
        action_details = oci_common_utils.convert_input_data_to_model_class(
            self.module.params, ImportConnectionDetails
        )
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.import_connection,
            call_fn_args=(),
            call_fn_kwargs=dict(
                catalog_id=self.module.params.get("catalog_id"),
                data_asset_key=self.module.params.get("data_asset_key"),
                import_connection_details=action_details,
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

    def import_data_asset(self):
        action_details = oci_common_utils.convert_input_data_to_model_class(
            self.module.params, ImportDataAssetDetails
        )
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.import_data_asset,
            call_fn_args=(),
            call_fn_kwargs=dict(
                catalog_id=self.module.params.get("catalog_id"),
                data_asset_key=self.module.params.get("data_asset_key"),
                import_data_asset_details=action_details,
                import_type=self.module.params.get("import_type"),
                is_missing_value_ignored=self.module.params.get(
                    "is_missing_value_ignored"
                ),
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

    def parse_connection(self):
        action_details = oci_common_utils.convert_input_data_to_model_class(
            self.module.params, ParseConnectionDetails
        )
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.parse_connection,
            call_fn_args=(),
            call_fn_kwargs=dict(
                catalog_id=self.module.params.get("catalog_id"),
                data_asset_key=self.module.params.get("data_asset_key"),
                parse_connection_details=action_details,
                connection_key=self.module.params.get("connection_key"),
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

    def remove_data_selector_patterns(self):
        action_details = oci_common_utils.convert_input_data_to_model_class(
            self.module.params, DataSelectorPatternDetails
        )
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.remove_data_selector_patterns,
            call_fn_args=(),
            call_fn_kwargs=dict(
                catalog_id=self.module.params.get("catalog_id"),
                data_asset_key=self.module.params.get("data_asset_key"),
                data_selector_pattern_details=action_details,
            ),
            waiter_type=oci_wait_utils.LIFECYCLE_STATE_WAITER_KEY,
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

    def synchronous_export(self):
        action_details = oci_common_utils.convert_input_data_to_model_class(
            self.module.params, ExportDataAssetDetails
        )
        response = oci_wait_utils.call_and_wait(
            call_fn=self.client.synchronous_export_data_asset,
            call_fn_args=(),
            call_fn_kwargs=dict(
                catalog_id=self.module.params.get("catalog_id"),
                data_asset_key=self.module.params.get("data_asset_key"),
                synchronous_export_data_asset_details=action_details,
                export_type=self.module.params.get("export_type"),
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
        dest = self.module.params.get("dest")
        chunk_size = oci_common_utils.MEBIBYTE
        with open(to_bytes(dest), "wb") as dest_file:
            for chunk in response.raw.stream(chunk_size, decode_content=True):
                dest_file.write(chunk)
        return None

    def validate_connection(self):
        action_details = oci_common_utils.convert_input_data_to_model_class(
            self.module.params, ValidateConnectionDetails
        )
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.validate_connection,
            call_fn_args=(),
            call_fn_kwargs=dict(
                catalog_id=self.module.params.get("catalog_id"),
                data_asset_key=self.module.params.get("data_asset_key"),
                validate_connection_details=action_details,
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


DataCatalogDataAssetActionsHelperCustom = get_custom_class(
    "DataCatalogDataAssetActionsHelperCustom"
)


class ResourceHelper(
    DataCatalogDataAssetActionsHelperCustom, DataCatalogDataAssetActionsHelperGen
):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec(
        supports_create=False, supports_wait=True
    )
    module_args.update(
        dict(
            import_file_contents=dict(type="str"),
            import_type=dict(
                type="list", elements="str", choices=["CUSTOM_PROPERTY_VALUES", "ALL"]
            ),
            is_missing_value_ignored=dict(type="bool"),
            wallet_secret_id=dict(type="str"),
            wallet_secret_name=dict(type="str"),
            connection_key=dict(type="str", no_log=True),
            items=dict(type="list", elements="str"),
            dest=dict(type="str"),
            export_scope=dict(
                type="list",
                elements="dict",
                options=dict(
                    object_key=dict(type="str", no_log=True),
                    export_type_ids=dict(type="list", elements="str"),
                ),
            ),
            export_type=dict(
                type="list", elements="str", choices=["CUSTOM_PROPERTY_VALUES", "ALL"]
            ),
            catalog_id=dict(type="str", required=True),
            data_asset_key=dict(type="str", required=True, no_log=True),
            connection_detail=dict(
                type="dict",
                options=dict(
                    enc_properties=dict(type="dict"),
                    key=dict(type="str", no_log=True),
                    description=dict(type="str"),
                    display_name=dict(aliases=["name"], type="str"),
                    time_created=dict(type="str"),
                    time_updated=dict(type="str"),
                    created_by_id=dict(type="str"),
                    updated_by_id=dict(type="str"),
                    custom_property_members=dict(
                        type="list",
                        elements="dict",
                        options=dict(
                            key=dict(type="str", no_log=True),
                            display_name=dict(aliases=["name"], type="str"),
                            description=dict(type="str"),
                            value=dict(type="str"),
                            data_type=dict(
                                type="str",
                                choices=[
                                    "TEXT",
                                    "RICH_TEXT",
                                    "BOOLEAN",
                                    "NUMBER",
                                    "DATE",
                                ],
                            ),
                            namespace_name=dict(type="str"),
                            namespace_key=dict(type="str", no_log=True),
                            is_multi_valued=dict(type="bool"),
                            is_hidden=dict(type="bool"),
                            is_editable=dict(type="bool"),
                            is_shown_in_list=dict(type="bool"),
                            is_event_enabled=dict(type="bool"),
                            is_list_type=dict(type="bool"),
                            allowed_values=dict(type="list", elements="str"),
                        ),
                    ),
                    properties=dict(type="dict"),
                    external_key=dict(type="str", no_log=True),
                    time_status_updated=dict(type="str"),
                    lifecycle_state=dict(
                        type="str",
                        choices=[
                            "CREATING",
                            "ACTIVE",
                            "INACTIVE",
                            "UPDATING",
                            "DELETING",
                            "DELETED",
                            "FAILED",
                            "MOVING",
                        ],
                    ),
                    is_default=dict(type="bool"),
                    data_asset_key=dict(type="str", no_log=True),
                    type_key=dict(type="str", no_log=True),
                    uri=dict(type="str"),
                ),
            ),
            connection_payload=dict(type="str"),
            action=dict(
                type="str",
                required=True,
                choices=[
                    "add_data_selector_patterns",
                    "import_connection",
                    "import_data_asset",
                    "parse_connection",
                    "remove_data_selector_patterns",
                    "synchronous_export",
                    "validate_connection",
                ],
            ),
        )
    )

    module = OCIAnsibleModule(argument_spec=module_args, supports_check_mode=True)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_helper = ResourceHelper(
        module=module,
        resource_type="data_asset",
        service_client_class=DataCatalogClient,
        namespace="data_catalog",
    )

    result = resource_helper.perform_action(module.params.get("action"))

    module.exit_json(**result)


if __name__ == "__main__":
    main()
