
# Video Management API

This is a FastAPI project for video management, allowing admins to upload videos, convert them to `.mp4`, search for videos by metadata, block downloads, and more.

## Features

- Upload videos in multiple formats (`mp4`, `mkv`, `avi`).
- Convert uploaded videos to `.mp4` format asynchronously.
- Search for videos using metadata (name, size).
- Block video downloads for specific IDs.
- Use PostgreSQL as the database and Redis for caching.

## Requirements

- Python 3.10+
- PostgreSQL
- Redis


## Setup Django Project

Clone the project

_using ssh_

```bash
git clone https://github.com/Dhruvik-Kakadiya/video_management.git
```

_or using http_

```bash
git clone 
```

Go to the project directory

```bash
cd video_management
```

Create a virtual environment

```bash
python3 -m venv ./venv
```

Activate a virtual environment

```bash
source venv/bin/activate
```

Install dependecies

```bash
pip install -r requirements.txt
```

Provide Environment variables in project root directory
```bash
touch .env
gedit .env
```

## Setup Database

Login to postgres console

```bash
sudo -u postgres psql
```

<span id="database_user_created">Create a new postgres user</span>

```sql
create user <POSTGRES_USERNAME> with encrypted password '<POSTGRES_PASSWORD>';
```

<span id="database_created">Create a new database with proper rights</span>

```sql
CREATE DATABASE <DATABASE_NAME> owner <POSTGRES_USERNAME>;
```

Exit the console

```sql
exit
```
## Start the Application
```sql
uvicorn app.main:app --reload
```

## Start the Application with docker
```sql
docker-compose up --build
```

## API Documentation
```sql
http://127.0.0.1:8000/docs
```