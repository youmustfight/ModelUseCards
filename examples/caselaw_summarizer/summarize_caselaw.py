from dotenv import load_dotenv
import re
import textwrap

from prompts import gpt_prompt_summary_concise, gpt_prompt_citing_slavery_summary
from utils import gpt_completion, open_txt_file


# Setup: Env (.env file in root )
load_dotenv()

# Summarizers
# DEMO example summarizing a passave. There are many flaws with this approach, it's a demo.
def summarize_caselaw(document_text):
    '''
    ---
    ModelBusiness:
        business_logic: Summarizing US caselaw. Splits into 3500 string length chunks, then summarizes each chunk (500 max tokens). Then summarizes the summary chunks withi 500 max tokens.
        models:
            - text-davinci-003
        tags:
            - completion
            - chunking
            - summarization
        prompts:
            - << gpt_prompt_summary_concise >>
    ---
    '''
    summary_chunks = []
    chunks = textwrap.wrap(document_text, 3500)
    for chunk in chunks:
        general_summary_chunk = gpt_completion(
            engine='text-davinci-003',
            max_tokens=500,
            prompt=gpt_prompt_summary_concise.replace('<<SOURCE_TEXT>>', chunk))
        summary_chunks.append(general_summary_chunk)
    # Summarize all chunks
    if len(summary_chunks) > 1:
        summary_joined = " ".join(summary_chunks)
        return gpt_completion(
            engine='text-davinci-003',
            max_tokens=500,
            prompt=gpt_prompt_summary_concise.replace('<<SOURCE_TEXT>>', summary_joined))
    else:
        return summary_chunks[0]

# This is a DEMO OF HOW TO NOT write summarizing code. It's to show an opitionated, potentially flawed flow for summarizing
def summarize_caselaw_mentioning_enslaved_people(document_text):
    '''
    ---
    ModelBusiness:
        business_logic: Summarizing US caselaw, with specific prompts if caselaw involves enslaved people. Splits into 3500 string length chunks, checks for the presence of the words 'slave' or 'chattle', and then uses 1 of 2 prompts to summarizing (500 max tokens). Finally, we summarize with a prompt trying to preserve the case's context related to slavery. These prompts are written in a way to stop hallucinating connections to slavery in caselaw that is irrelevant.
        models:
            - text-davinci-003
        tags:
            - completion
            - chunking
            - summarization
        prompts:
            - << gpt_prompt_citing_slavery_summary >>
            - << gpt_prompt_summary_concise >>
    ---
    '''
    summary_chunks = []
    chunks = textwrap.wrap(document_text, 3500)
    # Split document text into chunks crudely on string length (~2k token length max for text-davinci-003)
    for chunk in chunks:
        # If there is a mention of slavery, use a specific prompt to ensure that context is not lost
        if bool(re.search('slave|chattel', chunk, flags=re.IGNORECASE)):
            specific_summary_chunk = gpt_completion(
                engine='text-davinci-003',
                max_tokens=500,
                prompt=gpt_prompt_citing_slavery_summary.replace('<<SOURCE_TEXT>>', chunk))
            summary_chunks.append(specific_summary_chunk)
        # otherwise fallback to a general summary prompt (avoid leading the LLM to talk about slavery when it's not a present)
        else:
            general_summary_chunk = gpt_completion(
                engine='text-davinci-003',
                max_tokens=500,
                prompt=gpt_prompt_summary_concise.replace('<<SOURCE_TEXT>>', chunk))
            summary_chunks.append(general_summary_chunk)
    # Summarize all chunks
    if len(summary_chunks) > 1:
        summary_joined = " ".join(summary_chunks)
        return gpt_completion(
            engine='text-davinci-003',
            max_tokens=500,
            prompt=gpt_prompt_citing_slavery_summary.replace('<<SOURCE_TEXT>>', summary_joined))
    else:
        return summary_chunks[0]


# Run!
if __name__ == '__main__':
    print(f'========== Summarize Caselaw ==========')
    # --- caselaw (Gideon v. Wainwright)
    print('\n=== Gideon v. Wainwright ===\n')
    caselaw_one_txt = open_txt_file('./caselaw/gideon_v_wainwright.txt')
    caselaw_one_summary = summarize_caselaw(caselaw_one_txt)
    print(caselaw_one_summary)
    # --- caselaw that involves slavery (Bradford v. Jenkins)
    print('\n=== Bradford v. Jenkins ===\n')
    caselaw_two_txt = open_txt_file('./caselaw/bradford_v_jenkins.txt')
    caselaw_two_summary = summarize_caselaw_mentioning_enslaved_people(caselaw_two_txt)
    print(caselaw_two_summary)
    print('\n\n')
    exit()
