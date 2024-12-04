# Career Recommendation Chatbot

## Project Overview

This is a Flask-based web application that provides personalized career recommendations in technology fields. The chatbot helps users explore potential career paths based on their interests and skills across Computer Science (CS), Information Technology (IT), and Electronics and Communication Engineering (ECE) domains.

## Features

- Interactive chatbot interface
- Career recommendations based on user skills
- Real-time career data fetched from a PostgreSQL database
- Supports three technology domains: CS, IT, and ECE
- Provides detailed career information including:
  - Job role
  - Description
  - Required skills
  - Average salary
  - Growth potential

## Technologies Used

- Backend: 
  - Python
  - Flask
  - Requests
  - Flask-CORS
- Frontend:
  - HTML
  - Tailwind CSS
  - Vanilla JavaScript
- Database:
  - PostgreSQL
  - psycopg2

## Project Structure

```
career-recommendation-chatbot/
│
├── backend/
│   ├── career_upload_script.py    # Database upload script
│   └── chatbot_app.py             # Main Flask application
│
├── frontend/
│   └── index.html                 # Chatbot user interface
│
└── README.md                      # Project documentation
```

## Prerequisites

- Python 3.8+
- PostgreSQL
- pip (Python package manager)

## Installation

1. Clone the repository:
```bash
git clone https://github.com/Mohammad-416/Recommendation_System.git
cd Chatbot
```

2. Create a virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Set up PostgreSQL database
   - Create a new database
   - Update connection strings in the upload script and chatbot application

## Configuration

### Database Configuration
1. Create a `.env` file or set environment variables:
```
DATABASE_URL=postgresql://username:password@host:port/database
```

### API Endpoint
Update `CAREERS_API_URL` in the chatbot script with your actual API endpoint.

## Running the Application

1. Start the career data upload service:
```bash
python career_upload_script.py
```

2. Launch the chatbot application:
```bash
python main.py
```

3. Open `index.html` in your web browser

## Usage

1. Enter your name
2. Select a technology domain (CS/IT/ECE)
3. Share your current skills
4. Receive personalized career recommendations

## Customization

- Modify `CAREER_DATA` to add or update career information
- Adjust conversation flow in `CONVERSATION_STEPS`
- Customize frontend design in `index.html`


## License

Distributed under the MIT License. See `LICENSE` for more information.

## Contact

Mohammad - m9971359949@gmail.com

Project Link: [https://github.com/Mohammad-416/Recommendation_System](https://github.com/Mohammad-416/Recommendation_System)
```

## Troubleshooting

- Ensure all dependencies are installed
- Check database connection strings
- Verify API endpoint is accessible
- Review CORS configuration if facing cross-origin issues

## Future Improvements

- Add more detailed skill matching
- Implement user authentication
- Create a more sophisticated recommendation algorithm
- Add more technology domains