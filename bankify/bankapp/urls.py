from django.urls import path
from bankapp.views import GetBankListView, GetBankBranchDetails


urlpatterns = [
    path('bank-list/<int:limit>/', GetBankListView.as_view()),
    path('bank-details/', GetBankBranchDetails.as_view()),
    path('bank-details/<str:ifsc>/', GetBankBranchDetails.as_view()),
]
