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
module: oci_sch_service_connector
description: >-
    Due to size constraints we have not included the documentation in the module. Please check L(here,
    https://docs.oracle.com/en-us/iaas/tools/oci-ansible-collection/latest/collections/oracle/oci/oci_sch_service_connector_module.html)
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
    from oci.sch import ServiceConnectorClient
    from oci.sch.models import CreateServiceConnectorDetails
    from oci.sch.models import UpdateServiceConnectorDetails

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


class ServiceConnectorHelperGen(OCIResourceHelperBase):
    """Supported operations: create, update, get, list and delete"""

    def get_possible_entity_types(self):
        return super(ServiceConnectorHelperGen, self).get_possible_entity_types() + [
            "serviceconnector",
            "serviceconnectors",
            "schserviceconnector",
            "schserviceconnectors",
            "serviceconnectorresource",
            "serviceconnectorsresource",
            "sch",
        ]

    def get_module_resource_id_param(self):
        return "service_connector_id"

    def get_module_resource_id(self):
        return self.module.params.get("service_connector_id")

    def get_get_fn(self):
        return self.client.get_service_connector

    def get_get_model_from_summary_model(self, summary_model):
        return oci_common_utils.call_with_backoff(
            self.client.get_service_connector, service_connector_id=summary_model.id,
        ).data

    def get_resource(self):
        return oci_common_utils.call_with_backoff(
            self.client.get_service_connector,
            service_connector_id=self.module.params.get("service_connector_id"),
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
            self.client.list_service_connectors, **kwargs
        )

    def get_create_model_class(self):
        return CreateServiceConnectorDetails

    def create_resource(self):
        create_details = self.get_create_model()
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.create_service_connector,
            call_fn_args=(),
            call_fn_kwargs=dict(create_service_connector_details=create_details,),
            waiter_type=oci_wait_utils.WORK_REQUEST_WAITER_KEY,
            operation=oci_common_utils.CREATE_OPERATION_KEY,
            waiter_client=self.get_waiter_client(),
            resource_helper=self,
            wait_for_states=oci_common_utils.get_work_request_completed_states(),
        )

    def get_update_model_class(self):
        return UpdateServiceConnectorDetails

    def update_resource(self):
        update_details = self.get_update_model()
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.update_service_connector,
            call_fn_args=(),
            call_fn_kwargs=dict(
                service_connector_id=self.module.params.get("service_connector_id"),
                update_service_connector_details=update_details,
            ),
            waiter_type=oci_wait_utils.WORK_REQUEST_WAITER_KEY,
            operation=oci_common_utils.UPDATE_OPERATION_KEY,
            waiter_client=self.get_waiter_client(),
            resource_helper=self,
            wait_for_states=oci_common_utils.get_work_request_completed_states(),
        )

    def delete_resource(self):
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.delete_service_connector,
            call_fn_args=(),
            call_fn_kwargs=dict(
                service_connector_id=self.module.params.get("service_connector_id"),
            ),
            waiter_type=oci_wait_utils.WORK_REQUEST_WAITER_KEY,
            operation=oci_common_utils.DELETE_OPERATION_KEY,
            waiter_client=self.get_waiter_client(),
            resource_helper=self,
            wait_for_states=oci_common_utils.get_work_request_completed_states(),
        )


ServiceConnectorHelperCustom = get_custom_class("ServiceConnectorHelperCustom")


class ResourceHelper(ServiceConnectorHelperCustom, ServiceConnectorHelperGen):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec(
        supports_create=True, supports_wait=True
    )
    module_args.update(
        dict(
            compartment_id=dict(type="str"),
            display_name=dict(aliases=["name"], type="str"),
            description=dict(type="str"),
            source=dict(
                type="dict",
                options=dict(
                    log_sources=dict(
                        type="list",
                        elements="dict",
                        options=dict(
                            compartment_id=dict(type="str", required=True),
                            log_group_id=dict(type="str"),
                            log_id=dict(type="str"),
                        ),
                    ),
                    monitoring_sources=dict(
                        type="list",
                        elements="dict",
                        options=dict(
                            compartment_id=dict(type="str", required=True),
                            namespace_details=dict(
                                type="dict",
                                required=True,
                                options=dict(
                                    kind=dict(
                                        type="str", required=True, choices=["selected"]
                                    ),
                                    namespaces=dict(
                                        type="list",
                                        elements="dict",
                                        required=True,
                                        options=dict(
                                            namespace=dict(type="str", required=True),
                                            metrics=dict(
                                                type="dict",
                                                required=True,
                                                options=dict(
                                                    kind=dict(
                                                        type="str",
                                                        required=True,
                                                        choices=["all"],
                                                    )
                                                ),
                                            ),
                                        ),
                                    ),
                                ),
                            ),
                        ),
                    ),
                    kind=dict(
                        type="str",
                        required=True,
                        choices=["logging", "monitoring", "streaming"],
                    ),
                    stream_id=dict(type="str"),
                    cursor=dict(
                        type="dict",
                        options=dict(
                            kind=dict(
                                type="str",
                                required=True,
                                choices=["TRIM_HORIZON", "LATEST"],
                            )
                        ),
                    ),
                ),
            ),
            tasks=dict(
                type="list",
                elements="dict",
                options=dict(
                    function_id=dict(type="str"),
                    batch_size_in_kbs=dict(type="int"),
                    batch_time_in_sec=dict(type="int"),
                    kind=dict(
                        type="str", required=True, choices=["function", "logRule"]
                    ),
                    condition=dict(type="str"),
                ),
            ),
            target=dict(
                type="dict",
                options=dict(
                    topic_id=dict(type="str"),
                    enable_formatted_messaging=dict(type="bool"),
                    namespace=dict(type="str"),
                    bucket_name=dict(type="str"),
                    object_name_prefix=dict(type="str"),
                    batch_rollover_size_in_mbs=dict(type="int"),
                    batch_rollover_time_in_ms=dict(type="int"),
                    compartment_id=dict(type="str"),
                    metric_namespace=dict(type="str"),
                    metric=dict(type="str"),
                    dimensions=dict(
                        type="list",
                        elements="dict",
                        options=dict(
                            name=dict(type="str", required=True),
                            dimension_value=dict(
                                type="dict",
                                required=True,
                                options=dict(
                                    value=dict(type="str"),
                                    kind=dict(
                                        type="str",
                                        required=True,
                                        choices=["static", "jmesPath"],
                                    ),
                                    path=dict(type="str"),
                                ),
                            ),
                        ),
                    ),
                    function_id=dict(type="str"),
                    log_group_id=dict(type="str"),
                    log_source_identifier=dict(type="str"),
                    kind=dict(
                        type="str",
                        required=True,
                        choices=[
                            "notifications",
                            "objectStorage",
                            "monitoring",
                            "functions",
                            "loggingAnalytics",
                            "streaming",
                        ],
                    ),
                    stream_id=dict(type="str"),
                ),
            ),
            freeform_tags=dict(type="dict"),
            defined_tags=dict(type="dict"),
            service_connector_id=dict(aliases=["id"], type="str"),
            state=dict(type="str", default="present", choices=["present", "absent"]),
        )
    )

    module = OCIAnsibleModule(argument_spec=module_args, supports_check_mode=True)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_helper = ResourceHelper(
        module=module,
        resource_type="service_connector",
        service_client_class=ServiceConnectorClient,
        namespace="sch",
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
