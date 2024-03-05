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
module: oci_generic_artifacts_content_generic_artifact_content
description: >-
    Due to size constraints we have not included the documentation in the module. Please check L(here,
    https://docs.oracle.com/en-us/iaas/tools/oci-ansible-collection/latest/collections/oracle/oci/oci_generic_artifacts_content_generic_artifact_content_module.html)
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
    from oci.generic_artifacts_content import GenericArtifactsContentClient

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


class GenericArtifactContentHelperGen(OCIResourceHelperBase):
    """Supported operations: update and get"""

    def get_possible_entity_types(self):
        return super(
            GenericArtifactContentHelperGen, self
        ).get_possible_entity_types() + [
            "genericartifactcontent",
            "genericartifactcontents",
            "genericArtifactsContentgenericartifactcontent",
            "genericArtifactsContentgenericartifactcontents",
            "genericartifactcontentresource",
            "genericartifactcontentsresource",
            "content",
            "contents",
            "genericArtifactsContentcontent",
            "genericArtifactsContentcontents",
            "contentresource",
            "contentsresource",
            "genericartifactscontent",
        ]

    def get_module_resource_id_param(self):
        return "version"

    def get_module_resource_id(self):
        return self.module.params.get("version")

    def get_get_fn(self):
        return self.client.get_generic_artifact_content_by_path

    def get_resource(self):
        return oci_common_utils.call_with_backoff(
            self.client.get_generic_artifact_content_by_path,
            repository_id=self.module.params.get("repository_id"),
            artifact_path=self.module.params.get("artifact_path"),
            version=self.module.params.get("version"),
        )

    def update_resource(self):
        file_path = self.module.params.get("generic_artifact_content_file")
        with open(file_path, "rb") as input_file:
            return oci_wait_utils.call_and_wait(
                call_fn=self.client.put_generic_artifact_content_by_path,
                call_fn_args=(),
                call_fn_kwargs=dict(
                    repository_id=self.module.params.get("repository_id"),
                    artifact_path=self.module.params.get("artifact_path"),
                    version=self.module.params.get("version"),
                    generic_artifact_content_body=input_file,
                ),
                waiter_type=oci_wait_utils.NONE_WAITER_KEY,
                operation=oci_common_utils.UPDATE_OPERATION_KEY,
                waiter_client=self.get_waiter_client(),
                resource_helper=self,
                wait_for_states=self.get_wait_for_states_for_operation(
                    oci_common_utils.UPDATE_OPERATION_KEY,
                ),
            )


GenericArtifactContentHelperCustom = get_custom_class(
    "GenericArtifactContentHelperCustom"
)


class ResourceHelper(
    GenericArtifactContentHelperCustom, GenericArtifactContentHelperGen
):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec(
        supports_create=False, supports_wait=False
    )
    module_args.update(
        dict(
            generic_artifact_content_file=dict(type="str", required=True),
            repository_id=dict(type="str", required=True),
            artifact_path=dict(type="str", required=True),
            version=dict(type="str", required=True),
            state=dict(type="str", default="present", choices=["present"]),
        )
    )

    module = OCIAnsibleModule(argument_spec=module_args, supports_check_mode=True)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_helper = ResourceHelper(
        module=module,
        resource_type="generic_artifact_content",
        service_client_class=GenericArtifactsContentClient,
        namespace="generic_artifacts_content",
    )

    result = dict(changed=False)

    if resource_helper.is_update():
        result = resource_helper.update()

    module.exit_json(**result)


if __name__ == "__main__":
    main()
