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
module: oci_cims_incident
description: >-
    Due to size constraints we have not included the documentation in the module. Please check L(here,
    https://docs.oracle.com/en-us/iaas/tools/oci-ansible-collection/latest/collections/oracle/oci/oci_cims_incident_module.html)
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
    from oci.cims import IncidentClient
    from oci.cims.models import CreateIncident
    from oci.cims.models import UpdateIncident

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


class IncidentHelperGen(OCIResourceHelperBase):
    """Supported operations: create, update, get and list"""

    def get_possible_entity_types(self):
        return super(IncidentHelperGen, self).get_possible_entity_types() + [
            "incident",
            "incidents",
            "cimsincident",
            "cimsincidents",
            "incidentresource",
            "incidentsresource",
            "cims",
        ]

    def get_module_resource_id_param(self):
        return "incident_key"

    def get_module_resource_id(self):
        return self.module.params.get("incident_key")

    def get_get_fn(self):
        return self.client.get_incident

    def get_resource(self):
        optional_params = [
            "homeregion",
            "problem_type",
        ]
        optional_kwargs = dict(
            (param, self.module.params[param])
            for param in optional_params
            if self.module.params.get(param) is not None
        )
        return oci_common_utils.call_with_backoff(
            self.client.get_incident,
            incident_key=self.module.params.get("incident_key"),
            csi=self.module.params.get("csi"),
            ocid=self.module.params.get("ocid"),
            **optional_kwargs
        )

    def get_required_kwargs_for_list(self):
        required_list_method_params = [
            "csi",
            "compartment_id",
            "ocid",
        ]

        return dict(
            (param, self.module.params[param]) for param in required_list_method_params
        )

    def get_optional_kwargs_for_list(self):
        optional_list_method_params = ["homeregion", "problem_type"]

        return dict(
            (param, self.module.params[param])
            for param in optional_list_method_params
            if self.module.params.get(param) is not None
            and (
                self._use_name_as_identifier()
                or (
                    not self.module.params.get("key_by")
                    or param in self.module.params.get("key_by")
                )
            )
        )

    def list_resources(self):

        required_kwargs = self.get_required_kwargs_for_list()
        optional_kwargs = self.get_optional_kwargs_for_list()
        kwargs = oci_common_utils.merge_dicts(required_kwargs, optional_kwargs)
        return oci_common_utils.list_all_resources(self.client.list_incidents, **kwargs)

    def get_create_model_class(self):
        return CreateIncident

    def get_exclude_attributes(self):
        return ["ticket.contextual_data", "csi", "contacts"]

    def create_resource(self):
        create_details = self.get_create_model()
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.create_incident,
            call_fn_args=(),
            call_fn_kwargs=dict(
                create_incident_details=create_details,
                ocid=self.module.params.get("ocid"),
                homeregion=self.module.params.get("homeregion"),
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
        return UpdateIncident

    def update_resource(self):
        update_details = self.get_update_model()
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.update_incident,
            call_fn_args=(),
            call_fn_kwargs=dict(
                incident_key=self.module.params.get("incident_key"),
                csi=self.module.params.get("csi"),
                update_incident_details=update_details,
                ocid=self.module.params.get("ocid"),
                homeregion=self.module.params.get("homeregion"),
            ),
            waiter_type=oci_wait_utils.NONE_WAITER_KEY,
            operation=oci_common_utils.UPDATE_OPERATION_KEY,
            waiter_client=self.get_waiter_client(),
            resource_helper=self,
            wait_for_states=self.get_wait_for_states_for_operation(
                oci_common_utils.UPDATE_OPERATION_KEY,
            ),
        )


IncidentHelperCustom = get_custom_class("IncidentHelperCustom")


class ResourceHelper(IncidentHelperCustom, IncidentHelperGen):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec(
        supports_create=True, supports_wait=False
    )
    module_args.update(
        dict(
            compartment_id=dict(type="str"),
            problem_type=dict(
                type="str", choices=["LIMIT", "LEGACY_LIMIT", "TECH", "ACCOUNT"]
            ),
            contacts=dict(
                type="list",
                elements="dict",
                options=dict(
                    contact_name=dict(type="str"),
                    contact_email=dict(type="str"),
                    contact_phone=dict(type="str"),
                    contact_type=dict(
                        type="str",
                        choices=[
                            "PRIMARY",
                            "ALTERNATE",
                            "SECONDARY",
                            "ADMIN",
                            "MANAGER",
                        ],
                    ),
                ),
            ),
            referrer=dict(type="str"),
            incident_key=dict(type="str", no_log=True),
            csi=dict(type="str"),
            ticket=dict(
                type="dict",
                required=True,
                options=dict(
                    severity=dict(type="str", choices=["HIGHEST", "HIGH", "MEDIUM"]),
                    resource_list=dict(
                        type="list",
                        elements="dict",
                        options=dict(
                            item=dict(
                                type="dict",
                                options=dict(
                                    type=dict(
                                        type="str",
                                        required=True,
                                        choices=["tech", "limit"],
                                    ),
                                    category=dict(
                                        type="dict",
                                        options=dict(
                                            category_key=dict(type="str", no_log=True)
                                        ),
                                    ),
                                    sub_category=dict(
                                        type="dict",
                                        options=dict(
                                            sub_category_key=dict(
                                                type="str", no_log=True
                                            )
                                        ),
                                    ),
                                    issue_type=dict(
                                        type="dict",
                                        options=dict(
                                            issue_type_key=dict(type="str", no_log=True)
                                        ),
                                    ),
                                    name=dict(type="str"),
                                    current_limit=dict(type="int"),
                                    current_usage=dict(type="int"),
                                    requested_limit=dict(type="int"),
                                    limit_status=dict(
                                        type="str",
                                        choices=[
                                            "APPROVED",
                                            "PARTIALLY_APPROVED",
                                            "NOT_APPROVED",
                                        ],
                                    ),
                                ),
                            ),
                            region=dict(
                                type="str",
                                choices=[
                                    "DEV",
                                    "SEA",
                                    "INTEG_NEXT",
                                    "INTEG_STABLE",
                                    "PHX",
                                    "IAD",
                                    "FRA",
                                    "EU_FRANKFURT_1",
                                    "LHR",
                                    "YYZ",
                                    "NRT",
                                    "ICN",
                                    "BOM",
                                    "GRU",
                                    "SYD",
                                    "ZRH",
                                    "JED",
                                    "AMS",
                                    "KIX",
                                    "MEL",
                                    "YUL",
                                    "HYD",
                                    "YNY",
                                ],
                            ),
                            availability_domain=dict(
                                type="str",
                                choices=[
                                    "DEV_1",
                                    "DEV_2",
                                    "DEV_3",
                                    "INTEG_NEXT_1",
                                    "INTEG_STABLE_1",
                                    "SEA_AD_1",
                                    "SEA_AD_2",
                                    "SEA_AD_3",
                                    "PHX_AD_1",
                                    "PHX_AD_2",
                                    "PHX_AD_3",
                                    "US_ASHBURN_AD_1",
                                    "US_ASHBURN_AD_2",
                                    "US_ASHBURN_AD_3",
                                    "US_ASHBURN_AD_4",
                                    "EU_FRANKFURT_1_AD_1",
                                    "EU_FRANKFURT_1_AD_2",
                                    "EU_FRANKFURT_1_AD_3",
                                    "UK_LONDON_1_AD_1",
                                    "UK_LONDON_1_AD_2",
                                    "UK_LONDON_1_AD_3",
                                    "CA_TORONTO_1_AD_1",
                                    "AP_TOKYO_1_AD_1",
                                    "AP_SEOUL_1_AD_1",
                                    "AP_MUMBAI_1_AD_1",
                                    "SA_SAOPAULO_1_AD_1",
                                    "ME_JEDDAH_1_AD_1",
                                    "AP_OSAKA_1_AD_1",
                                    "AP_SYDNEY_1_AD_1",
                                    "EU_ZURICH_1_AD_1",
                                    "EU_AMSTERDAM_1_AD_1",
                                    "AP_MELBOURNE_1_AD_1",
                                    "CA_MONTREAL_1_AD_1",
                                    "AP_HYDERABAD_1_AD_1",
                                    "AP_CHUNCHEON_1_AD_1",
                                    "NO_AD",
                                ],
                            ),
                        ),
                    ),
                    title=dict(type="str"),
                    description=dict(type="str"),
                    contextual_data=dict(
                        type="dict",
                        options=dict(
                            client_id=dict(type="str", required=True),
                            schema_name=dict(type="str", required=True),
                            schema_version=dict(type="str", required=True),
                            payload=dict(type="str", required=True),
                        ),
                    ),
                    resource=dict(type="dict"),
                ),
            ),
            ocid=dict(type="str", required=True),
            homeregion=dict(type="str"),
            state=dict(type="str", default="present", choices=["present"]),
        )
    )

    module = OCIAnsibleModule(argument_spec=module_args, supports_check_mode=True)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_helper = ResourceHelper(
        module=module,
        resource_type="incident",
        service_client_class=IncidentClient,
        namespace="cims",
    )

    result = dict(changed=False)

    if resource_helper.is_update():
        result = resource_helper.update()
    elif resource_helper.is_create():
        result = resource_helper.create()

    module.exit_json(**result)


if __name__ == "__main__":
    main()
