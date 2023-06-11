import os
import guidance
from dotenv import load_dotenv

# Setup: Env (.env file in root )
load_dotenv()


# Setup: Generate Func
def gen_outline_cot(story_prompt: str) -> dict:
    '''
    ---
    ModelBusiness:
        business_logic: Generate a story outline in the writing style of 3 relevant famous writers.
        models:
            - gpt-3.5-turbo
        tags:
            - guidance
            - chat
        prompts:
            - << gen_outline_cot_prompt >>
    ---
    '''
    
    # --- propmpt & llm config
    gen_outline_cot_prompt = '''
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
    '''
    '''
    ---
    ModelBusinessPrompt:
        name: gen_outline_cot_prompt
        prompt: |
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
    ---
    '''
    llm = guidance.llms.OpenAI("gpt-3.5-turbo", token=os.environ.get('OPEN_AI_API_KEY'), caching=False)
    # --- execute (w/ args)
    program = guidance(gen_outline_cot_prompt, llm=llm)
    executed_program = program(story_prompt=story_prompt)
    # --- results
    return executed_program.variables().get('answer'), executed_program.variables().get('experts')


# Run!
if __name__ == '__main__':
    print(f'========== Generate Story Outline ==========')
    # --- get user input
    story_prompt = input('Describe the story: ')
    # --- generate & print
    response_gen_story, response_gen_experts = gen_outline_cot(story_prompt)
    print('\n')
    print('=== Story Outline ===\n')
    print(response_gen_story)
    print('\n')
    print('=== Experts Referenced ===\n')
    print(response_gen_experts)
    exit()
