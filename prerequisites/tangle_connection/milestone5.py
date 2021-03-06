"""
Encrypt data and store it on the Tangle.

simplecrypt library is needed for this example (`pip install simple-crypt`)!
"""
from iota import Iota, TryteString, Tag, ProposedTransaction
from simplecrypt import encrypt
from base64 import b64encode
from getpass import getpass
from iota.crypto.types import Seed
import json


# Generate Seed and retrieve address
print('Generating a random seed...')
my_seed = Seed.random(length=81)
print('Your seed is: ' + str(my_seed))

# Declare an API object
api = Iota(
    adapter='https://nodes.devnet.iota.org:443',
    seed=my_seed,
    testnet=True,
)

print('Generating the first unused address...')
# Generate an address from your seed to post the transfer to
my_address = api.get_new_addresses(index=42)['addresses'][0]

print("Save this address: " + str(my_address))

# Declare an API object
api = Iota(
    adapter='https://nodes.devnet.iota.org:443',
    seed=my_seed,
    testnet=True,
)

N = 5
declarations = []
# Some confidential information
for i in range(N):
    declarations.append({ 'id' : i })

for i in declarations:
    # Convert to JSON format
    json_data = json.dumps(i)

    print('Constructing transaction locally...')
    # Convert to trytes
    trytes_data = TryteString.from_unicode(json_data)

    # Tag is optional here
    my_tag = Tag(b'TESTINFORMATION')

    # Prepare a transaction object
    tx = ProposedTransaction(
        address=my_address,
        value=0,
        tag=my_tag,
        message=trytes_data,
    )

    print('Sending transfer...')
    # Send the transaction to the network
    response = api.send_transfer([tx])

    print('Check your transaction on the Tangle!')
    print('https://utils.iota.org/transaction/%s/devnet' % response['bundle'][0].hash)
    print('Tail transaction hash of the bundle is: %s' % response['bundle'].tail_transaction.hash)
