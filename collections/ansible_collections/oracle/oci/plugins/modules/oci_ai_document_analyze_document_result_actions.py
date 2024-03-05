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
module: oci_ai_document_analyze_document_result_actions
description: >-
    Due to size constraints we have not included the documentation in the module. Please check L(here,
    https://docs.oracle.com/en-us/iaas/tools/oci-ansible-collection/latest/collections/oracle/oci/oci_ai_document_analyze_document_result_actions_module.html)
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
    from oci.ai_document import AIServiceDocumentClient
    from oci.ai_document.models import AnalyzeDocumentDetails

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


class AiDocumentAnalyzeDocumentResultActionsHelperGen(OCIActionsHelperBase):
    """
    Supported actions:
        analyze_document
    """

    def analyze_document(self):
        action_details = oci_common_utils.convert_input_data_to_model_class(
            self.module.params, AnalyzeDocumentDetails
        )
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.analyze_document,
            call_fn_args=(),
            call_fn_kwargs=dict(analyze_document_details=action_details,),
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


AiDocumentAnalyzeDocumentResultActionsHelperCustom = get_custom_class(
    "AiDocumentAnalyzeDocumentResultActionsHelperCustom"
)


class ResourceHelper(
    AiDocumentAnalyzeDocumentResultActionsHelperCustom,
    AiDocumentAnalyzeDocumentResultActionsHelperGen,
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
            document=dict(
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
            output_location=dict(
                type="dict",
                options=dict(
                    namespace_name=dict(type="str", required=True),
                    bucket_name=dict(type="str", required=True),
                    prefix=dict(type="str", required=True),
                ),
            ),
            language=dict(type="str"),
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
            ocr_data=dict(
                type="dict",
                options=dict(
                    document_metadata=dict(
                        type="dict",
                        required=True,
                        options=dict(
                            page_count=dict(type="int", required=True),
                            mime_type=dict(type="str", required=True),
                        ),
                    ),
                    pages=dict(
                        type="list",
                        elements="dict",
                        required=True,
                        options=dict(
                            page_number=dict(type="int", required=True),
                            dimensions=dict(
                                type="dict",
                                options=dict(
                                    width=dict(type="float", required=True),
                                    height=dict(type="float", required=True),
                                    unit=dict(
                                        type="str",
                                        required=True,
                                        choices=["PIXEL", "INCH"],
                                    ),
                                ),
                            ),
                            detected_document_types=dict(
                                type="list",
                                elements="dict",
                                options=dict(
                                    document_type=dict(type="str", required=True),
                                    document_id=dict(type="str"),
                                    confidence=dict(type="float", required=True),
                                ),
                            ),
                            detected_languages=dict(
                                type="list",
                                elements="dict",
                                options=dict(
                                    language=dict(type="str", required=True),
                                    confidence=dict(type="float", required=True),
                                ),
                            ),
                            words=dict(
                                type="list",
                                elements="dict",
                                options=dict(
                                    text=dict(type="str", required=True),
                                    confidence=dict(type="float", required=True),
                                    bounding_polygon=dict(
                                        type="dict",
                                        required=True,
                                        options=dict(
                                            normalized_vertices=dict(
                                                type="list",
                                                elements="dict",
                                                required=True,
                                                options=dict(
                                                    x=dict(type="float", required=True),
                                                    y=dict(type="float", required=True),
                                                ),
                                            )
                                        ),
                                    ),
                                ),
                            ),
                            lines=dict(
                                type="list",
                                elements="dict",
                                options=dict(
                                    text=dict(type="str", required=True),
                                    confidence=dict(type="float", required=True),
                                    bounding_polygon=dict(
                                        type="dict",
                                        required=True,
                                        options=dict(
                                            normalized_vertices=dict(
                                                type="list",
                                                elements="dict",
                                                required=True,
                                                options=dict(
                                                    x=dict(type="float", required=True),
                                                    y=dict(type="float", required=True),
                                                ),
                                            )
                                        ),
                                    ),
                                    word_indexes=dict(
                                        type="list", elements="int", required=True
                                    ),
                                ),
                            ),
                            tables=dict(
                                type="list",
                                elements="dict",
                                options=dict(
                                    row_count=dict(type="int", required=True),
                                    column_count=dict(type="int", required=True),
                                    header_rows=dict(
                                        type="list",
                                        elements="dict",
                                        required=True,
                                        options=dict(
                                            cells=dict(
                                                type="list",
                                                elements="dict",
                                                required=True,
                                                options=dict(
                                                    text=dict(
                                                        type="str", required=True
                                                    ),
                                                    row_index=dict(
                                                        type="int", required=True
                                                    ),
                                                    column_index=dict(
                                                        type="int", required=True
                                                    ),
                                                    confidence=dict(
                                                        type="float", required=True
                                                    ),
                                                    bounding_polygon=dict(
                                                        type="dict",
                                                        required=True,
                                                        options=dict(
                                                            normalized_vertices=dict(
                                                                type="list",
                                                                elements="dict",
                                                                required=True,
                                                                options=dict(
                                                                    x=dict(
                                                                        type="float",
                                                                        required=True,
                                                                    ),
                                                                    y=dict(
                                                                        type="float",
                                                                        required=True,
                                                                    ),
                                                                ),
                                                            )
                                                        ),
                                                    ),
                                                    word_indexes=dict(
                                                        type="list",
                                                        elements="int",
                                                        required=True,
                                                    ),
                                                ),
                                            )
                                        ),
                                    ),
                                    body_rows=dict(
                                        type="list",
                                        elements="dict",
                                        required=True,
                                        options=dict(
                                            cells=dict(
                                                type="list",
                                                elements="dict",
                                                required=True,
                                                options=dict(
                                                    text=dict(
                                                        type="str", required=True
                                                    ),
                                                    row_index=dict(
                                                        type="int", required=True
                                                    ),
                                                    column_index=dict(
                                                        type="int", required=True
                                                    ),
                                                    confidence=dict(
                                                        type="float", required=True
                                                    ),
                                                    bounding_polygon=dict(
                                                        type="dict",
                                                        required=True,
                                                        options=dict(
                                                            normalized_vertices=dict(
                                                                type="list",
                                                                elements="dict",
                                                                required=True,
                                                                options=dict(
                                                                    x=dict(
                                                                        type="float",
                                                                        required=True,
                                                                    ),
                                                                    y=dict(
                                                                        type="float",
                                                                        required=True,
                                                                    ),
                                                                ),
                                                            )
                                                        ),
                                                    ),
                                                    word_indexes=dict(
                                                        type="list",
                                                        elements="int",
                                                        required=True,
                                                    ),
                                                ),
                                            )
                                        ),
                                    ),
                                    footer_rows=dict(
                                        type="list",
                                        elements="dict",
                                        required=True,
                                        options=dict(
                                            cells=dict(
                                                type="list",
                                                elements="dict",
                                                required=True,
                                                options=dict(
                                                    text=dict(
                                                        type="str", required=True
                                                    ),
                                                    row_index=dict(
                                                        type="int", required=True
                                                    ),
                                                    column_index=dict(
                                                        type="int", required=True
                                                    ),
                                                    confidence=dict(
                                                        type="float", required=True
                                                    ),
                                                    bounding_polygon=dict(
                                                        type="dict",
                                                        required=True,
                                                        options=dict(
                                                            normalized_vertices=dict(
                                                                type="list",
                                                                elements="dict",
                                                                required=True,
                                                                options=dict(
                                                                    x=dict(
                                                                        type="float",
                                                                        required=True,
                                                                    ),
                                                                    y=dict(
                                                                        type="float",
                                                                        required=True,
                                                                    ),
                                                                ),
                                                            )
                                                        ),
                                                    ),
                                                    word_indexes=dict(
                                                        type="list",
                                                        elements="int",
                                                        required=True,
                                                    ),
                                                ),
                                            )
                                        ),
                                    ),
                                    confidence=dict(type="float", required=True),
                                    bounding_polygon=dict(
                                        type="dict",
                                        required=True,
                                        options=dict(
                                            normalized_vertices=dict(
                                                type="list",
                                                elements="dict",
                                                required=True,
                                                options=dict(
                                                    x=dict(type="float", required=True),
                                                    y=dict(type="float", required=True),
                                                ),
                                            )
                                        ),
                                    ),
                                ),
                            ),
                            document_fields=dict(
                                type="list",
                                elements="dict",
                                options=dict(
                                    field_type=dict(
                                        type="str",
                                        required=True,
                                        choices=[
                                            "LINE_ITEM_GROUP",
                                            "LINE_ITEM",
                                            "LINE_ITEM_FIELD",
                                            "KEY_VALUE",
                                        ],
                                    ),
                                    field_label=dict(
                                        type="dict",
                                        options=dict(
                                            name=dict(type="str", required=True),
                                            confidence=dict(type="float"),
                                        ),
                                    ),
                                    field_name=dict(
                                        type="dict",
                                        options=dict(
                                            name=dict(type="str", required=True),
                                            confidence=dict(type="float"),
                                            bounding_polygon=dict(
                                                type="dict",
                                                options=dict(
                                                    normalized_vertices=dict(
                                                        type="list",
                                                        elements="dict",
                                                        required=True,
                                                        options=dict(
                                                            x=dict(
                                                                type="float",
                                                                required=True,
                                                            ),
                                                            y=dict(
                                                                type="float",
                                                                required=True,
                                                            ),
                                                        ),
                                                    )
                                                ),
                                            ),
                                            word_indexes=dict(
                                                type="list", elements="int"
                                            ),
                                        ),
                                    ),
                                    field_value=dict(
                                        type="dict",
                                        required=True,
                                        options=dict(
                                            value=dict(type="str"),
                                            value_type=dict(
                                                type="str",
                                                required=True,
                                                choices=[
                                                    "TIME",
                                                    "INTEGER",
                                                    "DATE",
                                                    "NUMBER",
                                                    "STRING",
                                                    "PHONE_NUMBER",
                                                    "ARRAY",
                                                ],
                                            ),
                                            text=dict(type="str"),
                                            confidence=dict(
                                                type="float", required=True
                                            ),
                                            bounding_polygon=dict(
                                                type="dict",
                                                required=True,
                                                options=dict(
                                                    normalized_vertices=dict(
                                                        type="list",
                                                        elements="dict",
                                                        required=True,
                                                        options=dict(
                                                            x=dict(
                                                                type="float",
                                                                required=True,
                                                            ),
                                                            y=dict(
                                                                type="float",
                                                                required=True,
                                                            ),
                                                        ),
                                                    )
                                                ),
                                            ),
                                            word_indexes=dict(
                                                type="list",
                                                elements="int",
                                                required=True,
                                            ),
                                            items=dict(
                                                type="list",
                                                elements="dict",
                                                options=dict(
                                                    field_type=dict(
                                                        type="str",
                                                        required=True,
                                                        choices=[
                                                            "LINE_ITEM_GROUP",
                                                            "LINE_ITEM",
                                                            "LINE_ITEM_FIELD",
                                                            "KEY_VALUE",
                                                        ],
                                                    ),
                                                    field_label=dict(type="FieldLabel"),
                                                    field_name=dict(type="FieldName"),
                                                    field_value=dict(
                                                        type="FieldValue", required=True
                                                    ),
                                                ),
                                            ),
                                        ),
                                    ),
                                ),
                            ),
                        ),
                    ),
                    detected_document_types=dict(
                        type="list",
                        elements="dict",
                        options=dict(
                            document_type=dict(type="str", required=True),
                            document_id=dict(type="str"),
                            confidence=dict(type="float", required=True),
                        ),
                    ),
                    detected_languages=dict(
                        type="list",
                        elements="dict",
                        options=dict(
                            language=dict(type="str", required=True),
                            confidence=dict(type="float", required=True),
                        ),
                    ),
                    document_classification_model_version=dict(type="str"),
                    language_classification_model_version=dict(type="str"),
                    text_extraction_model_version=dict(type="str"),
                    key_value_extraction_model_version=dict(type="str", no_log=True),
                    table_extraction_model_version=dict(type="str"),
                    errors=dict(
                        type="list",
                        elements="dict",
                        options=dict(
                            code=dict(type="str", required=True),
                            message=dict(type="str", required=True),
                        ),
                    ),
                    searchable_pdf=dict(type="str"),
                ),
            ),
            action=dict(type="str", required=True, choices=["analyze_document"]),
        )
    )

    module = OCIAnsibleModule(argument_spec=module_args, supports_check_mode=True)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_helper = ResourceHelper(
        module=module,
        resource_type="analyze_document_result",
        service_client_class=AIServiceDocumentClient,
        namespace="ai_document",
    )

    result = resource_helper.perform_action(module.params.get("action"))

    module.exit_json(**result)


if __name__ == "__main__":
    main()
