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
module: oci_data_science_model_provenance
description: >-
    Due to size constraints we have not included the documentation in the module. Please check L(here,
    https://docs.oracle.com/en-us/iaas/tools/oci-ansible-collection/latest/collections/oracle/oci/oci_data_science_model_provenance_module.html)
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
    from oci.data_science.models import CreateModelProvenanceDetails
    from oci.data_science.models import UpdateModelProvenanceDetails

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


class DataScienceModelProvenanceHelperGen(OCIResourceHelperBase):
    """Supported operations: create, update and get"""

    def get_possible_entity_types(self):
        return super(
            DataScienceModelProvenanceHelperGen, self
        ).get_possible_entity_types() + [
            "datasciencemodel",
            "datasciencemodels",
            "dataSciencedatasciencemodel",
            "dataSciencedatasciencemodels",
            "datasciencemodelresource",
            "datasciencemodelsresource",
            "modelprovenance",
            "modelprovenances",
            "dataSciencemodelprovenance",
            "dataSciencemodelprovenances",
            "modelprovenanceresource",
            "modelprovenancesresource",
            "provenance",
            "provenances",
            "dataScienceprovenance",
            "dataScienceprovenances",
            "provenanceresource",
            "provenancesresource",
            "datascience",
        ]

    def get_module_resource_id_param(self):
        return "model_id"

    def get_module_resource_id(self):
        return self.module.params.get("model_id")

    def get_get_fn(self):
        return self.client.get_model_provenance

    def get_resource(self):
        return oci_common_utils.call_with_backoff(
            self.client.get_model_provenance,
            model_id=self.module.params.get("model_id"),
        )

    def get_create_model_class(self):
        return CreateModelProvenanceDetails

    def create_resource(self):
        create_details = self.get_create_model()
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.create_model_provenance,
            call_fn_args=(),
            call_fn_kwargs=dict(
                model_id=self.module.params.get("model_id"),
                create_model_provenance_details=create_details,
            ),
            waiter_type=oci_wait_utils.NONE_WAITER_KEY,
            operation=oci_common_utils.CREATE_OPERATION_KEY,
            waiter_client=self.get_waiter_client(),
            resource_helper=self,
            wait_for_states=self.get_wait_for_states_for_operation(
                oci_common_utils.CREATE_OPERATION_KEY,
            ),
        )

    def get_update_model_class(self):
        return UpdateModelProvenanceDetails

    def update_resource(self):
        update_details = self.get_update_model()
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.update_model_provenance,
            call_fn_args=(),
            call_fn_kwargs=dict(
                model_id=self.module.params.get("model_id"),
                update_model_provenance_details=update_details,
            ),
            waiter_type=oci_wait_utils.NONE_WAITER_KEY,
            operation=oci_common_utils.UPDATE_OPERATION_KEY,
            waiter_client=self.get_waiter_client(),
            resource_helper=self,
            wait_for_states=self.get_wait_for_states_for_operation(
                oci_common_utils.UPDATE_OPERATION_KEY,
            ),
        )


DataScienceModelProvenanceHelperCustom = get_custom_class(
    "DataScienceModelProvenanceHelperCustom"
)


class ResourceHelper(
    DataScienceModelProvenanceHelperCustom, DataScienceModelProvenanceHelperGen
):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec(
        supports_create=True, supports_wait=False
    )
    module_args.update(
        dict(
            model_id=dict(aliases=["id"], type="str", required=True),
            repository_url=dict(type="str"),
            git_branch=dict(type="str"),
            git_commit=dict(type="str"),
            script_dir=dict(type="str"),
            training_script=dict(type="str"),
            training_id=dict(type="str"),
            state=dict(type="str", default="present", choices=["present"]),
        )
    )

    module = OCIAnsibleModule(argument_spec=module_args, supports_check_mode=True)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_helper = ResourceHelper(
        module=module,
        resource_type="model_provenance",
        service_client_class=DataScienceClient,
        namespace="data_science",
    )

    result = dict(changed=False)

    if resource_helper.is_update():
        result = resource_helper.update()
    elif resource_helper.is_create():
        result = resource_helper.create()

    module.exit_json(**result)


if __name__ == "__main__":
    main()
