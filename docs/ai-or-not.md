# AI or Not — Question Classification

Which questions need an AI/LLM and which can be answered with simple rules or data lookup?

## Questions that **do NOT need AI**

| # | Question | Reason |
|---|----------|--------|
| 1 | Where is the Training Office? | Direct lookup in `offices.csv` by name. |
| 2 | When does the Library open? | Hours field is already stored in `offices.csv`. |
| 3 | Hi / Hello / Xin chào | Greeting detected by keyword set; fixed reply. |
| 4 | Help | Keyword match returns a static help message. |
| 5 | What room is the IT Helpdesk in? | Single-field CSV lookup (room column). |
| 6 | List all offices | Iterate over `offices.csv` rows and format output. |
| 7 | Is the Library open on Saturday? | Parse the `hours` field and check for "Sat". |
| 8 | What is the room number of Student Affairs? | Exact-match lookup, returns `I.102`. |
| 9 | How many offices are in the system? | Count rows in `offices.csv`. |
| 10 | Which offices are open on Sunday? | Filter `hours` column for entries containing "Sun". |

## Questions that **need AI**

| # | Question | Reason |
|---|----------|--------|
| 1 | Can you summarise Chapter 3 of my textbook? | Requires reading comprehension and abstractive summarisation. |
| 2 | Why is quicksort faster than bubble sort in practice? | Needs conceptual explanation beyond any stored data. |
| 3 | Translate this paragraph into Vietnamese. | Natural-language translation requires a language model. |
| 4 | I'm stressed about exams — any advice? | Empathetic, context-sensitive response needs language understanding. |
| 5 | Compare the CS curriculum at HCMUS with MIT's. | Requires reasoning over multiple unstructured sources. |
| 6 | Write a Python function that reverses a linked list. | Code generation requires an LLM. |
| 7 | What career paths can I follow after a CS degree? | Open-ended advice drawing on broad world knowledge. |
| 8 | Explain the difference between TCP and UDP simply. | Conceptual explanation with simplification needs language generation. |
| 9 | Check my essay for grammar mistakes. | Grammar correction requires NLU and contextual rewriting. |
| 10 | Which electives should I pick if I like data science? | Personalised recommendation needs reasoning over preferences and course content. |
