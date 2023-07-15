from django.urls import include, path
# from rest_framework.authtoken.views import obtain_auth_token    
from .views import *

# Site


app_name = 'backapi'

urlpatterns = [
    path('tickets/', TicketOrderView.as_view()),
    path('createtickets/', TicketOrderCreate.as_view()),
    path('get_configuration_file/', GetConfFile.as_view()),
    path('single-file/', FileUploadView.as_view()),
    path('export_exel/', download_data),
    path('getByMonth/', GetByMonth.as_view()),
    # path('backapi/', include('backapi.urls')),
   
]

