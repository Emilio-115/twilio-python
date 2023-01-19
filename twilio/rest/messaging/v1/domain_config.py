# coding=utf-8
r"""
This code was generated by
\ / _    _  _|   _  _
 | (_)\/(_)(_|\/| |(/_  v1.0.0
      /       /
"""

from twilio.base import deserialize
from twilio.base import serialize
from twilio.base import values
from twilio.base.instance_context import InstanceContext
from twilio.base.instance_resource import InstanceResource
from twilio.base.list_resource import ListResource
from twilio.base.page import Page


class DomainConfigList(ListResource):
    """ PLEASE NOTE that this class contains beta products that are subject to
    change. Use them with caution. """

    def __init__(self, version):
        """
        Initialize the DomainConfigList

        :param Version version: Version that contains the resource

        :returns: twilio.rest.messaging.v1.domain_config.DomainConfigList
        :rtype: twilio.rest.messaging.v1.domain_config.DomainConfigList
        """
        super(DomainConfigList, self).__init__(version)

        # Path Solution
        self._solution = {}

    def get(self, domain_sid):
        """
        Constructs a DomainConfigContext

        :param domain_sid: Unique string used to identify the domain that this config should be associated with.

        :returns: twilio.rest.messaging.v1.domain_config.DomainConfigContext
        :rtype: twilio.rest.messaging.v1.domain_config.DomainConfigContext
        """
        return DomainConfigContext(self._version, domain_sid=domain_sid, )

    def __call__(self, domain_sid):
        """
        Constructs a DomainConfigContext

        :param domain_sid: Unique string used to identify the domain that this config should be associated with.

        :returns: twilio.rest.messaging.v1.domain_config.DomainConfigContext
        :rtype: twilio.rest.messaging.v1.domain_config.DomainConfigContext
        """
        return DomainConfigContext(self._version, domain_sid=domain_sid, )

    def __repr__(self):
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        :rtype: str
        """
        return '<Twilio.Messaging.V1.DomainConfigList>'


class DomainConfigPage(Page):
    """ PLEASE NOTE that this class contains beta products that are subject to
    change. Use them with caution. """

    def __init__(self, version, response, solution):
        """
        Initialize the DomainConfigPage

        :param Version version: Version that contains the resource
        :param Response response: Response from the API

        :returns: twilio.rest.messaging.v1.domain_config.DomainConfigPage
        :rtype: twilio.rest.messaging.v1.domain_config.DomainConfigPage
        """
        super(DomainConfigPage, self).__init__(version, response)

        # Path Solution
        self._solution = solution

    def get_instance(self, payload):
        """
        Build an instance of DomainConfigInstance

        :param dict payload: Payload response from the API

        :returns: twilio.rest.messaging.v1.domain_config.DomainConfigInstance
        :rtype: twilio.rest.messaging.v1.domain_config.DomainConfigInstance
        """
        return DomainConfigInstance(self._version, payload, )

    def __repr__(self):
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        :rtype: str
        """
        return '<Twilio.Messaging.V1.DomainConfigPage>'


