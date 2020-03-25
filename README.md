# Autodichiarazione_2.0

Content of the self declaration

Fields | Type
--- | --- 
Name | char[] 
Surname | char[] 
Date of birth | datetime 
Doc id number | char[] 
Departure time | datetime
Temperature | float
Reason  | char[] 
Destinations | [ [sequence of gps coord], [ ] ]



---

## Roadmap

### Milestone 0

- Simulate one user and associate a random home gps coordinate.
- Get list of nearby local activities as pharmacies or supermarkets or parks. 
- Simulate a first self declaration from Home to one destination
- Get detailed navigation instructions
- Simulate temporary declaration by pushing it to the distributed digital ledger, the Tangle
- Create a visualization tool to show the path

### Milestone 1

- Create two users and two declarations with same destination point and time interval
- Simulate positive results of the CoronaVirus test on User1 
- Create a Check function that given all declarations in the immutable digital ledger, and the id of a positive citizen returns a list of all possible contaminated users that have shared the same places in the same time. Should return User2 as a possible test candidate

### Milestone 2

- Create two users, two declarations with a portion of the path in common and same time interval
- Invoke the Check function, should return the orhter User

### Milestone 3

- Create N users, N declarations
- Simulate random positive test results
- Get list of possible contaminated citizens and detailed information related to exposure

---

## Test the system

Clone the repository: https://github.com/GiovanniBalestrieri/autodichiarazione_2.0.git

Create and activate vitual environment:
```bash
cd autodichiarazione_2.0
python3 -m venv environ
. environ/bin/activate
pip install --upgrade pip
```
Install requirements:
```bash
pip install -r requirements.txt
```

