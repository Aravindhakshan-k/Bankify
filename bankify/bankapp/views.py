from django.shortcuts import render
from django.views.generic import View
from django.http import JsonResponse
import pandas as pd


# Create your views here.
class GetBankListView(View):
    def get(self, request, *args, **kwargs):
        data = pd.read_csv("bankapp/data/bank_branches.csv")
        limit = kwargs.get('limit')
        val = data.head(limit)[["bank_name","branch","ifsc"]].to_dict('records')
        return JsonResponse(val, safe=False)

        
class GetBankBranchDetails(View):
    def get(self, request, *args, **kwargs):
        data = pd.read_csv("bankapp/data/bank_branches.csv")
        ifsc = kwargs.get('ifsc')
        if ifsc is None:
            return JsonResponse({'result':'ifsc Not Found in url', 'status':200})
        branch_data = data[data['ifsc']==ifsc.upper()]
        if branch_data.empty:
            return JsonResponse({'result':'ifsc Not Found in data', 'status':200})
        
        bank_data = {
            'bank_name':branch_data['bank_name'].iloc[0],
            'branch':branch_data['branch'].iloc[0],
            'address':branch_data['address'].iloc[0],
            'city':branch_data['city'].iloc[0],
            'district':branch_data['district'].iloc[0],
            'state':branch_data['state'].iloc[0],
        }
        return JsonResponse({'result':bank_data, 'status':200}, safe=False)