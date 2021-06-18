from PyQt5 import QtCore, QtGui, QtWidgets
from main.RestoreVault import RestoreVault
from main.addToken import AddToken
from main.titleBar import titleBar
from main.Token import ERC20Token
from main._import import _Import
from main.Excutor import Excutor
from main.singUp import SingUp
from main.mainGUI import Main
from main.logIn import LogIn
from main.Seed import Seed
from hashlib import sha256
from main.send import Send
from pyperclip import copy
from random import choice
from main import tools
from web3 import Web3
from time import sleep
from datetime import datetime
import json
import os



class Worker(QtCore.QThread):
    result = QtCore.pyqtSignal(str, str)
    def __init__(self, mode, w3=None, path=[], name=None, password=None, restoreData=[]):
        super().__init__()
        self.mode = mode
        if not self.mode in ('copy', 'restore'):
            self.path = path or [f'./keystore/{_name}.json' for _name in name]
            self.name = name
            self.password = password
            self.w3 = w3
        elif self.mode == 'restore':
            self.w3 = w3
            self.restoreData = restoreData
    
    def run(self):
        if self.mode == 'copy':
            sleep(0.3)

        elif self.mode == 'getPrv':
            for path, name in zip(self.path, self.name):
                with open(path) as f:
                    keystore = json.loads(f.read())
                    try: 
                        prvKey = self.w3.eth.account.decrypt(keystore, self.password).hex()
                        self.result.emit(
                            prvKey,
                            name
                        )
                    except :
                        self.result.emit(
                            'Error',
                            'Invalid Password!'
                        )
        
        elif self.mode in ('save', 'load'):
            keystore = self.path.encrypt(self.password)
            if self.mode == 'save':
                with open(f'./keystore/{self.name}.json', 'w') as f:
                    f.write(tools.dumps(keystore))
            
            prvKey = self.w3.eth.account.decrypt(keystore, self.password)
            self.result.emit(prvKey.hex(), self.name)
        
        elif self.mode == 'restore':
            oldPassword, newPassowrd = self.restoreData
            for accountName in os.listdir('./keystore'):
                with open('./keystore/' + accountName) as f:
                    keystore = json.loads(f.read())
                prvKey = self.w3.eth.account.decrypt(keystore, oldPassword)
                account = self.w3.eth.account.privateKeyToAccount(prvKey)
                keystore = account.encrypt(newPassowrd)
                with open('./keystore/' + accountName, 'w') as f:
                    f.write(json.dumps(keystore))

