from iota.commands.extended import find_transaction_objects
from iota import Iota, Address
from pprint import pprint

# Declare an API object
api = Iota('https://nodes.devnet.iota.org:443', testnet=True)
add = 'GUXQZUBPAADCYWOCIM9EMPWQDGAGBVNFKLCSROERRWTQDB9ZQVIZYIQNBA9UMQCMCKWOLKFCZAWZUTCLC'

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

all_declarations_terni = []

for i in list_bundle_hash:
    # Fetch the corresponding bundle objects
    try:
        bundle = api.get_bundles([i])['bundles'][0]
        print(api.get_bundles([i]))
        content =   bundle.get_messages()
        all_declaration_terni.append(content)
        #print(content)
    except Exception as e:
        print("Problem here")
        pprint(getattr(e, 'context', {}))

# At this point we should have a list with all transactions issued from Terni location
print("Retrieved: " + str(len(all_declarations_terni))


