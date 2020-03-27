from iota.commands.extended import find_transaction_objects
from iota import Iota, Address
from pprint import pprint

# Declare an API object
api = Iota('https://nodes.devnet.iota.org:443', testnet=True)

add = input('Insert Address from last milestone: ')

list_add = [Address(add)]
response = api.find_transaction_objects(addresses=list_add)


list_bundle_hash = []

if not response['transactions']:
    print('Couldn\'t find data for the given address.')
else:
    print('Found:')
    # Iterate over the fetched transaction objects
    for tx in response['transactions']:
        # If it is a tail, save the bundle hash to a list
        if tx.is_tail:
            print(tx.hash)
            list_bundle_hash.append(tx.hash)

for i in list_bundle_hash:
    # Fetch the corresponding bundle objects
    try:
        bundle = api.get_bundles([i])['bundles'][0]
        content =   bundle.get_messages()
        print(content)
    except Exception as e:
        print("Problem here")
        pprint(getattr(e, 'context', {}))

