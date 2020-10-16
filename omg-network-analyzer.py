#!/bin/env python

# imports
from web3 import Web3
import json

# Vars
omg_abi_file = "json_files/omg_abi.json"
infura_url_file = "json_files/infura_url.json"
# address for the main OMG Network contract
address = "0xd26114cd6EE289AccF82350c8d8487fedB8A0C07" 


""" Functions """
def load_infura_url():
	try:
		with open(infura_url_file) as infura:
			infura_url = json.load(infura)
			return infura_url["infura_url"]
	except ValueError:
		print("The infura url failed to load correctly.")

def load_abu_json_file():
	#abi is a json array which describes the smart contract
	try:
		with open(omg_abi_file) as f:
			abi_data = json.load(f)
			# print(json.dumps(abi_data, indent=4, sort_keys=True))
			return abi_data
	except ValueError:
		print("The ABI data did not load correctly.")

def test_web_connection():
	try:
		are_we_connected = web3_url.isConnected()
		if are_we_connected == True:
			print("Connection to the etherium network is established...\n")
	except ConnectionError:
		print("Connection to the ehterium network has failed...\n")

def build_contract(address,abi_data):
	""" address is the address of the deployed contract on the blockchain.  With these two pieces of information, we can recontract the smart contract in python and interact with it - https://etherscan.io/token/0xd26114cd6EE289AccF82350c8d8487fedB8A0C07 """
	try:
		built_contract = web3_url.eth.contract(address=address,abi=abi_data)
		return built_contract
	except ValueError:
		print("Failed to build contract correctly, please try again.")

def get_latest_eth_block_number():
	try:
		block_num = web3_url.eth.blockNumber
		return block_num
	except ValueError:
		print("We are unable to pull the latest block number.")

def get_latest_eth_block():
	try:
		latest_eth_block_info = web3_url.eth.getBlock('latest')
		return latest_eth_block_info
	except ValueError:
		print("We are unable to pull the latest OMG block information from the network.")

if __name__ == "__main__":
	""" load the URL, pass it to the web3 library, test the connection, and load the ABU data from the JSON file (found on etherscan.com)"""

	# assigning functions to vars
	infura_url = load_infura_url()
	web3_url = Web3(Web3.HTTPProvider(infura_url))
	test_web3_connection = test_web_connection()
	abi_data = load_abu_json_file()
	contract = build_contract(address,abi_data)
	omg_token = contract.functions.name().call()
	latest_block_num = get_latest_eth_block_number()
	latest_eth_block_info = get_latest_eth_block()
	total_supply = contract.functions.totalSupply().call()
	
	""" Calling all the functions!!!!!! """
	#prints token name
	print(f"TokenName:\n\t {omg_token}\n")
	print(f"Here is the latest block number for the OMG Network: \n\t {latest_block_num}\n")
	# prints total suppy of the token
	print(f"Total supply of OMG Network tokens: \n\t {web3_url.fromWei(total_supply, 'ether')}\n")
	#prints latest block
	print(f"Here is the latest OMG block information on the OMG Network:\n\t {latest_eth_block_info}")
	# dumps out information on the latest OMG Network ehterium block
	
	

	

