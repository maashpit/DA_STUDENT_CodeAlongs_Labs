#!/usr/bin/env python3
"""Looks Right. Is It?: see DataChallengeOverview&Steps.md for the steps."""

DATA_FILE = "timesheet_hours.csv"  # edit the filepath with the data

with open(DATA_FILE) as f:
    lines = f.read().splitlines()


# Before you write any code:
# 1. Each CSV row represents one employee working on one day.
# 2. employee_id, name, and day are text. Hours is an integer,
#    and rate is a decimal number (float).
# 3. The CSV has five employees with no missing fields.
#    The original Python staff list contains E106 instead of E104.


# ===== Day 1 =====

# Step 1: Follow the TypeError in `weekly_hours()` Back to Its Cause
# TODO: run the file as given and read the traceback from the bottom up
# TODO: add print(repr(hours)) as the first line of add_hours(); run again
# TODO: find that printed value in the CSV
# TODO: fix the line that reads the wrong column to read the hours column
# TODO: wrap that value in int() so add_hours() adds a number
# TODO: delete the print(repr(hours)) line once Rosa's total is right

def add_hours(total, hours):
    # Original debugging print:
    # print(repr(hours))
    return total + hours


def weekly_hours(lines, emp_id):
    total = 0
    for row in lines[1:]:
        parts = row.split(",")
        if parts[0] == emp_id:
            # Original incorrect code:
            # total = add_hours(total, parts[2])

            # Fixed: use the hours column and convert to integer
            total = add_hours(total, int(parts[3]))
    return total


print("Rosa Alvarez, weekly hours:", weekly_hours(lines, "E101"))


# Step 1, answer 1:
# Rosa (E101): 8 + 8 + 8 + 8 + 8 = 40 hours.
# I added up all five of her daily entries from the CSV.
#
# Step 1, answer 2:
# - Start at the bottom. The last line tells you the type of error.
# - The lines above show the file, function, and line where it happened.
# - I learned this from our Day 10 traceback lesson and Python's
#   traceback output.
#
# Step 1, answer 3:
# The traceback ended in add_hours() at "return total + hours".
# The actual bug was in weekly_hours(), where parts[2] was reading
# the day instead of the hours.
# I changed it to int(parts[3]) to read the correct column as a number.
#


# Step 2: Trace the ZeroDivisionError Back to the Hand-Typed Staff List
# TODO: run the file as given; note the last ID that printed
# TODO: compare every ID in `staff` with the IDs in the CSV
# TODO: replace the hand-typed `staff` list with an empty list
# TODO: loop over lines[1:]; append each row's employee ID to `staff` once
# TODO: print "employees in the file:" and len(staff)

def days_worked(lines, emp_id):
    days = 0
    for row in lines[1:]:
        if row.split(",")[0] == emp_id:
            days = days + 1
    return days


# Original incorrect staff list:
# staff = ["E101", "E102", "E103", "E106", "E105"]

# Fixed: build the staff list directly from the CSV
staff = []

for row in lines[1:]:
    emp_id = row.split(",")[0]
    if emp_id not in staff:
        staff.append(emp_id)

print("employees in the file:", len(staff))


for emp_id in staff:
    hours = weekly_hours(lines, emp_id)
    days = days_worked(lines, emp_id)

    # Original code printed hours instead of the average:
    # print(emp_id, "| hours:", hours, "| days:", days,
    #       "| average per day:", hours)

    # Fixed: divide total hours by days worked
    print(emp_id, "| hours:", hours, "| days:", days,
          "| average per day:", hours / days)


# Step 2, answer 1:
# There are 5 employees in the CSV.
# Their IDs are E101, E102, E103, E104, and E105.
#
# Step 2, answer 2:
# With the intended hours / days calculation, 3 employee lines
# printed before the crash. E103 was the last ID printed.
# The program then crashed while trying to process E106.
# The pasted starter code printed hours instead of dividing,
# so that version would not raise ZeroDivisionError until fixed.
#
# Step 2, answer 3:
# The bug was in the hand-typed staff list, not the division itself.
# E106 did not exist in the CSV, so days_worked() returned zero.
# Building the list from the CSV prevents nonexistent IDs.
#


# ===== Day 2 =====

