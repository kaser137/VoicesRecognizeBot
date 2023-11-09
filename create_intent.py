import json
import click
from google.cloud import dialogflow


def create_intent(display_name, training_phrases_parts, message_texts, project_id='voisesrecognize'):
    intents_client = dialogflow.IntentsClient()
    parent = dialogflow.AgentsClient.agent_path(project_id)
    training_phrases = []
    for training_phrases_part in training_phrases_parts:
        part = dialogflow.Intent.TrainingPhrase.Part(text=training_phrases_part)
        training_phrase = dialogflow.Intent.TrainingPhrase(parts=[part])
        training_phrases.append(training_phrase)
    messages = []
    for message_text in message_texts:
        text = dialogflow.Intent.Message.Text(text=message_text)
        message = dialogflow.Intent.Message(text=text)
        messages.append(message)

    intent = dialogflow.Intent(
        display_name=display_name, training_phrases=training_phrases, messages=messages
    )

    response = intents_client.create_intent(
        request={'parent': parent, 'intent': intent}
    )

    print('Intent created: {}'.format(response))


@click.command()
@click.option('--intent', default='questions.json', help='full path to the json file with intents.')
def main(intent):
    with open(intent, 'r') as file:
        intent_json = file.read()

    intents = json.loads(intent_json)

    for intent_name, intent_part in intents.items():
        create_intent(
            display_name=intent_name,
            training_phrases_parts=intent_part['questions'],
            message_texts=[intent_part['answer'], ]
        )


if __name__ == '__main__':
    main()
