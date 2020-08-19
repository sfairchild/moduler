from setuptools import setup

setup(
        name='Moduler',
        version='0.0.2',
        author='Sean Fairchild',
        author_email='seanf215@gmail.com',
        packages=['moduler'],
        scripts=['bin/moduler'],
        url='#TODO Change this',
        license='MIT',
        description='Used to checkout packages into a directory',
        long_description=open('README.txt').read(),
        install_requires=[
            "PyYAML >= 5.3.1",
            "pytest",
            ],
        zip_safe=False
        )

