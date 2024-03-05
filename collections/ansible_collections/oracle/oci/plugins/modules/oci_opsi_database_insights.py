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
module: oci_opsi_database_insights
description: >-
    Due to size constraints we have not included the documentation in the module. Please check L(here,
    https://docs.oracle.com/en-us/iaas/tools/oci-ansible-collection/latest/collections/oracle/oci/oci_opsi_database_insights_module.html)
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
    from oci.opsi import OperationsInsightsClient
    from oci.opsi.models import CreateDatabaseInsightDetails
    from oci.opsi.models import UpdateDatabaseInsightDetails

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


class DatabaseInsightsHelperGen(OCIResourceHelperBase):
    """Supported operations: create, update, get, list and delete"""

    def get_possible_entity_types(self):
        return super(DatabaseInsightsHelperGen, self).get_possible_entity_types() + [
            "opsidatabaseinsight",
            "opsidatabaseinsights",
            "opsiopsidatabaseinsight",
            "opsiopsidatabaseinsights",
            "opsidatabaseinsightresource",
            "opsidatabaseinsightsresource",
            "databaseinsights",
            "databaseinsight",
            "databaseinsightsresource",
            "databaseinsightresource",
            "opsi",
        ]

    def get_module_resource_id_param(self):
        return "database_insight_id"

    def get_module_resource_id(self):
        return self.module.params.get("database_insight_id")

    def get_get_fn(self):
        return self.client.get_database_insight

    def get_get_model_from_summary_model(self, summary_model):
        return oci_common_utils.call_with_backoff(
            self.client.get_database_insight, database_insight_id=summary_model.id,
        ).data

    def get_resource(self):
        return oci_common_utils.call_with_backoff(
            self.client.get_database_insight,
            database_insight_id=self.module.params.get("database_insight_id"),
        )

    def get_required_kwargs_for_list(self):
        return dict()

    def get_optional_kwargs_for_list(self):
        optional_list_method_params = [
            "compartment_id",
            "enterprise_manager_bridge_id",
            "exadata_insight_id",
            "opsi_private_endpoint_id",
        ]

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
            self.client.list_database_insights, **kwargs
        )

    def get_create_model_class(self):
        return CreateDatabaseInsightDetails

    def get_exclude_attributes(self):
        return ["deployment_type", "service_name", "dbm_private_endpoint_id"]

    def create_resource(self):
        create_details = self.get_create_model()
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.create_database_insight,
            call_fn_args=(),
            call_fn_kwargs=dict(create_database_insight_details=create_details,),
            waiter_type=oci_wait_utils.WORK_REQUEST_WAITER_KEY,
            operation=oci_common_utils.CREATE_OPERATION_KEY,
            waiter_client=self.get_waiter_client(),
            resource_helper=self,
            wait_for_states=oci_common_utils.get_work_request_completed_states(),
        )

    def get_update_model_class(self):
        return UpdateDatabaseInsightDetails

    def update_resource(self):
        update_details = self.get_update_model()
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.update_database_insight,
            call_fn_args=(),
            call_fn_kwargs=dict(
                database_insight_id=self.module.params.get("database_insight_id"),
                update_database_insight_details=update_details,
            ),
            waiter_type=oci_wait_utils.WORK_REQUEST_WAITER_KEY,
            operation=oci_common_utils.UPDATE_OPERATION_KEY,
            waiter_client=self.get_waiter_client(),
            resource_helper=self,
            wait_for_states=oci_common_utils.get_work_request_completed_states(),
        )

    def delete_resource(self):
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.delete_database_insight,
            call_fn_args=(),
            call_fn_kwargs=dict(
                database_insight_id=self.module.params.get("database_insight_id"),
            ),
            waiter_type=oci_wait_utils.WORK_REQUEST_WAITER_KEY,
            operation=oci_common_utils.DELETE_OPERATION_KEY,
            waiter_client=self.get_waiter_client(),
            resource_helper=self,
            wait_for_states=oci_common_utils.get_work_request_completed_states(),
        )


DatabaseInsightsHelperCustom = get_custom_class("DatabaseInsightsHelperCustom")


class ResourceHelper(DatabaseInsightsHelperCustom, DatabaseInsightsHelperGen):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec(
        supports_create=True, supports_wait=True
    )
    module_args.update(
        dict(
            enterprise_manager_identifier=dict(type="str"),
            enterprise_manager_bridge_id=dict(type="str"),
            enterprise_manager_entity_identifier=dict(type="str"),
            exadata_insight_id=dict(type="str"),
            compartment_id=dict(type="str"),
            database_id=dict(type="str"),
            database_resource_type=dict(type="str"),
            opsi_private_endpoint_id=dict(type="str"),
            dbm_private_endpoint_id=dict(type="str"),
            service_name=dict(type="str"),
            credential_details=dict(
                type="dict",
                options=dict(
                    credential_source_name=dict(type="str", required=True),
                    credential_type=dict(
                        type="str",
                        required=True,
                        choices=["CREDENTIALS_BY_SOURCE", "CREDENTIALS_BY_VAULT"],
                    ),
                    user_name=dict(type="str"),
                    password_secret_id=dict(type="str"),
                    wallet_secret_id=dict(type="str"),
                    role=dict(type="str", choices=["NORMAL"]),
                ),
            ),
            connection_details=dict(
                type="dict",
                options=dict(
                    hosts=dict(
                        type="list",
                        elements="dict",
                        required=True,
                        options=dict(host_ip=dict(type="str"), port=dict(type="int")),
                    ),
                    protocol=dict(type="str", choices=["TCP", "TCPS"]),
                    service_name=dict(type="str"),
                ),
            ),
            deployment_type=dict(
                type="str", choices=["VIRTUAL_MACHINE", "BARE_METAL", "EXACS"]
            ),
            system_tags=dict(type="dict"),
            entity_source=dict(
                type="str",
                choices=[
                    "EM_MANAGED_EXTERNAL_DATABASE",
                    "PE_COMANAGED_DATABASE",
                    "MACS_MANAGED_EXTERNAL_DATABASE",
                    "AUTONOMOUS_DATABASE",
                ],
            ),
            freeform_tags=dict(type="dict"),
            defined_tags=dict(type="dict"),
            database_insight_id=dict(aliases=["id"], type="str"),
            state=dict(type="str", default="present", choices=["present", "absent"]),
        )
    )

    module = OCIAnsibleModule(argument_spec=module_args, supports_check_mode=True)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_helper = ResourceHelper(
        module=module,
        resource_type="database_insights",
        service_client_class=OperationsInsightsClient,
        namespace="opsi",
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
