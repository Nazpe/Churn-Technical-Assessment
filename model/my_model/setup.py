from setuptools import setup, find_packages

setup(
    name='my_model',  # Package name
    version='0.1.0',  # Version
    packages=find_packages(),  # Automatically find the package in model/
    include_package_data=True,
    install_requires=[
        'numpy',
        'pandas',
        'joblib',
        'scikit-learn'
        'xgboost'
    ]
)