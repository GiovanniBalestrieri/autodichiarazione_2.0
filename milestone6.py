from iota.commands.extended import find_transaction_objects
from iota import Iota, Address
from pprint import pprint
import pickle, ast
from datetime import datetime, timedelta


class Point:
    def __init__(self,x,y):
        self.x = x
        self.y = y

def ccw(A,B,C):
    return (C.y-A.y) * (B.x-A.x) > (B.y-A.y) * (C.x-A.x)

# Return true if line segments AB and CD intersect
def intersect(A,B,C,D):
    return ccw(A,C,D) != ccw(B,C,D) and ccw(A,B,C) != ccw(A,B,D)

try:
    all_declarations_terni = pickle.load(open("percorsi.pkl", "rb"))
    print("Found Pickle file! Using it")
except:
    print("Pickle File not found")
    # Declare an API object
    api = Iota('https://nodes.devnet.iota.org:443', testnet=True)

    add = 'WHROQRSMHOVUXOIRUQDJAKBKLGTJMOPRPSBQBNQHRBLLSICDCQFZPIR9YXRQUTYXMITDLWRMLCUQPOTYB'
#    add = 'FNVOAXUEWEGMDRYUFIPCTQOOXIIKBINADOEEHFHLQ9WNZSOCMEOUTIT999HBBFPFBAQGPQCL9UWLRWOIW'

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
infected_id = 1306

## Fetch all trips of infected user

# prepare list of time intervals during which infected user went for a walk outside
infected_trips = []
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
                #time_of_commitment.append(dic['info']['start time'])
                infected_trips.append(dic)
                all_declarations_terni.remove(i)

#print(time_of_commitment)
print(infected_trips)


high_probability_constant = 0.8
low_probability_constant = 0.2

list_of_candidate_infected = {}

#for i in time_of_commitment:
for i in infected_trips:
    date_obj = datetime.strptime(i['info']['start time'], '%m-%d-%Y_%H:%M:%S')
    print("Riferimento: " + str(date_obj))
    min_date = date_obj - timedelta(minutes=15)
    max_date = date_obj + timedelta(minutes=15)
    print(str(type(min_date)) + "\t\t" + str(min_date))
    print(str(type(max_date)) + "\t\t\t" + str(max_date))
    
    list_same_time_trip = []
    for j in all_declarations_terni:  
        dic = ast.literal_eval(j[0])
        date_i = datetime.strptime(dic['info']['start time'], '%m-%d-%Y_%H:%M:%S')
        print("Valutando: " + str(date_i))
        if date_i >=  min_date and date_i < max_date:
            # Needs further investigation
            print("This user " + str(dic['uuid']) + " needs further investigation: " + str(dic['directions']))
            if i['directions'][-1] == dic['directions'][-1]:
                # Case same destination and same time
                print("same destination")
                # TODO sum all contributions 
                list_of_candidate_infected[dic['uuid']]=high_probability_constant
            else:
                print("Deep investigation")
                # Needs path interception check
                itinerary_a = i["directions"]
                itinerary_b = dic["directions"]
                
                # Creo liste di segmenti
                segments_a = list(zip(itinerary_a, itinerary_a[1:] + [itinerary_a[0]]))
                segments_b = list(zip(itinerary_b, itinerary_b[1:] + [itinerary_b[0]]))

                # TODO use to sum all contributions of intersections in paths
                n_intersections = 0

                for segm_a in segments_a:
                    for segm_b in segments_b:
                        a = Point(segm_a[0][0],segm_a[0][1])
                        b = Point(segm_a[1][0],segm_a[1][1])
                        c = Point(segm_b[0][0],segm_b[0][1])
                        d = Point(segm_b[1][0],segm_b[1][1])
    
                        if intersect(a, b, c, d):
                            print("found intersecting path")
                            # TODO sum all contributions
                            list_of_candidate_infected[dic['uuid']]=low_probability_constant
     
        else: 
            # Can be skipped
            pass


print("Number of candidate infeceted based:")
print(len(list_of_candidate_infected))
print(list_of_candidate_infected)
