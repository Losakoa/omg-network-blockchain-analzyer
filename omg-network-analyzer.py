#!/bin/env python

from web3 import Web3
import json

#Vars
infura_url = "<INSERT INFURA URL HERE"
web3_url = Web3(Web3.HTTPProvider(infura_url))
omg_abi_file = "json_files/omg_abi.json"
infura_url = "json_files/infura_url.json"
address = "0xd26114cd6EE289AccF82350c8d8487fedB8A0C07"


# def load_infura_url():
# 	try:
# 		with open(infura_url_file) as infura:
# 			infura_url = json.load(infura)
# 			return infura_url
# 	except ValueError:
# 		print("The infura url failed to load correctly.")

#is the connection established?

def load_abu_json_file():
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
			print("Connection to the etherium network is establishe...\n")
	except ConnectionError:
		print("Connection to the ehterium network has failed...\n")


def build_contract(address,abi_data):
	try:
		built_contract = web3_url.eth.contract(address=address,abi=abi_data)
		return built_contract
	except ValueError:
		print("Failed to build contract correctly, please try again.")
	

def get_latest_eth_block():
	latest_eth_block = web3_url.eth.getBlock('latest')
	print(f"Here is the latest OMG block information on the OMG Network:\n\t {latest_eth_block}")

def get_latest_eth_block_number():
	block_num = web3_url.eth.blockNumber
	print(f"Here is the latest block number for the OMG Network: \n\t {block_num}")



if __name__ == "__main__":
	test_web3 = test_web_connection()
	abi_data = load_abu_json_file()
	#abi is a json array which describes the smart contract
	#address is the address of the deployed contract on the blockchain
	# with these two pieces of information, we can recontract the smart contract in python and interact with it

	 #https://etherscan.io/token/0xd26114cd6EE289AccF82350c8d8487fedB8A0C07)

	# contract = web3_url.eth.contract(address=address,abi=abi_data) #assigning contract to 
	contract = build_contract(address,abi_data) 
	get_latest_eth_block_number()
	get_latest_eth_block()
	

	omg_token = contract.functions.name().call()
	print(omg_token)
	total_supply = contract.functions.totalSupply().call()
	print(web3_url.fromWei(total_supply, 'ether'))

	#prints the amount someone owns at the following address
	customer_supply = contract.functions.balanceOf("0xd26114cd6EE289AccF82350c8d8487fedB8A0C07").call()
	print(web3_url.fromWei(customer_supply,"ether"))

