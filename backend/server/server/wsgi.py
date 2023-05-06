"""
WSGI config for server project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/2.2/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

from apps.ml.check_classifier.VGG16 import VGG16

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'server.settings')

application = get_wsgi_application()


import inspect
from apps.ml.registry import MLRegistry
from apps.ml.check_classifier.random_forest import RandomForestClassifier
from apps.ml.check_classifier.extra_trees import ExtraTreesClassifier
try:
    registry = MLRegistry() # create ML registry
    # Random Forest classifier
    rf = RandomForestClassifier()
    # add to ML registry
    registry.add_algorithm(endpoint_name="WQRandomforest",
                            algorithm_object=rf,
                            algorithm_name="random forest",
                            algorithm_status="production",
                            algorithm_version="0.0.1",
                            owner="AIOT_TEAM",
                            algorithm_description="Random Forest with simple pre- and post-processing",
                            algorithm_code=inspect.getsource(RandomForestClassifier))
    # Extra Trees classifier
    et = ExtraTreesClassifier()
    # add to ML registry
    registry.add_algorithm(endpoint_name="WQRandomforest",
                            algorithm_object=et,
                            algorithm_name="extra trees",
                            algorithm_status="testing",
                            algorithm_version="0.0.1",
                            owner="AIOT_TEAM",
                            algorithm_description="Extra Trees with simple pre- and post-processing",
                            algorithm_code=inspect.getsource(RandomForestClassifier))
    
    vgg16 = VGG16()
    # add to ML registry
    registry.add_algorithm(endpoint_name="PDVGG16",
                            algorithm_object=vgg16,
                            algorithm_name="vgg16",
                            algorithm_status="production",
                            algorithm_version="0.0.1",
                            owner="AIOT_TEAM",
                            algorithm_description="vgg16 with simple pre- and post-processing",
                            algorithm_code=inspect.getsource(VGG16))
except Exception as e:
    print("Exception while loading the algorithms to the registry,", str(e))
except Exception as e:
    print("Exception while loading the algorithms to the registry,", str(e))