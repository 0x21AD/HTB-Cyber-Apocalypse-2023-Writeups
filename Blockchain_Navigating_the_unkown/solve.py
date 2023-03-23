import json
from web3 import Web3
from web3.auto import w3

# Set up the connection to the Ethereum network
w3 = Web3(Web3.HTTPProvider('http://138.68.162.218:32602'))
contract_address = '0x277bF073733A08Ce06C8c2168bCE6Db5f068AB50'
private_key = '0xfd15463cc7341dab2d9066ea797e1f9b43dfc82f473ed056a076a232c1f1aa41'

abi = [
	{
		"inputs": [
			{
				"internalType": "uint256",
				"name": "version",
				"type": "uint256"
			}
		],
		"name": "updateSensors",
		"outputs": [],
		"stateMutability": "nonpayable",
		"type": "function"
	},
	{
		"inputs": [],
		"name": "updated",
		"outputs": [
			{
				"internalType": "bool",
				"name": "",
				"type": "bool"
			}
		],
		"stateMutability": "view",
		"type": "function"
	}
]

# Load the contract instance
contract = w3.eth.contract(address=contract_address, abi=abi)

# Build the transaction object
nonce = w3.eth.get_transaction_count(w3.to_checksum_address('0x2a2872cDCFfB8B470F6E71114987ed6349358333'))
tx = contract.functions.updateSensors(10).build_transaction({
    'gas': 2000000,
    'gasPrice': w3.to_wei('10', 'gwei'),
    'nonce': nonce
})



# Sign and send the transaction
signed_tx = w3.eth.account.sign_transaction(tx, private_key)
tx_hash = w3.eth.send_raw_transaction(signed_tx.rawTransaction)

print(signed_tx)
# Wait for the transaction to be mined
tx_receipt = w3.eth.wait_for_transaction_receipt(tx_hash)

# Check the transaction status
if tx_receipt.status == 1:
    print("Transaction succeeded")
else:
    print("Transaction failed")
