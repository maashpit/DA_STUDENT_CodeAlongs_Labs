#!/usr/bin/env python3
"""Data Challenge: Build It Once, Use It Again
GitBook Quest 1.2: Build It Once, Use It Again

HOW TO RUN
    Open a terminal in the folder that holds data/ and run:
        python3 build-it-once_STUDENT.py
    If this file sits one folder below data/, run it from the folder
    above instead:  python3 build-it-once/build-it-once_STUDENT.py
    Or make it executable once:
        chmod +x build-it-once_STUDENT.py
    and from then on run it directly:
        ./build-it-once_STUDENT.py
    The first line, #!/usr/bin/env python3 (the "shebang"), is what
    makes ./ work. python3 <file> ignores it as a comment.

THE DATA      data/rec_center_signups.txt

ANSWER EVERYTHING IN THIS FILE
    - Code goes under each step's banner.
    - Written answers go in # comments under each "# Your answer:"
      line.
    - Run the file after every change. It runs top to bottom, so a
      later step can use anything an earlier step made.

HINTS live in the worksheet (DataChallengeOverview&Steps.md), collapsed
under each step. Open one only when you are stuck.

AI TOOLKIT: prompts to try and how to check them are in
DataChallengeOverview&Steps.md.

SUBMIT
    Commit this file (you may rename it build-it-once.py) to your own data
    challenge repo, inside your Module 1 folder. Paste its direct GitHub URL
    into the LMS.
    Submit once, at the end of Day 3. Keep every day's work in here.
"""

############################################################################
#  THE DATA: open data/rec_center_signups.txt and look at it
#  before you write any code. The worksheet's "The Data" section
#  shows how to load it.
############################################################################

# 1. What does one row represent?
# Your answer:
# Each row is one person signing up for one class, and how many sessions
# they booked. Like "Nia,Yoga,4" is just Nia doing Yoga for 4 sessions.

# 2. Which fields hold numbers, and which hold text?
# Your answer:
# The name and the class are text. Sessions is a number, but Python reads
# it in as text, so I have to wrap it in int() before I can add anything.

# 3. What already looks wrong, missing or inconsistent?
# Your answer:
# Nothing's blank or broken this time. The top two lines are just # notes,
# not real data, so those get skipped. The other thing is people show up
# more than once and there's no ID, so the name is the only way to match
# them. If someone typed "nia" instead of "Nia" it'd count as a whole
# different person.

############################################################################
#  DAY 1
############################################################################

# ===== Step 1: Write total_sessions(), Then Call It on Every Class and on Swim Only =====
# One function that adds up a sessions column, called twice: once on every
# record, once on just the Swim records.
#
# 1. Predict two numbers by hand off the file. Total sessions across every
#    class: add the third field down all 13 records. Total sessions for Swim
#    only: add that same field, but only on the records whose class is Swim.
#    Write both in a comment before you run anything.
# 2. Write total_sessions(records) so it adds up the sessions column across
#    every record in records and hands the total back with return, not
#    print.
# 3. Build swim_only: the records whose class is Swim, and nothing else.
# 4. Run it, and check both printed numbers against your two predictions.
#
# The arithmetic is the same arithmetic a plain loop would do. What changes
# is that the answer comes back to you instead of going to the screen.

# Prediction: I added up the whole sessions column and got 45.
# Prediction: Swim only is Omar 2, Rafi 5, Nia 2, Gwen 6, so 15.

with open("../data/rec_center_signups.txt") as f:
    signups = [line for line in f.read().splitlines()
               if line and not line.startswith("#")]

def total_sessions(records):
    # TODO: add up the sessions column across every record in `records`
    total = 0
    for record in records:
        total += int(record.split(",")[2])
    # TODO: hand the total back to whoever called this. Do not print it.
    return total

swim_only = []
# TODO: fill swim_only with just the Swim records
for record in signups:
    if record.split(",")[1] == "Swim":
        swim_only.append(record)

print("every class:", total_sessions(signups))
print("swim only:  ", total_sessions(swim_only))

