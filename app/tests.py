from django.test import SimpleTestCase

# Create your tests here.


class TestFontTimes(SimpleTestCase):
    def test_Chocolate_2(self):
        response = self.client.get("/warmup-2/font-times/?str_1=Chocolate&num_1=2")
        self.assertContains(response, "ChoCho")

    def test_Chocolate_3(self):
        response = self.client.get("/warmup-2/font-times/?str_1=Chocolate&num_1=3")
        self.assertContains(response, "ChoChoCho")

    def test_ABC_3(self):
        response = self.client.get("/warmup-2/font-times/?str_1=Abc&num_1=3")
        self.assertContains(response, "AbcAbcAbc")

class TestNoTeenSum(SimpleTestCase):
    def test_1_2_3(self):
        response = self.client.get("/logic-2/no-teen-sum/?int_value1=1&int_value2=2&int_value3=3")
        self.assertContains(response, "6")

    def test_3_2_1(self):
        response = self.client.get("/logic-2/no-teen-sum/?int_value1=2&int_value2=13&int_value3=1")
        self.assertContains(response, "3")

    def test_2_1_3(self):
        response = self.client.get("/logic-2/no-teen-sum/?int_value1=2&int_value2=1&int_value3=14")
        self.assertContains(response, "3")

    
class TestXYZ(SimpleTestCase):
    def test_abcxyz(self):
        response = self.client.get("/string-2/xyz-there/?xyz_string=abcxyz")
        self.assertContains(response, "True")

    def test_abc_xyz(self):
        response = self.client.get("/string-2/xyz-there/?xyz_string=abc.xyz")
        self.assertContains(response, "False")

    def test_xyz_abc(self):
        response = self.client.get("/string-2/xyz-there/?xyz_string=xyz.abc")
        self.assertContains(response, "True")
    
class TestCenteredAverage(SimpleTestCase):
    def test_1_through_10(self):
        response = self.client.get("/list-2/centered-average/?val_1=1&val_2=2&val_3=3&val_4=4&val_5=100&val_6=&val_7=")
        self.assertContains(response, "3")

    def test_1_1_5_5_10_8_7(self):
        response = self.client.get("/list-2/centered-average/?val_1=1&val_2=1&val_3=5&val_4=5&val_5=10&val_6=8&val_7=7")
        self.assertContains(response, "5")

    def test_10_4_2_4_2_0(self):
        response = self.client.get("/list-2/centered-average/?val_1=-10&val_2=-4&val_3=-2&val_4=-4&val_5=-2&val_6=0&val_7=")
        self.assertContains(response, "-3")