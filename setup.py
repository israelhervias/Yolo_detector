# setup.py
from setuptools import setup

setup(
    name='yolo_analyis',
    version='0.1',
    author='Israel Hervías Higueras',
    author_email='israelhervias@hotmail.com',
    maintainer='Israel Hervías Higueras',
    maintainer_email='israelhervias@hotmail.com',
    url='https://github.com/israelhervias/Yolo_Analysis_UOC',
    download_url='https://github.com/israelhervias/Yolo_Analysis_UOC/download',
    keywords=['Python', 'Machine_Learning', 'Python_package'],
    license='MIT',
    description='Python library to process images from cities',
    long_description='Python library to process images from cities from UOC.',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
    ],
    packages=['ejercicio1', 'ejercicio2', 'ejercicio3', 'ejercicio4',
    'ejercicio5', 'ejercicio6', 'ejercicio7'],
    include_package_data=True,
    install_requires=['requirements.txt'],
    python_requires='>=3.6',
    zip_safe=False,
)
