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

from .resource_py3 import Resource


class DiagnosticContract(Resource):
    """Diagnostic details.

    Variables are only populated by the server, and will be ignored when
    sending a request.

    All required parameters must be populated in order to send to Azure.

    :ivar id: Resource ID.
    :vartype id: str
    :ivar name: Resource name.
    :vartype name: str
    :ivar type: Resource type for API Management resource.
    :vartype type: str
    :param always_log: Specifies for what type of messages sampling settings
     should not apply. Possible values include: 'allErrors'
    :type always_log: str or ~azure.mgmt.apimanagement.models.AlwaysLog
    :param logger_id: Required. Resource Id of a target logger.
    :type logger_id: str
    :param sampling: Sampling settings for Diagnostic.
    :type sampling: ~azure.mgmt.apimanagement.models.SamplingSettings
    :param frontend: Diagnostic settings for incoming/outgoing HTTP messages
     to the Gateway.
    :type frontend:
     ~azure.mgmt.apimanagement.models.PipelineDiagnosticSettings
    :param backend: Diagnostic settings for incoming/outgoing HTTP messages to
     the Backend
    :type backend: ~azure.mgmt.apimanagement.models.PipelineDiagnosticSettings
    :param enable_http_correlation_headers: Whether to process Correlation
     Headers coming to Api Management Service. Only applicable to Application
     Insights diagnostics. Default is true.
    :type enable_http_correlation_headers: bool
    :param http_correlation_protocol: Sets correlation protocol to use for
     Application Insights diagnostics. Possible values include: 'None',
     'Legacy', 'W3C'
    :type http_correlation_protocol: str or
     ~azure.mgmt.apimanagement.models.HttpCorrelationProtocol
    """

    _validation = {
        'id': {'readonly': True},
        'name': {'readonly': True},
        'type': {'readonly': True},
        'logger_id': {'required': True},
    }

    _attribute_map = {
        'id': {'key': 'id', 'type': 'str'},
        'name': {'key': 'name', 'type': 'str'},
        'type': {'key': 'type', 'type': 'str'},
        'always_log': {'key': 'properties.alwaysLog', 'type': 'str'},
        'logger_id': {'key': 'properties.loggerId', 'type': 'str'},
        'sampling': {'key': 'properties.sampling', 'type': 'SamplingSettings'},
        'frontend': {'key': 'properties.frontend', 'type': 'PipelineDiagnosticSettings'},
        'backend': {'key': 'properties.backend', 'type': 'PipelineDiagnosticSettings'},
        'enable_http_correlation_headers': {'key': 'properties.enableHttpCorrelationHeaders', 'type': 'bool'},
        'http_correlation_protocol': {'key': 'properties.httpCorrelationProtocol', 'type': 'str'},
    }

    def __init__(self, *, logger_id: str, always_log=None, sampling=None, frontend=None, backend=None, enable_http_correlation_headers: bool=None, http_correlation_protocol=None, **kwargs) -> None:
        super(DiagnosticContract, self).__init__(**kwargs)
        self.always_log = always_log
        self.logger_id = logger_id
        self.sampling = sampling
        self.frontend = frontend
        self.backend = backend
        self.enable_http_correlation_headers = enable_http_correlation_headers
        self.http_correlation_protocol = http_correlation_protocol
