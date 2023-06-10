import os
import guidance
from dotenv import load_dotenv
from utils import extract_json_from_text_string

# Setup: Env (.env file in root )
load_dotenv()


# Setup: Generate Func
def gen_character_io(character_description: str) -> dict:
    '''
    ---
    ModelBusiness:
        business_logic: Generate a fictional character details in JSON format.
        models:
            - text-davinci-003
        tags:
            - guidance
            - completion
            - token healing
    ---
    '''
    
    # --- propmpt & llm config
    gen_character_io_prompt = '\n'.join([
        f'The following is a fictional character ({character_description}) in JSON format.',
        '''```json
        {
            "name": "{{gen 'name' stop='"'}}",
            "morale_alignment": "{{select 'order' options=alignment_options}}",
            "is_protagonist": "{{#select 'protagonist'}}Yes{{or}}No{{/select}}",
            "deepest_secret": {{gen 'secret_motive' stop=','}},
            "inventory_list": {{gen 'secret_motive' stop='}'}}
        }
        ```'''
    ])
    '''
    ---
    ModelBusinessPrompt:
        name: gen_character_io_prompt
        prompt: |
            The following is a fictional character ({character_description}) in JSON format.
            ```json
            {
                "name": "{{gen 'name' }}",
                "morale_alignment": "{{select 'order' options=alignment_options}}",
                "is_protagonist": "{{#select 'protagonist'}}Yes{{or}}No{{/select}}",
                "deepest_secret": {{gen 'secret_motive' }},
                "inventory_list": {{gen 'inventory_list' }}
            }
            ```
    ---
    '''
    llm = guidance.llms.OpenAI("text-davinci-003", token=os.environ.get('OPEN_AI_API_KEY'), caching=False)
    # --- execute (w/ args)
    program = guidance(gen_character_io_prompt, llm=llm)
    executed_program = program(alignment_options=["lawful good", "neutral good", "chaotic good"])
    # --- results
    return extract_json_from_text_string(executed_program.text)


# Run!
if __name__ == '__main__':
    print(f'========== Generate Story Character ==========')
    # --- get user input
    character_description = input('Describe the character: ')
    # --- generate & print
    response_gen_character = gen_character_io(character_description)
    print(response_gen_character)
    exit()
