# SUMMARIZERS
gpt_prompt_summary_concise = """
In the fewest words, summarize of the following passage:

PASSAGE: <<SOURCE_TEXT>>

SUMMARY:
"""
'''
---
ModelBusinessPrompt:
    name: gpt_prompt_summary_concise
    prompt: |
        In the fewest words, summarize of the following passage:

        PASSAGE: <<SOURCE_TEXT>>

        SUMMARY:
---
'''

gpt_prompt_summary_detailed = """
Write a detailed summary of the following:

<<SOURCE_TEXT>>

DETAILED SUMMARY:
"""
'''
---
ModelBusinessPrompt:
    name: gpt_prompt_summary_detailed
    prompt: |
        Write a detailed summary of the following:

        <<SOURCE_TEXT>>

        DETAILED SUMMARY:
---
'''

# SUMMARIZERS: CITING SLAVERY
# V1 - initial
# V2 - added strictness, "no explicit mention of slaves or slavery occurs".
# V3 - got rid of end sentence: 'If slaves or slavery is not explicitly mentioned, write '{GPT_NULL_PHRASE}
gpt_prompt_citing_slavery_summary = f"""
In the fewest words, summarize the context mentioning slaves in the following judicial opinion.

JUDICIAL OPINION: <<SOURCE_TEXT>>

SUMMARY:
"""
'''
---
ModelBusinessPrompt:
    name: gpt_prompt_citing_slavery_summary
    prompt: |
        In the fewest words, summarize the context mentioning slaves in the following judicial opinion.

        JUDICIAL OPINION: <<SOURCE_TEXT>>

        SUMMARY:
---
'''

gpt_prompt_citing_slavery_summary_one_liner = """
In a single sentence, summarize the following passage without excluding any references to slaves or slavery:

PASSAGE: <<SOURCE_TEXT>>

ONE SENTENCE SUMMARY:
"""
'''
---
ModelBusinessPrompt:
    name: gpt_prompt_citing_slavery_summary_one_liner
    prompt: |
        In a single sentence, summarize the following passage without excluding any references to slaves or slavery:

        PASSAGE: <<SOURCE_TEXT>>

        ONE SENTENCE SUMMARY:
---
'''
