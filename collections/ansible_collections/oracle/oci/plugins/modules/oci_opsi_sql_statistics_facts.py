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
module: oci_opsi_sql_statistics_facts
description: >-
    Due to size constraints we have not included the documentation in the module. Please check L(here,
    https://docs.oracle.com/en-us/iaas/tools/oci-ansible-collection/latest/collections/oracle/oci/oci_opsi_sql_statistics_facts_module.html)
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
    from oci.opsi import OperationsInsightsClient

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


class SqlStatisticsFactsHelperGen(OCIResourceFactsHelperBase):
    """Supported operations: list"""

    def get_required_params_for_list(self):
        return [
            "compartment_id",
        ]

    def list_resources(self):
        optional_list_method_params = [
            "database_type",
            "database_id",
            "id",
            "exadata_insight_id",
            "cdb_name",
            "host_name",
            "database_time_pct_greater_than",
            "sql_identifier",
            "analysis_time_interval",
            "time_interval_start",
            "time_interval_end",
            "sort_order",
            "sort_by",
            "category",
            "defined_tag_equals",
            "freeform_tag_equals",
            "defined_tag_exists",
            "freeform_tag_exists",
            "compartment_id_in_subtree",
            "vmcluster_name",
        ]
        optional_kwargs = dict(
            (param, self.module.params[param])
            for param in optional_list_method_params
            if self.module.params.get(param) is not None
        )
        return oci_common_utils.list_all_resources(
            self.client.summarize_sql_statistics,
            compartment_id=self.module.params.get("compartment_id"),
            **optional_kwargs
        )


SqlStatisticsFactsHelperCustom = get_custom_class("SqlStatisticsFactsHelperCustom")


class ResourceFactsHelper(SqlStatisticsFactsHelperCustom, SqlStatisticsFactsHelperGen):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec()
    module_args.update(
        dict(
            compartment_id=dict(type="str", required=True),
            database_type=dict(
                type="list",
                elements="str",
                choices=[
                    "ADW-S",
                    "ATP-S",
                    "ADW-D",
                    "ATP-D",
                    "EXTERNAL-PDB",
                    "EXTERNAL-NONCDB",
                    "COMANAGED-VM-CDB",
                    "COMANAGED-VM-PDB",
                    "COMANAGED-VM-NONCDB",
                    "COMANAGED-BM-CDB",
                    "COMANAGED-BM-PDB",
                    "COMANAGED-BM-NONCDB",
                    "COMANAGED-EXACS-CDB",
                    "COMANAGED-EXACS-PDB",
                    "COMANAGED-EXACS-NONCDB",
                ],
            ),
            database_id=dict(type="list", elements="str"),
            id=dict(type="list", elements="str"),
            exadata_insight_id=dict(type="list", elements="str"),
            cdb_name=dict(type="list", elements="str"),
            host_name=dict(type="list", elements="str"),
            database_time_pct_greater_than=dict(type="float"),
            sql_identifier=dict(type="list", elements="str"),
            analysis_time_interval=dict(type="str"),
            time_interval_start=dict(type="str"),
            time_interval_end=dict(type="str"),
            sort_order=dict(type="str", choices=["ASC", "DESC"]),
            sort_by=dict(
                type="str",
                choices=[
                    "databaseTimeInSec",
                    "executionsPerHour",
                    "executionsCount",
                    "cpuTimeInSec",
                    "ioTimeInSec",
                    "inefficientWaitTimeInSec",
                    "responseTimeInSec",
                    "planCount",
                    "variability",
                    "averageActiveSessions",
                    "databaseTimePct",
                    "inefficiencyInPct",
                    "changeInCpuTimeInPct",
                    "changeInIoTimeInPct",
                    "changeInInefficientWaitTimeInPct",
                    "changeInResponseTimeInPct",
                    "changeInAverageActiveSessionsInPct",
                    "changeInExecutionsPerHourInPct",
                    "changeInInefficiencyInPct",
                ],
            ),
            category=dict(
                type="list",
                elements="str",
                choices=[
                    "DEGRADING",
                    "VARIANT",
                    "INEFFICIENT",
                    "CHANGING_PLANS",
                    "IMPROVING",
                    "DEGRADING_VARIANT",
                    "DEGRADING_INEFFICIENT",
                    "DEGRADING_CHANGING_PLANS",
                    "DEGRADING_INCREASING_IO",
                    "DEGRADING_INCREASING_CPU",
                    "DEGRADING_INCREASING_INEFFICIENT_WAIT",
                    "DEGRADING_CHANGING_PLANS_AND_INCREASING_IO",
                    "DEGRADING_CHANGING_PLANS_AND_INCREASING_CPU",
                    "DEGRADING_CHANGING_PLANS_AND_INCREASING_INEFFICIENT_WAIT",
                    "VARIANT_INEFFICIENT",
                    "VARIANT_CHANGING_PLANS",
                    "VARIANT_INCREASING_IO",
                    "VARIANT_INCREASING_CPU",
                    "VARIANT_INCREASING_INEFFICIENT_WAIT",
                    "VARIANT_CHANGING_PLANS_AND_INCREASING_IO",
                    "VARIANT_CHANGING_PLANS_AND_INCREASING_CPU",
                    "VARIANT_CHANGING_PLANS_AND_INCREASING_INEFFICIENT_WAIT",
                    "INEFFICIENT_CHANGING_PLANS",
                    "INEFFICIENT_INCREASING_INEFFICIENT_WAIT",
                    "INEFFICIENT_CHANGING_PLANS_AND_INCREASING_INEFFICIENT_WAIT",
                ],
            ),
            defined_tag_equals=dict(type="list", elements="str"),
            freeform_tag_equals=dict(type="list", elements="str"),
            defined_tag_exists=dict(type="list", elements="str"),
            freeform_tag_exists=dict(type="list", elements="str"),
            compartment_id_in_subtree=dict(type="bool"),
            vmcluster_name=dict(type="list", elements="str"),
        )
    )

    module = OCIAnsibleModule(argument_spec=module_args)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_facts_helper = ResourceFactsHelper(
        module=module,
        resource_type="sql_statistics",
        service_client_class=OperationsInsightsClient,
        namespace="opsi",
    )

    result = []

    if resource_facts_helper.is_list():
        result = resource_facts_helper.list()
    else:
        resource_facts_helper.fail()

    module.exit_json(sql_statistics=result)


if __name__ == "__main__":
    main()
