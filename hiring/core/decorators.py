from django.contrib.auth.decorators import login_required
from functools import wraps
from django.http import HttpResponseForbidden
error_303_html = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Error 303 - See Other</title>
    <style>
        body {
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            background-color: #f5f5f5;
            color: #333;
            text-align: center;
            padding: 100px 20px;
        }

        .error-container {
            background-color: white;
            padding: 50px;
            border-radius: 12px;
            box-shadow: 0 8px 20px rgba(0,0,0,0.1);
            max-width: 500px;
            margin: 0 auto;
        }

        h1 {
            font-size: 72px;
            margin: 0;
            color: #ff5e5e;
        }

        h2 {
            margin: 20px 0;
            font-size: 28px;
        }

        p {
            font-size: 18px;
            color: #666;
        }

        a.button {
            display: inline-block;
            margin-top: 30px;
            padding: 12px 30px;
            background-color: #007bff;
            color: white;
            text-decoration: none;
            font-size: 16px;
            border-radius: 8px;
            transition: background-color 0.3s ease;
        }

        a.button:hover {
            background-color: #0056b3;
        }
    </style>
</head>
<body>
    <div class="error-container">
        <h1>303</h1>
        <h2>See Other</h2>
        <p>The requested resource has been replaced. Please follow the new location.</p>
        <a href="/" class="button">Return to Home</a>
    </div>
</body>
</html>
"""

def login_and_role_required(required_role):
    def decorator(view_func):
        @wraps(view_func)
        @login_required
        def _wrapped_view(request,*args,**kwargs):
            user=request.user
            if required_role=="applicant" and not user.is_applicant:
                return HttpResponseForbidden(error_303_html)

            if required_role=="recruiter" and not user.is_recruiter:
                return HttpResponseForbidden(error_303_html)
            return view_func(request,*args,**kwargs)
        return _wrapped_view
    return decorator