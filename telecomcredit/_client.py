from __future__ import annotations

from types import MethodType

from telecomcredit._credit_card import get_order_url, post_order
from telecomcredit._webhook import received_result


class TelecomCreditClient:
    _base_url: str = "https://secure.telecomcredit.co.jp/inetcredit/secure/order.pl"
    _clientip: str

    def __init__(self, *, clientip: str) -> None:
        self._clientip = clientip

        # 都度決済
        self.get_order_url = MethodType(get_order_url, self)
        self.post_order = MethodType(post_order, self)

        # 決済結果
        self.received_result = MethodType(received_result, self)
