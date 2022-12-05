from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from mypage.models import Inquiry
from mypage.serializers import InquiryListSerializer,AddinquiryListSerializer
# Create your views here.

#사용자 문의
class InquiryList(APIView):
    def get(self,request):
     inquiry = Inquiry.objects.all()  
     serializer = InquiryListSerializer(inquiry, many=True) 
     return Response(serializer.data, status=status.HTTP_200_OK)
 
class AddinquiryList(APIView):
    def post(self,request,category_id, product_id, user_id):
     serializer = AddinquiryListSerializer(data=request.data)
     if serializer.is_valid():
        serializer.save(category_id=category_id, product_id=product_id, user_id=user_id)
        return Response({"message":"문의가 등록되었습니다","data":"serializer.data"}, status=status.HTTP_201_CREATED)  
     else: 
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)    

#관리자 문의 페이지
class DirectorInquiry(APIView):
    def get(self,request):
     pass
 
    def post(self,request):
        pass


class ChangeUserInfo(APIView):
    pass