from rest_framework import permissions

class IsAuthorOrReadOnly(permissions.BasePermission):
    """
    Разрешение позволяет только автору объекта редактировать или удалять его.
    Для безопасных методов (GET, HEAD, OPTIONS) доступ открыт всем.
    """
    def has_object_permission(self, request, view, obj):
        # Ленивые вычисления: сначала проверяем безопасный метод, если да — True; иначе проверяем авторство
        return (
            request.method in permissions.SAFE_METHODS or
            obj.author == request.user
        )