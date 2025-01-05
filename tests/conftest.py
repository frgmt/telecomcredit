from __future__ import annotations

import pytest

from telecomcredit import TelecomCreditClient

_BASE_URL = "https://secure.telecomcredit.co.jp/inetcredit/secure/order.pl"
_CLIENTIP = "12345"


@pytest.fixture
def client() -> TelecomCreditClient:
    return TelecomCreditClient(clientip=_CLIENTIP)
