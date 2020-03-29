# Hack4Italy |Autodichiarazione_2.0

Video presentation: https://www.youtube.com/watch?v=Ce1ZMYNVdmQ&feature=youtu.be

---

Content of the self declaration 

Fields | Type
--- | --- 
UUID Citizen | char[] 
Dpi measures | char[]
Simptoms | char[]
Temperature | float
Geographical sector id | char[] 
Departure time | datetime
Arrival time | datetime
Reason  | char[] 
Destinations | [ [(gps_coord, timestamps) ], [ ] ]

---

## Roadmap

### Milestone 0

- Simulate one user and associate a random home gps coordinate.
- Simulate random destination point within a radius of 1 km from home position
- Simulate a first self declaration from Home to one destination
- Get detailed navigation instructions and fill the Destinations field of the self declaration
- Simulate temporary declaration by pushing it to the distributed digital ledger, the Tangle

### Milestone 1

 Create a visualization tool to show the path

### Milestone 2

- Create two users and two declarations with same destination point and time interval
- Use visualization tool to show the paths

### Milestone 3
 
- Retrieve all declarations sent to specific address
 [Issue compromised content: https://iota.stackexchange.com/questions/2499/problem-retrieving-the-content-of-zero-value-transactions-from-the-testnet]

## Mileston 4 [ Skipped straigth to Milestone 7 ]

 Assume User 1 is tested positive for the CoronaVirus after some time
- Create a Check function that given all declarations in the immutable digital ledger, and the id of a positive citizen returns a list of all possible contaminated users that have shared the same places in the same time. Should return User2 as a possible test candidate

### Milestone 5 [ Skipped ]

- Create two users, two declarations with a portion of the path in common and same time interval
- Use visualization tool to show the paths
- Invoke the Check function, should return the orhter User

### Milestone 6 

Investigate how to determine if two citizens have shared a portion of the path

### Milestone 7

- Create N users, N declarations
- Push to the Tangle
- Simulate random positive test results citizen with universally unique identifier XYZ
- Get list of possible contaminated citizens and detailed information related to exposure by retrieving declarations pushed on the Tangle and by considering if citizen have been to the same destination of a COVID19 patient and if they have shared a portion of the path at the same time.
- Associate a constant probability to each candidate as a function of their exposure to the COVID19 patient

---

## Test the system

Clone the repository:

```bash
git clone https://github.com/GiovanniBalestrieri/autodichiarazione_2.0.git
```

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

Test the milestone you prefer. If you are interested in the output of mileston0:

```bash
pythone milestone0.py
```

When you are done. Deactivate the virtual environment and go back to normal life

