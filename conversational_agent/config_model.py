from langchain.chat_models import init_chat_model

# Configure model details
MODEL_NAME = "gpt-oss:20b"
TEMPERATURE = 0.7
model = init_chat_model(
    model=MODEL_NAME, model_provider="ollama", temperature=TEMPERATURE
)
