import json
import ibm_watson
assistant = ibm_watson.AssistantV1(
    version='2019-02-28',
    iam_apikey='u1N9ThXmpZUk_-1_F1AaAw-11BbBXFtCbonmmerHbnFI',
    url='https://gateway-wdc.watsonplatform.net/assistant/api'
)

response = assistant.message(
    workspace_id='f5c5d93f-4f4b-46d6-b882-0baf0bf6c0a7',
    input={
        'text':'The session was amazing. I understood all the concepts clearly'
    }
).get_result()
#print(response)
#print(json.dumps(response, indent=2))

a=response
b=a['intents']
if b==[]:
    intent = 0
else:
    intent = b[0]['intent']
print(intent)

