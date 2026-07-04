# Curriculum — Excel (Buying Analyst, 1x → 10x)

The productivity story hangs on two axes:

- **Rows = task themes** that emerged from the NBUY survey.
- **Columns = the capability ladder** — the same task, climbing from hand-craft to GenAI.

Lessons are authored one at a time and grounded in `RESOURCES.md`. The grid is the map, not a
promise to build every cell. ✅ = a lesson is written and linked.

## Lessons so far (by theme)

<!-- BEGIN:auto:lessons -->
### Source & prepare

- [0001 — Tables: the modern foundation](lessons/tables-the-modern-foundation.html)
- [0002 — Sort & Filter: order and isolate](lessons/sort-and-filter.html)
- [0003 — Data validation: controlled dropdowns](lessons/data-validation-dropdowns.html)
- [0004 — Text formulas: clean & combine](lessons/text-formulas-clean-and-combine.html)
- [0005 — Get & Transform (Power Query)](lessons/get-and-transform-power-query.html)

### Summarise & analyse

- [0006 — Relative & absolute references](lessons/relative-and-absolute-references.html)
- [0007 — Logical functions & IFERROR](lessons/logical-functions-and-iferror.html)
- [0008 — Aggregation & precision](lessons/aggregation-and-precision.html)
- [0009 — SUMIFS: totals by criteria](lessons/sumifs-totals-by-criteria.html)
- [0010 — XLOOKUP: pull matching details](lessons/xlookup-pull-matching-details.html)
- [0011 — Date & time functions](lessons/date-and-time-functions.html)
- [0012 — PivotTables: summarise in seconds](lessons/pivottables-summarise-in-seconds.html)
  - [0012.1 — Slicers: swap the dropdowns for sliders](lessons/add-sliders-to-pivottables.html)
- [0013 — Dynamic arrays: FILTER, SORT & UNIQUE](lessons/dynamic-arrays-filter-sort-unique.html)

### Report & visualise

- [0014 — Number & custom formatting](lessons/number-and-custom-formatting.html)
- [0015 — Conditional formatting: make numbers signal](lessons/conditional-formatting-make-numbers-signal.html)
- [0016 — Charts: a clean column chart](lessons/charts-a-clean-column-chart.html)

### Communicate & present

- [0017 — Print- & export-ready tables](lessons/print-and-export-ready-tables.html)

### Automate the repetitive

- [0018 — Flash Fill & Text to Columns](lessons/flash-fill-and-text-to-columns.html)
- [0019 — Named ranges](lessons/named-ranges.html)
<!-- END:auto:lessons -->

All nine share one practice file: [`artefacts/excel-course-workbook.xlsx`](artefacts/excel-course-workbook.xlsx),
with a starter tab per lesson (e.g. `SUMIFS`) and a hidden worked-solution tab alongside it.


<!-- BEGIN:auto:grid -->
| Theme ↓ / Rung → | 1 · Manual craft (do it well by hand) | 2 · Aldi:GPT (chat, no tool use) | 3 · M365 Copilot (acts in Excel) | 4 · GitHub Copilot (builds the workbook) |
|---|---|---|---|---|
| **Source & prepare** | ✅ [0001 Tables](lessons/tables-the-modern-foundation.html); ✅ [0002 Sort & Filter](lessons/sort-and-filter.html); ✅ [0003 Data validation](lessons/data-validation-dropdowns.html); ✅ [0004 Text formulas](lessons/text-formulas-clean-and-combine.html); ✅ [0005 Get & Transform](lessons/get-and-transform-power-query.html); Get & Transform basics | Ask it to write/explain a formula or SQL snippet | "Clean and shape this pasted extract" | Build a clean, shaped workbook from a raw file |
| **Summarise & analyse** | ✅ [0006 References](lessons/relative-and-absolute-references.html); ✅ [0007 Logical & IFERROR](lessons/logical-functions-and-iferror.html); ✅ [0008 Aggregation & precision](lessons/aggregation-and-precision.html); ✅ [0009 SUMIFS](lessons/sumifs-totals-by-criteria.html); ✅ [0010 XLOOKUP](lessons/xlookup-pull-matching-details.html); ✅ [0011 Date & time](lessons/date-and-time-functions.html); ✅ [0012 PivotTables](lessons/pivottables-summarise-in-seconds.html); ↳ ✅ [0012.1 Slicers](lessons/add-sliders-to-pivottables.html); ✅ [0013 Dynamic arrays](lessons/dynamic-arrays-filter-sort-unique.html) | Interpret a pivot; sanity-check a calculation | "Summarise the trends in this range" | Build a workbook that summarises the data end-to-end |
| **Report & visualise** | ✅ [0014 Number formatting](lessons/number-and-custom-formatting.html); ✅ [0015 Conditional formatting](lessons/conditional-formatting-make-numbers-signal.html); ✅ [0016 Charts](lessons/charts-a-clean-column-chart.html) | Draft the commentary under a chart | Build a summary sheet from raw data | Build a formatted, charted report workbook |
| **Communicate & present** | ✅ [0017 Print- & export-ready](lessons/print-and-export-ready-tables.html) | Turn numbers into a short narrative | "Make a one-page summary for my director" | Build a print-ready one-page report workbook |
| **Automate the repetitive** | ✅ [0018 Flash Fill](lessons/flash-fill-and-text-to-columns.html); ✅ [0019 Named ranges](lessons/named-ranges.html); named ranges; fill-down discipline | Write a formula to replace manual steps | Office Scripts / repeatable actions | Script a repeatable clean-up & build from scratch |
<!-- END:auto:grid -->

## The 1x → 10x idea
Rung 1 makes you reliable and fast by hand — and gives you the judgement to check what the
machine does. Rung 2 offloads drafting and explanation. Rung 3 lets Copilot act on your actual
workbook. Rung 4 hands the whole build to an agent that creates the workbook from scratch. You
climb per theme, only once the rung below is solid.
