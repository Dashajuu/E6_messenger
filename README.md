# Basic Messenger Application

This is a basic messenger application that allows users to create group chats, private chats, and manage profiles. <br><br>
The project is built using <b>Django, Django REST Framework, Django Channels, WebSockets, Django allauth </b> for authentication.

## Project Structure
E6_messenger/<br>
├── messenger/<br>
│ ├── chat/ # Chat logic application (group and private chats)<br>
│ ├── main_app/ # API + home page<br>
│ ├── media/ # Media files (avatars)<br>
│ ├── messenger/ # Main application (settings, etc.)<br>
│ ├── profiles/ # User profile management<br>
│ ├── static/ # Static files (CSS, fonts, images)<br>
│ ├── templates/ # HTML templates<br>
│ ├── db.sqlite3<br>
│ ├── manage.py<br>
├── .gitignore<br>
└── requirements.txt<br>

## Features

- User authentication and profile management
- Creation and management of private and group chats
- Real-time messaging with WebSockets

## Tech Stack

- **Backend**: Python, Django, Django REST Framework, Django Channels
- **Frontend**: HTML, CSS, JavaScript
- **Authentication**: Django allauth
- **WebSockets**: For real-time messaging

## Installation

### Prerequisites

- Python 3.8+
- pip (Python package installer)

### Setup

1. **Clone the repository**:

   ```bash
   git clone https://github.com/Dashajuu/E6_messenger.git
   
2. **Create a virtual environment**:

   ```bash
   python -m venv m_venv
   m_venv\Scripts\activate
4. **Install dependencies**:

   ```bash
   pip install -r requirements.txt

5. **Apply migrations**:

   ```bash
   cd messenger
   python manage.py migrate

6. **Run the development server**:

   ```bash
   python manage.py runserver

7. **Access the application**:

   Open your browser and navigate to http://127.0.0.1:8000/
