from datetime import datetime
from hashlib import sha256

class Block:
    def __init__(self,transactions,previous_hash):
        self.transactions = transactions
        self.previous_hash = previous_hash
        self.timestamp = datetime.now()
        self.nonce = 0 
        self.hash = self.generate_hash()
        
    def generate_hash(self):
        block_header=  str(self.timestamp) + str(self.transactions) + str(self.previous_hash) + str(self.nonce)
        block_hash = sha256(block_header.encode())
        return block_hash.hexdigest()
    
    def print_contents(self):
        print("timestamp: " , self.timestamp)
        print("transactions: " , self.transactions)
        print("current_has: " , self.hash)
        print("previous_hash: " , self.previous_hash)
        