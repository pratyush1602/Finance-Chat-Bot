# Finance Chat Bot

A conversational AI chatbot designed to assist users with financial queries, offering an intelligent and interactive experience. The chatbot is capable of answering questions about personal finance, providing guidance on investments, and performing financial calculations, all while ensuring the user experience is intuitive and seamless.

## Features

- **Flow Orchestration**: The chatbot prompts the user field by field, ensuring each step of the conversation is structured. It handles conditional branches, where the flow can dynamically change based on user inputs, and signals completion once all required information is gathered.

- **Interactive Validation**: As the user interacts with the bot, real-time input validation is performed. If an answer is invalid or incomplete, the bot will provide clear error messages and re-prompt the user until a valid response is provided.

- **State Management**: The chatbot stores interim answers in a context object or session, allowing for seamless branching logic. This enables the bot to remember previous inputs, ensuring that responses are relevant to earlier choices and enabling personalized experiences.

- **Extensibility**: The chatbot's design follows a clear pattern for adding new fields or rules. As a result, you can extend the conversation with new queries or validation checks without requiring major changes to the underlying structure of the chatbot.

## Getting Started

Follow these steps to get the project running on your local machine:

- ### 1. Clone the Repository

  Clone the repository to your local machine using the following command:

  ```bash
  git clone https://github.com/pratyush1602/Finance-Chat-Bot.git


- ### 2. Navigate to Finance-Chat-Bot
  ```
    cd Finance-Chat-Bot

- ### 3. Run
  ```
    python chatbot.py
