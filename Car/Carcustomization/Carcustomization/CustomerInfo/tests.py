from django.test import TestCase, Client
from .models import DesireInfo
from django.urls import reverse, resolve
from .views import *

# Create your tests here.
class ModelTestCase(TestCase):
    def test_upload_CustomerName_blank(self):
        pk =DesireInfo.objects.create(CustomerName="milan")
        self.assertTrue(pk.upload_CustomerName_blank())
    def test_image_blank(self):
        pk =DesireInfo.objects.create(pdf="")
        self.assertTrue(pk.image_blank())
    def test_CustomerName_char(self):
        pk =DesireInfo.objects.create(CustomerName="milan")
        self.assertTrue(pk.CustomerName_char())

    def test_name(self):
        ok =DesireInfo.objects.create(CustomerName="h",CarName="h")
        self.assertEqual(str(ok),  
            'h')
    def test_str(self):
        ok =DesireInfo.objects.create(CustomerName="h",CarName="h")
        self.assertEqual(str(ok), 'h')        
    # def test_cover(self):
    #     pk =DesireInfo.objects.create(pdf==True)
    #     self.assertTrue(pk.cover())

    # def test_string_representation(self):
    #     info = DesireInfo(CustomerName="My string CustomerName")
    #     self.assertEqual(str(info), info.CustomerName)

    # def test_post_list_view(self):
    # # template_name = 'class_Order_list.html'
    #     # response = self.client.get(reverse('info'))
    #     self.assertEqual(response.status_code, 200)
    #     self.assertContains(response, 'just a test')
    #     self.assertTemplateUsed(response, 'class_Order_list.html')
        

