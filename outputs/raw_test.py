import unittest
import uuid
from datetime import datetime

class TestBaseModel(unittest.TestCase):
    def test_base_model_methods(self):
        my_model = BaseModel()
        my_model.name = "My First Model"
        my_model.my_number = 89
        self.assertEqual(my_model.name, "My First Model")
        self.assertEqual(my_model.my_number, 89)
        self.assertTrue(hasattr(my_model, 'id'))
        self.assertTrue(hasattr(my_model, 'created_at'))
        self.assertTrue(hasattr(my_model, 'updated_at'))

        initial_updated_at = my_model.updated_at
        my_model.save()
        self.assertNotEqual(initial_updated_at, my_model.updated_at)

        my_model_json = my_model.to_dict()
        self.assertIsInstance(my_model_json, dict)
        self.assertIn('name', my_model_json)
        self.assertIn('my_number', my_model_json)
        self.assertIn('id', my_model_json)
        self.assertIn('created_at', my_model_json)
        self.assertIn('updated_at', my_model_json)
        self.assertIn('__class__', my_model_json)
        self.assertEqual(my_model_json['name'], "My First Model")
        self.assertEqual(my_model_json['my_number'], 89)
        self.assertEqual(my_model_json['__class__'], 'BaseModel')

if __name__ == '__main__':
    unittest.main()
