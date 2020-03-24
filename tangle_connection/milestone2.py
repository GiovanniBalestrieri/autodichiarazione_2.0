from iota import Iota

api = Iota('https://nodes.devnet.iota.org:443', testnet = True)

# Define the tail transaction hash of the bundle whose messages you want to read
tail_hash = input('tail hash?')

print('Looking for bundle on the Tangle...')
bundle = api.get_bundles([tail_hash])

message = bundle['bundles'][0].tail_transaction.signature_message_fragment

print(message.decode(errors='ignore'))
   
    
