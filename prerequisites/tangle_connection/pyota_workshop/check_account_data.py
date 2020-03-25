from iota import Iota
from iota.crypto.types import Seed
from pprint import pprint
import time

# Put your seed from Tutorial 4.a here
my_seed = Seed(b'JJQTYOCGRLVANT9TMXIEYCNNIUXDPOQTWBL9SAENUXGWMRFDDEDOGISKJQFDSRJZMO9S9NZABZENDEYUP')

# Declare an API object
api = Iota(
    adapter='https://nodes.devnet.iota.org:443',
    seed=my_seed,
    testnet=True
)

# Script actually runs until it finds balance
success = False

while not success:
    print('Checking account information on the Tangle...')
    # Gather addresses, balance and bundles
    response = api.get_account_data()

    # response['balance'] is an integer!
    if response['balance']:
        print('Found the following information based on your seed:')
        pprint(response)
        success = True
    else:
        print('Zero balance found, retrying in 30 seconds...')
        time.sleep(30)
