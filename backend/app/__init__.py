from flask import Flask, json, jsonify

from backend.blockchain.blockchain import Blockchain

app = Flask(__name__)
blockchain = Blockchain()

"""
The goal is to use a public ledger to record transaction data in order to support a cyptocurrency
pub/sub pattern for real time interaction and updating (broadcasting) #PubNub its free for the moment
"""


@app.route('/')
def route_default():
    return 'welcome to the blockchain'


@app.route('/blockchain')
def route_blockchain():
    return jsonify(blockchain.to_json())


@app.route('/blockchain/mine')  # convention for resources in API
def route_blockchain_mine():
    transaction_data = 'stubbed_transaction_data'

    blockchain.add_block(transaction_data)
    return jsonify(blockchain.chain[-1].to_json())


app.run()
