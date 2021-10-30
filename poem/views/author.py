from django.db.models import Q
from django.views.generic import ListView

from poem.mixins import LoginPermissionMixin

from poem.models import Author


class AuthorListView(LoginPermissionMixin, ListView):
    model = Author
    paginate_by = 10
    queryset = Author.objects.all()
