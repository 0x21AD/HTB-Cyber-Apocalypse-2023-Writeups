import json
from web3 import Web3
from web3.auto import w3

# Set up the connection to the Ethereum network
w3 = Web3(Web3.HTTPProvider('http://165.232.100.46:30556'))
contract_address = '0x569EB6EA90CaB82D72c7489227B5d24443FBd164'
private_key = '0xe6b057a5a6a12205282f12d0baa561fcd7bc2b5911460996a78366425aa68f6e'

abi = [
	{
		"stateMutability": "payable",
		"type": "fallback"
	},
	{
		"inputs": [],
		"name": "firstShot",
		"outputs": [
			{
				"internalType": "bool",
				"name": "",
				"type": "bool"
			}
		],
		"stateMutability": "view",
		"type": "function"
	},
	{
		"inputs": [],
		"name": "secondShot",
		"outputs": [
			{
				"internalType": "bool",
				"name": "",
				"type": "bool"
			}
		],
		"stateMutability": "view",
		"type": "function"
	},
	{
		"inputs": [],
		"name": "third",
		"outputs": [],
		"stateMutability": "nonpayable",
		"type": "function"
	},
    {
		"inputs": [],
		"name": "Dummy",
		"outputs": [],
		"stateMutability": "nonpayable",
		"type": "function"
	},
	{
		"inputs": [],
		"name": "thirdShot",
		"outputs": [
			{
				"internalType": "bool",
				"name": "",
				"type": "bool"
			}
		],
		"stateMutability": "view",
		"type": "function"
	},
	{
		"stateMutability": "payable",
		"type": "receive"
	}
]
# Load the contract instance
contract = w3.eth.contract(address=contract_address, abi=abi)

# Build the transaction object
nonce = w3.eth.get_transaction_count(w3.to_checksum_address('0xbf68306f42ABd83b9698870d48Da7A037CaFb90d'))
tx = contract.functions.Dummy().build_transaction({
	'gas': 30000000,
    'gasPrice': w3.to_wei('10', 'gwei'),
    'nonce': nonce
})

nonce2 = nonce + 1

tx2 = {
    'to': '0x569EB6EA90CaB82D72c7489227B5d24443FBd164',
    'value': w3.to_wei(1, 'ether'),  # sending 1 ether to trigger the receive function
    'gas': 30000000,
    'gasPrice': w3.to_wei('10', 'gwei'),
    'nonce': nonce2
}

nonce3 = nonce2 + 1

tx3 = contract.functions.third().build_transaction({
    'gas': 30000000,
    'gasPrice': w3.to_wei('10', 'gwei'),
    'nonce': nonce3
})


# Sign and send the transaction
signed_tx = w3.eth.account.sign_transaction(tx, private_key)
signed_tx2 = w3.eth.account.sign_transaction(tx2, private_key=private_key)
signed_tx3 = w3.eth.account.sign_transaction(tx3, private_key)



tx_hash = w3.eth.send_raw_transaction(signed_tx.rawTransaction)
tx_hash2 = w3.eth.send_raw_transaction(signed_tx2.rawTransaction)
tx_hash3 = w3.eth.send_raw_transaction(signed_tx3.rawTransaction)



# Wait for the transaction to be mined
tx_receipt = w3.eth.wait_for_transaction_receipt(tx_hash)
tx_receipt2 = w3.eth.wait_for_transaction_receipt(tx_hash2)
tx_receipt3 = w3.eth.wait_for_transaction_receipt(tx_hash3)


# Check the transaction status
if tx_receipt.status == 1:
    print("Transaction succeeded")
else:
    print("Transaction failed")


if tx_receipt2.status == 1:
    print("Transaction succeeded")
else:
    print("Transaction failed")

if tx_receipt3.status == 1:
    print("Transaction succeeded")
else:
    print("Transaction failed")


first_shot_value = contract.functions.firstShot().call()
second_shot_value = contract.functions.secondShot().call()
third_shot_value = contract.functions.thirdShot().call()
print(f'firstShot: {first_shot_value}, secondShot: {second_shot_value}, thirdShot: {third_shot_value}')