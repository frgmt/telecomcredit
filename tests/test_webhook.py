from __future__ import annotations

from uuid import UUID

from telecomcredit import ContEnum, RelEnum, Result, TelecomCreditClient
from tests.conftest import _CLIENTIP

_REQUEST_DATA = {
    "clientip": _CLIENTIP,
    "money": 10000,
    "telno": "09012345678",
    "email": "test@test.com",
    "username": "TARO YAMADA",
    "rel": "yes",
    "cont": "no",
    "settle_uuid": "6ba7b810-9dad-11d1-80b4-00c04fd430c8",
    "option": "account_number",
}


def test_received_result(client: TelecomCreditClient) -> None:
    model: Result = client.received_result(**_REQUEST_DATA)
    assert (
        client._clientip,  # noqa: SLF001
        model.money,
        model.telno,
        model.email,
        model.username,
        model.rel,
        model.cont,
        model.settle_uuid,
        model.option,
    ) == (
        _REQUEST_DATA["clientip"],
        _REQUEST_DATA["money"],
        _REQUEST_DATA["telno"],
        _REQUEST_DATA["email"],
        _REQUEST_DATA["username"],
        RelEnum.YES,
        ContEnum.NO,
        UUID(_REQUEST_DATA["settle_uuid"]),
        _REQUEST_DATA["option"],
    )
