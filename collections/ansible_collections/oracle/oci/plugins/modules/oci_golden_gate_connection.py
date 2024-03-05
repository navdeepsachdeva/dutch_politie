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
module: oci_golden_gate_connection
description: >-
    Due to size constraints we have not included the documentation in the module. Please check L(here,
    https://docs.oracle.com/en-us/iaas/tools/oci-ansible-collection/latest/collections/oracle/oci/oci_golden_gate_connection_module.html)
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
    from oci.golden_gate import GoldenGateClient
    from oci.golden_gate.models import CreateConnectionDetails
    from oci.golden_gate.models import UpdateConnectionDetails

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


class ConnectionHelperGen(OCIResourceHelperBase):
    """Supported operations: create, update, get, list and delete"""

    def get_possible_entity_types(self):
        return super(ConnectionHelperGen, self).get_possible_entity_types() + [
            "goldengateconnection",
            "goldengateconnections",
            "goldenGategoldengateconnection",
            "goldenGategoldengateconnections",
            "goldengateconnectionresource",
            "goldengateconnectionsresource",
            "connection",
            "connections",
            "goldenGateconnection",
            "goldenGateconnections",
            "connectionresource",
            "connectionsresource",
            "goldengate",
        ]

    def get_module_resource_id_param(self):
        return "connection_id"

    def get_module_resource_id(self):
        return self.module.params.get("connection_id")

    def get_get_fn(self):
        return self.client.get_connection

    def get_get_model_from_summary_model(self, summary_model):
        return oci_common_utils.call_with_backoff(
            self.client.get_connection, connection_id=summary_model.id,
        ).data

    def get_resource(self):
        return oci_common_utils.call_with_backoff(
            self.client.get_connection,
            connection_id=self.module.params.get("connection_id"),
        )

    def get_required_kwargs_for_list(self):
        required_list_method_params = [
            "compartment_id",
        ]

        return dict(
            (param, self.module.params[param]) for param in required_list_method_params
        )

    def get_optional_kwargs_for_list(self):
        optional_list_method_params = ["display_name"]

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
            self.client.list_connections, **kwargs
        )

    def get_create_model_class(self):
        return CreateConnectionDetails

    def get_exclude_attributes(self):
        return [
            "ssl_crl",
            "wallet",
            "consumer_properties",
            "ssl_key",
            "service_account_key_file",
            "trust_store",
            "secret_access_key",
            "account_key",
            "producer_properties",
            "ssl_key_password",
            "private_key_passphrase",
            "key_store",
            "sas_token",
            "password",
            "private_key_file",
            "core_site_xml",
            "jndi_security_credentials",
            "fingerprint",
            "public_key_fingerprint",
            "key_store_password",
            "client_secret",
            "trust_store_password",
            "ssl_cert",
        ]

    def create_resource(self):
        create_details = self.get_create_model()
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.create_connection,
            call_fn_args=(),
            call_fn_kwargs=dict(create_connection_details=create_details,),
            waiter_type=oci_wait_utils.WORK_REQUEST_WAITER_KEY,
            operation=oci_common_utils.CREATE_OPERATION_KEY,
            waiter_client=self.get_waiter_client(),
            resource_helper=self,
            wait_for_states=oci_common_utils.get_work_request_completed_states(),
        )

    def get_update_model_class(self):
        return UpdateConnectionDetails

    def update_resource(self):
        update_details = self.get_update_model()
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.update_connection,
            call_fn_args=(),
            call_fn_kwargs=dict(
                connection_id=self.module.params.get("connection_id"),
                update_connection_details=update_details,
            ),
            waiter_type=oci_wait_utils.WORK_REQUEST_WAITER_KEY,
            operation=oci_common_utils.UPDATE_OPERATION_KEY,
            waiter_client=self.get_waiter_client(),
            resource_helper=self,
            wait_for_states=oci_common_utils.get_work_request_completed_states(),
        )

    def delete_resource(self):
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.delete_connection,
            call_fn_args=(),
            call_fn_kwargs=dict(connection_id=self.module.params.get("connection_id"),),
            waiter_type=oci_wait_utils.WORK_REQUEST_WAITER_KEY,
            operation=oci_common_utils.DELETE_OPERATION_KEY,
            waiter_client=self.get_waiter_client(),
            resource_helper=self,
            wait_for_states=oci_common_utils.get_work_request_completed_states(),
        )


ConnectionHelperCustom = get_custom_class("ConnectionHelperCustom")


