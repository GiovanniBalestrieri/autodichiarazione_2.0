from iota.commands.extended import find_transaction_objects
from iota import Address

list_add = [Address('LBWRSAKI9RGXUUNJGCPRNRYMFIIZEFOKOZGUUFRMA9IXVENWA9QCDHEQVXOBPTI9FTW9NYSZFSSQNHEIBQGQQJQAFC')]
transactions = find_transaction_objects(addresses=list_add)

for transaction in transactions:
  # Ignore input transactions; these have cryptographic signatures,
  # not human-readable messages.
  if transaction.value < 0:
    continue

  print(f'Message from {transaction.hash}:')

  message = transaction.signature_message_fragment
  if message is None:
    print('(None)')
  else:
    print(message.decode())
