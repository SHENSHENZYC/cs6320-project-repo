# AI Dialogue Assistant for Customized Trip Planning

Welcome to the AI Dialogue Assistant for Customized Trip Planning! This project aims to develop an AI-powered conversational chatbot that assists users in planning personalized trips, understanding user preferences, and managing existing travel plans.

## Table of Contents

- [AI Dialogue Assistant for Customized Trip Planning](#ai-dialogue-assistant-for-customized-trip-planning)
  - [Table of Contents](#table-of-contents)
  - [Project Overview](#project-overview)
  - [Team Members](#team-members)
  - [Installation](#installation)
    - [Prerequisites](#prerequisites)
    - [Clone the Repository](#clone-the-repository)
    - [Install Dependencies](#install-dependencies)
  - [Usage](#usage)
    - [Running the Chatbot](#running-the-chatbot)
    - [Features](#features)
  - [Data Sources](#data-sources)
  - [Project Structure](#project-structure)

## Project Overview

The goal of this project is to create a conversational chatbot that:

- Understands user intents and preferences using Natural Language Understanding (NLU).
- Provides tailored travel recommendations and assists in decision-making.
- Manages or cancels trips previously created, based on user input.
- Adjusts conversational tone and dialog structure according to user preferences.

**Key Features:**

- Common Ground Communication: Maintains shared knowledge during conversations.
- User Interaction: Engages users with natural language, asks open-ended questions, provides multiple-choice options, and confirms choices.
- Personal Preference Settings: Customizes interaction style, including loquacity and confirmation steps.
- Dialog Structure: Includes greeting, trip planning, trip management, and farewell phases.

## Team Members

- **Yichen Zhao**: Natural Language Understanding (NLU)
- **Ziyi Zhao**: Chatbot Response Generation
- **Ruoyu Xu**: Chatbot Response Generation and Customization

## Installation

### Prerequisites

- **Python 3.10+**

### Clone the Repository

```bash
git clone https://github.com/SHENSHENZYC/cs6320-project-repo.git
cd cs6320-project-repo
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

## Usage

### Running the Chatbot

Visit the following link to interact with the chatbot: [Chatbot Link](https://bot.dialogflow.com/0810a38f-a903-4877-bf93-1554c7d7e292). The source code for the chatbot is available in the `src/` directory, which serves as the backend for the chatbot.

### Features

- Recommend Destinations: The chatbot suggests popular travel destinations based on user preferences.
- Start a New Trip Plan: The chatbot guides you through planning a new trip.
- Manage Existing Trips: Modify or cancel trips by providing your track ID or contact information.
- Customize Interaction: Adjust the chatbot's conversational style according to your preferences.

## Data Sources

- Travel Agent Conversation Transcripts: Used to fine-tune the chatbot for travel-related interactions.
  - [American Express Travel Agent Transcripts](https://www.ai.sri.com/~communic/amex/amex.html)
- APIs:
  - ChatGPT API: For natural language understanding and generation.
  - Google Search API: To fetch real-time information on flights, hotels, and attractions.

## Project Structure

- **`data/`**: Contains datasets and data-related scripts.
- **`docs/`**: Project documentation and design diagrams.
- **`notebooks/`**: Jupyter notebooks for data exploration and prototyping.
- **`src/`**: Source code for the chatbot.
- **`tests/`**: Unit and integration tests.
- **`.gitignore`**: Specifies intentionally untracked files to ignore.
- **`config.json`**: Configuration file for API keys.
- **`requirements.txt`**: List of Python dependencies.
- **`README.md`**: Project overview and instructions.
