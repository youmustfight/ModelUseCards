# Model Business Card for caselaw_summarizer 

## Business Logic

### summarize_caselaw

Description: Summarizing US caselaw. Splits into 3500 string length chunks, then summarizes each chunk (500 max tokens). Then summarizes the summary chunks withi 500 max tokens.

Tags: completion, chunking, summarization

Prompts:
- << gpt_prompt_summary_concise >>

### summarize_caselaw_mentioning_enslaved_people

Description: Summarizing US caselaw, with specific prompts if caselaw involves enslaved people. Splits into 3500 string length chunks, checks for the presence of the words 'slave' or 'chattle', and then uses 1 of 2 prompts to summarizing (500 max tokens). Finally, we summarize with a prompt trying to preserve the case's context related to slavery. These prompts are written in a way to stop hallucinating connections to slavery in caselaw that is irrelevant.

Tags: completion, chunking, summarization

Prompts:
- << gpt_prompt_citing_slavery_summary >>
- << gpt_prompt_summary_concise >>


---

## Models

- text-davinci-003

---

## Prompts

### gpt_prompt_summary_concise

```
In the fewest words, summarize of the following passage:

PASSAGE: <<SOURCE_TEXT>>

SUMMARY:
```

### gpt_prompt_summary_detailed

```
Write a detailed summary of the following:

<<SOURCE_TEXT>>

DETAILED SUMMARY:
```

### gpt_prompt_citing_slavery_summary

```
In the fewest words, summarize the context mentioning slaves in the following judicial opinion.

JUDICIAL OPINION: <<SOURCE_TEXT>>

SUMMARY:
```

### gpt_prompt_citing_slavery_summary_one_liner

```
In a single sentence, summarize the following passage without excluding any references to slaves or slavery:

PASSAGE: <<SOURCE_TEXT>>

ONE SENTENCE SUMMARY:
```

