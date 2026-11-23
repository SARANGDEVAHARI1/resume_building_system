# Django Static Resume Web App - Project Summary

For this assignment, I created a simple Django web application to display a static resume of a person. Here is a summary of my approach, the challenges I ran into, and what I learned.

### 1. Approach

- **Project & App Setup**: I started by setting up the Django project and then created a separate app called `resume_app`. I registered it in the `settings.py` file to keep things organized.
- **Routing**: I mapped the main project URL to include the app URLs using Django's `include` function, routing the home page (`""`) directly to my resume view.
- **View Function**: In `resume_app/views.py`, I created `resume_view`. This function defines a Python dictionary containing all the resume info (name, age, gender, email, a list of skills, and an education dictionary) and passes it to the HTML template as context.
- **Templates & Inheritance**: Instead of duplicating HTML boilerplate, I used template inheritance:
  - `base.html` has the main page layout, meta tags, and loads the CSS.
  - `resume.html` extends `base.html` using the `{% extends %}` tag and fills in the content.
- **Gender-Based Emoji Logic**: Inside the template, I wrote an `{% if %}` statement to check the gender string from the view. If it's `'male'`, it shows 👦; if `'female'`, it shows 👩; otherwise, it shows 🧑.
- **Static CSS**: I saved my styles in a static CSS file under `static/css/style.css` and loaded it in the template using the `{% load static %}` and `{% static %}` tags.

---

### 2. Challenges & How I Solved Them

- **Setting Up Static Files**: Django didn't load the CSS file at first. I realized I needed to explicitly add the `STATICFILES_DIRS` configuration in `settings.py` to point to my root static folder. Once I did that, it worked perfectly.
- **Removing Unused Django Apps**: The initial Django setup came with a lot of built-in apps like admin, auth, and sessions that are not needed for a simple static page. I cleaned up `settings.py` by removing them from `INSTALLED_APPS`, removing their middlewares, and cleaning up the `urls.py` file to keep the application lightweight.

---

### 3. Learning Outcomes

This project helped me understand:
- How to structure a Django project with multiple apps and modular URL routing.
- How to pass data from a Python backend (views) and render it dynamically on the frontend using Django template variables and loops.
- How template inheritance works in Django to keep templates DRY (Don't Repeat Yourself).
- How to configure and load static assets (like CSS styles) in a web page.
