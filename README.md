# Google AI Personal Assistant

## Overview

Google AI Personal Assistant is an AI-powered automation assistant built using Streamlit, n8n, Google Gemini, and Google Workspace integrations. The application allows users to interact with Google services using natural language commands. Users can create tasks, schedule calendar events, send emails, create Google documents, and automate multi-step workflows through a simple chat interface.

The project combines a Streamlit frontend with an n8n AI Agent workflow, enabling seamless communication between the user, Gemini AI, and Google Workspace applications.

---

## Features

- Natural language chat interface
- Create Google Tasks
- Schedule Google Calendar events
- Send Gmail messages
- Create and update Google Docs
- Multi-step workflow automation
- AI Agent powered by Google Gemini
- Integration with Google Workspace tools
- Webhook-based communication between Streamlit and n8n

---

## Architecture

```text
User
  ↓
Streamlit Frontend
  ↓
n8n Webhook
  ↓
AI Agent (Google Gemini)
  ↓
Google Workspace Tools
   ├── Google Tasks
   ├── Google Calendar
   ├── Gmail
   └── Google Docs
```

---

## Tech Stack

### Frontend
- Streamlit

### Backend & Automation
- n8n
- Webhooks

### AI
- Google Gemini

### Google Integrations
- Google Tasks
- Google Calendar
- Gmail
- Google Docs

### Programming Language
- Python

---

## Project Structure

```text
google-all-task-workflow/
│
├── app.py
├── requirements.txt
├── README.md
├── .gitignore
│
├── screenshots/
│   ├── streamlit-ui.png
│   ├── n8n-workflow.png
│
└── n8n-workflow/
    └── google-all-task-workflow.json
```

---

## Installation

### Clone Repository

```bash
git clone <repository-url>
cd google-all-task-workflow
```

### Create Virtual Environment

```bash
python -m venv venv
```

### Activate Environment

Windows:

```bash
venv\Scripts\activate
```

Mac/Linux:

```bash
source venv/bin/activate
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

### Run Application

```bash
streamlit run app.py
```

Application will be available at:

```text
http://localhost:8501
```

---

## Example Commands

Create a task:

```text
Create a task called "Follow up with Michael"
```

Schedule a meeting:

```text
Schedule a meeting with Michael on 26 June 2026 at 10:00 AM IST
```

Send an email:

```text
Send an email to john@example.com regarding the product launch meeting
```

Create a document:

```text
Create a Google document and add meeting notes
```

Multi-step workflow:

```text
Create a task called "Send Message to Michael", schedule a calendar event for 26 June 2026 at 10:00 AM IST, send an email regarding the SaaS product launch discussion, and create a Google document summarizing the action.
```

---

## n8n Workflow

The automation layer is implemented using n8n AI Agent workflows.

Integrated tools include:

- Google Tasks
- Google Calendar
- Gmail
- Google Docs
- Google Gemini Chat Model
- Memory Node
- Webhook Trigger

The Streamlit application sends user requests to an n8n webhook endpoint, where the AI Agent determines which tools to invoke and executes the required actions.

---

## Screenshots

### Streamlit User Interface

Add screenshot:

```text
screenshots/streamlit-ui.png
```

### n8n Workflow

Add screenshot:

```text
screenshots/n8n-workflow.png
```

---

## Key Learnings

- AI Agent design and tool calling
- Workflow automation using n8n
- Google Workspace integrations
- Prompt engineering
- Webhook-based communication
- Building AI-powered productivity assistants
- Multi-step task orchestration

---

## Future Improvements

- User authentication
- Conversation memory persistence
- Voice input support
- WhatsApp integration
- Slack integration
- File attachment support
- Meeting summarization
- Expense tracking workflows

---

## Author

**Sourab Gairola**

LinkedIn: Add your LinkedIn profile

GitHub: Add your GitHub profile

---

## Disclaimer

This project is intended for learning, experimentation, and demonstration purposes. API credentials, OAuth tokens, and sensitive configuration files are excluded from the repository.