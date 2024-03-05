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
module: oci_ai_vision_analyze_image_result_actions
description: >-
    Due to size constraints we have not included the documentation in the module. Please check L(here,
    https://docs.oracle.com/en-us/iaas/tools/oci-ansible-collection/latest/collections/oracle/oci/oci_ai_vision_analyze_image_result_actions_module.html)
    for the module documentation.
author: Oracle (@oracle)
"""


from ansible_collections.oracle.oci.plugins.module_utils import (
    oci_common_utils,
    oci_wait_utils,
)
from ansible_collections.oracle.oci.plugins.module_utils.oci_resource_utils import (
    OCIActionsHelperBase,
    OCIAnsibleModule,
    get_custom_class,
)

try:
    from oci.ai_vision import AIServiceVisionClient
    from oci.ai_vision.models import AnalyzeImageDetails

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


class AiVisionAnalyzeImageResultActionsHelperGen(OCIActionsHelperBase):
    """
    Supported actions:
        analyze_image
    """

    def analyze_image(self):
        action_details = oci_common_utils.convert_input_data_to_model_class(
            self.module.params, AnalyzeImageDetails
        )
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.analyze_image,
            call_fn_args=(),
            call_fn_kwargs=dict(analyze_image_details=action_details,),
            waiter_type=oci_wait_utils.NONE_WAITER_KEY,
            operation="{0}_{1}".format(
                self.module.params.get("action").upper(),
                oci_common_utils.ACTION_OPERATION_KEY,
            ),
            waiter_client=self.get_waiter_client(),
            resource_helper=self,
            wait_for_states=self.get_action_desired_states(
                self.module.params.get("action")
            ),
        )


AiVisionAnalyzeImageResultActionsHelperCustom = get_custom_class(
    "AiVisionAnalyzeImageResultActionsHelperCustom"
)


class ResourceHelper(
    AiVisionAnalyzeImageResultActionsHelperCustom,
    AiVisionAnalyzeImageResultActionsHelperGen,
):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec(
        supports_create=False, supports_wait=False
    )
    module_args.update(
        dict(
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
            image=dict(
                type="dict",
                required=True,
                options=dict(
                    namespace_name=dict(type="str"),
                    bucket_name=dict(type="str"),
                    object_name=dict(type="str"),
                    source=dict(
                        type="str", required=True, choices=["OBJECT_STORAGE", "INLINE"]
                    ),
                    data=dict(type="str"),
                ),
            ),
            compartment_id=dict(type="str"),
            action=dict(type="str", required=True, choices=["analyze_image"]),
        )
    )

    module = OCIAnsibleModule(argument_spec=module_args, supports_check_mode=True)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_helper = ResourceHelper(
        module=module,
        resource_type="analyze_image_result",
        service_client_class=AIServiceVisionClient,
        namespace="ai_vision",
    )

    result = resource_helper.perform_action(module.params.get("action"))

    module.exit_json(**result)


if __name__ == "__main__":
    main()
