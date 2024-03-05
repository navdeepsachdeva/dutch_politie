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
module: oci_announcements_service_announcements_collection_facts
description: >-
    Due to size constraints we have not included the documentation in the module. Please check L(here,
    https://docs.oracle.com/en-us/iaas/tools/oci-ansible-collection/latest/collections/oracle/oci/oci_announcements_service_announcements_collection_facts_module.html)
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
    from oci.announcements_service import AnnouncementClient

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


class AnnouncementsCollectionFactsHelperGen(OCIResourceFactsHelperBase):
    """Supported operations: list"""

    def get_required_params_for_list(self):
        return [
            "compartment_id",
        ]

    def list_resources(self):
        optional_list_method_params = [
            "announcement_type",
            "lifecycle_state",
            "is_banner",
            "sort_by",
            "sort_order",
            "time_one_earliest_time",
            "time_one_latest_time",
            "environment_name",
            "service",
            "platform_type",
            "exclude_announcement_types",
            "should_show_only_latest_in_chain",
            "chain_id",
        ]
        optional_kwargs = dict(
            (param, self.module.params[param])
            for param in optional_list_method_params
            if self.module.params.get(param) is not None
        )
        return oci_common_utils.list_all_resources(
            self.client.list_announcements,
            compartment_id=self.module.params.get("compartment_id"),
            **optional_kwargs
        )


AnnouncementsCollectionFactsHelperCustom = get_custom_class(
    "AnnouncementsCollectionFactsHelperCustom"
)


class ResourceFactsHelper(
    AnnouncementsCollectionFactsHelperCustom, AnnouncementsCollectionFactsHelperGen
):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec()
    module_args.update(
        dict(
            compartment_id=dict(type="str", required=True),
            announcement_type=dict(type="str"),
            lifecycle_state=dict(type="str", choices=["ACTIVE", "INACTIVE"]),
            is_banner=dict(type="bool"),
            sort_by=dict(
                type="str",
                choices=[
                    "timeOneValue",
                    "timeTwoValue",
                    "timeCreated",
                    "referenceTicketNumber",
                    "summary",
                    "announcementType",
                ],
            ),
            sort_order=dict(type="str", choices=["ASC", "DESC"]),
            time_one_earliest_time=dict(type="str"),
            time_one_latest_time=dict(type="str"),
            environment_name=dict(type="str"),
            service=dict(type="str"),
            platform_type=dict(type="str", choices=["IAAS", "SAAS"]),
            exclude_announcement_types=dict(type="list", elements="str"),
            should_show_only_latest_in_chain=dict(type="bool"),
            chain_id=dict(type="str"),
        )
    )

    module = OCIAnsibleModule(argument_spec=module_args)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_facts_helper = ResourceFactsHelper(
        module=module,
        resource_type="announcements_collection",
        service_client_class=AnnouncementClient,
        namespace="announcements_service",
    )

    result = []

    if resource_facts_helper.is_list():
        result = resource_facts_helper.list()
    else:
        resource_facts_helper.fail()

    module.exit_json(announcements_collection=result)


if __name__ == "__main__":
    main()
