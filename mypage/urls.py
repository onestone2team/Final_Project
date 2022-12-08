from django.urls import path
from mypage import views


urlpatterns = [
    path('profile/', views.ChangeUserInfo.as_view(), name='change_user_info_view'),
    path('profile/password/', views.ChangeUserPassword.as_view(), name='change_user_password'),
    path('inquiry/', views.InquiryList.as_view(), name='InquiryList'),
    path('<int:category_id>/<int:product_id>/inquiry/', views.AddinquiryList.as_view(), name='AddinquiryList'),
    path('admin/inquiry/', views.AdminInquiry.as_view(), name='DirectorInquiry'),
    path('admin/inquiry/<int:Inquiry_id>/', views.AddadminInquiry.as_view(), name='AddadminInquiry'),
    path('myorderlist/', views.MyOrderListView.as_view(), name='change_user_info_view'),
    path('mypayment/', views.UserPaymentView.as_view(), name="user_product_view"),
]