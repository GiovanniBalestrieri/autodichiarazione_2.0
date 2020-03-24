from iota import Iota

# The seed that will be used to generate an address
seed = 'TWFHPDYLKPVDNDJSBDONGHUEWOMK9OZBYESEWRUTLORNRKRO9RR9PAY9JZREOURK9NLUJNSAMVFIQTGYH'

# Connect to a node
api = Iota('https://nodes.devnet.iota.org:443', seed, testnet = True)

# Define the security level of the address
security_level = 2

# Generate an unspent address with security level 2
address = api.get_new_addresses(index=0, count=1, security_level = security_level)['addresses'][0]

is_spent = api.were_addresses_spent_from([address])['states'][0]

if is_spent:
    print('Address %s is spent!' % address )
else:
    print('Your address is: %s' % address )
