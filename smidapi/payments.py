class PaymentGateway:
    def pay(self, provider, amount, **kwargs):
        if provider == 'alipay':
            return self._alipay(amount, **kwargs)
        if provider == 'wechat':
            return self._wechat(amount, **kwargs)
        if provider == 'kakaopay':
            return self._kakaopay(amount, **kwargs)
        raise ValueError('Unsupported provider')

    def _alipay(self, amount, **kwargs):
        # integrate with Alipay SDK here
        return {'provider': 'alipay', 'amount': amount, 'status': 'success'}

    def _wechat(self, amount, **kwargs):
        # integrate with WeChat Pay SDK here
        return {'provider': 'wechat', 'amount': amount, 'status': 'success'}

    def _kakaopay(self, amount, **kwargs):
        # integrate with KakaoPay SDK here
        return {'provider': 'kakaopay', 'amount': amount, 'status': 'success'}
