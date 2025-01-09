# RAG-on-SQL-Data

This project demonstrates a **Retrieval-Augmented Generation (RAG)** system leveraging SQL databases and Google Cloud's Vertex AI. The aim is to retrieve relevant information from a SQL database and use a language model to generate insights or responses based on that data.

---

## Features

- **SQL Data Retrieval**: Extract relevant records from the SQLite database (`students.db`) using custom queries.
- **Integration with Vertex AI**: Use Google Cloud's Vertex AI for LLM-based data augmentation.
- **Configurable and Extensible**: Easily adapt for other databases or cloud providers.
- **Secure Configuration**: Manage credentials and keys safely with `.gitignore`.

---

## Folder Structure

```plaintext
sql_rag_project/
├── db/
│   └── students.db          # SQLite database
├── keys/
│   └── <service-account.json>  # Google Cloud service account credentials
├── services/
│   ├── db_service.py        # Handles database interactions
│   ├── llm_service.py       # Interacts with Vertex AI
├── venv/                    # Python virtual environment
├── .gitignore               # Excludes sensitive files and environment configs
├── app.py                   # Main application entry point
└── requirements.txt         # Python dependencies
