# Lab — Column-Typing & Collection-Concern Practice

**Skills assessed:** Data Literacy, Critical Thinking, Curiosity (see this lab's own `RUBRIC.md`)

**Estimated time:** ~100 minutes (10 min intro · 75 min collaborative work · 15 min shareout)

## Scenario

You've just joined a data team, and someone drops `data/energy_sample.csv` in your lap: country-level energy figures your team wants to use in a report next week. Nobody has documented it. Before a single chart gets made or a single number gets quoted, somebody has to say — out loud, with a reason — what each column actually holds, how much data is really in there, and what about the way it was collected should make a careful analyst cautious. Today that somebody is your group.

*Work with your group, but complete and push/commit your own copy of this lab — collaboration is encouraged, a shared submission isn't.*

## Your Objectives

### 1. Open the Raw File Before You Classify a Single Column

*Same lab dataset from DATASET.md — a different file than the project's own co2-data, on purpose. Run every command from the module folder, so `data/energy_sample.csv` resolves.*

```bash
head data/energy_sample.csv
```

The dataset contains energy information for 10 countries from 2015 to 2021, including population, energy per capita, and fossil fuel and renewable energy shares.

### 2. Preview Every Column's Actual Values — All Seven, Not Just the First Few

*Hint: `cut` is new. It pulls specific columns out of a line: `-d,` says the columns are separated by commas, and `-f` says which ones you want.*

```bash
for i in 1 2 3 4 5 6 7; do
    cut -d, -f"$i" data/energy_sample.csv
done
```

### 3. Classify All Seven Columns, Each With a Reason Drawn From the Data

| Column | Type | Reason |
|---|---|---|
| country | Categorical | Country names like Nigeria and Brazil |
| year | Temporal / Discrete | Years from 2015–2021 |
| iso_code | Categorical | Country identifiers like NGA and BRA |
| population | Numerical / Discrete | Whole-number population counts |
| energy_per_capita | Numerical / Continuous | Decimal values measuring energy per person |
| fossil_share_energy | Numerical / Continuous | Percentages of fossil fuel energy |
| renewables_share_energy | Numerical / Continuous | Percentages of renewable energy |

### 4. Confirm How Many Rows and How Many Countries You Actually Have

*Hint: `sort` and `uniq -c` work together: `uniq -c` counts repeats, but only ones sitting next to each other, so the values have to be sorted first.*

```bash
wc -l data/energy_sample.csv

tail -n +2 data/energy_sample.csv | cut -d, -f1 | sort | uniq -c
```

The dataset contains **70 data rows, 10 countries, and 7 years per country**.

### 5. Check Whether Every Country Reports Every Column — Then Name Two Collection Concerns

I personally used `grep` to narrow down to specific countries and check their respective columns.

```bash
grep "Nigeria," data/energy_sample.csv
grep "Kenya," data/energy_sample.csv
```

I found that Nigeria and Kenya were missing both fossil fuel and renewable energy shares for all seven years, totaling 14 rows with missing energy share data.

**Concern 1 — Missing Data:** Nigeria has a population of over 218 million in 2021 but no reported renewable energy share. Why is this information missing, and does it affect our comparisons?

**Concern 2 — Reporting Consistency:** Fossil fuel and renewable shares don't always add up to 100%. This makes me question what other energy sources are included and whether countries are reporting consistently.

## Share Out

*First: how did your group figure out whether every country reports every column? Compare the different approaches.*

*Second: which collection concerns did your group flag, and which single data-quality question did you sharpen out of them?*

### 1. How did you check the columns?

Figuring out whether every country reports every column wasn't too difficult. I could use `cut` and `sort` to examine the data, but I personally used `grep` to narrow it down to specific countries and check their values. This is how I noticed the missing data for Nigeria and Kenya.

### 2. What concerns and questions came up?

I thought it was interesting comparing countries with large populations and their respective energy shares, whether fossil fuels or renewables. I want to investigate whether population has any relationship with a country's energy mix.

What this dataset doesn't explicitly show is the connection to average household income. We have energy per capita, but knowing how much the average household earns would provide important context about a country's development and energy consumption.

**My Data-Quality Question:**

Why are fossil fuel and renewable energy shares missing for Nigeria and Kenya across all seven years, and were their energy statistics collected using the same methods as the other countries?