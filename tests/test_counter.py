"""
Test Cases for Counter Web Service

Create a service that can keep a track of multiple counters
- API must be RESTful - see the status.py file. Following these guidelines, you can make assumptions about
how to call the web service and assert what it should return.
- The endpoint should be called /counters
- When creating a counter, you must specify the name in the path.
- Duplicate names must return a conflict error code.
- The service must be able to update a counter by name.
- The service must be able to read the counter
"""
from unittest import TestCase

# we need to import the unit under test - counter
from src.counter import app 
from src.counter import COUNTERS

# we need to import the file that contains the status codes
from src import status 

class CounterTest(TestCase):
    """Counter tests"""
    def setUp(self):
        self.client = app.test_client()

    def test_create_a_counter(self):
        """It should create a counter"""
        client = app.test_client()
        result = client.post('/counters/foo')
        self.assertEqual(result.status_code, status.HTTP_201_CREATED)

    def test_duplicate_a_counter(self):
        """It should return an error for duplicates"""
        result = self.client.post('/counters/bar')
        self.assertEqual(result.status_code, status.HTTP_201_CREATED)
        result = self.client.post('/counters/bar')
        self.assertEqual(result.status_code, status.HTTP_409_CONFLICT)

    def test_update_a_counter(self):
        """It should update a counter"""
        # 1. Make a call to Create a counter.
        result = self.client.post('/counters/update')

        # 2. Ensure that it returned a successful return code.
        self.assertEqual(result.status_code, status.HTTP_201_CREATED)

        # 3. Check the counter value as a baseline.
        baseline_value = result.get_json()['update']
        self.assertEqual(baseline_value, 0)

        # 4. Make a call to Update the counter that you just created.
        updated_result = self.client.put('/counters/update')
        
        # 5. Ensure that it returned a successful return code.
        self.assertEqual(updated_result.status_code, status.HTTP_200_OK)

        # 6. Check that the counter value is one more than the baseline you measured in step 3.
        updated_value = updated_result.get_json()['update']
        self.assertEqual(updated_value, baseline_value+1)

        # Check that updating a new client returns a proper return code.
        result2 = self.client.put('/counters/update_fail')
        self.assertEqual(result2.status_code, status.HTTP_204_NO_CONTENT)

    def test_read_a_counter(self):
        """It should read a counter"""
        # Make a call to create a counter, and put the counter
        self.client.post('/counters/read')
        self.client.put('/counters/read')

        # Make a call to get a counter, and ensure it returned a good code
        result = self.client.get('/counters/read')
        self.assertEqual(result.status_code, status.HTTP_200_OK)

        # Check that reading a fake client returns a proper return code.
        result2 = self.client.get('/counters/read_fail')
        self.assertEqual(result2.status_code, status.HTTP_404_NOT_FOUND)

    def test_delete_a_counter(self):
        """It should delete a counter"""
        # Make a call to create a counter, and put the counter
        self.client.post('/counters/delete')
        self.client.put('/counters/delete')

        # Make a call to delete a counter, and ensure it returned a good code
        result = self.client.delete('/counters/delete')
        self.assertEqual(result.status_code, status.HTTP_204_NO_CONTENT)

        # Check that reading a fake client returns a proper return code.
        result2 = self.client.delete('/counters/delete_fail')
        self.assertEqual(result2.status_code, status.HTTP_404_NOT_FOUND)
