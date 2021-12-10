from setuptools import setup

with open('README.md.md', encoding="utf-8") as readme_file:
    readme = readme_file.read()

setup(
    name='food_ordering',
    description='Order food property with pub/sub',
    author='H. Aydın Taşoyan',
    author_email='atasoyan@gmail.com',
    long_description=readme,
    test_suite='food_ordering/test/'
)