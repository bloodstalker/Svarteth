#!/bin/python3
import feedparser
import json
import web3

from web3 import Web3, HTTPProvider, TestRPCProvider
from solc import compile_source
from web3.contract import ConciseContract

def Contract_Sol():
    def __init__(self, source_code, w3):
        self.source_code = source_code
        self.w3 = w3

    def compile(self):
        compiled = compile_source(self.source_code)
        interface = compiled['<stdin>:Svarteth']

    def deploy(self):
        self.contract = self.w3.eth.contract(abi=interface['abi'], bytecode=interface['bin'])
        self.tx_hash = self.contract.deploy(transaction={'from':w3.eth.account[0], 'gas':410000})
        self.tx_receipt = self.w3.eth.getTransactionReceipt(self.tx_hash)
        self.contract_address = self.tx_receipt['contractAddress']
        self.contract_instance = w3.eth.contract(interface['abi'], self.contract_address, ContractFactoryClass=ConciseContract)

def dumpRssData(which):
    feed = feedparser.parse(which)
    print(len(feed['entries']))
    for i in range(0, len(feed['entries'])):
        print("title: " + repr(feed['entries'][i].title))
        print("description: " + repr(feed['entries'][i].summary))


def main():
    dumpRssData("http://dark-world.ru/rss/albums/")
    w3 = Web3(TestRPCProvider())

if __name__ == "__main__":
    main()
