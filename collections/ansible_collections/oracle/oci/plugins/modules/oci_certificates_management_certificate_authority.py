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
module: oci_certificates_management_certificate_authority
description: >-
    Due to size constraints we have not included the documentation in the module. Please check L(here,
    https://docs.oracle.com/en-us/iaas/tools/oci-ansible-collection/latest/collections/oracle/oci/oci_certificates_management_certificate_authority_module.html)
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
    from oci.certificates_management import CertificatesManagementClient
    from oci.certificates_management.models import CreateCertificateAuthorityDetails
    from oci.certificates_management.models import UpdateCertificateAuthorityDetails

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


class CertificateAuthorityHelperGen(OCIResourceHelperBase):
    """Supported operations: create, update, get and list"""

    def get_possible_entity_types(self):
        return super(
            CertificateAuthorityHelperGen, self
        ).get_possible_entity_types() + [
            "certificateauthority",
            "certificateauthorities",
            "certificatesManagementcertificateauthority",
            "certificatesManagementcertificateauthorities",
            "certificateauthorityresource",
            "certificateauthoritiesresource",
            "certificatesmanagement",
        ]

    def get_module_resource_id_param(self):
        return "certificate_authority_id"

    def get_module_resource_id(self):
        return self.module.params.get("certificate_authority_id")

    def get_get_fn(self):
        return self.client.get_certificate_authority

    def get_get_model_from_summary_model(self, summary_model):
        return oci_common_utils.call_with_backoff(
            self.client.get_certificate_authority,
            certificate_authority_id=summary_model.id,
        ).data

    def get_resource(self):
        return oci_common_utils.call_with_backoff(
            self.client.get_certificate_authority,
            certificate_authority_id=self.module.params.get("certificate_authority_id"),
        )

    def get_required_kwargs_for_list(self):
        return dict()

    def get_optional_kwargs_for_list(self):
        optional_list_method_params = [
            "compartment_id",
            "name",
            "certificate_authority_id",
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
            self.client.list_certificate_authorities, **kwargs
        )

    def get_create_model_class(self):
        return CreateCertificateAuthorityDetails

    def get_exclude_attributes(self):
        return ["certificate_authority_config"]

    def create_resource(self):
        create_details = self.get_create_model()
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.create_certificate_authority,
            call_fn_args=(),
            call_fn_kwargs=dict(create_certificate_authority_details=create_details,),
            waiter_type=oci_wait_utils.LIFECYCLE_STATE_WAITER_KEY,
            operation=oci_common_utils.CREATE_OPERATION_KEY,
            waiter_client=self.get_waiter_client(),
            resource_helper=self,
            wait_for_states=self.get_wait_for_states_for_operation(
                oci_common_utils.CREATE_OPERATION_KEY,
            ),
        )

    def get_update_model_class(self):
        return UpdateCertificateAuthorityDetails

    def update_resource(self):
        update_details = self.get_update_model()
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.update_certificate_authority,
            call_fn_args=(),
            call_fn_kwargs=dict(
                certificate_authority_id=self.module.params.get(
                    "certificate_authority_id"
                ),
                update_certificate_authority_details=update_details,
            ),
            waiter_type=oci_wait_utils.LIFECYCLE_STATE_WAITER_KEY,
            operation=oci_common_utils.UPDATE_OPERATION_KEY,
            waiter_client=self.get_waiter_client(),
            resource_helper=self,
            wait_for_states=self.get_wait_for_states_for_operation(
                oci_common_utils.UPDATE_OPERATION_KEY,
            ),
        )


CertificateAuthorityHelperCustom = get_custom_class("CertificateAuthorityHelperCustom")


class ResourceHelper(CertificateAuthorityHelperCustom, CertificateAuthorityHelperGen):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec(
        supports_create=True, supports_wait=True
    )
    module_args.update(
        dict(
            name=dict(type="str"),
            compartment_id=dict(type="str"),
            kms_key_id=dict(type="str"),
            certificate_authority_id=dict(aliases=["id"], type="str"),
            description=dict(type="str"),
            current_version_number=dict(type="int"),
            certificate_authority_config=dict(
                type="dict",
                options=dict(
                    issuer_certificate_authority_id=dict(type="str"),
                    signing_algorithm=dict(
                        type="str",
                        choices=[
                            "SHA256_WITH_RSA",
                            "SHA384_WITH_RSA",
                            "SHA512_WITH_RSA",
                            "SHA256_WITH_ECDSA",
                            "SHA384_WITH_ECDSA",
                            "SHA512_WITH_ECDSA",
                        ],
                    ),
                    subject=dict(
                        type="dict",
                        options=dict(
                            common_name=dict(type="str", required=True),
                            country=dict(type="str"),
                            domain_component=dict(type="str"),
                            distinguished_name_qualifier=dict(type="str"),
                            generation_qualifier=dict(type="str"),
                            given_name=dict(type="str"),
                            initials=dict(type="str"),
                            locality_name=dict(type="str"),
                            organization=dict(type="str"),
                            organizational_unit=dict(type="str"),
                            pseudonym=dict(type="str"),
                            serial_number=dict(type="str"),
                            state_or_province_name=dict(type="str"),
                            street=dict(type="str"),
                            surname=dict(type="str"),
                            title=dict(type="str"),
                            user_id=dict(type="str"),
                        ),
                    ),
                    config_type=dict(
                        type="str",
                        required=True,
                        choices=[
                            "ROOT_CA_GENERATED_INTERNALLY",
                            "SUBORDINATE_CA_ISSUED_BY_INTERNAL_CA",
                        ],
                    ),
                    version_name=dict(type="str"),
                    stage=dict(type="str", choices=["CURRENT", "PENDING"]),
                    validity=dict(
                        type="dict",
                        options=dict(
                            time_of_validity_not_before=dict(type="str"),
                            time_of_validity_not_after=dict(type="str", required=True),
                        ),
                    ),
                ),
            ),
            certificate_revocation_list_details=dict(
                type="dict",
                options=dict(
                    object_storage_config=dict(
                        type="dict",
                        required=True,
                        options=dict(
                            object_storage_namespace=dict(type="str"),
                            object_storage_bucket_name=dict(type="str", required=True),
                            object_storage_object_name_format=dict(
                                type="str", required=True
                            ),
                        ),
                    ),
                    custom_formatted_urls=dict(type="list", elements="str"),
                ),
            ),
            freeform_tags=dict(type="dict"),
            defined_tags=dict(type="dict"),
            certificate_authority_rules=dict(
                type="list",
                elements="dict",
                options=dict(
                    rule_type=dict(
                        type="str",
                        required=True,
                        choices=["CERTIFICATE_AUTHORITY_ISSUANCE_EXPIRY_RULE"],
                    ),
                    leaf_certificate_max_validity_duration=dict(type="str"),
                    certificate_authority_max_validity_duration=dict(type="str"),
                ),
            ),
            state=dict(type="str", default="present", choices=["present"]),
        )
    )

    module = OCIAnsibleModule(argument_spec=module_args, supports_check_mode=True)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_helper = ResourceHelper(
        module=module,
        resource_type="certificate_authority",
        service_client_class=CertificatesManagementClient,
        namespace="certificates_management",
    )

    result = dict(changed=False)

    if resource_helper.is_update_using_name():
        result = resource_helper.update_using_name()
    elif resource_helper.is_update():
        result = resource_helper.update()
    elif resource_helper.is_create():
        result = resource_helper.create()

    module.exit_json(**result)


if __name__ == "__main__":
    main()