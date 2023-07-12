# Project-4-Fundraiser-Backend

Fundraiser is a crowd-funding platform powered by Django and React. This repository contains the Django backend for Fundraiser. It handles user registration and authentication, and provides RESTful API endpoints for managing users, campaigns, and donations.

## Table of Contents

- [Getting Started](#getting-started)
  - [Prerequisites](#prerequisites)
  - [Installation](#installation)
- [Usage](#usage)
  - [Endpoints](#endpoints)
- [Contributing](#contributing)
- [License](#license)
- [Contact](#contact)

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.

### Prerequisites

- Python 3.7 or higher
- Django 3.2.5 or higher
- Django Rest Framework 3.12.4 or higher
- django-cors-headers 3.7.0 or higher

### Installation

1. Clone the repo (git clone https://github.com/lschmidtfellner/Project-4-Fundraiser-Backend)
2. Set up a virtual environment and activate it (mkvirtualenv fundraising_platform)
3. Install Python packages (pip install -r requirements.txt)
4. Set up the database (python3 manage.py makemigrations then python3 manage.py migrate)
5. Create a superuser (python3 manage.py createsuperuser)
6. Run the server (python3 manage.py runserver)

## Usage

The backend provides several API endpoints for the frontend to consume. Please refer to the Endpoints section for more details.

### Endpoints

| Endpoint                                  | Method           | Description                                                 |
| ----------------------------------------- | ---------------- | ----------------------------------------------------------- |
| `/api/register/`                          | POST             | Register a new user                                         |
| `/api/login/`                             | POST             | Log in a user                                               |
| `/api/campaigns/`                         | GET, POST        | Get all campaigns, create a campaign                        |
| `/api/campaigns/{campaign_id}/`           | GET, PUT, PATCH, DELETE | Manage a specific campaign                      |
| `/api/campaigns/{campaign_id}/donations/` | GET              | Get all donations for a specific campaign                   |
| `/api/donations/`                         | GET, POST        | Get all donations, create a donation                        |
| `/api/donations/{donation_id}/`           | GET, PUT, PATCH, DELETE | Manage a specific donation                      |
| `/api/users/`                             | GET              | Get all users                                               |
| `/api/users/{user_id}/`                   | GET, PUT, PATCH, DELETE | Manage a specific user                          |
| `/api/users/{user_id}/donations/`         | GET              | Get all donations from a specific user                      |
| `/api/users/{user_id}/campaigns/`         | GET              | Get all campaigns from a specific user                      |

## Contributing

Any contributions are greatly appreciated.

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## License

This project was created for educational purposes as part of the curriculum at General Assembly. It is not intended for commercial use or distribution.

## Contact

Cicely: https://github.com/brooksienyc | cicelybrooks@gmail.com
Luke: https://github.com/lschmidtfellner | lschmidtfellner@gmail.com
Kevin: https://github.com/kevininga | kevininga813@gmail.com
Mike: https://github.com/michael-fesselmeyer | michael.fesselmeyer@gmail.com 