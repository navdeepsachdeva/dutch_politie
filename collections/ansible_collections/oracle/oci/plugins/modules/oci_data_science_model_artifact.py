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
module: oci_data_science_model_artifact
description: >-
    Due to size constraints we have not included the documentation in the module. Please check L(here,
    https://docs.oracle.com/en-us/iaas/tools/oci-ansible-collection/latest/collections/oracle/oci/oci_data_science_model_artifact_module.html)
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
    from oci.data_science import DataScienceClient

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


class DataScienceModelArtifactHelperGen(OCIResourceHelperBase):
    """Supported operations: create and get"""

    def get_possible_entity_types(self):
        return super(
            DataScienceModelArtifactHelperGen, self
        ).get_possible_entity_types() + [
            "datasciencemodel",
            "datasciencemodels",
            "dataSciencedatasciencemodel",
            "dataSciencedatasciencemodels",
            "datasciencemodelresource",
            "datasciencemodelsresource",
            "modelartifact",
            "modelartifacts",
            "dataSciencemodelartifact",
            "dataSciencemodelartifacts",
            "modelartifactresource",
            "modelartifactsresource",
            "artifact",
            "artifacts",
            "dataScienceartifact",
            "dataScienceartifacts",
            "artifactresource",
            "artifactsresource",
            "datascience",
        ]

    def get_get_fn(self):
        return self.client.get_model_artifact_content

    def get_resource(self):
        return oci_common_utils.call_with_backoff(
            self.client.get_model_artifact_content,
            model_id=self.module.params.get("model_id"),
        )

    def create_resource(self):
        file_path = self.module.params.get("model_artifact_file")
        with open(file_path, "rb") as input_file:
            return oci_wait_utils.call_and_wait(
                call_fn=self.client.create_model_artifact,
                call_fn_args=(),
                call_fn_kwargs=dict(
                    model_id=self.module.params.get("model_id"),
                    content_length=self.module.params.get("content_length"),
                    model_artifact=input_file,
                    content_disposition=self.module.params.get("content_disposition"),
                ),
                waiter_type=oci_wait_utils.NONE_WAITER_KEY,
                operation=oci_common_utils.CREATE_OPERATION_KEY,
                waiter_client=self.get_waiter_client(),
                resource_helper=self,
                wait_for_states=self.get_wait_for_states_for_operation(
                    oci_common_utils.CREATE_OPERATION_KEY,
                ),
            )


DataScienceModelArtifactHelperCustom = get_custom_class(
    "DataScienceModelArtifactHelperCustom"
)


class ResourceHelper(
    DataScienceModelArtifactHelperCustom, DataScienceModelArtifactHelperGen
):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec(
        supports_create=True, supports_wait=False
    )
    module_args.update(
        dict(
            model_artifact_file=dict(type="str", required=True),
            model_id=dict(type="str", required=True),
            content_length=dict(type="int"),
            content_disposition=dict(type="str"),
            state=dict(type="str", default="present", choices=["present"]),
        )
    )

    module = OCIAnsibleModule(argument_spec=module_args, supports_check_mode=True)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_helper = ResourceHelper(
        module=module,
        resource_type="model_artifact",
        service_client_class=DataScienceClient,
        namespace="data_science",
    )

    result = dict(changed=False)

    if resource_helper.is_create():
        result = resource_helper.create()

    module.exit_json(**result)


if __name__ == "__main__":
    main()
