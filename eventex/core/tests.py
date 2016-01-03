from django.test import TestCase


class HomeTest(TestCase):

    def setUp(self):
        self.response = self.client.get("/")

    def test_get_root(self):
        """
        GET / must return status code 200
        """
        self.assertEquals(200, self.response.status_code)

    def test_template_root(self):
        """
         GET / must have index.html as template
        """
        self.assertTemplateUsed(self.response, "index.html")

