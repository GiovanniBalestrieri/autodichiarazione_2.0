# Connection to Tangle, a decentralized network allowing peer-to-peer transactions without intermediaries or fees. 

By using IOTA, you can build applications that benefit from the following:
-    Authenticity: Prove that you have sent a self-declaration
-    Integrity: Prove that your data is unchanged
-    Confidentiality: Control who has access to your data through encryption

More info: https://docs.iota.org/docs/getting-started/0.1/network/the-tangle

## Trust:
All published self-declarations can be seen as valid transactions agreed on by all nodes, removing the need to trust a single entity in the network.

## Integrity
The Tangle is an immutable data structure (Direct Acyclic Graph) that contains an up-to-date history of transactions.All transactions in the Tangle are immutable and transparent.
Each transaction references the transaction hashes of two previous ones. So, if the contents of any transaction were to change, the hashes would be invalid, making the transactions invalid.

## Security and privacy
IOTA uses quantum-robust one-time signatures to stop attackers from altering your self-declaration.
IOTA networks are peer-to-peer networks where no central authority controls the Tangle. Instead, all nodes hold a copy of it and reach a consensus on its contents.

## Cost saving
The Tangle is free to use. You don't need to pay a subscription, or sign a contract. Even transactions are feeless. You can store data on the Tangle with no restrictions.

## Scalability
For each transaction that's attached to the Tangle, two previous transactions are validated. This process makes IOTA incredibly scalable because more new transactions lead to faster validations.

# Roadmap

We are going to build this solition step by step

## Milestone 0 
Connect to the Tangle

## Milestone 1
Create self-declaration json and push it to the DevNet. Pushing a self-declaration is equivalent to issuing a transaction.

A transaction is a single transfer instruction that can either withdraw IOTA tokens from an address, deposit them into an address, or have zero-value (contain data, a message, or a signature). If you want to send anything to an IOTA network, you must send it to a node as a transaction.

For this purpose we will use a Zero-value transaction: A transaction that has 0 value and might carry messages or signatures.

A transaction’s unique identifier in IOTA is the TransactionHash, that is generated from the trytes of the transaction. If any trytes change in the transaction, the returning transaction hash would alter. This way, transaction hashes ensure the immutability of the Tangle.


To become accepted by the network, a transaction has to be attached to the Tangle. The attachment process means that the transaction should reference two unconfirmed transactions (tips) in the Tangle and do a small proof-of-work. 

To send or receive any transaction using the Tangle, you will need to specify an address. An address is like a physical mailbox on your entrance door: anyone can drop things in your mailbox (send you messages or tokens).

Addresses are generated from your seed through cryptographic functions. There are 957 different addresses that one might generate from a seed



