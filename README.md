# jwt_authentication_django_register_login
complete project for register/login user with JWT in Django Rest Frame Work (drf).
This Repository created for implementing JWT in DRF. 
step 0 ---> 
1- creating project
2- pip install Django
3- pip install djangorestframework
4- pip install djangorestframework-samplejwt
5- pip install pillow (for upload/save image, user Avatar)

step 1 --->
1- django-admin startproject src .
2- django-admin startapp User
3- django-admin startapp ResApi { for all RestApi's who we want to create}
4- go to src->setting-> INSTALLED_APPS and add below codes:
    'rest_framework',
    'User.apps.UserConfig',
    'RestApi.apps.RestapiConfig',
    
4- go to src-> settings and add below codes :
    REST_FRAMEWORK = {
        'DEFAULT_PERMISSION_CLASSES': [
            'rest_framework.permissions.AllowAny'
       ],
        'DEFAULT_AUTHENTICATION_CLASSES': [
            'rest_framework_simplejwt.authentication.JWTAuthentication',
       ]
}

5- create Custom User Model {go to User-> models)
6- now you need to understand your custom User model to django:
   go to src-> settings and add below code:
   AUTH_USER_MODEL = 'User.User'


