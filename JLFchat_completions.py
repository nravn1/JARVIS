import numpy as np

class ChatCompletions:
    def __init__(self, arr, client):
        self.arr = arr
        self.client = client
        self.chatModel = "gpt-3.5-turbo-1106"
        self.chatMaxTokens = 1200

    def get_response(self):
        num_rows, num_cols = self.arr.shape

        if self.chatModel == "gpt-3.5-turbo-1106":
            messages = [{"role": self.arr[i, 0], "content": self.arr[i, 1]} for i in range(num_rows)]

            response = self.client.chat.completions.create(
                model=self.chatModel,
                max_tokens=self.chatMaxTokens,
                messages=messages
            )
            
            return response.choices[0].message.content
        else:
            return "!! Sorry but you are using an unknown Model requested: " + self.chatModel