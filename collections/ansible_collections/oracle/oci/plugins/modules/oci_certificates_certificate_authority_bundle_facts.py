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
module: oci_certificates_certificate_authority_bundle_facts
description: >-
    Due to size constraints we have not included the documentation in the module. Please check L(here,
    https://docs.oracle.com/en-us/iaas/tools/oci-ansible-collection/latest/collections/oracle/oci/oci_certificates_certificate_authority_bundle_facts_module.html)
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
    from oci.certificates import CertificatesClient

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


class CertificateAuthorityBundleFactsHelperGen(OCIResourceFactsHelperBase):
    """Supported operations: get"""

    def get_required_params_for_get(self):
        return [
            "certificate_authority_id",
        ]

    def get_resource(self):
        optional_get_method_params = [
            "version_number",
            "certificate_authority_version_name",
            "stage",
        ]
        optional_kwargs = dict(
            (param, self.module.params[param])
            for param in optional_get_method_params
            if self.module.params.get(param) is not None
        )
        return oci_common_utils.call_with_backoff(
            self.client.get_certificate_authority_bundle,
            certificate_authority_id=self.module.params.get("certificate_authority_id"),
            **optional_kwargs
        )


CertificateAuthorityBundleFactsHelperCustom = get_custom_class(
    "CertificateAuthorityBundleFactsHelperCustom"
)


class ResourceFactsHelper(
    CertificateAuthorityBundleFactsHelperCustom,
    CertificateAuthorityBundleFactsHelperGen,
):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec()
    module_args.update(
        dict(
            certificate_authority_id=dict(aliases=["id"], type="str", required=True),
            version_number=dict(type="int"),
            certificate_authority_version_name=dict(type="str"),
            stage=dict(
                type="str",
                choices=["CURRENT", "PENDING", "LATEST", "PREVIOUS", "DEPRECATED"],
            ),
        )
    )

    module = OCIAnsibleModule(argument_spec=module_args)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_facts_helper = ResourceFactsHelper(
        module=module,
        resource_type="certificate_authority_bundle",
        service_client_class=CertificatesClient,
        namespace="certificates",
    )

    result = []

    if resource_facts_helper.is_get():
        result = resource_facts_helper.get()
    else:
        resource_facts_helper.fail()

    module.exit_json(certificate_authority_bundle=result)


if __name__ == "__main__":
    main()
