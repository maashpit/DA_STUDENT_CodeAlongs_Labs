# Lab — Column-Typing & Collection-Concern Practice

**Skills assessed:** Data Literacy, Critical Thinking, Curiosity (see this lab's own `RUBRIC.md`)

**Estimated time:** ~100 minutes (10 min intro · 75 min collaborative work · 15 min shareout)

## Scenario

You've just joined a data team, and someone drops `data/energy_sample.csv` in your lap: country-level energy figures your team wants to use in a report next week. Nobody has documented it. Before a single chart gets made or a single number gets quoted, somebody has to say — out loud, with a reason — what each column actually holds, how much data is really in there, and what about the way it was collected should make a careful analyst cautious. Today that somebody is your group.

*Work with your group, but complete and push/commit your own copy of this lab — collaboration is encouraged, a shared submission isn't.*

## Your Objectives

- **Open the Raw File Before You Classify a Single Column**
  - *Same lab dataset from DATASET.md — a different file than the project's own co2-data, on purpose. Run every command from the module folder, so `data/energy_sample.csv` resolves.*

- **Preview Every Column's Actual Values — All Seven, Not Just the First Few**
  - *Hint: `cut` is new. It pulls specific columns out of a line: `-d,` says the columns are separated by commas, and `-f` says which ones you want.*

- **Classify All Seven Columns, Each With a Reason Drawn From the Data**

- **Confirm How Many Rows and How Many Countries You Actually Have**
  - *Hint: `sort` and `uniq -c` are new, and they work together: `uniq -c` counts repeats, but only ones sitting next to each other, so the values have to be sorted first.*

- **Check Whether Every Country Reports Every Column — Then Name Two Collection Concerns**

## Share Out

Two questions, in this order. First: how did your group figure out whether every country reports every column? Different groups almost certainly took different routes to the same file — compare them before deciding which you'd reach for next time. Second: which collection concerns did your group flag, and which single data-quality question did you sharpen out of them? Put each group's question up where everyone can read it, then ask the class which ones a real analyst could actually go answer — and which ones sound serious but can't be checked.

I want to see the relationship between fossil share energy and renewable energy share. Theres a definite connection?
To answer the first question, figuring out if every country reports every column wasn't too difficult I can sort the data by the column and see if the country has the respective data point 
I personally used grep to narrow down to a specifc country and went through the different columns that grep gave me

I think it was interesting seeing the comparison in countries that have a large population and their respective energy share whether it be fossil fuels or renewable. Nigeria has no renewable energy data even though they have a sizeable population. I want to see the relationship between fossil share energy and renewable energy share. Theres a definite connection with the population

What this data set shows but doesnt explicitly state is the connection to the average household income of each country. We have energy per capita but we need to see how much each household on average is making, I think thats a really important insight to show the comparison of the development of these countries in context of how much and what kinds of energy they use. 

