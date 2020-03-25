from iota.commands.extended import find_transaction_objects
from iota import Iota, Address

# Declare an API object
api = Iota('https://nodes.devnet.iota.org:443', testnet=True)

add = input('Insert Address from last milestone: ')

list_add = [Address(add)]
response = api.find_transaction_objects(addresses=list_add)

if not response['transactions']:
    print('Couldn\'t find data for the given address.')
else:
    print('Found:')
    # Iterate over the fetched transaction objects
    for tx in response['transactions']:
        # data is in the signature_message_fragment attribute as trytes, we need
        # to decode it into a unicode string
        data = tx.signature_message_fragment.decode(errors='ignore')
        print(data)
