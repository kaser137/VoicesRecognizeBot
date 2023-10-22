import json
from google.cloud import dialogflow


def create_intent(display_name, training_phrases_parts, message_texts, project_id='voisesrecognize'):
    intents_client = dialogflow.IntentsClient()
    parent = dialogflow.AgentsClient.agent_path(project_id)
    training_phrases = []
    for training_phrases_part in training_phrases_parts:
        part = dialogflow.Intent.TrainingPhrase.Part(text=training_phrases_part)
        training_phrase = dialogflow.Intent.TrainingPhrase(parts=[part])
        training_phrases.append(training_phrase)

    text = dialogflow.Intent.Message.Text(text=message_texts)
    message = dialogflow.Intent.Message(text=text)

    intent = dialogflow.Intent(
        display_name=display_name, training_phrases=training_phrases, messages=[message]
    )

    response = intents_client.create_intent(
        request={"parent": parent, "intent": intent}
    )

    print("Intent created: {}".format(response))


with open('questions.json', "r") as my_file:
    queries_json = my_file.read()

queries = json.loads(queries_json)

for query in queries:
    create_intent(
        display_name=query,
        training_phrases_parts=queries[query]['questions'],
        message_texts=[queries[query]['answer'],]
    )
