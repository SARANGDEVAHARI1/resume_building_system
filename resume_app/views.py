from django.shortcuts import render

def resume_view(request):
    context = {
        "name": "Alex ",
        "age": 26,
        "gender": "male",  # Used in template to display gender emoji
        "email": "alex@email.com",
        "skills": ["Python", "Django", "JavaScript", "React", "PostgreSQL", "Git", "HTML5", "CSS"],
        "education": {
            "degree": "Bachelor of Science in Computer Science",
            "school": "University of Clt",
            "period": "2017 - 2021",
            "details": "Specialized in Software Engineering and Database Systems."
        },
        "experience": [
            {
                "role": "Software Developer",
                "company": "TCS",
                "period": "2021 - Present",
                "description": "Building backends using Django/Python and frontends using React."
            }
        ]
    }
    return render(request, "resume.html", context)
