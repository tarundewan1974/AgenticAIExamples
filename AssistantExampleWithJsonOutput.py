from litellm import completion
from typing import List, Dict
import json
jira_spec = {
    'Story Title': 'Title of the story',
    
    'Description': {
        'Functional': 'Functional information of the story.',
        'Non Functional': 'Non Functional Requirement of the story'
    },
    'Acceptance Criteria': 'Acceptance Criteria of the story.',
}

def generate_response(messages: List[Dict]) -> str:
    """Call LLM to get response"""
    response = completion(
        model="openai/gpt-4o",
        messages=messages,
        max_tokens=1024
    )
    return response.choices[0].message.content


messages = [
    {"role": "system", "content": "You are an Product Owner that defines only one jira story for any business requirement ."},
    {"role": "user", "content": f"Please implement: {json.dumps(jira_spec)}"}
]

initialresponse = generate_response(messages)
print("First Response:\n" + initialresponse)
messages.append({"role": "assistant", "content":initialresponse})
messages.append({
      "role": "user",
      "content": "Make Functional and Non Functional requirements in bullet points"
   })

print("\n=== Final Response ===")
finalresponse = generate_response(messages)
print(finalresponse)
