# Docker Flask MySQL App

A simple containerized web application using Flask and MySQL.

## Architecture

User → Flask API → MySQL Database

## Tech Stack

- Python (Flask)
- MySQL
- Docker
- Docker Compose

## Setup

Clone the repo:

git clone <repo>

Run:

docker-compose up --build

Access app:

http://localhost:5000

## API Endpoints

POST /add_user
GET /users