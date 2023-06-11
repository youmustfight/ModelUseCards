# Model Business Card for story_generator 

## Business Logic

### gen_character_io

Description: Generate a fictional character details in JSON format.

Tags: guidance, completion, token healing

Prompts:
- << gen_character_io_prompt >>

### gen_outline_cot

Description: Generate a story outline in the writing style of 3 relevant famous writers.

Tags: guidance, chat

Prompts:
- << gen_outline_cot_prompt >>


---

## Models

- gpt-3.5-turbo
- text-davinci-003

---

## Prompts

### gen_character_io_prompt

```
The following is a fictional character ({character_description}) in JSON format.
'''json
{
    "name": "{{gen 'name' }}",
    "morale_alignment": "{{select 'order' options=alignment_options}}",
    "is_protagonist": "{{#select 'protagonist'}}Yes{{or}}No{{/select}}",
    "deepest_secret": {{gen 'secret_motive' }},
    "inventory_list": {{gen 'inventory_list' }}
}
'''
```

### gen_outline_cot_prompt

```
{{#system~}}
You are a helpful assistant.
{{~/system}}
{{#user~}}
I want a story outline written given the following prompt:
{{story_prompt}}
Who are 3 world-class writers (past or present) who would be great at writing this?
Please don't do the task yet.
{{~/user}}
{{#assistant~}}
{{gen 'experts' temperature=0 max_tokens=300}}
{{~/assistant}}
{{#user~}}
Great, now please do the writing task as if these experts had collaborated in a joint anonymous effort.
In other words, their identity is not revealed, nor is the fact that there is a panel of experts writing.
Please start your answer with ANSWER:
{{~/user}}
{{#assistant~}}
{{gen 'answer' temperature=0 max_tokens=1000}}
{{~/assistant}}
```

