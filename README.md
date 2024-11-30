# product-management-system


Your task is to develop a simple Product Management System using FastAPI, SQLalchemy, Alembic, and Pydantic. Feel free to add other technologies if you will.
Requirements:

## Model:
Create a Product model with fields id, name, description, price, and created_at. The id should be the primary key.
API Endpoints:

### 1. Create Product:
Create an API endpoint /products/ (POST request) that receives a product's name, description and price in JSON format and stores it in the database.
### 2. Get Product:
Create an API endpoint /products/{id} (GET request) that retrieves a product based on the id.
### 3. Update Product:
Create an API endpoint /products/{id} (PUT request) that updates a product's name, description or price based on the id.
### 4. Delete Product:
Create an API endpoint /products/{id} (DELETE request) that deletes a product based on the id.


## Database:
Use SQLalchemy ORM to manage database operations.

### Migrations:
Use Alembic for database migration. Make sure to create a new database revision file every time the Product model changes.
### Validation:
Use Pydantic for data validation. Validate the name, description, and price for proper format.

## Should contain:

 - A repository containing all the code.
 - A README.md file explaining how to run the application and API usage.
 - Postman collection or CURL commands to test the API. 

### Additional tasks for extra points:
 - Implement a basic inventory management feature (i.e., track the quantity of each product).
 - Implement a simple product category classification (i.e., each product can belong to a category). 
 - Write unit tests for your API endpoints. 
 - Remember, while the completion of the task is important, we also want to see good software engineering practices. Keep in mind principles like DRY, SOLID.
