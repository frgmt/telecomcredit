from __future__ import annotations

from urllib.parse import urlencode

from requests_mock import POST, Mocker

from telecomcredit import TelecomCreditClient
from tests.conftest import _BASE_URL, _CLIENTIP

_REQUEST_DATA = {
    "clientip": _CLIENTIP,
    "money": 10000,
    "sendid": "telecom",
    "additional_param": "test",
}


def test_get_order_url(client: TelecomCreditClient) -> None:
    url = client.get_order_url(money=10000, sendid="telecom", additional_param="test")
    assert url == f"{_BASE_URL}?{urlencode(_REQUEST_DATA)}"


def test_post_order(requests_mock: Mocker, client: TelecomCreditClient) -> None:
    requests_mock.post(_BASE_URL, text=urlencode(_REQUEST_DATA))
    client.post_order(money=10000, sendid="telecom", additional_param="test")

    assert (
        requests_mock.call_count,
        requests_mock.request_history[0].method,
        requests_mock.request_history[0].url,
        requests_mock.request_history[0].text,
    ) == (1, POST, _BASE_URL, urlencode(_REQUEST_DATA))
