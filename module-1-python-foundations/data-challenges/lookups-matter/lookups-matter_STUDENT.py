#!/usr/bin/env python3
"""Lookups Matter: see DataChallengeOverview&Steps.md for the steps."""

import csv

DATA_FILE = "member_directory.csv"  # edit the filepath with the data
CHECKINS_FILE = "door_checkins.txt"  # edit the filepath with the data

with open(DATA_FILE, newline="") as f:
    members = list(csv.DictReader(f))


# Step 1: Write `find_linear()` to Return the Member and Its Comparisons
def find_linear(members, member_id):
    # TODO: assign `comparisons` to 0
    comparisons = 0
    # TODO: loop over `members`; add 1 to `comparisons` for every row
    for row in members:
        comparisons += 1
    # TODO: inside the loop, return row, comparisons on a member_id match
        if row ["member_id"] == member_id:
            return row, comparisons
    # TODO: after the loop, return None, comparisons
    return None, comparisons
    


row, count = find_linear(members, "M1150")
print("members in the directory:", len(members))
print("found:", row["name"], "at", row["home_branch"])
print("comparisons:", count)

# Step 1, answer 1:
# I predicted 150 comparisons for M1150 because
# the IDs start at M1001, and 1150 - 1000 = 150.


# Step 2: Total the Comparisons for All 20 Swipes in `door_checkins.txt`
# TODO: open CHECKINS_FILE in a with block as `f`
with open(CHECKINS_FILE) as f:
    swipes = f.read().splitlines()
# TODO: inside it, assign `swipes` to f.read().splitlines()
# TODO: assign `linear_total` and `not_members` to 0
linear_total = 0
not_members = 0
# TODO: loop over `swipes`; call find_linear(members, member_id)
for member_id in swipes:
    row, count = find_linear(members, member_id)
# TODO: print the ID, the name or "NOT A MEMBER", and the comparisons
    if row is None:
        print(member_id, "NOT A MEMBER", count)
        not_members += 1
# TODO: add each count to `linear_total`
# TODO: add 1 to `not_members` for every swipe with no row
    else:
        print(member_id,row["name"], count)

    linear_total += count

print("swipes:", len(swipes), "| not members:", not_members)
print("linear total comparisons:", linear_total)

# Step 2, answer 1:
# I predicted 4, 12, and 27 comparisons for the
# first three swipes, totaling 43.
# A non-member would take 312 comparisons.

# Step 2, answer 2:
# M1313 and M2041 cost the most with 312 comparisons each because they aren't members.
# The linear search checks every row before determining they don't exist.


# Step 3: Build `members_by_id` and Find the Swipe Where It Pays Off
# TODO: assign `members_by_id` to an empty dict and `build_steps` to 0
# TODO: loop over `members`; store each row under row["member_id"]
# TODO: add 1 to `build_steps` for every row
# TODO: write find_dict(members_by_id, member_id)
# TODO: make find_dict() return members_by_id.get(member_id), 1
members_by_id = {}
build_steps = 0

for row in members:
    members_by_id[row["member_id"]] = row
    build_steps += 1

def find_dict(members_by_id, member_id):
    return members_by_id.get(member_id), 1

print("build cost:", build_steps, "| keys in the dict:", len(members_by_id))

# TODO: assign `linear_running` to 0 and `dict_running` to build_steps
linear_running = 0
dict_running = build_steps
pays_off_at = None
swipe_number = 0
# TODO: assign `pays_off_at` to None and `swipe_number` to 0
for member_id in swipes:
    # TODO: add 1 to `swipe_number`
    swipe_number += 1
    _, linear_count = find_linear(members, member_id)
    _, dict_count = find_dict(members_by_id, member_id)
    # TODO: add each search's count to its running total
    # TODO: print swipe_number, the ID and both running totals
    # TODO: the first time dict_running < linear_running, set `pays_off_at`
    linear_running += linear_count
    dict_running += dict_count

    print("swipe", swipe_number, member_id,
          "| linear so far:", linear_running,
          "| dict so far:", dict_running)

    if pays_off_at is None and dict_running < linear_running:
        pays_off_at = swipe_number    

print("dict pays off at swipe:", pays_off_at)
print("morning totals | linear:", linear_running, "| dict:", dict_running)

# Step 3, answer 1:
# I predicted swipe 6 because the linear total
# would exceed the dictionary total by then.

# Step 3, answer 2:
# A dictionary works well because each member
# has a unique ID that can be used as a key.
# At swipe 6 (M1313), linear search had 574
# comparisons while the dict had 318 steps.

# Step 3, answer 3:
# A list would be better if there were only
# a few members or very few searches, because
# building the dictionary has an upfront cost.

# Step 4: Test an AI Speed Claim Against Your Totals and Write a Verdict
# TODO: replace the text below with your AI's claim, word for word
ai_claim = "For 20 lookups among 312 members, a dictionary uses about 20 lookup steps compared with up to 6,240 linear-search comparisons. " \
"However, building the dictionary requires 312 additional steps, bringing its total to 332."
print("AI CLAIM:", ai_claim)

# TODO: unpack find_linear() for swipes[0] into `_, front_count`
# TODO: unpack find_linear() for "M1313" into `_, absent_count`
# TODO: assign `ratio` to round(linear_running / dict_running, 1)

_, front_count = find_linear(members, swipes[0])
_, absent_count = find_linear(members, "M1313")

ratio = round(linear_running / dict_running, 1)

print("one front-of-file swipe | linear:", front_count, "| dict: 1")
print("one non-member swipe | linear:", absent_count, "| dict: 1")
print("whole morning | linear:", linear_running, "| dict:", dict_running,
      "| ratio:", ratio)

# TODO: replace the text below with your own verdict
verdict = (
    "Linear search is O(n) because it checks rows one at a time. "
    "Dictionary lookup is O(1) average-case because it uses a key. "
    "My linear search took 2924 comparisons, while the dictionary "
    "took 332 steps including the build cost. The dictionary was "
    "8.8 times more efficient.")

print("VERDICT:", verdict)

# Step 4, answer 1:
# The AI calculated 332 dictionary steps,
# including the cost. It also correctly described
# the worst-case linear total as 6240, but the actual
# number was 2924. The first swipe took 4 linear
# comparisons and a non-member took 312.

# Step 4, answer 2:
# Yes, the AI counted all 312 build steps.
# After comparing my actual totals, it clarified
# that 6240 was a worst-case estimate.
# The actual ratio was 2924 / 332 = 8.8.
