from django.urls import path, include
from feedback.views import create_post,post_view
from django.conf.urls import url

urlpatterns = [
	path('create/',create_post),
	path('viewpost/',post_view),
	#path('admin/', admin.site.urls),
]