# ===== Step 2: Count Long Bookings at Two Different Cutoffs With One Function =====
# The board changed the long-booking cutoff from 4 sessions to 2. Answering
# both should cost you one extra argument, not a second function.
#
# 1. Predict both returned: counts in a comment, reading the third field
#    down the file: once for 4 or more, once for 2 or more.
# 2. Write count_long_bookings(records, minimum) so it counts the records
#    whose sessions number is minimum or more, and returns that count.
# 3. Write show_long_bookings(records, minimum) so it prints a sentence with
#    the same count in it. Only print. Do not add a return.
# 4. Run the whole file, including the lines at the bottom that were written
#    for you.
# 5. Write down what handed_back holds, and why. It is on the last printed
#    line.
# 6. Name the parameter and the arguments, pointing at the lines: which name
#    is minimum, and which values are the 4 and the 2.
#
# One of the two functions you just wrote gives you something back. The
# other only puts something on the screen.

# Prediction: 4 or more should be 7. The only ones under 4 are the 1s,
# the 2s and Omar's 3.
# Prediction: 2 or more should be 11. Everything except the two 1s.

def count_long_bookings(records, minimum):
    # TODO: count the records whose sessions number is `minimum` or more
    count = 0
    for record in records:
        if int(record.split(",")[2]) >= minimum:
            count += 1
    # TODO: return the count
    return count

def show_long_bookings(records, minimum):
    # TODO: print a sentence with the same count in it. Only print.
    print(count_long_bookings(records, minimum), "bookings have",
          minimum, "or more sessions")

print("returned:", count_long_bookings(signups, 4))
print("returned:", count_long_bookings(signups, 2))

handed_back = show_long_bookings(signups, 4)
print("what show_long_bookings handed back:", handed_back)

# Your answer:
# handed_back is None. show_long_bookings prints the number on the screen
# but never returns it, so there's nothing to hand back.
# minimum is the parameter, it's the name up in the def line. The 4 and
# the 2 are the arguments, they're what I actually pass in when I call it.

# ----- Share Out: Day 1 -----
# Last 15 minutes, back together as a class. Bring:
#
# - Your two totals. Whole file, and Swim only. If your numbers differ from
#   another group's, say so. You read the same file, so one of you has a bug
#   worth finding.
# - Your function next to the loop it replaced. Name the specific thing that
#   got easier. Not "cleaner."
# - What show_long_bookings handed back, and why. Say what that tells you
#   about return versus print.
# - Which name is the parameter and which value is the argument, pointing at
#   your own two lines.
#
# Be ready to answer "why did you do it that way?"

# Your notes for the share out:
# I got 45 for everything and 15 for Swim.
# What got easier is I didn't have to write the loop twice. For Swim I just
# called the same function on a smaller list. When the cutoff changed I
# just changed the number I passed in, no new function.
# Print just shows you the number. Return actually gives it back so you can
# save it or use it somewhere else.

############################################################################
#  DAY 2
############################################################################

# ===== Step 3: Count the Same Bookings Without a Cutoff Parameter, and Compare =====
# Two functions that answer the same question. The one you wrote on Day 1
# takes the cutoff as a parameter. This one takes no cutoff at all.
#
# 1. Predict both printed counts with no new arithmetic. You already
#    produced the count at a cutoff of 4 and the count at a cutoff of 2 in
#    Day 1's second step. All you are predicting here is which of those two
#    numbers each of the two identical-looking calls prints. Write both in a
#    comment, and write why.
# 2. Write count_reaching_outside(records) so it counts the same thing
#    count_long_bookings does, but takes no minimum parameter. It reads
#    sessions_cutoff from outside the function instead.
# 3. Call it once at a cutoff of 4, printing the result.
# 4. Call it again, unchanged, after sessions_cutoff becomes 2, and print
#    that result too. The call line is identical both times.
# 5. Print count_long_bookings(signups, 4) underneath for comparison.
#
# Both versions run clean. Decide which of the two you would trust in a file
# you did not write, and say what in the call line told you.

# Prediction: First one prints 7, second one prints 11. The lines look the
# exact same, but the function grabs sessions_cutoff from outside, and that
# got switched from 4 to 2 in between the two calls.

sessions_cutoff = 4

def count_reaching_outside(records):
    # TODO: same count as count_long_bookings, but take NO minimum
    # parameter. Read sessions_cutoff from outside the function instead.
    count = 0
    for record in records:
        if int(record.split(",")[2]) >= sessions_cutoff:
            count += 1
    return count

