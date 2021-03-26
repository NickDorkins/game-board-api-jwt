from django.urls import path
from .views import RulesList, RulesDetail

urlpatterns = [
    path('', RulesList.as_view(), name='rules_list'),
    path('<int:pk>/', RulesDetail.as_view(), name='rules_detail'),
    
]
