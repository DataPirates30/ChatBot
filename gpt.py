# Transformer is a deep learning architecture that allows AI models to process and generate text efficiently.
# Before transformers , AI used RNN models and LSTM models to generate text, which struggled with long sentences and were slow.
# As these models used to process one word at a time, they needed more computation power and memory
# Transformers models can process the entire sentence at once, which makes them faster and more efficient.
# Transformers in a general sense is a compiler, whereas LSTM models and RNN models are interpreters.

from transformers import pipeline

generator = pipeline('text-generation', model='gpt2')

# Generate a sequence of text based on the given prompt
response = generator("Once upon a time", max_length=100, num_return_sequences=5)

