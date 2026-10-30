#!/usr/bin/env python3
"""Pick the Right Container: see DataChallengeOverview&Steps.md."""

import json

DATA_FILE = "../data/station_taps.csv"  # edit the filepath with the data
with open(DATA_FILE) as f:
    rows = [line.split(",") for line in f.read().splitlines() if line]

header = rows[0]
taps = rows[1:]


# ===== Day 1 =====
# Step 1: Write `scan_for()` and Count Its Comparisons for Three Tap IDs
def scan_for(tap_id, records):
    comparisons = 0
    for row in records:
        comparisons += 1
        if row[0] == tap_id:
            return comparisons
    return comparisons


print("columns:", header)
print("rows in the log:", len(taps))
print("comparisons to find T001:", scan_for("T001", taps))
print("comparisons to find T040:", scan_for("T040", taps))
print("comparisons to find T999:", scan_for("T999", taps))


# Step 1, answer 1:
# T001: 1. Its the first row, the scan should find it on the first check through
# T040: 40. It's the last row, so the scan has to chel all 40 rows to reach it.
# T999: 40. the value doesnt exist so the scan will check all 40 before ending

# Step 1, answer 2:
# Plan around the worst case, 40 (T040 or T999). You can't count on the tap
# being near the top, and a tap that isn't there always costs a full scan.
# The worst case grows with the log: 400 rows would mean 400 checks.


# Step 2: Print Scan Cost at 5 to 40 Rows, Then Count a Nested Pair Loop
for size in [5, 10, 20, 40]:
    worst = scan_for("T999", taps[:size])
    # TODO: print "rows:", `size`, "| worst-case comparisons:", `worst`
    print("rows:", size, "| worst-case comparisons:", worst)
# TODO: assign `pairs` to 0; loop over `taps` with a loop over `taps` inside
pairs = 0
for a in taps:
    for b in taps:
# TODO: add 1 to `pairs` in the inner loop
        pairs += 1
# TODO: print len(taps) and `pairs`
print("rows:", len(taps), "| pairs:", pairs)
# TODO: assign `big` to len(taps) * 10
big = len(taps) * 10
# TODO: print the scan's worst case and the pair loop's count on `big` rows
print("scan worst case on", big, "rows:", big)
print("pair loop on", big, "rows:", big * big)

# Step 2, answer 1:
# Scan worst case: 5 rows = 5, 10 rows = 10, 20 rows = 20, 40 rows = 40 (one check per row)
# Pair loop on 40 rows: 40 x 40 = 1600
# On 400 rows (40 x 10): scan = 400, pair loop = 400 x 400 = 160000
#
# Step 2, answer 2:
# The scan's work grows at the same rate as the rows: 10 times the rows means 10 times the work.
# The pair loop's work grows with the rows times themselves: 10 times the rows means 100 times the work.


# ===== Day 2 =====

# Step 3: Count Taps Per Card With Two Parallel Lists, and Their Comparisons
# TODO: assign `card_ids` to an empty list (each card, first-seen order)
card_ids = []
# TODO: assign `tap_counts` to an empty list (the count for card_ids[i])
tap_counts = []
# TODO: assign `comparisons` to 0
comparisons = 0
# TODO: loop over `taps`; assign `card` to row[1] and `found` to False
for row in taps:
    card = row[1]
    found = False
# TODO: inside it, loop over range(len(card_ids)); add 1 to `comparisons`
    for i in range(len(card_ids)):
        comparisons += 1
# TODO: if card_ids[i] == card, add 1 to tap_counts[i], set found, break
        if card_ids[i] == card:
            tap_counts[i] += 1
            found = True
            break
# TODO: after the inner loop, if not found, append `card` and 1 to the lists
    if not found:
        card_ids.append(card)
        tap_counts.append(1)

busiest = tap_counts.index(max(tap_counts))
print("distinct cards:", len(card_ids))
print("comparisons the two parallel lists needed:", comparisons)
print("busiest card:", card_ids[busiest], "with", max(tap_counts), "taps")

# Step 3, answer 1:
# I expect more than 40, because every tap has to search the card_ids list,
# and that list keeps getting longer as new cards show up (up to 12 cards).
#
# Step 3, answer 2:
# The real count is 190, much more than the 40 rows. Each tap does its own
# scan through card_ids, so the work is rows times the length of the list,
# not just one step per row.


# Step 4: Count Taps Per Card With a Dictionary, and Stations With a Set
# TODO: assign `taps_by_card` to an empty dict (card ID: tap count)
taps_by_card = {}
# TODO: assign `lookups` to 0
lookups = 0
# TODO: loop over `taps`; add 1 to `lookups`
for row in taps:
    lookups += 1
# TODO: add 1 to row[1]'s count in `taps_by_card`, or set it to 1 if new
    card = row[1]
    if card in taps_by_card:
        taps_by_card[card] += 1
    else:
        taps_by_card[card] = 1
