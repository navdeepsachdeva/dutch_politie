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
module: oci_service_mesh_ingress_gateway
description: >-
    Due to size constraints we have not included the documentation in the module. Please check L(here,
    https://docs.oracle.com/en-us/iaas/tools/oci-ansible-collection/latest/collections/oracle/oci/oci_service_mesh_ingress_gateway_module.html)
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
    from oci.service_mesh import ServiceMeshClient
    from oci.service_mesh.models import CreateIngressGatewayDetails
    from oci.service_mesh.models import UpdateIngressGatewayDetails

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


class IngressGatewayHelperGen(OCIResourceHelperBase):
    """Supported operations: create, update, get, list and delete"""

    def get_possible_entity_types(self):
        return super(IngressGatewayHelperGen, self).get_possible_entity_types() + [
            "ingressgateway",
            "ingressgateways",
            "serviceMeshingressgateway",
            "serviceMeshingressgateways",
            "ingressgatewayresource",
            "ingressgatewaysresource",
            "servicemesh",
        ]

    def get_module_resource_id_param(self):
        return "ingress_gateway_id"

    def get_module_resource_id(self):
        return self.module.params.get("ingress_gateway_id")

    def get_get_fn(self):
        return self.client.get_ingress_gateway

    def get_get_model_from_summary_model(self, summary_model):
        return oci_common_utils.call_with_backoff(
            self.client.get_ingress_gateway, ingress_gateway_id=summary_model.id,
        ).data

    def get_resource(self):
        return oci_common_utils.call_with_backoff(
            self.client.get_ingress_gateway,
            ingress_gateway_id=self.module.params.get("ingress_gateway_id"),
        )

    def get_required_kwargs_for_list(self):
        required_list_method_params = [
            "compartment_id",
        ]

        return dict(
            (param, self.module.params[param]) for param in required_list_method_params
        )

    def get_optional_kwargs_for_list(self):
        optional_list_method_params = ["name", "mesh_id"]

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
            self.client.list_ingress_gateways, **kwargs
        )

    def get_create_model_class(self):
        return CreateIngressGatewayDetails

    def create_resource(self):
        create_details = self.get_create_model()
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.create_ingress_gateway,
            call_fn_args=(),
            call_fn_kwargs=dict(create_ingress_gateway_details=create_details,),
            waiter_type=oci_wait_utils.WORK_REQUEST_WAITER_KEY,
            operation=oci_common_utils.CREATE_OPERATION_KEY,
            waiter_client=self.get_waiter_client(),
            resource_helper=self,
            wait_for_states=oci_common_utils.get_work_request_completed_states(),
        )

    def get_update_model_class(self):
        return UpdateIngressGatewayDetails

    def update_resource(self):
        update_details = self.get_update_model()
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.update_ingress_gateway,
            call_fn_args=(),
            call_fn_kwargs=dict(
                ingress_gateway_id=self.module.params.get("ingress_gateway_id"),
                update_ingress_gateway_details=update_details,
            ),
            waiter_type=oci_wait_utils.WORK_REQUEST_WAITER_KEY,
            operation=oci_common_utils.UPDATE_OPERATION_KEY,
            waiter_client=self.get_waiter_client(),
            resource_helper=self,
            wait_for_states=oci_common_utils.get_work_request_completed_states(),
        )

    def delete_resource(self):
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.delete_ingress_gateway,
            call_fn_args=(),
            call_fn_kwargs=dict(
                ingress_gateway_id=self.module.params.get("ingress_gateway_id"),
            ),
            waiter_type=oci_wait_utils.WORK_REQUEST_WAITER_KEY,
            operation=oci_common_utils.DELETE_OPERATION_KEY,
            waiter_client=self.get_waiter_client(),
            resource_helper=self,
            wait_for_states=oci_common_utils.get_work_request_completed_states(),
        )


IngressGatewayHelperCustom = get_custom_class("IngressGatewayHelperCustom")


class ResourceHelper(IngressGatewayHelperCustom, IngressGatewayHelperGen):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec(
        supports_create=True, supports_wait=True
    )
    module_args.update(
        dict(
            name=dict(type="str"),
            mesh_id=dict(type="str"),
            compartment_id=dict(type="str"),
            description=dict(type="str"),
            hosts=dict(
                type="list",
                elements="dict",
                options=dict(
                    name=dict(type="str", required=True),
                    hostnames=dict(type="list", elements="str"),
                    listeners=dict(
                        type="list",
                        elements="dict",
                        required=True,
                        options=dict(
                            protocol=dict(
                                type="str",
                                required=True,
                                choices=["HTTP", "TLS_PASSTHROUGH", "TCP"],
                            ),
                            port=dict(type="int", required=True),
                            tls=dict(
                                type="dict",
                                options=dict(
                                    mode=dict(
                                        type="str",
                                        required=True,
                                        choices=[
                                            "DISABLED",
                                            "PERMISSIVE",
                                            "TLS",
                                            "MUTUAL_TLS",
                                        ],
                                    ),
                                    server_certificate=dict(
                                        type="dict",
                                        options=dict(
                                            certificate_id=dict(type="str"),
                                            type=dict(
                                                type="str",
                                                required=True,
                                                choices=[
                                                    "OCI_CERTIFICATES",
                                                    "LOCAL_FILE",
                                                ],
                                            ),
                                            secret_name=dict(type="str"),
                                        ),
                                    ),
                                    client_validation=dict(
                                        type="dict",
                                        options=dict(
                                            trusted_ca_bundle=dict(
                                                type="dict",
                                                options=dict(
                                                    secret_name=dict(type="str"),
                                                    type=dict(
                                                        type="str",
                                                        required=True,
                                                        choices=[
                                                            "LOCAL_FILE",
                                                            "OCI_CERTIFICATES",
                                                        ],
                                                    ),
                                                    ca_bundle_id=dict(type="str"),
                                                ),
                                            ),
                                            subject_alternate_names=dict(
                                                type="list", elements="str"
                                            ),
                                        ),
                                    ),
                                ),
                            ),
                        ),
                    ),
                ),
            ),
            access_logging=dict(
                type="dict", options=dict(is_enabled=dict(type="bool"))
            ),
            mtls=dict(type="dict", options=dict(maximum_validity=dict(type="int"))),
            freeform_tags=dict(type="dict"),
            defined_tags=dict(type="dict"),
            ingress_gateway_id=dict(aliases=["id"], type="str"),
            state=dict(type="str", default="present", choices=["present", "absent"]),
        )
    )

    module = OCIAnsibleModule(argument_spec=module_args, supports_check_mode=True)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_helper = ResourceHelper(
        module=module,
        resource_type="ingress_gateway",
        service_client_class=ServiceMeshClient,
        namespace="service_mesh",
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
