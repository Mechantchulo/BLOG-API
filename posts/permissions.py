from rest_framework import permissions

class IsAuthorOrReadOnly(permissions.BasePermission):
    
    def has_object_permission(self, request, view, obj):
        #check if the request is safe(GET, HEAD, OPTIONS)
        if request.method in permissions.SAFE_METHODS:
            return True
        #check if the user is the author of the post
        
        return obj.author == request.user