# TODO: assign `stations` to set(); loop over `taps` and .add() row[2]
stations = set()
for row in taps:
    stations.add(row[2])
# TODO: assign `repeat_riders` to 0
repeat_riders = 0
# TODO: loop over `taps_by_card`; add 1 to `repeat_riders` if a count is > 1
for card in taps_by_card:
    if taps_by_card[card] > 1:
        repeat_riders += 1

print("distinct cards:", len(taps_by_card))
print("lookups the dictionary needed:", lookups)
print("unique stations:", len(stations), sorted(stations))
print("cards that tapped more than once:", repeat_riders)
print("taps for C001:", taps_by_card["C001"])

# Step 4, answer 1:
# 40 lookups. A dictionary goes straight to the key, so it's one lookup per row,
# and there are 40 rows.
#
# Step 4, answer 2:
# As the Input Size grows, the parallel lists' work grows much faster than the rows,
# because every row has to scan a list that keeps getting longer.
# As the Input Size grows, the dictionary's work grows at the same rate as the rows,
# one lookup each.
#
# Step 4, answer 3:
# taps_by_card (Dictionary): counts taps per card; finds a card directly by its ID.
# stations (Set): keeps unique stations; adding a repeat just does nothing.
# A list for stations would need an "if not in" scan before every add, so the
# more stations there are, the more checks each row costs.
#
# Step 4, answer 4:
# C012. There are 12 distinct cards but only 11 repeat riders, because C012
# only tapped once.




# ===== Day 3 =====

# Step 5: Save the Summary as JSON and Read the TypeError a Set Causes
# TODO: replace each None with your Day 2 value; keep `stations` a set
summary = {
    "service_day": "2026-03-02",
    "total_taps": len(taps),
    "distinct_cards": len(taps_by_card),
    "stations": stations,
    "taps_by_card": taps_by_card,}

print("about to serialize", len(summary), "keys")
# TODO: run the file and answer below before you change anything
# TODO: then put # in front of the next two lines so Step 6 can run
#text = json.dumps(summary, indent=2)
#print(text)

# Step 5, answer 1:
# TypeError: Object of type set is not JSON serializable
#
# Step 5, answer 2:
# The "stations" key broke it. Its value is a set, and JSON has no set type.
# JSON only knows text, numbers, true/false, lists and dictionaries.
#
# Step 5, answer 3:
# Yes, "about to serialize 5 keys" printed before the error, so everything
# above worked and the crash happened on the json.dumps line (line 182).


# Step 6: Write `tap_summary.json`, Reload It, and Check Which Types Survived
# TODO: assign summary["stations"] to a type JSON can hold; keep the key
summary["stations"] = sorted(stations)
# TODO: json.dump() `summary` into a with open("tap_summary.json", "w")
with open("tap_summary.json", "w") as f:
    json.dump(summary, f, indent=2)
# TODO: replace None with json.load() of "tap_summary.json"
with open("tap_summary.json") as f:
    reloaded = json.load(f)

print("total_taps came back as:", reloaded["total_taps"])
print("taps_by_card came back as a", type(reloaded["taps_by_card"]).__name__)
print("C001 straight out of the file:", reloaded["taps_by_card"]["C001"])
print("stations came back as a", type(reloaded["stations"]).__name__)
print("round trip identical:", reloaded["taps_by_card"] == taps_by_card)

# Step 6, answer 1:
# Yes. reloaded["taps_by_card"]["C001"] gives 6 straight from tap_summary.json,
# without opening the raw CSV.
#
# Step 6, answer 2:
# taps_by_card survived ("round trip identical: True"). stations came back as a
# list, not a set, so it lost the set's job: it would now let duplicates in.

# ===== Personal Reflection: How This Data Gets Used in Real Life =====
#
# This data is the kind of thing a transit agency like the MTA collects every
# day. Our file only had 40 taps, but a real agency would have millions.
#
# I think a few different teams would actually use this:
# - Planners could use the busiest stations and times to decide where to add
#   more trains or staff during rush hour.
# - The fare team could look at repeat riders to figure out if weekly or
#   monthly passes are worth offering.
# - Operations could watch for a station that suddenly gets a lot more taps
#   than normal, since that could mean an event or a problem.
#
# This challenge showed me why picking the right container matters. With 40
# rows the list and the dictionary both worked fine, but the list needed 190
# comparisons and the dictionary only needed 40 lookups. At millions of taps,
# that gap would be the difference between a report that runs overnight and
# one that doesn't finish. Saving the summary as JSON also matters, because
# that's how the results get passed to another program, like a dashboard.
#
# One thing I'd keep in mind is privacy. A card ID can show someone's daily
# routine, so this data would need to be protected before anyone uses it.