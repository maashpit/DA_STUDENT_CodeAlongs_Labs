#!/usr/bin/env python3
"""Meet the Objects: see DataChallengeOverview&Steps.md for the steps."""

import json

DATA_FILE = "../data/bike_stations.json"  # edit the filepath with the data

with open(DATA_FILE) as f:
    stations = json.load(f)


# ===== Day 1 =====

# Step 1: Reproduce the Parallel-List Bug and Name the Wrong Stations
# TODO: assign `names` and `bikes` to two empty lists
names = []
bikes = []
# TODO: loop over `stations`; append each one's "name" to `names`
# TODO: append the same station's "bikes_available" to `bikes`
for station in stations:
    names.append(station["name"])
    bikes.append(station["bikes_available"])
names.pop(2)

print("stations in the file:", len(stations))
# TODO: loop over range(len(names)); print names[i], "|", bikes[i], "bikes"
for i in range(len(names)):
    print(names[i], "|", bikes[i], "bikes")
# Step 1, answer 1:
# Each record is one bike station, stored as a dictionary.
# Numbers: capacity, bikes_available. Text: name, station_id.
# needs_maintenance is True/False. What looks wrong: [describe it]
#
# Step 1, answer 2:
# .pop(2) removes the item at index 2 from names and returns that
# removed name. Every name after it shifts left one spot, so names
# ends up one shorter than bikes.
#
# Step 1, answer 3:
# Every station after the popped one got the count of the station
# before it: [name at old index 3] got [name at old index 2]'s count,
# and so on to the end. Nobody sees the real count of the last
# station, [last station's name], because the loop stops early.


# Step 2: Define the Station Class and Prove Two Instances Are Independent
class Station:
    # TODO: add __init__ with name (str), capacity and bikes_available (int)
    # TODO: in __init__, assign each parameter to self.<same name>
    def __init__(self, name, capacity, bikes_available, station_id, needs_maintenance):
        self.name = name
        self.capacity = capacity
        self.bikes_available = bikes_available
        # TODO: add a parameter and self.<name> for each extra field you agreed
        self.station_id = station_id
        self.needs_maintenance = needs_maintenance

    # TODO: add needs_restock(self): True if bikes_available < capacity / 4
    def needs_restock(self):
        return self.bikes_available < self.capacity / 4


# TODO: assign `fleet` to []; loop over `stations` as `s`
fleet = []
for s in stations:
    # TODO: append Station(s["name"], s["capacity"], s["bikes_available"])
    fleet.append(Station(s["name"], s["capacity"], s["bikes_available"],
                         s["station_id"], s["needs_maintenance"]))

# TODO: assign `busy`, `quiet` to two stations with equal needs_restock()
busy = fleet[0]
quiet = fleet[1]

# TODO: print both needs_restock() answers
print(busy.name, busy.needs_restock())
print(quiet.name, quiet.needs_restock())

# TODO: set busy.bikes_available to 0, then print both answers again
busy.bikes_available = 0
print(busy.name, busy.needs_restock())
print(quiet.name, quiet.needs_restock())

# Step 2, answer 1:
# name - "which station"
# capacity - "how many docks it has"
# bikes_available - "how many bikes are there right now"
# station_id - [dispatcher's phrase, e.g. "the station number"]
# needs_maintenance - [dispatcher's phrase, e.g. "is it broken"]
#
# Step 2, answer 2:
# [Where your lists differed, what each of you argued, which you kept]
#
# Step 2, answer 3:
# I left out [field] because the dispatcher only needs to know where
# a station is and whether it needs bikes, not [what that field is].
#
# Step 2, answer 4:
# Before: [busy name] -> [False], [quiet name] -> [False]
# After setting [busy name]'s bikes to 0: [busy] -> True, [quiet] -> False
# Only the station I changed moved, so each Station keeps its own
# bikes_available. Changing one object does not change the other.


# ===== Day 2 =====

# Step 3: Add `__str__` and Find Out Which of Four Prints It Changes
print(fleet[0])
print(fleet[:2])


# TODO: copy your Station class from Step 2 here
class Station:
    def __init__(self, name, capacity, bikes_available, station_id, needs_maintenance):
        self.name = name
        self.capacity = capacity
        self.bikes_available = bikes_available
        self.station_id = station_id
        self.needs_maintenance = needs_maintenance

    def needs_restock(self):
        return self.bikes_available < self.capacity / 4

    # TODO: add __str__(self) to return text like "Grand Army Plaza: 6 of 48 bikes"
    # TODO: build it from self.name, self.bikes_available and self.capacity
    def __str__(self):
        return f"{self.name}: {self.bikes_available} of {self.capacity} bikes"


# TODO: rebuild `fleet` from this class with the same loop as Step 2
fleet = []
for s in stations:
    fleet.append(Station(s["name"], s["capacity"], s["bikes_available"],
                         s["station_id"], s["needs_maintenance"]))

print(fleet[0])
print(fleet[:2])

# Step 3, answer 1:
# 1. print(fleet[0]) before __str__: <__main__.Station object at 0x...>
# 2. print(fleet[:2]) before __str__: [<...Station object...>, <...>]
# 3. print(fleet[0]) after __str__: Grand Army Plaza: 6 of 48 bikes
# 4. print(fleet[:2]) after __str__: [prediction you made]
#
# Step 3, answer 2:
# Print 4 was wrong: the list still showed the ugly object text.
# A list displays its items with __repr__, not __str__.


## Step 4: Add `__repr__` and Print the Van List for You and the Dispatcher
# TODO: copy your Station class from Step 3 here
class Station:
    def __init__(self, name, capacity, bikes_available, station_id, needs_maintenance):
        self.name = name
        self.capacity = capacity
        self.bikes_available = bikes_available
        self.station_id = station_id
        self.needs_maintenance = needs_maintenance

    def needs_restock(self):
        return self.bikes_available < self.capacity / 4

    def __str__(self):
        return f"{self.name}: {self.bikes_available} of {self.capacity} bikes"

    # TODO: add __repr__(self) to return text like "Station('Grand Army Plaza', 6)"
    def __repr__(self):
        return f"Station('{self.name}', {self.bikes_available})"


# TODO: rebuild `fleet` from this class with the same loop as Step 2
fleet = []
for s in stations:
    fleet.append(Station(s["name"], s["capacity"], s["bikes_available"], s["station_id"], s["needs_maintenance"]))

# TODO: assign `van_list` to []; loop over `fleet`
van_list = []
for station in fleet:
    # TODO: append each station whose needs_restock() returns True to `van_list`
    if station.needs_restock():
        van_list.append(station)

print(van_list)
for station in van_list:
    print(station)

# Step 4, answer 1:
# I predict [N] stations land in van_list. print(van_list) will use
# __repr__ because it is printing a list.
#
# Step 4, answer 2:
# __str__ is the readable answer for a dispacher: name and bikes.
# __repr__ is for me, the programmer: it shows exactly which object
# I'm holding, written like code (Station('Name', 6)).
#
# Step 4, answer 3:
# I'd hand the dispatcher the one-per-line printout, because it reads
# like a sentence ("X: 3 of 40 bikes") and shows capacity too.
