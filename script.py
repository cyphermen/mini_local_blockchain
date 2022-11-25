from blockchain import Blockchain

block_one_transactions = {"sender":"s1", "receiver": "r1", "amount":"100"}
block_two_transactions = {"sender": "s2", "receiver":"r2", "amount":"50"}
block_three_transactions = {"sender":"s3", "receiver":"r3", "amount":"25"}

local_blockchain=Blockchain()
local_blockchain.add_block(block_one_transactions)
local_blockchain.add_block(block_two_transactions)
local_blockchain.add_block(block_three_transactions)
local_blockchain.print_blocks()
print("***************************************")
fake_transactions = {"sender": "s2", "receiver":"fake_receiver_2", "amount":"10000"}

local_blockchain.chain[2].transactions =fake_transactions
local_blockchain.print_blocks()
local_blockchain.validate_chain()