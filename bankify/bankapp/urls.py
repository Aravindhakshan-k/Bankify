from django.urls import path
from bankapp.views import GetBankListView, GetBankBranchDetails, HomeView


urlpatterns = [
    path('', HomeView.as_view()),
    path('bank-list/', GetBankListView.as_view()),
    path('bank-list/<int:limit>/', GetBankListView.as_view()),
    path('bank-details/', GetBankBranchDetails.as_view()),
    path('bank-details/<str:ifsc>/', GetBankBranchDetails.as_view()),
]