class DomainConfigContext(InstanceContext):
    """ PLEASE NOTE that this class contains beta products that are subject to
    change. Use them with caution. """

    def __init__(self, version, domain_sid):
        """
        Initialize the DomainConfigContext

        :param Version version: Version that contains the resource
        :param domain_sid: Unique string used to identify the domain that this config should be associated with.

        :returns: twilio.rest.messaging.v1.domain_config.DomainConfigContext
        :rtype: twilio.rest.messaging.v1.domain_config.DomainConfigContext
        """
        super(DomainConfigContext, self).__init__(version)

        # Path Solution
        self._solution = {'domain_sid': domain_sid, }
        self._uri = '/LinkShortening/Domains/{domain_sid}/Config'.format(**self._solution)

    def update(self, messaging_service_sids, fallback_url=values.unset,
               callback_url=values.unset,
               messaging_service_sids_action=values.unset):
        """
        Update the DomainConfigInstance

        :param list[unicode] messaging_service_sids: A list of messagingServiceSids (with prefix MG)
        :param unicode fallback_url: We will redirect requests to urls we are unable to identify to this url.
        :param unicode callback_url: URL to receive click events to your webhook whenever the recipients click on the shortened links
        :param unicode messaging_service_sids_action: An action type for messaging_service_sids operation (ADD, DELETE, REPLACE)

        :returns: The updated DomainConfigInstance
        :rtype: twilio.rest.messaging.v1.domain_config.DomainConfigInstance
        """
        data = values.of({
            'MessagingServiceSids': serialize.map(messaging_service_sids, lambda e: e),
            'FallbackUrl': fallback_url,
            'CallbackUrl': callback_url,
            'MessagingServiceSidsAction': messaging_service_sids_action,
        })

        payload = self._version.update(method='POST', uri=self._uri, data=data, )

        return DomainConfigInstance(self._version, payload, domain_sid=self._solution['domain_sid'], )

    def fetch(self):
        """
        Fetch the DomainConfigInstance

        :returns: The fetched DomainConfigInstance
        :rtype: twilio.rest.messaging.v1.domain_config.DomainConfigInstance
        """
        payload = self._version.fetch(method='GET', uri=self._uri, )

        return DomainConfigInstance(self._version, payload, domain_sid=self._solution['domain_sid'], )

    def __repr__(self):
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        :rtype: str
        """
        context = ' '.join('{}={}'.format(k, v) for k, v in self._solution.items())
        return '<Twilio.Messaging.V1.DomainConfigContext {}>'.format(context)


class DomainConfigInstance(InstanceResource):
    """ PLEASE NOTE that this class contains beta products that are subject to
    change. Use them with caution. """

    def __init__(self, version, payload, domain_sid=None):
        """
        Initialize the DomainConfigInstance

        :returns: twilio.rest.messaging.v1.domain_config.DomainConfigInstance
        :rtype: twilio.rest.messaging.v1.domain_config.DomainConfigInstance
        """
        super(DomainConfigInstance, self).__init__(version)

        # Marshaled Properties
        self._properties = {
            'domain_sid': payload.get('domain_sid'),
            'config_sid': payload.get('config_sid'),
            'messaging_service_sids': payload.get('messaging_service_sids'),
            'fallback_url': payload.get('fallback_url'),
            'callback_url': payload.get('callback_url'),
            'date_created': deserialize.iso8601_datetime(payload.get('date_created')),
            'date_updated': deserialize.iso8601_datetime(payload.get('date_updated')),
            'url': payload.get('url'),
        }

        # Context
        self._context = None
        self._solution = {'domain_sid': domain_sid or self._properties['domain_sid'], }

    @property
    def _proxy(self):
        """
        Generate an instance context for the instance, the context is capable of
        performing various actions.  All instance actions are proxied to the context

        :returns: DomainConfigContext for this DomainConfigInstance
        :rtype: twilio.rest.messaging.v1.domain_config.DomainConfigContext
        """
        if self._context is None:
            self._context = DomainConfigContext(self._version, domain_sid=self._solution['domain_sid'], )
        return self._context

    @property
    def domain_sid(self):
        """
        :returns: The unique string that we created to identify the Domain resource.
        :rtype: unicode
        """
        return self._properties['domain_sid']

    @property
    def config_sid(self):
        """
        :returns: The unique string that we created to identify the Domain config (prefix ZK).
        :rtype: unicode
        """
        return self._properties['config_sid']

    @property
    def messaging_service_sids(self):
        """
        :returns: A list of messagingServiceSids (with prefix MG).
        :rtype: list[unicode]
        """
        return self._properties['messaging_service_sids']

    @property
    def fallback_url(self):
        """
        :returns: We will redirect requests to urls we are unable to identify to this url.
        :rtype: unicode
        """
        return self._properties['fallback_url']

    @property
    def callback_url(self):
        """
        :returns: URL to receive click events to your webhook whenever the recipients click on the shortened links.
        :rtype: unicode
        """
        return self._properties['callback_url']

    @property
    def date_created(self):
        """
        :returns: Date this Domain Config was created.
        :rtype: datetime
        """
        return self._properties['date_created']

    @property
    def date_updated(self):
        """
        :returns: Date that this Domain Config was last updated.
        :rtype: datetime
        """
        return self._properties['date_updated']

    @property
    def url(self):
        """
        :returns: The url
        :rtype: unicode
        """
        return self._properties['url']

    def update(self, messaging_service_sids, fallback_url=values.unset,
               callback_url=values.unset,
               messaging_service_sids_action=values.unset):
        """
        Update the DomainConfigInstance

        :param list[unicode] messaging_service_sids: A list of messagingServiceSids (with prefix MG)
        :param unicode fallback_url: We will redirect requests to urls we are unable to identify to this url.
        :param unicode callback_url: URL to receive click events to your webhook whenever the recipients click on the shortened links
        :param unicode messaging_service_sids_action: An action type for messaging_service_sids operation (ADD, DELETE, REPLACE)

        :returns: The updated DomainConfigInstance
        :rtype: twilio.rest.messaging.v1.domain_config.DomainConfigInstance
        """
        return self._proxy.update(
            messaging_service_sids,
            fallback_url=fallback_url,
            callback_url=callback_url,
            messaging_service_sids_action=messaging_service_sids_action,
        )

    def fetch(self):
        """
        Fetch the DomainConfigInstance

        :returns: The fetched DomainConfigInstance
        :rtype: twilio.rest.messaging.v1.domain_config.DomainConfigInstance
        """
        return self._proxy.fetch()

    def __repr__(self):
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        :rtype: str
        """
        context = ' '.join('{}={}'.format(k, v) for k, v in self._solution.items())
        return '<Twilio.Messaging.V1.DomainConfigInstance {}>'.format(context)