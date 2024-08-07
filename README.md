# Flask User Management Application

This project is a simple Flask application that manages user data stored in a SQLite database. It provides endpoints to load user data and fetch user data based on specific criteria.

## Features

- Load user data from a local JSON file into a SQLite database.
- Convert user names to uppercase before storing them.
- Fetch all users or a specific user based on their name.
- Validate and format data using Marshmallow.
- Cross-Origin Resource Sharing (CORS) enabled.
- 
## Project Structure
.  
├── app.py  
├── data.json  
├── pyproject.toml  
├── README.md  
└── requirements.txt
   

## Prerequisites

- Python 3.x
- Flask

## Setup Instructions

1. **Clone the repository:**

   ```bash
   git clone https://github.com/jpdas27/data_extraction_bulk.git
   cd data_extraction_bulk
   ```
2. **Create and activate a virtual environment:**
   ```bash
   python -m venv venv
   source venv/bin/activate   # On Windows, use `venv\Scripts\activate`
   ```
3. **Install Dependency:**
   ```bash
   pip install -r requirements.txt
   ```
4. **Run the application:**
      
   Run the Flask application to create the database file and table:
   ```bash
   python app.py
   ```

## Usage

**Endpoints**

**1. GET /fetch-data**

Loads user data from data.json .

   ```bash
   curl http://127.0.0.1:5000/load_data "
   ```
**2. GET /get-processed-data**

Fetches all users data.

```bash
curl http://127.0.0.1:5000/get-processed-data
```

**3. GET /get-processed-data?name=<name>**

Fetches a specific user by name.

```bash
curl http://127.0.0.1:5000/get-processed-data?uname=alice
```