print("cutoff", sessions_cutoff, "gives", count_reaching_outside(signups))

sessions_cutoff = 2

# TODO: call count_reaching_outside(signups) again, unchanged, and print it
print("cutoff", sessions_cutoff, "gives", count_reaching_outside(signups))
# TODO: print count_long_bookings(signups, 4) underneath for comparison
print("count_long_bookings(signups, 4):", count_long_bookings(signups, 4))

# ===== Step 4: Pass the Last Member In and Out, Then Trigger an UnboundLocalError =====
# The coordinator wants each sign-up printed next to the one before it. The
# top half is yours to write. The bottom half is written for you, and is
# supposed to raise.
#
# 1. Write log_signup(record, previous_member) so it pulls the member name
#    out of record, prints the previous member and this one on one line, and
#    returns this member's name.
# 2. Call it on signups[0], then on signups[1], storing what it returns back
#    into last_member each time. Predict both printed lines in a comment
#    first, reading the names off the top of the file.
# 3. Leave log_signup_broken exactly as written. It tries the same job by
#    reading and then updating last_seen, a name defined above the function.
# 4. Predict in a comment whether its print line will work. The step above
#    showed a function reading an outside name just fine.
# 5. Run the file, read the traceback, and write down the exception name,
#    the variable and the line it points at, in your own words, before you
#    look anything up.
#
# global is not the fix. The working half of this same step already shows
# what is: pass the value in, return it back out.
#
# This step is supposed to raise UnboundLocalError. Run it, read the
# traceback, answer below, then put a # in front of the line that raises so
# the steps after it can run.

# Prediction: "previous: nobody yet | this: Nia"
#             "previous: Nia | this: Omar"
# Prediction for the broken one: I thought the print would work, since
# Step 3 read an outside variable with no problem.

def log_signup(record, previous_member):
    # TODO: pull the member name out of `record`
    member = record.split(",")[0]
    # TODO: print the previous member and this one on one line
    print("previous:", previous_member, "| this:", member)
    # TODO: return this member's name
    return member

last_member = "nobody yet"
# TODO: call log_signup on signups[0], then on signups[1], storing
# what it returns back into last_member each time
last_member = log_signup(signups[0], last_member)
last_member = log_signup(signups[1], last_member)

last_seen = "nobody yet"

def log_signup_broken(record):
    # Leave this body exactly as written. It is supposed to raise.
    print("previous:", last_seen)
    last_seen = record.split(",")[0]
    return last_seen

# log_signup_broken(signups[2])

# Your answer:
# It crashed with UnboundLocalError on last_seen, pointing at the print
# line. Since the function sets last_seen on the next line, Python decides
# last_seen belongs to the function the whole time. So when the print
# tries to use it, it doesn't have a value yet.

# ----- Share Out: Day 2 -----
# Last 15 minutes, back together as a class. Bring:
#
# - Which of the two functions you would trust in a file you did not write,
#   and what in the call line decided it.
# - The exception name and the variable it named, plus your own one-sentence
#   account of the rule. Written before you looked anything up.
# - Why the print line failed when it only reads last_seen, and what
#   deleting the line below it changed.
# - Anything AI told you about global. Say whether it offered it as the fix,
#   and what you did instead.
#
# Be ready to answer "why did you do it that way?"

# Your notes for the share out:
# I'd trust count_long_bookings, because you can see the 4 right in the
# call. With count_reaching_outside you can't tell what it's gonna use,
# and the same exact line gave me 7 and then 11.
# The rule: if a function sets a variable anywhere inside it, that
# variable counts as the function's own the whole way through. If you
# delete the line that sets it, the print works again, because now it's
# only reading it, so Python looks outside.
# You don't need global. Just pass it in and return it back out, like
# log_signup does.

############################################################################
#  DAY 3
############################################################################

# ===== Step 5: Build Per-Member Totals Out of Three Functions, Not One =====
# The coordinator wants per-member totals. Write this as three functions,
# not one.
#
# 1. Write sessions_in(record) so it pulls the sessions number out of a
#    single record and returns it.
# 2. Write signups_for(records, member) so it returns just the records
#    belonging to one member.
# 3. Write total_for(records, member) so it returns that member's total
#    sessions, doing almost nothing itself. It gets its work done by calling
#    the other two.
# 4. Predict Gwen's total in a comment, adding up Gwen's rows in the file by
#    hand.
# 5. Print one line per member for Nia, Omar, Tess, Rafi and Gwen, and check
#    Gwen's line against your comment.
#
# Before you run it, show your partner the line where each of the three
# functions gets called.

