# BLOGS
BLOGS

# Django Blog Application

## Setup Instructions

1. Clone the repository:
   ```bash
   git clone <your-repository-url>
   cd blog_project


2. Create a virtual environment and install dependencies:
python -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`
pip install -r requirements.txt

3. python manage.py makemigrations/migrate

4. python manage.py createsuperuser

5. python manage.py runserver


API Endpoints:

Authentication
Obtain token: POST /api/token/
Refresh token: POST /api/token/refresh/

Posts
List all posts: GET /api/posts/
Create a new post: POST /api/posts/
Retrieve a single post: GET /api/posts/<id>/
Update a post: PUT /api/posts/<id>/
Delete a post: DELETE /api/posts/<id>/

Comments
List all comments for a post: GET /api/posts/<post_id>/comments/
Create a new comment for a post: POST /api/posts/<post_id>/comments/


6. Running test
python manage.py test
