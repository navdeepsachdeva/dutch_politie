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
module: oci_apigateway_deployment
description: >-
    Due to size constraints we have not included the documentation in the module. Please check L(here,
    https://docs.oracle.com/en-us/iaas/tools/oci-ansible-collection/latest/collections/oracle/oci/oci_apigateway_deployment_module.html)
    for the module documentation.
author: Oracle (@oracle)
"""


from ansible_collections.oracle.oci.plugins.module_utils import (
    oci_common_utils,
    oci_wait_utils,
    oci_config_utils,
)
from ansible_collections.oracle.oci.plugins.module_utils.oci_resource_utils import (
    OCIResourceHelperBase,
    get_custom_class,
    OCIAnsibleModule,
)

try:
    from oci.apigateway import WorkRequestsClient
    from oci.apigateway import DeploymentClient
    from oci.apigateway.models import CreateDeploymentDetails
    from oci.apigateway.models import UpdateDeploymentDetails

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


class ApigatewayDeploymentHelperGen(OCIResourceHelperBase):
    """Supported operations: create, update, get, list and delete"""

    def get_waiter_client(self):
        return oci_config_utils.create_service_client(self.module, WorkRequestsClient)

    def get_possible_entity_types(self):
        return super(
            ApigatewayDeploymentHelperGen, self
        ).get_possible_entity_types() + [
            "deployment",
            "deployments",
            "apigatewaydeployment",
            "apigatewaydeployments",
            "deploymentresource",
            "deploymentsresource",
            "apigateway",
        ]

    def get_module_resource_id_param(self):
        return "deployment_id"

    def get_module_resource_id(self):
        return self.module.params.get("deployment_id")

    def get_get_fn(self):
        return self.client.get_deployment

    def get_get_model_from_summary_model(self, summary_model):
        return oci_common_utils.call_with_backoff(
            self.client.get_deployment, deployment_id=summary_model.id,
        ).data

    def get_resource(self):
        return oci_common_utils.call_with_backoff(
            self.client.get_deployment,
            deployment_id=self.module.params.get("deployment_id"),
        )

    def get_required_kwargs_for_list(self):
        required_list_method_params = [
            "compartment_id",
        ]

        return dict(
            (param, self.module.params[param]) for param in required_list_method_params
        )

    def get_optional_kwargs_for_list(self):
        optional_list_method_params = ["gateway_id", "display_name"]

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
            self.client.list_deployments, **kwargs
        )

    def get_create_model_class(self):
        return CreateDeploymentDetails

    def create_resource(self):
        create_details = self.get_create_model()
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.create_deployment,
            call_fn_args=(),
            call_fn_kwargs=dict(create_deployment_details=create_details,),
            waiter_type=oci_wait_utils.WORK_REQUEST_WAITER_KEY,
            operation=oci_common_utils.CREATE_OPERATION_KEY,
            waiter_client=self.get_waiter_client(),
            resource_helper=self,
            wait_for_states=oci_common_utils.get_work_request_completed_states(),
        )

    def get_update_model_class(self):
        return UpdateDeploymentDetails

    def update_resource(self):
        update_details = self.get_update_model()
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.update_deployment,
            call_fn_args=(),
            call_fn_kwargs=dict(
                deployment_id=self.module.params.get("deployment_id"),
                update_deployment_details=update_details,
            ),
            waiter_type=oci_wait_utils.WORK_REQUEST_WAITER_KEY,
            operation=oci_common_utils.UPDATE_OPERATION_KEY,
            waiter_client=self.get_waiter_client(),
            resource_helper=self,
            wait_for_states=oci_common_utils.get_work_request_completed_states(),
        )

    def delete_resource(self):
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.delete_deployment,
            call_fn_args=(),
            call_fn_kwargs=dict(deployment_id=self.module.params.get("deployment_id"),),
            waiter_type=oci_wait_utils.WORK_REQUEST_WAITER_KEY,
            operation=oci_common_utils.DELETE_OPERATION_KEY,
            waiter_client=self.get_waiter_client(),
            resource_helper=self,
            wait_for_states=oci_common_utils.get_work_request_completed_states(),
        )


ApigatewayDeploymentHelperCustom = get_custom_class("ApigatewayDeploymentHelperCustom")


class ResourceHelper(ApigatewayDeploymentHelperCustom, ApigatewayDeploymentHelperGen):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec(
        supports_create=True, supports_wait=True
    )
    module_args.update(
        dict(
            gateway_id=dict(type="str"),
            compartment_id=dict(type="str"),
            path_prefix=dict(type="str"),
            display_name=dict(aliases=["name"], type="str"),
            specification=dict(
                type="dict",
                options=dict(
                    request_policies=dict(
                        type="dict",
                        options=dict(
                            authentication=dict(
                                type="dict",
                                options=dict(
                                    validation_policy=dict(
                                        type="dict",
                                        options=dict(
                                            uri=dict(type="str"),
                                            client_details=dict(
                                                type="dict",
                                                options=dict(
                                                    client_id=dict(type="str"),
                                                    client_secret_id=dict(type="str"),
                                                    client_secret_version_number=dict(
                                                        type="int", no_log=True
                                                    ),
                                                    type=dict(
                                                        type="str",
                                                        required=True,
                                                        choices=[
                                                            "CUSTOM",
                                                            "VALIDATION_BLOCK",
                                                        ],
                                                    ),
                                                ),
                                            ),
                                            source_uri_details=dict(
                                                type="dict",
                                                options=dict(
                                                    uri=dict(type="str"),
                                                    type=dict(
                                                        type="str",
                                                        required=True,
                                                        choices=[
                                                            "DISCOVERY_URI",
                                                            "VALIDATION_BLOCK",
                                                        ],
                                                    ),
                                                ),
                                            ),
                                            is_ssl_verify_disabled=dict(type="bool"),
                                            max_cache_duration_in_hours=dict(
                                                type="int"
                                            ),
                                            type=dict(
                                                type="str",
                                                required=True,
                                                choices=[
                                                    "REMOTE_JWKS",
                                                    "REMOTE_DISCOVERY",
                                                    "STATIC_KEYS",
                                                ],
                                            ),
                                            additional_validation_policy=dict(
                                                type="dict",
                                                options=dict(
                                                    issuers=dict(
                                                        type="list", elements="str"
                                                    ),
                                                    audiences=dict(
                                                        type="list", elements="str"
                                                    ),
                                                    verify_claims=dict(
                                                        type="list",
                                                        elements="dict",
                                                        options=dict(
                                                            key=dict(
                                                                type="str",
                                                                required=True,
                                                                no_log=True,
                                                            ),
                                                            values=dict(
                                                                type="list",
                                                                elements="str",
                                                            ),
                                                            is_required=dict(
                                                                type="bool"
                                                            ),
                                                        ),
                                                    ),
                                                ),
                                            ),
                                            keys=dict(
                                                type="list",
                                                elements="dict",
                                                no_log=False,
                                                options=dict(
                                                    kty=dict(
                                                        type="str", choices=["RSA"]
                                                    ),
                                                    use=dict(
                                                        type="str", choices=["sig"]
                                                    ),
                                                    key_ops=dict(
                                                        type="list",
                                                        elements="str",
                                                        choices=["verify"],
                                                        no_log=True,
                                                    ),
                                                    alg=dict(type="str"),
                                                    n=dict(type="str"),
                                                    e=dict(type="str"),
                                                    kid=dict(type="str", required=True),
                                                    format=dict(
                                                        type="str",
                                                        required=True,
                                                        choices=["JSON_WEB_KEY", "PEM"],
                                                    ),
                                                    key=dict(type="str", no_log=True),
                                                ),
                                            ),
                                        ),
                                    ),
                                    token_auth_scheme=dict(type="str", no_log=True),
                                    max_clock_skew_in_seconds=dict(type="float"),
                                    issuers=dict(type="list", elements="str"),
                                    audiences=dict(type="list", elements="str"),
                                    verify_claims=dict(
                                        type="list",
                                        elements="dict",
                                        options=dict(
                                            key=dict(
                                                type="str", required=True, no_log=True
                                            ),
                                            values=dict(type="list", elements="str"),
                                            is_required=dict(type="bool"),
                                        ),
                                    ),
                                    public_keys=dict(
                                        type="dict",
                                        no_log=False,
                                        options=dict(
                                            keys=dict(
                                                type="list",
                                                elements="dict",
                                                no_log=False,
                                                options=dict(
                                                    kty=dict(
                                                        type="str", choices=["RSA"]
                                                    ),
                                                    use=dict(
                                                        type="str", choices=["sig"]
                                                    ),
                                                    key_ops=dict(
                                                        type="list",
                                                        elements="str",
                                                        choices=["verify"],
                                                        no_log=True,
                                                    ),
                                                    alg=dict(type="str"),
                                                    n=dict(type="str"),
                                                    e=dict(type="str"),
                                                    kid=dict(type="str", required=True),
                                                    format=dict(
                                                        type="str",
                                                        required=True,
                                                        choices=["JSON_WEB_KEY", "PEM"],
                                                    ),
                                                    key=dict(type="str", no_log=True),
                                                ),
                                            ),
                                            type=dict(
                                                type="str",
                                                required=True,
                                                choices=["STATIC_KEYS", "REMOTE_JWKS"],
                                            ),
                                            uri=dict(type="str"),
                                            is_ssl_verify_disabled=dict(type="bool"),
                                            max_cache_duration_in_hours=dict(
                                                type="int"
                                            ),
                                        ),
                                    ),
                                    is_anonymous_access_allowed=dict(type="bool"),
                                    type=dict(
                                        type="str",
                                        required=True,
                                        choices=[
                                            "TOKEN_AUTHENTICATION",
                                            "JWT_AUTHENTICATION",
                                            "CUSTOM_AUTHENTICATION",
                                        ],
                                    ),
                                    function_id=dict(type="str"),
                                    token_header=dict(type="str", no_log=True),
                                    token_query_param=dict(type="str", no_log=True),
                                    parameters=dict(type="dict"),
                                    cache_key=dict(
                                        type="list", elements="str", no_log=True
                                    ),
                                    validation_failure_policy=dict(
                                        type="dict",
                                        options=dict(
                                            response_code=dict(type="str"),
                                            response_message=dict(type="str"),
                                            response_header_transformations=dict(
                                                type="dict",
                                                options=dict(
                                                    set_headers=dict(
                                                        type="dict",
                                                        options=dict(
                                                            items=dict(
                                                                type="list",
                                                                elements="dict",
                                                                required=True,
                                                                options=dict(
                                                                    name=dict(
                                                                        type="str",
                                                                        required=True,
                                                                    ),
                                                                    values=dict(
                                                                        type="list",
                                                                        elements="str",
                                                                        required=True,
                                                                    ),
                                                                    if_exists=dict(
                                                                        type="str",
                                                                        choices=[
                                                                            "OVERWRITE",
                                                                            "APPEND",
                                                                            "SKIP",
                                                                        ],
                                                                    ),
                                                                ),
                                                            )
                                                        ),
                                                    ),
                                                    rename_headers=dict(
                                                        type="dict",
                                                        options=dict(
                                                            items=dict(
                                                                type="list",
                                                                elements="dict",
                                                                required=True,
                                                                options=dict(
                                                                    _from=dict(
                                                                        type="str",
                                                                        required=True,
                                                                    ),
                                                                    to=dict(
                                                                        type="str",
                                                                        required=True,
                                                                    ),
                                                                ),
                                                            )
                                                        ),
                                                    ),
                                                    filter_headers=dict(
                                                        type="dict",
                                                        options=dict(
                                                            type=dict(
                                                                type="str",
                                                                required=True,
                                                                choices=[
                                                                    "ALLOW",
                                                                    "BLOCK",
                                                                ],
                                                            ),
                                                            items=dict(
                                                                type="list",
                                                                elements="dict",
                                                                required=True,
                                                                options=dict(
                                                                    name=dict(
                                                                        type="str",
                                                                        required=True,
                                                                    )
                                                                ),
                                                            ),
                                                        ),
                                                    ),
                                                ),
                                            ),
                                            type=dict(
                                                type="str",
                                                required=True,
                                                choices=["MODIFY_RESPONSE", "OAUTH2"],
                                            ),
                                            client_details=dict(
                                                type="dict",
                                                options=dict(
                                                    client_id=dict(type="str"),
                                                    client_secret_id=dict(type="str"),
                                                    client_secret_version_number=dict(
                                                        type="int", no_log=True
                                                    ),
                                                    type=dict(
                                                        type="str",
                                                        required=True,
                                                        choices=[
                                                            "CUSTOM",
                                                            "VALIDATION_BLOCK",
                                                        ],
                                                    ),
                                                ),
                                            ),
                                            source_uri_details=dict(
                                                type="dict",
                                                options=dict(
                                                    uri=dict(type="str"),
                                                    type=dict(
                                                        type="str",
                                                        required=True,
                                                        choices=[
                                                            "DISCOVERY_URI",
                                                            "VALIDATION_BLOCK",
                                                        ],
                                                    ),
                                                ),
                                            ),
                                            scopes=dict(type="list", elements="str"),
                                            max_expiry_duration_in_hours=dict(
                                                type="int"
                                            ),
                                            use_cookies_for_session=dict(type="bool"),
                                            use_cookies_for_intermediate_steps=dict(
                                                type="bool"
                                            ),
                                            use_pkce=dict(type="bool"),
                                            response_type=dict(
                                                type="str", choices=["CODE"]
                                            ),
                                            fallback_redirect_path=dict(type="str"),
                                            logout_path=dict(type="str"),
                                        ),
                                    ),
                                ),
                            ),
                            rate_limiting=dict(
                                type="dict",
                                options=dict(
                                    rate_in_requests_per_second=dict(
                                        type="int", required=True
                                    ),
                                    rate_key=dict(
                                        type="str",
                                        required=True,
                                        choices=["CLIENT_IP", "TOTAL"],
                                        no_log=True,
                                    ),
                                ),
                            ),
                            cors=dict(
                                type="dict",
                                options=dict(
                                    allowed_origins=dict(
                                        type="list", elements="str", required=True
                                    ),
                                    allowed_methods=dict(type="list", elements="str"),
                                    allowed_headers=dict(type="list", elements="str"),
                                    exposed_headers=dict(type="list", elements="str"),
                                    is_allow_credentials_enabled=dict(type="bool"),
                                    max_age_in_seconds=dict(type="int"),
                                ),
                            ),
                            mutual_tls=dict(
                                type="dict",
                                options=dict(
                                    is_verified_certificate_required=dict(type="bool"),
                                    allowed_sans=dict(type="list", elements="str"),
                                ),
                            ),
                            usage_plans=dict(
                                type="dict",
                                options=dict(
                                    token_locations=dict(
                                        type="list",
                                        elements="str",
                                        required=True,
                                        no_log=True,
                                    )
                                ),
                            ),
                            dynamic_authentication=dict(
                                type="dict",
                                options=dict(
                                    selection_source=dict(
                                        type="dict",
                                        required=True,
                                        options=dict(
                                            type=dict(
                                                type="str",
                                                default="SINGLE",
                                                choices=["SINGLE"],
                                            ),
                                            selector=dict(type="str", required=True),
                                        ),
                                    ),
                                    authentication_servers=dict(
                                        type="list",
                                        elements="dict",
                                        required=True,
                                        options=dict(
                                            key=dict(
                                                type="dict",
                                                required=True,
                                                no_log=False,
                                                options=dict(
                                                    expression=dict(type="str"),
                                                    type=dict(
                                                        type="str",
                                                        default="ANY_OF",
                                                        choices=["WILDCARD", "ANY_OF"],
                                                    ),
                                                    is_default=dict(type="bool"),
                                                    name=dict(
                                                        type="str", required=True
                                                    ),
                                                    values=dict(
                                                        type="list", elements="str"
                                                    ),
                                                ),
                                            ),
                                            authentication_server_detail=dict(
                                                type="dict",
                                                required=True,
                                                options=dict(
                                                    validation_policy=dict(
                                                        type="dict",
                                                        options=dict(
                                                            uri=dict(type="str"),
                                                            client_details=dict(
                                                                type="dict",
                                                                options=dict(
                                                                    client_id=dict(
                                                                        type="str"
                                                                    ),
                                                                    client_secret_id=dict(
                                                                        type="str"
                                                                    ),
                                                                    client_secret_version_number=dict(
                                                                        type="int",
                                                                        no_log=True,
                                                                    ),
                                                                    type=dict(
                                                                        type="str",
                                                                        required=True,
                                                                        choices=[
                                                                            "CUSTOM",
                                                                            "VALIDATION_BLOCK",
                                                                        ],
                                                                    ),
                                                                ),
                                                            ),
                                                            source_uri_details=dict(
                                                                type="dict",
                                                                options=dict(
                                                                    uri=dict(
                                                                        type="str"
                                                                    ),
                                                                    type=dict(
                                                                        type="str",
                                                                        required=True,
                                                                        choices=[
                                                                            "DISCOVERY_URI",
                                                                            "VALIDATION_BLOCK",
                                                                        ],
                                                                    ),
                                                                ),
                                                            ),
                                                            is_ssl_verify_disabled=dict(
                                                                type="bool"
                                                            ),
                                                            max_cache_duration_in_hours=dict(
                                                                type="int"
                                                            ),
                                                            type=dict(
                                                                type="str",
                                                                required=True,
                                                                choices=[
                                                                    "REMOTE_JWKS",
                                                                    "REMOTE_DISCOVERY",
                                                                    "STATIC_KEYS",
                                                                ],
                                                            ),
                                                            additional_validation_policy=dict(
                                                                type="dict",
                                                                options=dict(
                                                                    issuers=dict(
                                                                        type="list",
                                                                        elements="str",
                                                                    ),
                                                                    audiences=dict(
                                                                        type="list",
                                                                        elements="str",
                                                                    ),
                                                                    verify_claims=dict(
                                                                        type="list",
                                                                        elements="dict",
                                                                        options=dict(
                                                                            key=dict(
                                                                                type="str",
                                                                                required=True,
                                                                                no_log=True,
                                                                            ),
                                                                            values=dict(
                                                                                type="list",
                                                                                elements="str",
                                                                            ),
                                                                            is_required=dict(
                                                                                type="bool"
                                                                            ),
                                                                        ),
                                                                    ),
                                                                ),
                                                            ),
                                                            keys=dict(
                                                                type="list",
                                                                elements="dict",
                                                                no_log=False,
                                                                options=dict(
                                                                    kty=dict(
                                                                        type="str",
                                                                        choices=["RSA"],
                                                                    ),
                                                                    use=dict(
                                                                        type="str",
                                                                        choices=["sig"],
                                                                    ),
                                                                    key_ops=dict(
                                                                        type="list",
                                                                        elements="str",
                                                                        choices=[
                                                                            "verify"
                                                                        ],
                                                                        no_log=True,
                                                                    ),
                                                                    alg=dict(
                                                                        type="str"
                                                                    ),
                                                                    n=dict(type="str"),
                                                                    e=dict(type="str"),
                                                                    kid=dict(
                                                                        type="str",
                                                                        required=True,
                                                                    ),
                                                                    format=dict(
                                                                        type="str",
                                                                        required=True,
                                                                        choices=[
                                                                            "JSON_WEB_KEY",
                                                                            "PEM",
                                                                        ],
                                                                    ),
                                                                    key=dict(
                                                                        type="str",
                                                                        no_log=True,
                                                                    ),
                                                                ),
                                                            ),
                                                        ),
                                                    ),
                                                    token_auth_scheme=dict(
                                                        type="str", no_log=True
                                                    ),
                                                    max_clock_skew_in_seconds=dict(
                                                        type="float"
                                                    ),
                                                    issuers=dict(
                                                        type="list", elements="str"
                                                    ),
                                                    audiences=dict(
                                                        type="list", elements="str"
                                                    ),
                                                    verify_claims=dict(
                                                        type="list",
                                                        elements="dict",
                                                        options=dict(
                                                            key=dict(
                                                                type="str",
                                                                required=True,
                                                                no_log=True,
                                                            ),
                                                            values=dict(
                                                                type="list",
                                                                elements="str",
                                                            ),
                                                            is_required=dict(
                                                                type="bool"
                                                            ),
                                                        ),
                                                    ),
                                                    public_keys=dict(
                                                        type="dict",
                                                        no_log=False,
                                                        options=dict(
                                                            keys=dict(
                                                                type="list",
                                                                elements="dict",
                                                                no_log=False,
                                                                options=dict(
                                                                    kty=dict(
                                                                        type="str",
                                                                        choices=["RSA"],
                                                                    ),
                                                                    use=dict(
                                                                        type="str",
                                                                        choices=["sig"],
                                                                    ),
                                                                    key_ops=dict(
                                                                        type="list",
                                                                        elements="str",
                                                                        choices=[
                                                                            "verify"
                                                                        ],
                                                                        no_log=True,
                                                                    ),
                                                                    alg=dict(
                                                                        type="str"
                                                                    ),
                                                                    n=dict(type="str"),
                                                                    e=dict(type="str"),
                                                                    kid=dict(
                                                                        type="str",
                                                                        required=True,
                                                                    ),
                                                                    format=dict(
                                                                        type="str",
                                                                        required=True,
                                                                        choices=[
                                                                            "JSON_WEB_KEY",
                                                                            "PEM",
                                                                        ],
                                                                    ),
                                                                    key=dict(
                                                                        type="str",
                                                                        no_log=True,
                                                                    ),
                                                                ),
                                                            ),
                                                            type=dict(
                                                                type="str",
                                                                required=True,
                                                                choices=[
                                                                    "STATIC_KEYS",
                                                                    "REMOTE_JWKS",
                                                                ],
                                                            ),
                                                            uri=dict(type="str"),
                                                            is_ssl_verify_disabled=dict(
                                                                type="bool"
                                                            ),
                                                            max_cache_duration_in_hours=dict(
                                                                type="int"
                                                            ),
                                                        ),
                                                    ),
                                                    is_anonymous_access_allowed=dict(
                                                        type="bool"
                                                    ),
                                                    type=dict(
                                                        type="str",
                                                        required=True,
                                                        choices=[
                                                            "TOKEN_AUTHENTICATION",
                                                            "JWT_AUTHENTICATION",
                                                            "CUSTOM_AUTHENTICATION",
                                                        ],
                                                    ),
                                                    function_id=dict(type="str"),
                                                    token_header=dict(
                                                        type="str", no_log=True
                                                    ),
                                                    token_query_param=dict(
                                                        type="str", no_log=True
                                                    ),
                                                    parameters=dict(type="dict"),
                                                    cache_key=dict(
                                                        type="list",
                                                        elements="str",
                                                        no_log=True,
                                                    ),
                                                    validation_failure_policy=dict(
                                                        type="dict",
                                                        options=dict(
                                                            response_code=dict(
                                                                type="str"
                                                            ),
                                                            response_message=dict(
                                                                type="str"
                                                            ),
                                                            response_header_transformations=dict(
                                                                type="dict",
                                                                options=dict(
                                                                    set_headers=dict(
                                                                        type="dict",
                                                                        options=dict(
                                                                            items=dict(
                                                                                type="list",
                                                                                elements="dict",
                                                                                required=True,
                                                                                options=dict(
                                                                                    name=dict(
                                                                                        type="str",
                                                                                        required=True,
                                                                                    ),
                                                                                    values=dict(
                                                                                        type="list",
                                                                                        elements="str",
                                                                                        required=True,
                                                                                    ),
                                                                                    if_exists=dict(
                                                                                        type="str",
                                                                                        choices=[
                                                                                            "OVERWRITE",
                                                                                            "APPEND",
                                                                                            "SKIP",
                                                                                        ],
                                                                                    ),
                                                                                ),
                                                                            )
                                                                        ),
                                                                    ),
                                                                    rename_headers=dict(
                                                                        type="dict",
                                                                        options=dict(
                                                                            items=dict(
                                                                                type="list",
                                                                                elements="dict",
                                                                                required=True,
                                                                                options=dict(
                                                                                    _from=dict(
                                                                                        type="str",
                                                                                        required=True,
                                                                                    ),
                                                                                    to=dict(
                                                                                        type="str",
                                                                                        required=True,
                                                                                    ),
                                                                                ),
                                                                            )
                                                                        ),
                                                                    ),
                                                                    filter_headers=dict(
                                                                        type="dict",
                                                                        options=dict(
                                                                            type=dict(
                                                                                type="str",
                                                                                required=True,
                                                                                choices=[
                                                                                    "ALLOW",
                                                                                    "BLOCK",
                                                                                ],
                                                                            ),
                                                                            items=dict(
                                                                                type="list",
                                                                                elements="dict",
                                                                                required=True,
                                                                                options=dict(
                                                                                    name=dict(
                                                                                        type="str",
                                                                                        required=True,
                                                                                    )
                                                                                ),
                                                                            ),
                                                                        ),
                                                                    ),
                                                                ),
                                                            ),
                                                            type=dict(
                                                                type="str",
                                                                required=True,
                                                                choices=[
                                                                    "MODIFY_RESPONSE",
                                                                    "OAUTH2",
                                                                ],
                                                            ),
                                                            client_details=dict(
                                                                type="dict",
                                                                options=dict(
                                                                    client_id=dict(
                                                                        type="str"
                                                                    ),
                                                                    client_secret_id=dict(
                                                                        type="str"
                                                                    ),
                                                                    client_secret_version_number=dict(
                                                                        type="int",
                                                                        no_log=True,
                                                                    ),
                                                                    type=dict(
                                                                        type="str",
                                                                        required=True,
                                                                        choices=[
                                                                            "CUSTOM",
                                                                            "VALIDATION_BLOCK",
                                                                        ],
                                                                    ),
                                                                ),
                                                            ),
                                                            source_uri_details=dict(
                                                                type="dict",
                                                                options=dict(
                                                                    uri=dict(
                                                                        type="str"
                                                                    ),
                                                                    type=dict(
                                                                        type="str",
                                                                        required=True,
                                                                        choices=[
                                                                            "DISCOVERY_URI",
                                                                            "VALIDATION_BLOCK",
                                                                        ],
                                                                    ),
                                                                ),
                                                            ),
                                                            scopes=dict(
                                                                type="list",
                                                                elements="str",
                                                            ),
                                                            max_expiry_duration_in_hours=dict(
                                                                type="int"
                                                            ),
                                                            use_cookies_for_session=dict(
                                                                type="bool"
                                                            ),
                                                            use_cookies_for_intermediate_steps=dict(
                                                                type="bool"
                                                            ),
                                                            use_pkce=dict(type="bool"),
                                                            response_type=dict(
                                                                type="str",
                                                                choices=["CODE"],
                                                            ),
                                                            fallback_redirect_path=dict(
                                                                type="str"
                                                            ),
                                                            logout_path=dict(
                                                                type="str"
                                                            ),
                                                        ),
                                                    ),
                                                ),
                                            ),
                                        ),
                                    ),
                                ),
                            ),
                        ),
                    ),
                    logging_policies=dict(
                        type="dict",
                        options=dict(
                            access_log=dict(
                                type="dict", options=dict(is_enabled=dict(type="bool"))
                            ),
                            execution_log=dict(
                                type="dict",
                                options=dict(
                                    is_enabled=dict(type="bool"),
                                    log_level=dict(
                                        type="str", choices=["INFO", "WARN", "ERROR"]
                                    ),
                                ),
                            ),
                        ),
                    ),
                    routes=dict(
                        type="list",
                        elements="dict",
                        options=dict(
                            path=dict(type="str", required=True),
                            methods=dict(
                                type="list",
                                elements="str",
                                choices=[
                                    "ANY",
                                    "HEAD",
                                    "GET",
                                    "POST",
                                    "PUT",
                                    "PATCH",
                                    "DELETE",
                                    "OPTIONS",
                                ],
                            ),
                            request_policies=dict(
                                type="dict",
                                options=dict(
                                    authorization=dict(
                                        type="dict",
                                        options=dict(
                                            allowed_scope=dict(
                                                type="list", elements="str"
                                            ),
                                            type=dict(
                                                type="str",
                                                default="AUTHENTICATION_ONLY",
                                                choices=[
                                                    "ANY_OF",
                                                    "ANONYMOUS",
                                                    "AUTHENTICATION_ONLY",
                                                ],
                                            ),
                                        ),
                                    ),
                                    cors=dict(
                                        type="dict",
                                        options=dict(
                                            allowed_origins=dict(
                                                type="list",
                                                elements="str",
                                                required=True,
                                            ),
                                            allowed_methods=dict(
                                                type="list", elements="str"
                                            ),
                                            allowed_headers=dict(
                                                type="list", elements="str"
                                            ),
                                            exposed_headers=dict(
                                                type="list", elements="str"
                                            ),
                                            is_allow_credentials_enabled=dict(
                                                type="bool"
                                            ),
                                            max_age_in_seconds=dict(type="int"),
                                        ),
                                    ),
                                    query_parameter_validations=dict(
                                        type="dict",
                                        options=dict(
                                            parameters=dict(
                                                type="list",
                                                elements="dict",
                                                options=dict(
                                                    required=dict(type="bool"),
                                                    name=dict(
                                                        type="str", required=True
                                                    ),
                                                ),
                                            ),
                                            validation_mode=dict(
                                                type="str",
                                                choices=[
                                                    "ENFORCING",
                                                    "PERMISSIVE",
                                                    "DISABLED",
                                                ],
                                            ),
                                        ),
                                    ),
                                    header_validations=dict(
                                        type="dict",
                                        options=dict(
                                            headers=dict(
                                                type="list",
                                                elements="dict",
                                                options=dict(
                                                    required=dict(type="bool"),
                                                    name=dict(
                                                        type="str", required=True
                                                    ),
                                                ),
                                            ),
                                            validation_mode=dict(
                                                type="str",
                                                choices=[
                                                    "ENFORCING",
                                                    "PERMISSIVE",
                                                    "DISABLED",
                                                ],
                                            ),
                                        ),
                                    ),
                                    body_validation=dict(
                                        type="dict",
                                        options=dict(
                                            required=dict(type="bool"),
                                            content=dict(type="dict", required=True),
                                            validation_mode=dict(
                                                type="str",
                                                choices=[
                                                    "ENFORCING",
                                                    "PERMISSIVE",
                                                    "DISABLED",
                                                ],
                                            ),
                                        ),
                                    ),
                                    header_transformations=dict(
                                        type="dict",
                                        options=dict(
                                            set_headers=dict(
                                                type="dict",
                                                options=dict(
                                                    items=dict(
                                                        type="list",
                                                        elements="dict",
                                                        required=True,
                                                        options=dict(
                                                            name=dict(
                                                                type="str",
                                                                required=True,
                                                            ),
                                                            values=dict(
                                                                type="list",
                                                                elements="str",
                                                                required=True,
                                                            ),
                                                            if_exists=dict(
                                                                type="str",
                                                                choices=[
                                                                    "OVERWRITE",
                                                                    "APPEND",
                                                                    "SKIP",
                                                                ],
                                                            ),
                                                        ),
                                                    )
                                                ),
                                            ),
                                            rename_headers=dict(
                                                type="dict",
                                                options=dict(
                                                    items=dict(
                                                        type="list",
                                                        elements="dict",
                                                        required=True,
                                                        options=dict(
                                                            _from=dict(
                                                                type="str",
                                                                required=True,
                                                            ),
                                                            to=dict(
                                                                type="str",
                                                                required=True,
                                                            ),
                                                        ),
                                                    )
                                                ),
                                            ),
                                            filter_headers=dict(
                                                type="dict",
                                                options=dict(
                                                    type=dict(
                                                        type="str",
                                                        required=True,
                                                        choices=["ALLOW", "BLOCK"],
                                                    ),
                                                    items=dict(
                                                        type="list",
                                                        elements="dict",
                                                        required=True,
                                                        options=dict(
                                                            name=dict(
                                                                type="str",
                                                                required=True,
                                                            )
                                                        ),
                                                    ),
                                                ),
                                            ),
                                        ),
                                    ),
                                    query_parameter_transformations=dict(
                                        type="dict",
                                        options=dict(
                                            set_query_parameters=dict(
                                                type="dict",
                                                options=dict(
                                                    items=dict(
                                                        type="list",
                                                        elements="dict",
                                                        required=True,
                                                        options=dict(
                                                            name=dict(
                                                                type="str",
                                                                required=True,
                                                            ),
                                                            values=dict(
                                                                type="list",
                                                                elements="str",
                                                                required=True,
                                                            ),
                                                            if_exists=dict(
                                                                type="str",
                                                                choices=[
                                                                    "OVERWRITE",
                                                                    "APPEND",
                                                                    "SKIP",
                                                                ],
                                                            ),
                                                        ),
                                                    )
                                                ),
                                            ),
                                            rename_query_parameters=dict(
                                                type="dict",
                                                options=dict(
                                                    items=dict(
                                                        type="list",
                                                        elements="dict",
                                                        required=True,
                                                        options=dict(
                                                            _from=dict(
                                                                type="str",
                                                                required=True,
                                                            ),
                                                            to=dict(
                                                                type="str",
                                                                required=True,
                                                            ),
                                                        ),
                                                    )
                                                ),
                                            ),
                                            filter_query_parameters=dict(
                                                type="dict",
                                                options=dict(
                                                    type=dict(
                                                        type="str",
                                                        required=True,
                                                        choices=["ALLOW", "BLOCK"],
                                                    ),
                                                    items=dict(
                                                        type="list",
                                                        elements="dict",
                                                        required=True,
                                                        options=dict(
                                                            name=dict(
                                                                type="str",
                                                                required=True,
                                                            )
                                                        ),
                                                    ),
                                                ),
                                            ),
                                        ),
                                    ),
                                    response_cache_lookup=dict(
                                        type="dict",
                                        options=dict(
                                            type=dict(
                                                type="str",
                                                required=True,
                                                choices=["SIMPLE_LOOKUP_POLICY"],
                                            ),
                                            is_enabled=dict(type="bool"),
                                            is_private_caching_enabled=dict(
                                                type="bool"
                                            ),
                                            cache_key_additions=dict(
                                                type="list", elements="str", no_log=True
                                            ),
                                        ),
                                    ),
                                ),
                            ),
                            response_policies=dict(
                                type="dict",
                                options=dict(
                                    header_transformations=dict(
                                        type="dict",
                                        options=dict(
                                            set_headers=dict(
                                                type="dict",
                                                options=dict(
                                                    items=dict(
                                                        type="list",
                                                        elements="dict",
                                                        required=True,
                                                        options=dict(
                                                            name=dict(
                                                                type="str",
                                                                required=True,
                                                            ),
                                                            values=dict(
                                                                type="list",
                                                                elements="str",
                                                                required=True,
                                                            ),
                                                            if_exists=dict(
                                                                type="str",
                                                                choices=[
                                                                    "OVERWRITE",
                                                                    "APPEND",
                                                                    "SKIP",
                                                                ],
                                                            ),
                                                        ),
                                                    )
                                                ),
                                            ),
                                            rename_headers=dict(
                                                type="dict",
                                                options=dict(
                                                    items=dict(
                                                        type="list",
                                                        elements="dict",
                                                        required=True,
                                                        options=dict(
                                                            _from=dict(
                                                                type="str",
                                                                required=True,
                                                            ),
                                                            to=dict(
                                                                type="str",
                                                                required=True,
                                                            ),
                                                        ),
                                                    )
                                                ),
                                            ),
                                            filter_headers=dict(
                                                type="dict",
                                                options=dict(
                                                    type=dict(
                                                        type="str",
                                                        required=True,
                                                        choices=["ALLOW", "BLOCK"],
                                                    ),
                                                    items=dict(
                                                        type="list",
                                                        elements="dict",
                                                        required=True,
                                                        options=dict(
                                                            name=dict(
                                                                type="str",
                                                                required=True,
                                                            )
                                                        ),
                                                    ),
                                                ),
                                            ),
                                        ),
                                    ),
                                    response_cache_store=dict(
                                        type="dict",
                                        options=dict(
                                            type=dict(
                                                type="str",
                                                required=True,
                                                choices=["FIXED_TTL_STORE_POLICY"],
                                            ),
                                            time_to_live_in_seconds=dict(
                                                type="int", required=True
                                            ),
                                        ),
                                    ),
                                ),
                            ),
                            logging_policies=dict(
                                type="dict",
                                options=dict(
                                    access_log=dict(
                                        type="dict",
                                        options=dict(is_enabled=dict(type="bool")),
                                    ),
                                    execution_log=dict(
                                        type="dict",
                                        options=dict(
                                            is_enabled=dict(type="bool"),
                                            log_level=dict(
                                                type="str",
                                                choices=["INFO", "WARN", "ERROR"],
                                            ),
                                        ),
                                    ),
                                ),
                            ),
                            backend=dict(
                                type="dict",
                                required=True,
                                options=dict(
                                    allowed_post_logout_uris=dict(
                                        type="list", elements="str"
                                    ),
                                    post_logout_state=dict(type="str"),
                                    url=dict(type="str"),
                                    connect_timeout_in_seconds=dict(type="float"),
                                    read_timeout_in_seconds=dict(type="float"),
                                    send_timeout_in_seconds=dict(type="float"),
                                    is_ssl_verify_disabled=dict(type="bool"),
                                    function_id=dict(type="str"),
                                    body=dict(type="str"),
                                    status=dict(type="int"),
                                    headers=dict(
                                        type="list",
                                        elements="dict",
                                        options=dict(
                                            name=dict(type="str"),
                                            value=dict(type="str"),
                                        ),
                                    ),
                                    type=dict(
                                        type="str",
                                        required=True,
                                        choices=[
                                            "OAUTH2_LOGOUT_BACKEND",
                                            "HTTP_BACKEND",
                                            "ORACLE_FUNCTIONS_BACKEND",
                                            "STOCK_RESPONSE_BACKEND",
                                            "DYNAMIC_ROUTING_BACKEND",
                                        ],
                                    ),
                                    selection_source=dict(
                                        type="dict",
                                        options=dict(
                                            type=dict(
                                                type="str",
                                                default="SINGLE",
                                                choices=["SINGLE"],
                                            ),
                                            selector=dict(type="str", required=True),
                                        ),
                                    ),
                                    routing_backends=dict(
                                        type="list",
                                        elements="dict",
                                        options=dict(
                                            key=dict(
                                                type="dict",
                                                required=True,
                                                no_log=False,
                                                options=dict(
                                                    expression=dict(type="str"),
                                                    type=dict(
                                                        type="str",
                                                        default="ANY_OF",
                                                        choices=["WILDCARD", "ANY_OF"],
                                                    ),
                                                    is_default=dict(type="bool"),
                                                    name=dict(
                                                        type="str", required=True
                                                    ),
                                                    values=dict(
                                                        type="list", elements="str"
                                                    ),
                                                ),
                                            ),
                                            backend=dict(
                                                type="dict",
                                                required=True,
                                                options=dict(
                                                    type=dict(
                                                        type="str",
                                                        required=True,
                                                        choices=[
                                                            "ORACLE_FUNCTIONS_BACKEND",
                                                            "HTTP_BACKEND",
                                                            "STOCK_RESPONSE_BACKEND",
                                                            "DYNAMIC_ROUTING_BACKEND",
                                                            "OAUTH2_LOGOUT_BACKEND",
                                                        ],
                                                    )
                                                ),
                                            ),
                                        ),
                                    ),
                                ),
                            ),
                        ),
                    ),
                ),
            ),
            freeform_tags=dict(type="dict"),
            defined_tags=dict(type="dict"),
            deployment_id=dict(aliases=["id"], type="str"),
            state=dict(type="str", default="present", choices=["present", "absent"]),
        )
    )

    module = OCIAnsibleModule(argument_spec=module_args, supports_check_mode=True)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_helper = ResourceHelper(
        module=module,
        resource_type="deployment",
        service_client_class=DeploymentClient,
        namespace="apigateway",
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
