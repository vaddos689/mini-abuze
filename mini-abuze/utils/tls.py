import tls_client
import tls_client.sessions
from random import choice


def get_session(self, headers: dict) -> tls_client.sessions.Session:
    session = tls_client.Session(client_identifier=choice(['chrome_103',
                                                           'chrome_104',
                                                           'chrome_105',
                                                           'chrome_106',
                                                           'chrome_107',
                                                           'chrome_108',
                                                           'chrome109',
                                                           'Chrome110',
                                                           'chrome111',
                                                           'chrome112',
                                                           'firefox_102',
                                                           'firefox_104',
                                                           'firefox108',
                                                           'Firefox110',
                                                           'opera_89',
                                                           'opera_90']),
                                 random_tls_extension_order=True)
    session.headers.update(headers)

    return session
