# LLM Chat Application

Use this application to send prompts to an LLM (ChatGPT by default).

## How to run

There are two requirements for the application to run:

1. The environment variable `OPENAI_API_KEY` must be set to a valid OpenAI API key.
2. A MongoDB instance must be running on the default port (27017) on localhost.

To start the application, run `fastapi run main.py` form the `backend` directory.

The application will run on `http://localhost:8000/api/v1`.
Prompts can be sent to `/api/v1/chat` with a POST request in the format `{"prompt": <your prompt here>}`.