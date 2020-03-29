from iota.commands.extended import find_transaction_objects
from iota import Iota, Address
from pprint import pprint
import pickle, ast

try:
    all_declarations_terni = pickle.load(open("percorsi.pkl", "rb"))
    print("Found Pickle file! Using it")
except:
    print("Pickle File not found")
    # Declare an API object
    api = Iota('https://nodes.devnet.iota.org:443', testnet=True)

    add = 'FNVOAXUEWEGMDRYUFIPCTQOOXIIKBINADOEEHFHLQ9WNZSOCMEOUTIT999HBBFPFBAQGPQCL9UWLRWOIW'

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
            print(content)
            all_declarations_terni.append(content)
        except Exception as e:
            print("Problem here")
            pprint(getattr(e, 'context', {}))

    # Save them to pickle
    with open('percorsi.pkl', 'wb') as f:
        pickle.dump(all_declarations_terni, f)

# At this point we should have a list with all transactions issued from Terni location
print("Retrieved: " + str(len(all_declarations_terni)))

# Assume citizen with uuid 1226 is tested positive for the CoronaVirus after some time
infected_id = 1692

## Fetch all trips of infected user

# prepare list of time intervals during which infected user went for a walk outside
time_of_commitment = []

for i in all_declarations_terni:
    # TODO remove maudit string representation of dist
    dic = ast.literal_eval(i[0])
    if 'uuid' in dic:
        print(dic['uuid'])
        if dic['uuid'] == infected_id:
            print("Found infected id")
            if 'info' in dic:
                print(dic['info'])
                time_of_commitment.append(dic['info']['start time'])

print(time_of_commitment)
