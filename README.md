# Django REST Backend API for admin site

This is a Python DRF project that provides handle goods for the backend site.

## :memo: Table of Contents

- [Installation](#rocket-getting-started)
- [Design Choices](#wrench-design-choices)
- [API Endpoints](#computer-api-endpoints)
- [Next to do](#sparkles-what-next)

## :rocket: Installation 

1. **Clone the repository**:

   ```
   https://github.com/Tarasidze/goods-service-api.git
   cd to your goods-service-api  


2. **Set your API key as an environment variable (example in .env.sample):**
   ```
   change API_KEY in .env
   change database credential
   ```
3. **Build Docker image and run it:**
   ```   
   docker-compose up --build
   ```
4. **Create admin User**
   ```
   docker exec -it goods_service_api-app-1 /bin/bash
   python manage.py createsuperuser   

   ```
5. **Now you can enter to admin page using your web browser **
   ```
   http://127.0.0.1:8000/admin/

   ```

## :wrench: Design Choices

### Database

```
The application uses SQLLite or POSTGRES databases.
Two tables, Article and Category, are defined to store goods and necessary info.
The file goods\models.py is used to define the table schemas,
and a relationship is established between them.
```
### Django REST

```
Django is chosen for building the RESTful API due to its performance
and automatic documentation generation using Swagger UI.
The API includes endpoints for retrieving Goods and Category.
```

## :computer: API Endpoints

Category CRUD API
- `POST /cities`: Create a new category.
- `GET /cities`: Get a list of all categories.
- `GET /cities/{city_id}`: Get the details of a specific category.
- `PUT /cities/{city_id}`: Update the details of a specific category.
- `DELETE /cities/{city_id}`: Delete a specific category.

Article(Goods) CRUD API
- `POST /cities`: Create a new goods.
- `GET /cities`: Get a list of all goods.
- `GET /cities/{city_id}`: Get the details of a specific goods.
- `PUT /cities/{city_id}`: Update the details of a specific goods.
- `DELETE /cities/{city_id}`: Delete a specific goods.

Swagger documentation endpoints 
- `api/doc/swagger/`: documentation endpoint
- `api/doc/`: Get GoodsAPI.yaml file

## :sparkles: What Next?

```angular2html
- add email notifications (almost done)
- add a feature to generate PDF
- add tests
```
