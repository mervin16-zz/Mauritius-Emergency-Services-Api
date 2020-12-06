import unittest
from app import app


class TweetsResourceTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        pass

    @classmethod
    def tearDownClass(cls):
        pass

    def setUp(self):
        # creates a test client
        self.app = app.test_client()
        # propagate the exceptions to the test client
        self.app.testing = True

    def tearDown(self):
        pass

    ############################################################
    ###################### Error Handling ######################
    ############################################################

    def test_error_404(self):
        # Arrange
        url_case = ["/", "/en", "/fr", "/en/service", "/fr/service"]

        for url in url_case:
            # Act
            result = self.app.get(url)
            result_json = result.get_json()

            # Assert
            self.assertEqual(result_json["services"], [])
            self.assertEqual(
                result_json["message"], "No services found under this identifier."
            )
            self.assertFalse(result_json["success"])
            self.assertEqual(result.status_code, 404)

    ############################################################
    ###################### Resource Paths ######################
    ############################################################

    def test_services_en_all(self):
        # Arrange
        url = "/en/services"
        expected_size = 18

        # Act
        result = self.app.get(url)
        result_json = result.get_json()

        # Assert
        self.assertTrue("services" in result_json)
        self.assertEqual(len(result_json["services"]), expected_size)
        self.assertEqual(result_json["message"], "")
        self.assertTrue(result_json["success"])
        self.assertEqual(result.status_code, 200)

    def test_services_fr_all(self):
        # Arrange
        url = "/fr/services"
        expected_size = 18

        # Act
        result = self.app.get(url)
        result_json = result.get_json()

        # Assert
        self.assertTrue("services" in result_json)
        self.assertEqual(len(result_json["services"]), expected_size)
        self.assertEqual(result_json["message"], "")
        self.assertTrue(result_json["success"])
        self.assertEqual(result.status_code, 200)

    def test_services_en_one(self):
        # Arrange
        url_case = [
            "/en/service/security-police-direct-2",
            "/en/service/health-ambulance",
            "/en/service/security-police-tourism",
        ]

        for url in url_case:
            # Act
            result = self.app.get(url)
            result_json = result.get_json()

            # Assert
            self.assertEqual(len(result_json["services"]), 1)
            self.assertTrue("services" in result_json)
            self.assertEqual(result_json["message"], "")
            self.assertTrue(result_json["success"])
            self.assertEqual(result.status_code, 200)

    def test_services_fr_one(self):
        # Arrange
        url_case = [
            "/fr/service/security-police-direct-2",
            "/fr/service/health-ambulance",
            "/fr/service/security-police-tourism",
        ]

        for url in url_case:
            # Act
            result = self.app.get(url)
            result_json = result.get_json()

            # Assert
            self.assertEqual(len(result_json["services"]), 1)
            self.assertTrue("services" in result_json)
            self.assertEqual(result_json["message"], "")
            self.assertTrue(result_json["success"])
            self.assertEqual(result.status_code, 200)