# Prediction: Gwen has Pottery 2 and Swim 6, so 8.

# Three function names. Everything else is yours.

def sessions_in(record):
    return int(record.split(",")[2])

def signups_for(records, member):
    matches = []
    for record in records:
        if record.split(",")[0] == member:
            matches.append(record)
    return matches

def total_for(records, member):
    # This one should get its work done by calling the other two.
    total = 0
    for record in signups_for(records, member):
        total += sessions_in(record)
    return total

# TODO: print a line per member
members = ["Nia", "Omar", "Tess", "Rafi", "Gwen"]
for member in members:
    print(member, total_for(signups, member))

# ===== Step 6: Run total_for() on Five Inputs Nobody Asked For, Then Judge Each Answer =====
# No new functions. Call the ones you already have on inputs nobody asked
# for, and write a verdict beside each printed result.
#
# 1. total_for on an empty list. Print the result.
# 2. total_for on a list holding exactly one record.
# 3. total_for with a member name that is not in the file at all, such as
#    "Marco".
# 4. total_for with a name differing from a real member's only by
#    capitalization, such as "nia" for Nia.
# 5. signups_for on the empty list.
# 6. Add up the per-member totals for all five members, and print that sum
#    beside total_sessions(signups). The two should agree.
# 7. Write a verdict beside each of the five results in a comment: right, or
#    just a number that did not crash? Argue each one with your partner
#    first.
#
# Every line runs clean. Two of them deserve a different answer than they
# get.

# No new functions. Call the ones you already have, on inputs nobody
# asked for, and write a verdict beside each printed result.

# TODO: an empty list
print("empty list:", total_for([], "Nia"))
# Verdict: 0, that's right. No records means no sessions.

# TODO: a list holding exactly one record
print("one record:", total_for([signups[0]], "Nia"))
# Verdict: 4, that's right. The one record is Nia's Yoga, which is 4.

# TODO: a member name that is not in the file at all
print("not in file:", total_for(signups, "Marco"))
# Verdict: 0, but that's kind of lying. Marco isn't even a member, and 0
# makes it look like he signed up and booked nothing. It should tell you
# he's not in there.

# TODO: a name that differs from a real member's only by capitalization
print("wrong case:", total_for(signups, "nia"))
# Verdict: 0, and that's just wrong. Nia actually has 12. It's checking
# with ==, which cares about capital letters, so "nia" matches nobody.

print("signups_for empty:", signups_for([], "Nia"))
# Verdict: [], that's right. Nothing in, nothing out.

# TODO: then: do the per-member totals add up to the whole-file total?
per_member_sum = 0
for member in members:
    per_member_sum += total_for(signups, member)
print("per-member sum:", per_member_sum, "| whole file:",
      total_sessions(signups))
# Both came out to 45, so every session belongs to one of the five people.

# ----- Share Out: Day 3 -----
# Last 15 minutes, back together as a class. Bring:
#
# - Your verdict on one edge case. Pick the strangest result. Say whether
#   the answer is right or just quiet, and what you would change if this
#   were the center's real data. If you and your partner disagreed, bring
#   both positions.
# - Your cross-check. Did the five per-member totals add up to the
#   whole-file total? Say how you would run that check on a 430-row file you
#   cannot eyeball.
# - Three functions or one? Say which you wrote and what it cost or saved
#   you.
# - One question you could not settle, or one thing you would do differently
#   starting over. Half-finished thinking is what this slot is for.
#
# Be ready to answer "why did you do it that way?"

# Your notes for the share out:
# The weirdest one is "nia" giving 0 when Nia really has 12. If this was
# real data I'd lowercase both names before comparing, and flag any name
# that doesn't match anybody.
# Cross-check: 45 and 45, so it lines up. On a 430-row file I wouldn't
# type the names out myself. I'd pull the list of names from the data and
# let the code compare the two totals for me.
# I did three functions. Each one's small, so it's easy to test by itself,
# and the int(split) part only lives in one spot instead of being copied
# all over.
