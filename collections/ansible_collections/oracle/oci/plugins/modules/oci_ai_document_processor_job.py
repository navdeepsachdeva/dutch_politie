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
module: oci_ai_document_processor_job
description: >-
    Due to size constraints we have not included the documentation in the module. Please check L(here,
    https://docs.oracle.com/en-us/iaas/tools/oci-ansible-collection/latest/collections/oracle/oci/oci_ai_document_processor_job_module.html)
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
    from oci.ai_document import AIServiceDocumentClient
    from oci.ai_document.models import CreateProcessorJobDetails

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


class AiDocumentProcessorJobHelperGen(OCIResourceHelperBase):
    """Supported operations: create and get"""

    def get_possible_entity_types(self):
        return super(
            AiDocumentProcessorJobHelperGen, self
        ).get_possible_entity_types() + [
            "processorjob",
            "processorjobs",
            "aiDocumentprocessorjob",
            "aiDocumentprocessorjobs",
            "processorjobresource",
            "processorjobsresource",
            "aidocument",
        ]

    def get_get_fn(self):
        return self.client.get_processor_job

    def get_resource(self):
        return oci_common_utils.call_with_backoff(
            self.client.get_processor_job,
            processor_job_id=self.module.params.get("processor_job_id"),
        )

    def get_create_model_class(self):
        return CreateProcessorJobDetails

    def create_resource(self):
        create_details = self.get_create_model()
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.create_processor_job,
            call_fn_args=(),
            call_fn_kwargs=dict(create_processor_job_details=create_details,),
            waiter_type=oci_wait_utils.LIFECYCLE_STATE_WAITER_KEY,
            operation=oci_common_utils.CREATE_OPERATION_KEY,
            waiter_client=self.get_waiter_client(),
            resource_helper=self,
            wait_for_states=self.get_wait_for_states_for_operation(
                oci_common_utils.CREATE_OPERATION_KEY,
            ),
        )


AiDocumentProcessorJobHelperCustom = get_custom_class(
    "AiDocumentProcessorJobHelperCustom"
)


class ResourceHelper(
    AiDocumentProcessorJobHelperCustom, AiDocumentProcessorJobHelperGen
):
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
                    data=dict(type="str"),
                    source_type=dict(
                        type="str",
                        required=True,
                        choices=["INLINE_DOCUMENT_CONTENT", "OBJECT_STORAGE_LOCATIONS"],
                    ),
                    object_locations=dict(
                        type="list",
                        elements="dict",
                        options=dict(
                            namespace_name=dict(type="str", required=True),
                            bucket_name=dict(type="str", required=True),
                            object_name=dict(type="str", required=True),
                        ),
                    ),
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
            compartment_id=dict(type="str", required=True),
            display_name=dict(aliases=["name"], type="str"),
            processor_config=dict(
                type="dict",
                required=True,
                options=dict(
                    processor_type=dict(type="str", required=True, choices=["GENERAL"]),
                    document_type=dict(
                        type="str",
                        choices=[
                            "INVOICE",
                            "RECEIPT",
                            "RESUME",
                            "TAX_FORM",
                            "DRIVER_LICENSE",
                            "PASSPORT",
                            "BANK_STATEMENT",
                            "CHECK",
                            "PAYSLIP",
                            "OTHERS",
                        ],
                    ),
                    features=dict(
                        type="list",
                        elements="dict",
                        required=True,
                        options=dict(
                            model_id=dict(type="str"),
                            tenancy_id=dict(type="str"),
                            max_results=dict(type="int"),
                            generate_searchable_pdf=dict(type="bool"),
                            feature_type=dict(
                                type="str",
                                required=True,
                                choices=[
                                    "DOCUMENT_CLASSIFICATION",
                                    "KEY_VALUE_EXTRACTION",
                                    "LANGUAGE_CLASSIFICATION",
                                    "TEXT_EXTRACTION",
                                    "TABLE_EXTRACTION",
                                ],
                            ),
                        ),
                    ),
                    is_zip_output_enabled=dict(type="bool"),
                    language=dict(type="str"),
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
        resource_type="processor_job",
        service_client_class=AIServiceDocumentClient,
        namespace="ai_document",
    )

    result = dict(changed=False)

    if resource_helper.is_create():
        result = resource_helper.create()

    module.exit_json(**result)


if __name__ == "__main__":
    main()