class ResourceHelper(ConnectionHelperCustom, ConnectionHelperGen):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec(
        supports_create=True, supports_wait=True
    )
    module_args.update(
        dict(
            compartment_id=dict(type="str"),
            subnet_id=dict(type="str"),
            technology_type=dict(type="str"),
            fingerprint=dict(type="str"),
            wallet=dict(type="str"),
            session_mode=dict(type="str"),
            servers=dict(type="str"),
            database_id=dict(type="str"),
            service_account_key_file=dict(type="str"),
            account_name=dict(type="str"),
            account_key=dict(type="str", no_log=True),
            sas_token=dict(type="str", no_log=True),
            azure_tenant_id=dict(type="str"),
            client_id=dict(type="str"),
            client_secret=dict(type="str", no_log=True),
            endpoint=dict(type="str"),
            should_use_jndi=dict(type="bool"),
            jndi_connection_factory=dict(type="str"),
            jndi_provider_url=dict(type="str"),
            jndi_initial_context_factory=dict(type="str"),
            jndi_security_principal=dict(type="str"),
            jndi_security_credentials=dict(type="str"),
            connection_factory=dict(type="str"),
            deployment_id=dict(type="str"),
            should_validate_server_certificate=dict(type="bool"),
            tenancy_id=dict(type="str"),
            region=dict(type="str"),
            user_id=dict(type="str"),
            public_key_fingerprint=dict(type="str", no_log=True),
            url=dict(type="str"),
            access_key_id=dict(type="str"),
            secret_access_key=dict(type="str", no_log=True),
            connection_url=dict(type="str"),
            authentication_type=dict(type="str"),
            private_key_file=dict(type="str"),
            private_key_passphrase=dict(type="str", no_log=True),
            core_site_xml=dict(type="str"),
            port=dict(type="int"),
            database_name=dict(type="str"),
            ssl_mode=dict(type="str"),
            ssl_ca=dict(type="str"),
            ssl_crl=dict(type="str"),
            ssl_cert=dict(type="str"),
            ssl_key=dict(type="str", no_log=True),
            private_ip=dict(type="str"),
            additional_attributes=dict(
                type="list",
                elements="dict",
                options=dict(
                    name=dict(type="str", required=True),
                    value=dict(type="str", required=True),
                ),
            ),
            db_system_id=dict(type="str"),
            stream_pool_id=dict(type="str"),
            bootstrap_servers=dict(
                type="list",
                elements="dict",
                options=dict(
                    host=dict(type="str", required=True),
                    port=dict(type="int"),
                    private_ip=dict(type="str"),
                ),
            ),
            security_protocol=dict(type="str"),
            trust_store=dict(type="str"),
            trust_store_password=dict(type="str", no_log=True),
            key_store=dict(type="str", no_log=True),
            key_store_password=dict(type="str", no_log=True),
            ssl_key_password=dict(type="str", no_log=True),
            consumer_properties=dict(type="str"),
            producer_properties=dict(type="str"),
            host=dict(type="str"),
            connection_type=dict(
                type="str",
                choices=[
                    "POSTGRESQL",
                    "KAFKA_SCHEMA_REGISTRY",
                    "MICROSOFT_SQLSERVER",
                    "JAVA_MESSAGE_SERVICE",
                    "GOOGLE_BIGQUERY",
                    "AMAZON_KINESIS",
                    "SNOWFLAKE",
                    "AZURE_DATA_LAKE_STORAGE",
                    "MONGODB",
                    "AMAZON_S3",
                    "HDFS",
                    "OCI_OBJECT_STORAGE",
                    "ELASTICSEARCH",
                    "AZURE_SYNAPSE_ANALYTICS",
                    "REDIS",
                    "MYSQL",
                    "GENERIC",
                    "GOOGLE_CLOUD_STORAGE",
                    "KAFKA",
                    "ORACLE",
                    "GOLDENGATE",
                    "AMAZON_REDSHIFT",
                    "ORACLE_NOSQL",
                ],
            ),
            display_name=dict(aliases=["name"], type="str"),
            description=dict(type="str"),
            freeform_tags=dict(type="dict"),
            defined_tags=dict(type="dict"),
            vault_id=dict(type="str"),
            key_id=dict(type="str"),
            nsg_ids=dict(type="list", elements="str"),
            connection_string=dict(type="str"),
            username=dict(type="str"),
            password=dict(type="str", no_log=True),
            connection_id=dict(aliases=["id"], type="str"),
            state=dict(type="str", default="present", choices=["present", "absent"]),
        )
    )

    module = OCIAnsibleModule(argument_spec=module_args, supports_check_mode=True)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_helper = ResourceHelper(
        module=module,
        resource_type="connection",
        service_client_class=GoldenGateClient,
        namespace="golden_gate",
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
