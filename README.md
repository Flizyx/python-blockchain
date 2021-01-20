**Activate the virtual environment**

```
python3 -m venv blockchain-env
    source blockchain-env/bin/activate
blockchain-env\Scripts\activate
```

**Install all packages**

```
pip3 install -r requirements.txt
```

https://github.com/15Dkatz/python-blockchain-tutorial/tree/aee78721a361da57161d92a9cfa0ebef95b0c411

```
python -m backend.blockchain.blockchain
python -m backend.blockchain.block
python -m backend.util.crypto_hash
```

**Run the tests**
Make sure to activate the virtual environment.

```
python -m pytest backend/tests
```
