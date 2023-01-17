# import os
# import openai

# openai.api_key = os.getenv("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")

# response = openai.Completion.create(
#   model="text-davinci-003",
#   prompt="The following is a conversation with an AI assistant. The assistant is helpful, creative, clever, and very friendly.\n\nHuman: Hello, who are you?\nAI: I am an AI created by OpenAI. How can I help you today?\nHuman: I'd like to cancel my subscription.\nAI:",
#   temperature=0.9,
#   max_tokens=150,
#   top_p=1,
#   frequency_penalty=0.0,
#   presence_penalty=0.6,
#   stop=[" Human:", " AI:"]
# )


from api.prompt import Prompt
import os
import openai
from dotenv import load_dotenv
load_dotenv()

openai.api_key = os.getenv("OPENAI_API_KEY")

class ChatGPT:
    def __init__(self):
        self.prompt = Prompt()
        self.model = os.getenv("OPENAI_MODEL", default = "text-davinci-003")
        #self.model = os.getenv("OPENAI_MODEL", default = "chatbot")
        self.temperature = float(os.getenv("OPENAI_TEMPERATURE", default = 0))
        self.frequency_penalty = float(os.getenv("OPENAI_FREQUENCY_PENALTY", default = 0))
        self.presence_penalty = float(os.getenv("OPENAI_PRESENCE_PENALTY", default = 0.6))
        self.max_tokens = int(os.getenv("OPENAI_MAX_TOKENS", default = 240))

    def get_response(self):
        response = openai.Completion.create(
            model=self.model,
            prompt=self.prompt.generate_prompt(),
            temperature=self.temperature,
            frequency_penalty=self.frequency_penalty,
            presence_penalty=self.presence_penalty,
            max_tokens=self.max_tokens
        )
        return response['choices'][0]['text'].strip()

    def add_msg(self, text):
        self.prompt.add_msg(text)

# response = openai.Completion.create(
#   model="text-davinci-003",
#   prompt="\nHuman: 寫一篇小說\nAI:",
#   temperature=0.9,
#   max_tokens=150,
#   top_p=1,
#   frequency_penalty=0.0,
#   presence_penalty=0.6,
#   stop=[" Human:", " AI:"]
# )
# print(response["choices"][0]["text"])