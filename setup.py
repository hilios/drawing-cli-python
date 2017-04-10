from setuptools import setup, find_packages


setup(
    name='simple-draw',
    version='1.0.0',
    packages=find_packages(),
    include_package_data=True,
    install_requires=[],
    entry_points='''
        [console_scripts]
        simple-draw=main:run
    ''',
)