# Step 3: Find Why Four of the Five Weekly Hour Totals Are Wrong
# TODO: add up Rosa's (E101) and Mei's (E103) hours by hand first
# TODO: print("starting", emp, "total is", total) first in the outer loop
# TODO: move the line that sets `total` inside the outer loop
# TODO: delete the "starting" print once all five totals are right

records = []

for row in lines[1:]:
    emp_id, name, day, hours, rate = row.split(",")
    records.append({"id": emp_id, "name": name, "day": day,
                    "hours": int(hours), "rate": float(rate)})


employee_ids = []

for r in records:
    if r["id"] not in employee_ids:
        employee_ids.append(r["id"])


# Original incorrect placement:
# total = 0

for emp in employee_ids:
    # Fixed: reset total for each employee
    total = 0

    # Temporary debugging print from the TODO:
    # print("starting", emp, "total is", total)

    name = ""

    for r in records:
        if r["id"] == emp:
            name = r["name"]
            total = total + r["hours"]

    print(emp, name, "| weekly hours:", total)


# Step 3, answer 1:
# Rosa (E101): 8 + 8 + 8 + 8 + 8 = 40 hours.
# Mei (E103): 6 + 7 + 8 + 6 + 5 = 32 hours.
# I checked both totals against the CSV.
#
# Step 3, answer 2:
# Before the fix, total started at 0 for Rosa but kept her
# 40 hours when moving to E102.
# Each employee started with the previous employees' hours.
# The problem was that total = 0 was outside the outer loop.
# Moving it inside makes every employee start at zero.
#
# Step 3, answer 3:
# Rosa's number was correct because she was the first employee,
# so the running total started at zero.
# Priya was last, so her total included all five employees' hours.
# Resetting total inside the loop gives each employee their own sum.
#


# Step 4: Fix Two Overtime Bugs That Overpay the Firm by $1,810 a Week
# TODO: work out Rosa's, Darnell's and Mei's pay by hand first
# TODO: fix weekly_pay() so it follows the handbook rule word for word
# TODO: fix the other line that compares `total` against 40 the same way

def weekly_pay(hours, rate):
    # Original incorrect code:
    # if hours >= 40:
    #     return hours * rate * 1.5
    # return hours * rate

    # Fixed: first 40 hours are regular pay
    # Only hours beyond 40 get time-and-a-half
    if hours > 40:
        return 40 * rate + (hours - 40) * rate * 1.5

    return hours * rate


owed_overtime = 0
payroll = 0.0

for emp in employee_ids:
    total = 0
    name = ""
    rate = 0.0

    for r in records:
        if r["id"] == emp:
            name = r["name"]
            rate = r["rate"]
            total = total + r["hours"]

    # Original incorrect condition:
    # if total >= 40:

    # Fixed: overtime begins after 40 hours
    if total > 40:
        owed_overtime = owed_overtime + 1

    pay = weekly_pay(total, rate)
    payroll = payroll + pay

    print(f"{name:16} {total:3} hrs  ${pay:>9,.2f}")


print("employees owed overtime:", owed_overtime)
print(f"TOTAL PAYROLL: ${payroll:,.2f}")


# Step 4, answer 1:
# Rosa (40 hours at $24.00):
# 40 x $24.00 = $960.00
#
# Darnell (46 hours at $31.50):
# 40 x $31.50 = $1,260.00
# 6 x ($31.50 x 1.5) = $283.50
# Total = $1,543.50
#
# Mei (32 hours at $28.00):
# 32 x $28.00 = $896.00
#
# All three calculations match the handbook overtime rule.
#
# Step 4, answer 2:
# Bug 1 was in weekly_pay().
# It multiplied all hours by 1.5 when someone worked 40 or more.
# I changed it so the first 40 hours receive regular pay,
# and only the extra hours receive 1.5 times the regular rate.
#
# Bug 2 was in the overtime employee count.
# The condition total >= 40 incorrectly counted employees
# who worked exactly 40 hours.
# I changed it to total > 40.
#
# Step 4, answer 3:
# Rosa worked exactly 40 hours, so she should receive regular pay
# and should not count as an overtime employee.
# Her case catches the incorrect >= comparison because exactly
# 40 is the boundary between regular hours and overtime.
# Someone working below or above 40 would not catch that
# specific boundary mistake.
#