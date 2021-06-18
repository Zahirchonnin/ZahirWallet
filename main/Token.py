class ERC20Token:
    def __init__(self, w3, contract):
        self.w3 = w3
        self.contract = contract
        self.name = self.contract.functions.name().call()
        self.symbol = self.contract.functions.symbol().call()
        self.decimals = self.contract.functions.decimals().call()
        self.totalSupply = f"{self.w3.fromWei(self.contract.functions.totalSupply().call(), 'ether')} {self.symbol}"
        self.methods = {
            'totalSupply': self.totalSupply,
            'transfer': self.transfer,
            'transferFrom': self.transferFrom,
            'approve': self.approve,
            'balanceOf': self.balanceOf,
            'allowance': self.allowance
        }
    
    def makeTXN(self, private_key, txn):

        signed_txn = self.w3.eth.account.signTransaction(txn, private_key=private_key)

        signed_txn_hash = self.w3.eth.sendRawTransaction(signed_txn.rawTransaction)

        self.w3.eth.waitForTransactionReceipt(signed_txn_hash)

        return txn
    
    def transfer(self, _, _to, _value, _from, prvKey):
        nonce = self.w3.eth.getTransactionCount(_from)
        
        try:
            tx = self.contract.functions.transfer(_to, _value).buildTransaction(
                {
                'from': _from,
                'nonce': nonce
                }
            )
            self.makeTXN(prvKey, tx)
            return "Transaction succeeded!"
        
        except :
            return "Insufficient balance!"

    def transferFrom(self, _owner, _to, _value, _from, prvKey):
        nonce = self.w3.eth.getTransactionCount(_from)
        try:
            tx = self.contract.functions.transferFrom(
                _owner, _to, _value
            ).buildTransaction(
                {'from': _from, 'nonce': nonce}
            )
            self.makeTXN(prvKey, tx)
            return "Transaction succeeded!"
        except :
            return "Insufficient balance!"

    def approve(self, *args):
        _spender, _, _value, _from, prvKey = args
        nonce = self.w3.eth.getTransactionCount(_from)
        tx = self.contract.functions.approve(_spender, _value).buildTransaction(
                {'from': _from, 'nonce': nonce}
            )
        self.makeTXN(prvKey, tx)
        return "Transaction succeeded!"

    def balanceOf(self, *args):
        _owner = args[0]
        balance = self.w3.fromWei(self.contract.functions.balanceOf(_owner).call(), 'ether')
        return f"{balance} {self.symbol}"
    
    def allowance(self, *args):
        _owner, _spender = args[:2]
        return self.contract.functions.allowance(_owner, _spender).call()
    
    def excuteMethod(self, method, _owner, _to, _value, _from, prvKey):
        if method == 'totalSupply': return self.methods[method]
        return self.methods[method](
            _owner, _to, self.w3.toWei(_value, 'ether'), 
            _from, prvKey
            )