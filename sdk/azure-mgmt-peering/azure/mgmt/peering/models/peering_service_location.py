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

from .resource import Resource


class PeeringServiceLocation(Resource):
    """PeeringService location.

    Variables are only populated by the server, and will be ignored when
    sending a request.

    :ivar name: The name of the resource.
    :vartype name: str
    :ivar id: The ID of the resource.
    :vartype id: str
    :ivar type: The type of the resource.
    :vartype type: str
    :param country: Country of the customer
    :type country: str
    :param state: State of the customer
    :type state: str
    :param azure_region: Azure region for the location
    :type azure_region: str
    """

    _validation = {
        'name': {'readonly': True},
        'id': {'readonly': True},
        'type': {'readonly': True},
    }

    _attribute_map = {
        'name': {'key': 'name', 'type': 'str'},
        'id': {'key': 'id', 'type': 'str'},
        'type': {'key': 'type', 'type': 'str'},
        'country': {'key': 'properties.country', 'type': 'str'},
        'state': {'key': 'properties.state', 'type': 'str'},
        'azure_region': {'key': 'properties.azureRegion', 'type': 'str'},
    }

    def __init__(self, **kwargs):
        super(PeeringServiceLocation, self).__init__(**kwargs)
        self.country = kwargs.get('country', None)
        self.state = kwargs.get('state', None)
        self.azure_region = kwargs.get('azure_region', None)