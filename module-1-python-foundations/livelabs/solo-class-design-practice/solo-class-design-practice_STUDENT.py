#!/usr/bin/env python3
"""Lab: Solo Class Design Rep
GitBook Quest 1.8: Meet the Objects

HOW TO RUN
    Open a terminal in this file's folder and run:
        python3 solo-class-design-practice_STUDENT.py
    Or make it executable once:
        chmod +x solo-class-design-practice_STUDENT.py
    and from then on run it directly:
        ./solo-class-design-practice_STUDENT.py
    The first line, #!/usr/bin/env python3 (the "shebang"), is what
    makes ./ work. python3 <file> ignores it as a comment.

ANSWER EVERYTHING IN THIS FILE
    - Code goes under each step's banner.
    - Written answers go in # comments under each "# Your answer:"
      line.
    - Run the file after every change. It runs top to bottom, so a
      later step can use anything an earlier step made.

HINTS live in the worksheet (LiveLabOverview&Steps.md), collapsed
under each step. Open one only when you are stuck.

SUBMIT
    Commit this file (you may rename it solo-class-design-practice.py) to your own data
    challenge repo, inside your Module 1 folder. Paste its direct GitHub URL
    into the LMS.
"""

# ===== Step 1: Read the Stakeholder Need =====
# A new stakeholder need. Not the board-game or office-supply domain from
# lecture, and not one of the project's own 4 scenarios.

# Your answer:
# The volunteer coordinator at the community tool library needs to know the name of each tool, 
# how many are available, and whether it needs a safety check or not. 
#

# ===== Step 2: Decide Your Attributes, Each With a Reason From the Scenario =====

# Your answer:
# tool_name       -> "What the tool is."
# available_count -> "How many are free to borrow right now."
# is_power_tool   -> "Power tools need a quick inspection after every use."
#                    I store whether it's a power tool, and a method will
#                    decide if it needs a safety check.
#

# ===== Step 3: Write __init__ and a Method, From Scratch =====
# There is no single correct design here. Your class name, your attribute
# names and your method can all differ from everyone else's and still be
# right. The test is whether each one traces back to the stakeholder
# paragraph.

# TODO: Write __init__ and a Method, From Scratch
class CommunityTool:
    def __init__(self, tool_name, available_count, is_power_tool):
        self.tool_name = tool_name
        self.available_count = available_count
        self.is_power_tool = is_power_tool
    
    def tools_available(self):
        return self.available_count > 0

    def needs_safety_check(self):
        if self.is_power_tool:
            return True
        else:
            return False 


# ===== Step 4: Instantiate 2+ Objects, Confirm Independent Storage =====
# The same proof Day 13's lecture asked for, now on a class you designed
# yourself. Predict what each print() will show before you run it.

# TODO: Instantiate 2+ Objects, Confirm Independent Storage
drill = CommunityTool("Drill", 5, True)
hammer = CommunityTool("Hammer", 8, False)
ladder = CommunityTool("Ladder", 3, False)
hand_saw = CommunityTool("Hand_Saw", 4, False)
chainsaw = CommunityTool("Chainsaw", 1, True)

tools = [drill, hammer, ladder, hand_saw, chainsaw]
for tool in tools:
    print(tool.tool_name, tool.available_count, tool.needs_safety_check())

# Independence test: change only the chainsaw
# Prediction: chainsaw -> 0, drill -> 5 (unchanged)
chainsaw.available_count = 0
print(chainsaw.tool_name, chainsaw.available_count, chainsaw.tools_available())
print(drill.tool_name, drill.available_count, drill.tools_available())

# Predictions:
# drill.needs_safety_check()  -> True
# ladder.needs_safety_check() -> False
# drill.available_count()     -> 5

# ===== Step 5: Justify Your Design Choice in 2-3 Sentences =====

# Your answer:
# I gave CommunityTool three attributes because the volunteer coordinator asked
# for three things: tool_name (what the tool is), available_count (how many are
# free to borrow right now), and is_power_tool (whether it needs a safety check).
# I stored is_power_tool instead of needs_safety_check because the coordinator said
# power tools need an inspection after every use, so knowing it is a power tool
# is enough to know it needs a check.
# My two methods answer the coordinator's questions: tools_available() says whether
# at least one is free right now, and needs_safety_check() says whether the tool
# must be inspected before it goes out again.

# ----- Share Out -----
# Last 15 minutes, back together as a class. Bring:
#
# Come ready to show your class and defend it. Specifically:
# - The attribute list you chose, and for each one, the phrase in the
#   coordinator's request it came from. If you can't point at a phrase for
#   an attribute, say so - that's a real finding, not a failure.
# - One attribute you considered and rejected, and why. - Your method: what
#   question does it answer, and why would the coordinator reach for it
#   first?
# - Anything you got stuck on. Designing from a paragraph with nobody to
#   check against is genuinely hard, and naming where it was hard is worth
#   more to the room than a tidy answer.
#
# Expect to be asked "why that attribute and not another?" - there is no
# single right list here, so the reasoning IS the answer.
#
# Be ready to answer "why did you do it that way?"

# Your notes for the share out:
# I initially thought about making a needs_safety_check attribute but I decided to pivot
# and use it as a method instead. It would just repeat is_power_tool since every power 
# tool needs a check. 
# I also was going to use tool_inventory to represent the count at first but rejected it because
# the coordinator asks how many are free right now, not how many the community center owns. 
