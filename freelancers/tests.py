from django.test import TestCase
from django.core.files.uploadedfile import SimpleUploadedFile
from datetime import datetime

from .models import Freelancer


class FrelancerTestCases(TestCase):

    def setUp(self) -> None:
        image = SimpleUploadedFile("freelancer.jpg", content=b'', content_type="image/jpg")
        self.freelancer = Freelancer.objects.create(name='Freelancer', description="I am an expert!", phone='09999',
                                                    email='freelancer@gmail.com', top_seller=False, photo=image,
                                                    date_hired=datetime.now())

    def test_is_top_seller(self):
        self.assertFalse(self.freelancer.top_seller)
