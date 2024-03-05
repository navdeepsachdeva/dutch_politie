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
module: oci_data_catalog_custom_property_facts
description: >-
    Due to size constraints we have not included the documentation in the module. Please check L(here,
    https://docs.oracle.com/en-us/iaas/tools/oci-ansible-collection/latest/collections/oracle/oci/oci_data_catalog_custom_property_facts_module.html)
    for the module documentation.
author: Oracle (@oracle)
"""


from ansible_collections.oracle.oci.plugins.module_utils import oci_common_utils
from ansible_collections.oracle.oci.plugins.module_utils.oci_resource_utils import (
    OCIResourceFactsHelperBase,
    get_custom_class,
    OCIAnsibleModule,
)

try:
    from oci.data_catalog import DataCatalogClient

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


class DataCatalogCustomPropertyFactsHelperGen(OCIResourceFactsHelperBase):
    """Supported operations: get, list"""

    def get_required_params_for_get(self):
        return [
            "catalog_id",
            "namespace_id",
            "custom_property_key",
        ]

    def get_required_params_for_list(self):
        return [
            "catalog_id",
            "namespace_id",
        ]

    def get_resource(self):
        optional_get_method_params = [
            "fields",
        ]
        optional_kwargs = dict(
            (param, self.module.params[param])
            for param in optional_get_method_params
            if self.module.params.get(param) is not None
        )
        return oci_common_utils.call_with_backoff(
            self.client.get_custom_property,
            catalog_id=self.module.params.get("catalog_id"),
            namespace_id=self.module.params.get("namespace_id"),
            custom_property_key=self.module.params.get("custom_property_key"),
            **optional_kwargs
        )

    def list_resources(self):
        optional_list_method_params = [
            "display_name",
            "display_name_contains",
            "data_types",
            "type_name",
            "lifecycle_state",
            "time_created",
            "time_updated",
            "created_by_id",
            "updated_by_id",
            "fields",
            "sort_order",
            "sort_by",
        ]
        optional_kwargs = dict(
            (param, self.module.params[param])
            for param in optional_list_method_params
            if self.module.params.get(param) is not None
        )
        return oci_common_utils.list_all_resources(
            self.client.list_custom_properties,
            catalog_id=self.module.params.get("catalog_id"),
            namespace_id=self.module.params.get("namespace_id"),
            **optional_kwargs
        )


DataCatalogCustomPropertyFactsHelperCustom = get_custom_class(
    "DataCatalogCustomPropertyFactsHelperCustom"
)


class ResourceFactsHelper(
    DataCatalogCustomPropertyFactsHelperCustom, DataCatalogCustomPropertyFactsHelperGen
):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec()
    module_args.update(
        dict(
            custom_property_key=dict(type="str", no_log=True),
            catalog_id=dict(type="str", required=True),
            namespace_id=dict(type="str", required=True),
            display_name=dict(aliases=["name"], type="str"),
            display_name_contains=dict(type="str"),
            data_types=dict(
                type="list",
                elements="str",
                choices=["TEXT", "RICH_TEXT", "BOOLEAN", "NUMBER", "DATE"],
            ),
            type_name=dict(
                type="list",
                elements="str",
                choices=[
                    "DATA_ASSET",
                    "AUTONOMOUS_DATA_WAREHOUSE",
                    "HIVE",
                    "KAFKA",
                    "MYSQL",
                    "ORACLE_OBJECT_STORAGE",
                    "AUTONOMOUS_TRANSACTION_PROCESSING",
                    "ORACLE",
                    "POSTGRESQL",
                    "MICROSOFT_AZURE_SQL_DATABASE",
                    "MICROSOFT_SQL_SERVER",
                    "IBM_DB2",
                    "DATA_ENTITY",
                    "LOGICAL_ENTITY",
                    "TABLE",
                    "VIEW",
                    "ATTRIBUTE",
                    "FOLDER",
                    "ORACLE_ANALYTICS_SUBJECT_AREA_COLUMN",
                    "ORACLE_ANALYTICS_LOGICAL_COLUMN",
                    "ORACLE_ANALYTICS_PHYSICAL_COLUMN",
                    "ORACLE_ANALYTICS_ANALYSIS_COLUMN",
                    "ORACLE_ANALYTICS_SERVER",
                    "ORACLE_ANALYTICS_CLOUD",
                    "ORACLE_ANALYTICS_SUBJECT_AREA",
                    "ORACLE_ANALYTICS_DASHBOARD",
                    "ORACLE_ANALYTICS_BUSINESS_MODEL",
                    "ORACLE_ANALYTICS_PHYSICAL_DATABASE",
                    "ORACLE_ANALYTICS_PHYSICAL_SCHEMA",
                    "ORACLE_ANALYTICS_PRESENTATION_TABLE",
                    "ORACLE_ANALYTICS_LOGICAL_TABLE",
                    "ORACLE_ANALYTICS_PHYSICAL_TABLE",
                    "ORACLE_ANALYTICS_ANALYSIS",
                    "DATABASE_SCHEMA",
                    "TOPIC",
                    "CONNECTION",
                    "GLOSSARY",
                    "TERM",
                    "CATEGORY",
                    "FILE",
                    "BUCKET",
                    "MESSAGE",
                    "UNRECOGNIZED_FILE",
                ],
            ),
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
            time_created=dict(type="str"),
            time_updated=dict(type="str"),
            created_by_id=dict(type="str"),
            updated_by_id=dict(type="str"),
            fields=dict(
                type="list",
                elements="str",
                choices=[
                    "key",
                    "displayName",
                    "description",
                    "dataType",
                    "namespaceName",
                    "lifecycleState",
                    "timeCreated",
                    "timeUpdated",
                    "createdById",
                    "updatedById",
                    "properties",
                ],
            ),
            sort_order=dict(type="str", choices=["ASC", "DESC"]),
            sort_by=dict(type="str", choices=["DISPLAYNAME", "USAGECOUNT"]),
        )
    )

    module = OCIAnsibleModule(argument_spec=module_args)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_facts_helper = ResourceFactsHelper(
        module=module,
        resource_type="custom_property",
        service_client_class=DataCatalogClient,
        namespace="data_catalog",
    )

    result = []

    if resource_facts_helper.is_get():
        result = [resource_facts_helper.get()]
    elif resource_facts_helper.is_list():
        result = resource_facts_helper.list()
    else:
        resource_facts_helper.fail()

    module.exit_json(custom_properties=result)


if __name__ == "__main__":
    main()
