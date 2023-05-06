from django.test import TestCase
import inspect
from apps.ml.check_classifier.VGG16 import VGG16
from apps.ml.registry import MLRegistry
from apps.ml.check_classifier.random_forest import RandomForestClassifier
from apps.ml.check_classifier.extra_trees import ExtraTreesClassifier

class MLTests(TestCase):
    def test_rf_algorithm(self):
        input_data =  {
            "ph": 5.735724,
            "Hardness": 158.318741,
            "Solids": 25363.016594,
            "Chloramines": 7.728601,
            "Sulfate": 377.543291,
            "Conductivity": 568.304671,
            "Organic_carbon": 13.626624,
            "Trihalomethanes": 75.952337,
            "Turbidity": 4.732954
           
        }
        my_alg = RandomForestClassifier()
        response = my_alg.compute_prediction(input_data)
        self.assertEqual('OK', response['status'])
        self.assertTrue('label' in response)
        self.assertEqual('1', response['label'])

    def test_registry(self):
            registry = MLRegistry()
            self.assertEqual(len(registry.endpoints), 0)
            endpoint_name = "WQRandomforest"
            algorithm_object = RandomForestClassifier()
            algorithm_name = "random forest"
            algorithm_status = "production"
            algorithm_version = "0.0.1"
            algorithm_owner = "AIOT_TEAM"
            algorithm_description = "Random Forest with simple pre- and post-processing"
            algorithm_code = inspect.getsource(RandomForestClassifier)
            # add to registry
            registry.add_algorithm(endpoint_name, algorithm_object, algorithm_name,
                        algorithm_status, algorithm_version, algorithm_owner,
                        algorithm_description, algorithm_code)
            # there should be one endpoint available
            self.assertEqual(len(registry.endpoints), 1)
    def test_registryvgg16(self):
        registry = MLRegistry()
        self.assertEqual(len(registry.endpoints), 0)
        endpoint_name = "vgg16"
        algorithm_object = RandomForestClassifier()
        algorithm_name = "vgg16"
        algorithm_status = "production"
        algorithm_version = "0.0.1"
        algorithm_owner = "AIOT_TEAM"
        algorithm_description = "VGG16 with simple pre- and post-processing"
        algorithm_code = inspect.getsource(VGG16)
        # add to registry
        registry.add_algorithm(endpoint_name, algorithm_object, algorithm_name,
                    algorithm_status, algorithm_version, algorithm_owner,
                    algorithm_description, algorithm_code)
        # there should be one endpoint available
        self.assertEqual(len(registry.endpoints), 1)
    def test_VGG16_algorithm(self):
       
        input_data = "D:/gp project/plant disess/New Plant Diseases Dataset(Augmented)/New Plant Diseases Dataset(Augmented)/test/AppleCedarRust1.JPG"
           
        
        my_alg = VGG16()
        response = my_alg.compute_prediction(input_data)
        print(response)
        self.assertEqual('OK', response['status'])
        # self.assertTrue('label' in response)
        self.assertEqual(('Apple___Cedar_apple_rust', 2), response['label'])


    def test_et_algorithm(self):
        input_data = {
            "ph": 5.735724,
            "Hardness": 158.318741,
            "Solids": 25363.016594,
            "Chloramines": 7.728601,
            "Sulfate": 377.543291,
            "Conductivity": 568.304671,
            "Organic_carbon": 13.626624,
            "Trihalomethanes": 75.952337,
            "Turbidity": 4.732954
           
        }
        my_alg = ExtraTreesClassifier()
        response = my_alg.compute_prediction(input_data)
        self.assertEqual('OK', response['status'])
        self.assertTrue('label' in response)
        self.assertEqual('0', response['label'])