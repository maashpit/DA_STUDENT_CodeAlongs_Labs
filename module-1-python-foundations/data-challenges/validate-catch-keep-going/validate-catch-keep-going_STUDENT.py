#!/usr/bin/env python3
"""Validate, Catch, Keep Going: see DataChallengeOverview&Steps.md."""

DATA_FILE = "../data/service_requests.csv"  # edit the filepath with the data

# Open the file and split it into a list with one string per line.
with open(DATA_FILE) as f:
    lines = f.read().splitlines()

# The first line is the column names. Every line after it is a row of data.
# "if line" drops any blank lines.
header = lines[0]
rows = [line for line in lines[1:] if line]


# ===== Day 1 =====

# Step 1: Write `validate_request()` to Return a Verdict and a Reason

# Constants hold the rules, so each rule lives in one easy-to-find place.
EXPECTED_FIELDS = 5
ALLOWED_STATUS = ["Open", "In Progress", "Closed"]


def validate_request(row):
    # Cut the row at each comma. This gives a list of its fields.
    fields = row.split(",")

    # Rule 1: check the field count first. Unpacking a row that doesn't have
    # exactly 5 fields would crash on the next line.
    if len(fields) != EXPECTED_FIELDS:
        # str() turns the number into text so it can join the message.
        return False, "wrong field count: " + str(len(fields))

    # Give each of the 5 fields a name that matches the header.
    request_id, complaint_type, borough, days_open, status = fields

    # Rule 2: the borough can't be empty.
    if borough == "":
        return False, "borough is empty"

    # Rule 3: the status must be on the allowed list.
    if status not in ALLOWED_STATUS:
        return False, "status not allowed: " + status

    # The row only reaches this line if it passed all three rules.
    return True, "ok"


# Test three rows before running the whole file:
# one good row, one with no borough, and one with a bad status.
print(validate_request("SR-1001,Noise - Residential,Brooklyn,3,Closed"))
print(validate_request("SR-1004,Rodent,,6,Closed"))
print(validate_request("SR-1009,Water System,Queens,4,Escalated"))

# Step 1, answer 1:
# Each row is one 311-style service request with five fields: request ID,
# complaint type, borough, days open, and status. A few rows already look wrong.
# SR-1004 has no borough, SR-1009 has the status "Escalated," and SR-1011 is
# missing a field. In days_open, watch out for "3 days" in SR-1007 and -3 in
# SR-1013, because neither one is a valid day count.
# Step 1, answer 2:
# The caller takes the values apart with ok, reason = validate_request(row).
# The function is really handing back one tuple holding two values.


# Step 2: Run All 15 Rows Through the Validator and Report Each Rejection

# valid is an accumulator. It starts at 0 and grows inside the loop.
valid = 0

for row in rows:
    # Unpack the returned tuple into its verdict and its reason.
    ok, reason = validate_request(row)
    if ok:
        valid += 1
    else:
        # [0] is the first field, which is the request ID.
        print(row.split(",")[0], "REJECTED -", reason)

print("header:", header)
print("rows read:", len(rows))
print("passed Day 1 validation:", valid)

# Step 2, answer 1:
# Before running this, I hand-checked all 15 rows against our three rules, and
# 3 rows should fail. SR-1004 breaks the empty borough rule, SR-1009 breaks the
# allowed status rule, and SR-1011 breaks the field count rule.
# Step 2, answer 2:
# SR-1007 ("3 days") and SR-1013 (-3) got through. The validator only checks
# field count, borough, and status, so it never looks at days_open.


# ===== Day 2 =====

# Step 3: Build the Days-Open Report With No Protection and Watch It Crash
# This step is commented out so Step 4 can run. To see the crash, remove the #
# from the code below, run the file, then put the # back.

# total_days = 0
# counted = 0
# for row in rows:
#     ok, reason = validate_request(row)
#     # continue skips the rest of this pass and moves to the next row.
#     if not ok:
#         continue
#     # [3] is the fourth field. Counting starts at 0.
#     # int() crashes here on SR-1007 because "3 days" isn't a whole number.
#     days_open = int(row.split(",")[3])
#     total_days += days_open
#     counted += 1
#     print(row.split(",")[0], "days open:", days_open)
#
# print("average days open:", total_days / counted)

# Step 3, answer 1:
# 5 report lines print before it crashes. SR-1007 stops it.
# Step 3, answer 2:
# ValueError: invalid literal for int() with base 10: '3 days'
# 5 rows were counted before the crash.
# Step 3, answer 3:
# SR-1008 through SR-1015 are never reached, so they aren't checked or counted, and the average never prints.


# Step 4: Rebuild the Report So Every Row Is Counted or Skipped


def check_days_open(value):
    # try runs code that might raise an error.
    try:
        days = int(value)
    # except runs only if int() raises a ValueError, as it does for "3 days".
    # Naming ValueError means other kinds of errors aren't hidden.
    except ValueError:
        return False, "days_open is not a number: " + value

    # int("-3") works, so the try can't catch it. An if has to check the rule.
    if days < 0:
        return False, "days_open is negative: " + value

    return True, "ok"


# Exceeds (Functions): a third check for another field.
# validate_request only catches an empty borough. This also catches typos.
ALLOWED_BOROUGHS = ["Manhattan", "Brooklyn", "Queens", "Bronx", "Staten Island"]


def check_borough(value):
    if value not in ALLOWED_BOROUGHS:
        return False, "borough not recognized: " + value
    return True, "ok"


# Exceeds (Problem Solving): test one more bad value.
# Prediction: "3.5" will be caught by the try, because int() can't convert
# text with a decimal point and raises ValueError.
print(check_days_open("3.5"))

# Test the new function with one good borough and one typo.
print(check_borough("Brooklyn"))
print(check_borough("Brookyln"))

# Reset the accumulators. skipped is new, so every row gets accounted for.
total_days = 0
counted = 0
skipped = 0

for row in rows:
    # First check: is the row's structure good?
    ok, reason = validate_request(row)

    # Second check: runs only if the first one passed. It overwrites ok and
    # reason with its own result.
    if ok:
        ok, reason = check_days_open(row.split(",")[3])

    # Third check: runs only if the row has passed so far.
    if ok:
        ok, reason = check_borough(row.split(",")[2])

    # ok is True here only if the row passed all three checks.
    if ok:
        total_days += int(row.split(",")[3])
        counted += 1
    else:
        skipped += 1
        print(row.split(",")[0], "SKIPPED -", reason)

print("counted:", counted, "| skipped:", skipped)
# round(..., 1) keeps one decimal place.
print("average days open:", round(total_days / counted, 1))

# Exceeds (Attention to Detail): the program checks its own sum.
if counted + skipped != len(rows):
    print("WARNING: counted + skipped does not match the row count:", counted + skipped, "vs", len(rows))
else:
    print("all rows accounted for:", counted, "+", skipped, "=", len(rows))

# Step 4, answer 1:
# 5 rows get skipped: SR-1004, SR-1007, SR-1009, SR-1011, and SR-1013. The Day 1
# validator let SR-1007 and SR-1013 through.
# Step 4, answer 2:
# A try caught "3 days" because int() raises ValueError on it. An if could also
# catch it by checking the text first. An if caught -3. A try alone could not,
# because int("-3") works and raises no error.
# Step 4, answer 3:
# Yes. 10 counted + 5 skipped = 15 rows.