class ZahirWallet(titleBar):
    def __init__(self):
        super().__init__()
        try: os.makedirs('keystore')
        except FileExistsError: pass
        self.rpc = Web3.HTTPProvider('http://127.0.0.1:8545')
        self.w3 = Web3(self.rpc)
        self.prvKey = None
        self.tempsAccounts = {}
        self.initializeUI()

    def initializeUI(self):
        self.msg = QtWidgets.QMessageBox()
        self.logIn = LogIn()
        self.restoreVault = RestoreVault()
        self.Main = Main()
        self._Import = _Import()
        self.Send = Send()
        self.AddToken = AddToken()
        self.SingUp = SingUp()
        self.Seed = Seed()
        self.Excutor = Excutor()
        self.close.clicked.connect(self.closeEvent)
        self.minimize.clicked.connect(
            lambda: self.showMinimized()
           )
        self.provider.clicked.connect(
            lambda: self.frame.show()
        )
        self.cancel.clicked.connect(
            lambda: self.frame.hide()
        )
        self.save.clicked.connect(self.changeRPC)

        self.contanier.addWidget(self.logIn)
        self.contanier.addWidget(self.restoreVault)
        self.contanier.addWidget(self.Main)
        self.contanier.addWidget(self._Import)
        self.contanier.addWidget(self.Send)
        self.contanier.addWidget(self.AddToken)
        self.contanier.addWidget(self.SingUp)
        self.contanier.addWidget(self.Seed)
        self.contanier.addWidget(self.Excutor)
        self.widgets = {
            "logIn": 0, "SingUp": 6, "restoreVault": 1,
            "Main": 2, "_Import": 3, "Send": 4, "AddToken": 5,
            "Seed": 7, 'Excutor': 8
            }

        self.SingUp.create.clicked.connect(self.register)

        self.logIn.submit.clicked.connect(self.checkData)
        self.logIn.restore.clicked.connect(
            lambda: self.contanier.setCurrentIndex(self.widgets['restoreVault'])
            )

        self.Seed.next.clicked.connect(
            lambda: self.contanier.setCurrentIndex(self.widgets['Main'])
            )
            
        self.restoreVault.restore.clicked.connect(self.Resotre)
        self.restoreVault.back.clicked.connect(
            lambda: self.contanier.setCurrentIndex(self.widgets['logIn'])
            )

        self.Main.copy.clicked.connect(self._copy)

        self.Main.accounts.currentTextChanged.connect(
            lambda: self.getAccount(True)
            )

        self.Main._import.clicked.connect(
            lambda: self.contanier.setCurrentIndex(self.widgets['_Import'])
            )
                
        self.Main.send.clicked.connect(
            lambda: self.contanier.setCurrentIndex(self.widgets['Send'])
            )
        
        self.Main.add_token.clicked.connect(
            lambda: self.contanier.setCurrentIndex(self.widgets['AddToken'])
            )
        
        self.Main.create.clicked.connect(self.createAccount)
        
        self._Import.back.clicked.connect(
            lambda: self.contanier.setCurrentIndex(self.widgets['Main'])
            )
        
        self._Import.way.currentTextChanged.connect(self.updateInputs)
        self._Import.browse.clicked.connect(self.Browse)
        self._Import._import.clicked.connect(self.addAccount)
        
        self.Send.back.clicked.connect(
            lambda: self.contanier.setCurrentIndex(self.widgets['Main'])
            )
        
        self.Send.send.clicked.connect(self.sendCoin)
        
        self.AddToken.cancel.clicked.connect(
            lambda: self.contanier.setCurrentIndex(self.widgets['Main'])
            )
        
        self.AddToken.tokenAddress.textChanged.connect(self.checkToken)
        self.AddToken.abi.textChanged.connect(self.checkToken)
        self.AddToken.add.clicked.connect(self.getToken)

        self.Excutor.methods.currentTextChanged.connect(self.getInputs)
        self.Excutor.excute.clicked.connect(self.applyMethod)
        self.Excutor.back.clicked.connect(
            lambda: self.contanier.setCurrentIndex(self.widgets['Main'])
        )

        if not 'data.json' in os.listdir('.'):
            self.contanier.setCurrentIndex(self.widgets['SingUp'])
            
    def checkData(self):
        with open('data.json') as f:
            data = tools.loads(f.read())
            
        self.password = self.logIn.password.text()
        if sha256(self.password.encode()).hexdigest() == data['KeyData']['mac']:
            self.loading_label.show()
            self.worker = Worker(
                w3=self.w3, mode='getPrv', 
                name=[name.replace('.json', '') for name in os.listdir('./keystore')],
                password=self.password
                )
            self.worker.start()

            self.worker.result.connect(self._addAccount)
            self.worker.finished.connect(
                lambda: self.loading_label.hide()
            )
            self.provider.show()
            self.contanier.setCurrentIndex(self.widgets['Main'])
        
        else:
            self.msg.information(
                self, 'Wrong', 'Wrong password',
                self.msg.Ok, self.msg.Ok
            )
    
    def Resotre(self):
        phrase = self.restoreVault.seed.toPlainText()
        with open('data.json') as f:
            data = tools.loads(f.read())
        
        if sha256(phrase.encode()).hexdigest() == data['seedHash']:
            newPassword = self.restoreVault.password.text()

            if newPassword != self.restoreVault.pwd_conf.text():
                self.msg.information(self, 'Worng',
                "password doesn't match", self.msg.Ok, self.msg.Ok)
        
            elif len(newPassword) < 8 or (newPassword.isalpha() and newPassword.isnumeric()):
                self.msg.information(
                    self, 'Worng',
                    "Weak password (Min 8 chr, Min one digit", self.msg.Ok, self.msg.Ok
                )
            
            else:
                key = tools.derive_key(phrase.encode())
                oldPassword = tools.decryptor(data['KeyData']['cipherdata'], key)
                self.loading_label.show()
                self.worker = Worker(
                    mode='restore', w3=self.w3,
                    restoreData=[oldPassword, newPassword]
                )
                self.worker.start()
                self.worker.finished.connect(
                    lambda: self.restoreEnd(phrase, newPassword, key)
                    )
        
        else:
            self.msg.information(
                self, 'Wrong', 'You entered wrong seed phrase.',
                self.msg.Ok, self.msg.Ok
            )
        
    def restoreEnd(self, phrase, newPassword, key):
            self.loading_label.hide()
            data = {
                "seedHash": sha256(phrase.encode()).hexdigest(),
                "KeyData": {'cipherdata': tools.encryptor(newPassword.encode(), key), 
                'mac': sha256(newPassword.encode()).hexdigest()}
                }
            with open('data.json', 'w') as f:
                f.write(tools.dumps(data))
            
            self.contanier.setCurrentIndex(self.widgets['logIn'])

    def register(self):
        self.password = self.SingUp.password.text()
        if self.password != self.SingUp.password_conf.text():
            self.msg.information(self, 'Worng',
            "password doesn't match", self.msg.Ok, self.msg.Ok)
        
        elif len(self.password) < 8 or (self.password.isalpha() and self.password.isnumeric()):
            self.msg.information(
                self, 'Worng',
                "Weak password (Min 8 chr, Min one digit", self.msg.Ok, self.msg.Ok
            )
        
        else:
            self.contanier.setCurrentIndex(self.widgets["Seed"])
            with open('words.txt') as f:
                words = f.read().split('\n')
            
            phrase = ' '.join([choice(words) for i in '__________'])
            self.Seed.seed.setPlainText(phrase)
            key = tools.derive_key(phrase.encode())
            data = {
                "seedHash": sha256(phrase.encode()).hexdigest(),
                "KeyData": {
                    'cipherdata': tools.encryptor(self.password.encode(), key), 
                    'mac': sha256(self.password.encode()).hexdigest()
                    },
                }
            self.provider.show()

            with open('data.json', 'w') as f:
                f.write(tools.dumps(data))
    
    

    def closeEvent(self, evnet=None):
        answer = self.msg.question(
            self, 'Quit', 'Are your sure you want to exit?',
            self.msg.Yes | self.msg.No, self.msg.No
        )

        if answer == self.msg.Yes: exit()

    def createAccount(self):
        name = QtWidgets.QInputDialog.getText(self, 'Name', 'Enter account name.')[0]
        if not name: return

        self.account = self.w3.eth.account.create()
        answer = self.msg.question(
            self, 'Save?', 'Do you want to save this account.', 
            self.msg.Yes | self.msg.No, self.msg.No
            )
        self.loading_label.show()

        if answer == self.msg.Yes: mode = 'save'
        else: mode = 'load'

        self.worker = Worker(
            w3=self.w3, mode=mode, path=self.account, 
            name=name, password=self.password
            )
        self.worker.start()
        self.worker.result.connect(self._addAccount)
        self.worker.finished.connect(
            lambda: self.loading_label.hide()
        )

    def getAccount(self, get=False):
        if get:
            name = self.Main.accounts.currentText()
            if name + '.json' not in os.listdir('./keystore'):
                account = self.tempsAccounts[name]
                if '.json' in account:
                    self.loading_label.show()
                    self.wokrer = Worker(
                        w3=self.w3, mode='getPrv', path=account,
                        name=[name], password=self.password
                        )
                    self.wokrer.result.connect(self._addAccount)
                    self.worker.start()
                    self.worker.finished.connect(
                        lambda: self.loading_label.hide()
                    )
                
                else: self._addAccount(account, name)
            
            else:
                self.loading_label.show()
                self.worker = Worker(w3=self.w3, mode='getPrv', name=[name], password=self.password)
                self.worker.result.connect(self._addAccount)
                self.worker.start()
                self.worker.finished.connect(
                    lambda: self.loading_label.hide()
                )

    def _copy(self):
        copy(self.Main.account_address.text())
        self.worker = Worker(mode='copy')
        self.copy_icon_label.show()
        self.worker.start()
        self.worker.finished.connect(
            lambda: self.copy_icon_label.hide()
        )

    def updateInputs(self):
        way = self._Import.way.currentText()
        self._Import.password.hide()
        self._Import.browse.hide()
        self._Import.chosen.hide()
        if way == 'JSON File':
            self._Import.browse.show()
            self._Import.chosen.show()
        
        else:
            self._Import.password.show()
    
    def Browse(self):
        json_file, _ = QtWidgets.QFileDialog.getOpenFileName(self, "Open Json", "",
        "json Files (*.json)")
        if json_file:
            self._Import.chosen.setText(json_file)
        
    def addAccount(self):
        way = self._Import.way.currentText()
        name = QtWidgets.QInputDialog.getText(
            self, 'name', 'Enter account name.', 
            )[0]
        if way == 'JSON File':
            self.loading_label.show()
            password = QtWidgets.QInputDialog.getText(
                self, 'password', 'Enter account password.', 
                QtWidgets.QLineEdit.Password
                )[0]
            path=self._Import.chosen.text()
            self.worker = Worker(
                w3=self.w3, mode='getPrv', path=[path], 
                name=[name], password=password
                )
            self.worker.result.connect(self._addAccount)
            self.worker.start()
            self.worker.finished.connect(
                lambda: self.loading_label.hide()
            )
            self._Import.chosen.setText('No file chosen')
        else:
            prvKey = self._Import.password.text()
            self._addAccount(prvKey, name)
            self._Import.password.clear()
        
        self.contanier.setCurrentIndex(self.widgets['Main'])
    
    def _addAccount(self, prvKey, acc_name):
        if prvKey == 'Error':
            return self.msg.information(self, 'Error', "Invalid password", self.msg.Ok, self.msg.Ok)
        try:
            self.prvKey = prvKey
            try:
                self.tempsAccounts[acc_name]
            except KeyError:
                self.tempsAccounts[acc_name] = self.prvKey
            
            self.account = self.w3.eth.account.privateKeyToAccount(self.prvKey)
            if self.Main.accounts.findText(acc_name) == -1:
                self.Main.accounts.addItem(acc_name)
            
            self.Main.account_address.setText(self.account.address)
            balance = self.w3.fromWei(
                self.w3.eth.get_balance(self.account.address), 
                'ether'
                )
            self.Main.balance.setText(str(balance))
        except :
            self.msg.information(
                self, 'Error', 'Invalid private key',
                self.msg.Ok, self.msg.Ok
            )

    def sendCoin(self):
        if self.prvKey:
            nonce = self.w3.eth.getTransactionCount(self.account.address)
            _from = self.Main.account_address.text()
            _to = self.Send.To.text()
            amount = self.Send.amount.value()
            if amount > self.w3.eth.get_balance(self.Main.account_address.text()):
                return self.msg.information(
                    self, 'Amount!', 'insufficient balance',
                    self.msg.Ok, self.msg.Ok
                )
            try:
            
                transaction = {
                    'from': self.w3.toChecksumAddress(_from),
                    'to': self.w3.toChecksumAddress(_to),
                    'value': self.w3.toWei(amount, 'ether'),
                    'gas': 100000,
                    'gasPrice': self.w3.toWei('1', 'gwei'),
                    'nonce': nonce
                    }
                
                signed = self.w3.eth.account.signTransaction(transaction, self.prvKey)
                tx = self.w3.eth.sendRawTransaction(signed.rawTransaction)
                data = self.w3.eth.wait_for_transaction_receipt(tx)
                tx_hash = data['transactionHash'].hex()
                tx_index = str(data['transactionIndex'])
                amount = self.w3.fromWei(amount)
                self.Main.addTx(
                    tx_index, tx_hash, 
                    datetime.now().strftime("%m/%d/%y %H:%M"), str(amount)
                    )
                self.contanier.setCurrentIndex(self.widgets['Main'])
            except:
                self.msg.information(
                    self, 'Invalid input!', 'Address or amount Invalid!',
                    self.msg.Ok, self.msg.Ok
                    )

        else:
            self.msg.information(
                self, 'No account', 'add a account first.',
                self.msg.Ok, self.msg.Ok
            )
        
    def getToken(self):
        _address = self.AddToken.tokenAddress.text()
        abi = self.AddToken.abi.toPlainText()
        contract = self.w3.eth.contract(address=_address, abi=abi)
        _ERC20Token = ERC20Token(self.w3, contract)
        excute = QtWidgets.QPushButton(self.Main.scrollAreaWidgetContents_2)
        excute.setProperty('token', _ERC20Token)
        excute.clicked.connect(self.prepare)
        name = _ERC20Token.name
        symbol = _ERC20Token.symbol
        balance = _ERC20Token.balanceOf(self.Main.account_address.text())
        self.Main.addToken(name, symbol, _address, balance, excute)
        self.contanier.setCurrentIndex(self.widgets['Main'])
    
    def checkToken(self):
        try:
            address = self.w3.toChecksumAddress(self.AddToken.tokenAddress.text())
            abi = self.AddToken.abi.toPlainText()
            contract = self.w3.eth.contract(address=address, abi=abi)
            contract.functions.name().call()
            if str(contract.all_functions()) == '[<Function balanceOf(address)>, <Function transfer(address,uint256)>, <Function transferFrom(address,address,uint256)>, <Function approve(address,uint256)>, <Function allowance(address,address)>, <Function name()>, <Function symbol()>, <Function totalSupply()>, <Function decimals()>]':
                self.AddToken.add.setEnabled(True)
        except:
            pass
    
    def TokenExcutor(self):
        token = self.excutor.property('token')
    
    def prepare(self):
        self._excutor = self.sender()
        self.contanier.setCurrentIndex(self.widgets['Excutor'])
    
    def getInputs(self):
        self.Excutor._from.clear()
        self.Excutor._to.clear()
        self.Excutor._value.setValue(0)
        self.Excutor._from.hide()
        self.Excutor._to.hide()
        self.Excutor._value.hide()
        self.Excutor.result.hide()
        method = self.Excutor.methods.currentText()
        
        if method == 'transfer':
            self.Excutor._to.setPlaceholderText('Receive address')
            self.Excutor._to.show() 
            self.Excutor._value.show()
        
        elif method == 'transferFrom':
            self.Excutor._to.setPlaceholderText('Receive address')
            self.Excutor._from.setPlaceholderText('Owner address')
            self.Excutor._from.show() 
            self.Excutor._to.show() 
            self.Excutor._value.show()
        
        elif method == 'approve':
            self.Excutor._to.setPlaceholderText('Spender address')
            self.Excutor._to.show() 
            self.Excutor._value.show()

        elif method == 'balanceOf':
            self.Excutor._from.setPlaceholderText('Owner address')
            self.Excutor._from.show()
        
        elif method == 'allowance':
            self.Excutor._from.setPlaceholderText('Owner address')
            self.Excutor._to.setPlaceholderText('Spender address')
            self.Excutor._from.show()
            self.Excutor._to.show()
        
    def applyMethod(self):
        token = self._excutor.property('token')
        self._excutor.property('balance').setText(token.balanceOf(
            self.Main.account_address.text()
        ))

        _from = self.Excutor._from.text()
        _to = self.Excutor._to.text()
        _value = self.Excutor._value.value()
        method = self.Excutor.methods.currentText()
        self.Excutor.result.show()
        result = token.excuteMethod(
            method ,_from, _to, _value, 
            self.Main.account_address.text(), self.prvKey
        )
        self.Excutor.result.setText(str(result))
    
    def changeRPC(self):
        rpcs = [self.RPCUrl.itemText(i) for i in range(self.RPCUrl.count())]
        rpcUrl = self.RPCUrl.currentText()
        
        if rpcUrl.startswith('http'):
            rpc = Web3.HTTPProvider(rpcUrl)
        
        elif rpcUrl.startswith('wss'):
            rpc = Web3.WebsocketProvider(rpcUrl)
        
        else:
            self.msg.information(self, 'Unknow rpc.',
            'Could not Identify this rpc', self.msg.Ok, self.msg.Ok
            )
        if not rpc in rpcs: self.RPCUrl.addItem(rpcUrl)
        self.w3 = Web3(rpc)
        if self.w3.isConnected():
            self.rpc = rpc
            self.frame.hide()
        
        else:
            self.w3 = Web3(self.rpc)
            self.msg.information(self, 'Not connected.',
            'Could not connect to this rpc', self.msg.Ok, self.msg.Ok
            )

if __name__ == '__main__':
    import sys
    app = QtWidgets.QApplication(sys.argv)
    ZahirWallet = ZahirWallet()
    ZahirWallet.show()
    sys.exit(app.exec_())
        