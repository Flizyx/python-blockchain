from backend.blockchain.block import Block, GENESIS_DATA


def test_mine_function():
    last_block = Block.genesis()
    data = 'test-data'
    block = Block.mine_block(last_block, data)

    assert isinstance(block, Block)  # check if block is a Block instance
    assert block.data == data
    assert block.last_hash == last_block.hash


def test_genesis():
    genesis = Block.genesis()

    assert isinstance(genesis, Block)
    for key, value in GENESIS_DATA.items():  # nor genesis.key
        getattr(genesis, key) == value
