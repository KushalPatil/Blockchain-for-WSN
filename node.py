from uuid import uuid4

from blockchain import Blockchain
from utility.verification import Verification
from wallet import Wallet

class Node:
    """The node which runs the local blockchain instance.
    Attributes:
        :id: The id of the node.
        :blockchain: The blockchain which is run by this node.
    """
    def __init__(self):
        # self.id = str(uuid4())
        self.wallet = Wallet()
        self.wallet.create_keys()
        self.blockchain = Blockchain(self.wallet.public_key)

    def get_transaction_value(self):
        tx_recipient = 'new node'
        tx_amount = 17.0
        return tx_recipient, tx_amount

    def get_user_choice(self):
        user_input = input('Your choice: ')
        return user_input

    def print_blockchain_elements(self):
        for block in self.blockchain.chain:
            print('Outputting Block')
            print(block)
        else:
            print('-' * 20)

    def listen_for_input(self):
        waiting_for_input = True
        while waiting_for_input:
            print('----------------------------CA control panel----------------------------')
            print('1: Add a new node')
            print('2: Mine node')
            print('3: Output the blockchain blocks')
            print('4: Check node validity')
            print('5: Create CPAN')
            print('6: Load CPAN')
            print('7: Save keys')
            print('q: Quit')
            print('a : Attack Script')
            user_choice = self.get_user_choice()
            if user_choice == '1':
                tx_data = self.get_transaction_value()
                recipient, amount = tx_data
                signature = self.wallet.sign_transaction(self.wallet.public_key, recipient, amount)
                if self.blockchain.add_transaction(recipient, self.wallet.public_key, signature, amount=amount):
                    print('Node Added!')
                else:
                    print('Node Addition failed!')
                print(self.blockchain.get_open_transactions())
            elif user_choice == '2':
                if not self.blockchain.mine_block():
                    print('Mining failed. Got no keys?')
            elif user_choice == '3':
                self.print_blockchain_elements()
            elif user_choice == '4':
                if Verification.verify_transactions(self.blockchain.get_open_transactions(), self.blockchain.get_balance):
                    print('All nodes are valid')
                else:
                    print('There are invalid nodes')
            elif user_choice == '5':
                self.wallet.create_keys()
                self.blockchain = Blockchain(self.wallet.public_key)
            elif user_choice == '6':
                self.wallet.load_keys()
                self.blockchain = Blockchain(self.wallet.public_key)
            elif user_choice == '7':
                self.wallet.save_keys()
            elif user_choice == 'q':
                waiting_for_input = False
            elif user_choice == 'a':
                with open('blockchain.txt', 'r') as file :
                    filedata = file.read()
                filedata = filedata.replace('10','changed')
                print('Ledger Altered by changing Data/Mining value......')
                with open('blockchain.txt', 'w') as file1:
                    file1.write(filedata)
                print('Write Successful.....')
            else:
                print('Input was invalid, please pick a value from the list!')
            if not Verification.verify_chain(self.blockchain.chain):
                print('Ledger has been altered or modified.......')
                #self.print_blockchain_elements()3
                print('Invalid blockchain!')
                print('Fetching new blockchain from other CPAN...')
                with open('CPAN_BLCKCHN.txt', 'r') as file :
                    filedata = file.read()
                print('Loading the Authentic Ledger into the local instance......')
                with open('blockchain.txt', 'w') as file:
                    file.write(filedata)
                print('Load Successful.....')
                print('Local instance Loaded.....')
                break
            print('Balance of {}: {:6.2f}'.format(self.wallet.public_key, self.blockchain.get_balance()))
        else:
            print('User left!')

        print('Done!')

if __name__ == '__main__':
    node = Node()
    node.listen_for_input()
