from transformers import AutoTokenizer, AutoModelForCausalLM
import torch

# Load pre-trained model and tokenizer
model_name = "microsoft/DialoGPT-medium"
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForCausalLM.from_pretrained(model_name)

# Define conversation history
conversation_history = "Hello, how are you today?"

while True:
    # Get user input
    user_input = input("You: ")

    # Append user input to conversation history
    conversation_history = conversation_history + user_input + tokenizer.eos_token

    # Tokenize input and generate bot's response
    input_ids = tokenizer.encode(conversation_history, return_tensors='pt')
    bot_response_ids = model.generate(input_ids, max_length=1000, pad_token_id=tokenizer.eos_token_id)

    # Decode bot's response
    bot_response = tokenizer.decode(bot_response_ids[:, input_ids.shape[-1]:][0], skip_special_tokens=True)
    print("Bot:", bot_response)

    # Update conversation history
    conversation_history += bot_response + tokenizer.eos_token
