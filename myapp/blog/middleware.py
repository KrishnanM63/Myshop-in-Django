from django.urls import reverse
from django.shortcuts import redirect

class RedirectAuthenticatedUserMidleware:
    def __init__(self,get_response):
        self.get_response = get_response
        
    def __call__(self,request):
        paths_to_redirect = []
        if request.user.is_authenticated:
            paths_to_redirect = [reverse("regiseter_form"),reverse("login")]
                
        if request.path in   paths_to_redirect :
            return redirect(reverse("home"))
            
        response = self.get_response(request) 
        return response
    
class RestrictUnauthenticatedUserMiddleware:
    def __init__(self,get_response):
        self.get_response = get_response

    def __call__(self, request):
        restricted_paths = [reverse("cart"), reverse("place_order")]  # only these need login
        if not request.user.is_authenticated and request.path in restricted_paths:
            return redirect(reverse("login"))
        return self.get_response(request)
   
       
                