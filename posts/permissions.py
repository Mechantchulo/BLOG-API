from rest_framework import permissions  # Import the permissions module from Django REST framework

class IsAuthorOrReadOnly(permissions.BasePermission):  # Define a custom permission class inheriting from BasePermission
    
    def has_object_permission(self, request, view, obj):  # Define a method to check object-level permissions
        # Check if the request method is considered "safe" (e.g., GET, HEAD, OPTIONS)
        if request.method in permissions.SAFE_METHODS:
            return True  # Allow access if the request is safe
        # Check if the user making the request is the author of the object
        return obj.author == request.user  # Grant access only if the user is the author
