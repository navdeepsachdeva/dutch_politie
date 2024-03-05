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
module: oci_database_autonomous_database_character_sets_facts
short_description: Fetches details about one or multiple AutonomousDatabaseCharacterSets resources in Oracle Cloud Infrastructure
description:
    - Fetches details about one or multiple AutonomousDatabaseCharacterSets resources in Oracle Cloud Infrastructure
    - Gets a list of supported character sets.
version_added: "2.9.0"
author: Oracle (@oracle)
options:
    is_shared:
        description:
            - Specifies whether this request is for Autonomous Database on Shared infrastructure. By default, this request will be for Autonomous Database on
              Dedicated Exadata Infrastructure.
        type: bool
    character_set_type:
        description:
            - Specifies whether this request pertains to database character sets or national character sets.
        type: str
        choices:
            - "DATABASE"
            - "NATIONAL"
extends_documentation_fragment: [ oracle.oci.oracle, oracle.oci.oracle_name_option ]
"""

EXAMPLES = """
- name: List autonomous_database_character_sets
  oci_database_autonomous_database_character_sets_facts:

    # optional
    is_shared: true
    character_set_type: DATABASE

"""

RETURN = """
autonomous_database_character_sets:
    description:
        - List of AutonomousDatabaseCharacterSets resources
    returned: on success
    type: complex
    contains:
        name:
            description:
                - A valid Oracle character set.
            returned: on success
            type: str
            sample: name_example
    sample: [{
        "name": "name_example"
    }]
"""

from ansible_collections.oracle.oci.plugins.module_utils import oci_common_utils
from ansible_collections.oracle.oci.plugins.module_utils.oci_resource_utils import (
    OCIResourceFactsHelperBase,
    get_custom_class,
    OCIAnsibleModule,
)

try:
    from oci.database import DatabaseClient

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


class AutonomousDatabaseCharacterSetsFactsHelperGen(OCIResourceFactsHelperBase):
    """Supported operations: list"""

    def get_required_params_for_list(self):
        return []

    def list_resources(self):
        optional_list_method_params = [
            "is_shared",
            "character_set_type",
            "name",
        ]
        optional_kwargs = dict(
            (param, self.module.params[param])
            for param in optional_list_method_params
            if self.module.params.get(param) is not None
        )
        return oci_common_utils.list_all_resources(
            self.client.list_autonomous_database_character_sets, **optional_kwargs
        )


AutonomousDatabaseCharacterSetsFactsHelperCustom = get_custom_class(
    "AutonomousDatabaseCharacterSetsFactsHelperCustom"
)


class ResourceFactsHelper(
    AutonomousDatabaseCharacterSetsFactsHelperCustom,
    AutonomousDatabaseCharacterSetsFactsHelperGen,
):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec()
    module_args.update(
        dict(
            is_shared=dict(type="bool"),
            character_set_type=dict(type="str", choices=["DATABASE", "NATIONAL"]),
            name=dict(type="str"),
        )
    )

    module = OCIAnsibleModule(argument_spec=module_args)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_facts_helper = ResourceFactsHelper(
        module=module,
        resource_type="autonomous_database_character_sets",
        service_client_class=DatabaseClient,
        namespace="database",
    )

    result = []

    if resource_facts_helper.is_list():
        result = resource_facts_helper.list()
    else:
        resource_facts_helper.fail()

    module.exit_json(autonomous_database_character_sets=result)


if __name__ == "__main__":
    main()
