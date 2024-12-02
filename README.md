# Product Management System API

The **Product Management System API** is a FastApi-based async project for managing products and categories
## Installing

### Prerequisites

- Python 3.8+
- Install PostgreSQL and create db
- Docker

### Steps to Install Locally

1. **Clone the Repository**:

    ```bash
    git clone https://github.com/vladislav-tsybuliak1/spy-cat-agency
    cd spy-cat-agency
    ```

2. **Create a Virtual Environment**:

    ```bash
    python3 -m venv venv
    source venv/bin/activate  # On Windows: venv\Scripts\activate
    ```

3. **Install Dependencies**:

    ```bash
    pip install -r requirements.txt
    ```
4. **Create .env file and set up environment variables**:
    See ```env.sample```

5. **Run Migrations**:

    ```bash
    alembic upgrade head
    ```

6. **Start the Server**:

    ```bash
   python src/main.py
    ```

## Run with Docker

### Steps to Run Using Docker

1. **Build the Docker Image**:

    ```bash
    docker-compose build
    ```

2. **Start the Services**:

    ```bash
    docker-compose up
    ```

3. **Access the API**:

    - The API will be available at `http://localhost:8000/`.


### API Endpoints

The API endpoints for the Product Management System are.

- in **Postman Collection**: [Product Management System API](https://elements.getpostman.com/redirect?entityId=38620122-24bd5e35-fb00-47b9-8141-7040250e6407&entityType=collection)
- at `http://localhost:8000/docs`

## Contact
For any inquiries, please contact [vladislav.tsybuliak@gmail.com](mailto:vladislav.tsybuliak@gmail.com).
