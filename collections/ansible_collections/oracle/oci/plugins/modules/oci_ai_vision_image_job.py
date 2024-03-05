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
module: oci_ai_vision_image_job
description: >-
    Due to size constraints we have not included the documentation in the module. Please check L(here,
    https://docs.oracle.com/en-us/iaas/tools/oci-ansible-collection/latest/collections/oracle/oci/oci_ai_vision_image_job_module.html)
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
    from oci.ai_vision import AIServiceVisionClient
    from oci.ai_vision.models import CreateImageJobDetails

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


class AiVisionImageJobHelperGen(OCIResourceHelperBase):
    """Supported operations: create and get"""

    def get_possible_entity_types(self):
        return super(AiVisionImageJobHelperGen, self).get_possible_entity_types() + [
            "imagejob",
            "imagejobs",
            "aiVisionimagejob",
            "aiVisionimagejobs",
            "imagejobresource",
            "imagejobsresource",
            "aivision",
        ]

    def get_get_fn(self):
        return self.client.get_image_job

    def get_resource(self):
        return oci_common_utils.call_with_backoff(
            self.client.get_image_job,
            image_job_id=self.module.params.get("image_job_id"),
        )

    def get_create_model_class(self):
        return CreateImageJobDetails

    def create_resource(self):
        create_details = self.get_create_model()
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.create_image_job,
            call_fn_args=(),
            call_fn_kwargs=dict(create_image_job_details=create_details,),
            waiter_type=oci_wait_utils.LIFECYCLE_STATE_WAITER_KEY,
            operation=oci_common_utils.CREATE_OPERATION_KEY,
            waiter_client=self.get_waiter_client(),
            resource_helper=self,
            wait_for_states=self.get_wait_for_states_for_operation(
                oci_common_utils.CREATE_OPERATION_KEY,
            ),
        )


AiVisionImageJobHelperCustom = get_custom_class("AiVisionImageJobHelperCustom")


class ResourceHelper(AiVisionImageJobHelperCustom, AiVisionImageJobHelperGen):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec(
        supports_create=True, supports_wait=True
    )
    module_args.update(
        dict(
            input_location=dict(
                type="dict",
                required=True,
                options=dict(
                    source_type=dict(
                        type="str",
                        required=True,
                        choices=["OBJECT_LIST_INLINE_INPUT_LOCATION"],
                    ),
                    object_locations=dict(
                        type="list",
                        elements="dict",
                        required=True,
                        options=dict(
                            namespace_name=dict(type="str", required=True),
                            bucket_name=dict(type="str", required=True),
                            object_name=dict(type="str", required=True),
                        ),
                    ),
                ),
            ),
            features=dict(
                type="list",
                elements="dict",
                required=True,
                options=dict(
                    language=dict(
                        type="str",
                        choices=[
                            "ENG",
                            "CES",
                            "DAN",
                            "NLD",
                            "FIN",
                            "FRA",
                            "DEU",
                            "ELL",
                            "HUN",
                            "ITA",
                            "NOR",
                            "POL",
                            "POR",
                            "RON",
                            "RUS",
                            "SLK",
                            "SPA",
                            "SWE",
                            "TUR",
                            "ARA",
                            "CHI_SIM",
                            "HIN",
                            "JPN",
                            "KOR",
                            "OTHERS",
                        ],
                    ),
                    feature_type=dict(
                        type="str",
                        required=True,
                        choices=[
                            "TEXT_DETECTION",
                            "OBJECT_DETECTION",
                            "IMAGE_CLASSIFICATION",
                        ],
                    ),
                    max_results=dict(type="int"),
                    model_id=dict(type="str"),
                ),
            ),
            output_location=dict(
                type="dict",
                required=True,
                options=dict(
                    namespace_name=dict(type="str", required=True),
                    bucket_name=dict(type="str", required=True),
                    prefix=dict(type="str", required=True),
                ),
            ),
            compartment_id=dict(type="str"),
            display_name=dict(aliases=["name"], type="str"),
            is_zip_output_enabled=dict(type="bool"),
            state=dict(type="str", default="present", choices=["present"]),
        )
    )

    module = OCIAnsibleModule(argument_spec=module_args, supports_check_mode=True)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_helper = ResourceHelper(
        module=module,
        resource_type="image_job",
        service_client_class=AIServiceVisionClient,
        namespace="ai_vision",
    )

    result = dict(changed=False)

    if resource_helper.is_create():
        result = resource_helper.create()

    module.exit_json(**result)


if __name__ == "__main__":
    main()
