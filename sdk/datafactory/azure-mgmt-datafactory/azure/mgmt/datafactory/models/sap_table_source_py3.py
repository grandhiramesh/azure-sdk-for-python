# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
#
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from .copy_source_py3 import CopySource


class SapTableSource(CopySource):
    """A copy activity source for SAP Table source.

    All required parameters must be populated in order to send to Azure.

    :param additional_properties: Unmatched properties from the message are
     deserialized this collection
    :type additional_properties: dict[str, object]
    :param source_retry_count: Source retry count. Type: integer (or
     Expression with resultType integer).
    :type source_retry_count: object
    :param source_retry_wait: Source retry wait. Type: string (or Expression
     with resultType string), pattern:
     ((\\d+)\\.)?(\\d\\d):(60|([0-5][0-9])):(60|([0-5][0-9])).
    :type source_retry_wait: object
    :param max_concurrent_connections: The maximum concurrent connection count
     for the source data store. Type: integer (or Expression with resultType
     integer).
    :type max_concurrent_connections: object
    :param type: Required. Constant filled by server.
    :type type: str
    :param row_count: The number of rows to be retrieved. Type: integer(or
     Expression with resultType integer).
    :type row_count: object
    :param row_skips: The number of rows that will be skipped. Type: integer
     (or Expression with resultType integer).
    :type row_skips: object
    :param rfc_table_fields: The fields of the SAP table that will be
     retrieved. For example, column0, column1. Type: string (or Expression with
     resultType string).
    :type rfc_table_fields: object
    :param rfc_table_options: The options for the filtering of the SAP Table.
     For example, COLUMN0 EQ SOME VALUE. Type: string (or Expression with
     resultType string).
    :type rfc_table_options: object
    :param batch_size: Specifies the maximum number of rows that will be
     retrieved at a time when retrieving data from SAP Table. Type: integer (or
     Expression with resultType integer).
    :type batch_size: object
    :param custom_rfc_read_table_function_module: Specifies the custom RFC
     function module that will be used to read data from SAP Table. Type:
     string (or Expression with resultType string).
    :type custom_rfc_read_table_function_module: object
    :param partition_option: The partition mechanism that will be used for SAP
     table read in parallel.
    :type partition_option: object
    :param partition_settings: The settings that will be leveraged for SAP
     table source partitioning.
    :type partition_settings:
     ~azure.mgmt.datafactory.models.SapTablePartitionSettings
    """

    _validation = {
        'type': {'required': True},
    }

    _attribute_map = {
        'additional_properties': {'key': '', 'type': '{object}'},
        'source_retry_count': {'key': 'sourceRetryCount', 'type': 'object'},
        'source_retry_wait': {'key': 'sourceRetryWait', 'type': 'object'},
        'max_concurrent_connections': {'key': 'maxConcurrentConnections', 'type': 'object'},
        'type': {'key': 'type', 'type': 'str'},
        'row_count': {'key': 'rowCount', 'type': 'object'},
        'row_skips': {'key': 'rowSkips', 'type': 'object'},
        'rfc_table_fields': {'key': 'rfcTableFields', 'type': 'object'},
        'rfc_table_options': {'key': 'rfcTableOptions', 'type': 'object'},
        'batch_size': {'key': 'batchSize', 'type': 'object'},
        'custom_rfc_read_table_function_module': {'key': 'customRfcReadTableFunctionModule', 'type': 'object'},
        'partition_option': {'key': 'partitionOption', 'type': 'object'},
        'partition_settings': {'key': 'partitionSettings', 'type': 'SapTablePartitionSettings'},
    }

    def __init__(self, *, additional_properties=None, source_retry_count=None, source_retry_wait=None, max_concurrent_connections=None, row_count=None, row_skips=None, rfc_table_fields=None, rfc_table_options=None, batch_size=None, custom_rfc_read_table_function_module=None, partition_option=None, partition_settings=None, **kwargs) -> None:
        super(SapTableSource, self).__init__(additional_properties=additional_properties, source_retry_count=source_retry_count, source_retry_wait=source_retry_wait, max_concurrent_connections=max_concurrent_connections, **kwargs)
        self.row_count = row_count
        self.row_skips = row_skips
        self.rfc_table_fields = rfc_table_fields
        self.rfc_table_options = rfc_table_options
        self.batch_size = batch_size
        self.custom_rfc_read_table_function_module = custom_rfc_read_table_function_module
        self.partition_option = partition_option
        self.partition_settings = partition_settings
        self.type = 'SapTableSource'
