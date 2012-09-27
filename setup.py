from setuptools import find_packages
from setuptools import setup


setup(
    name='trust.policy',
    version='0.1',
    description="Trust Policy",
    long_description=open("README.rst").read(),
    # Get more strings from
    # http://pypi.python.org/pypi?:action=list_classifiers
    classifiers=[
        "Framework :: Plone",
        "Framework :: Plone :: 4.2",
        "Programming Language :: Python",
        "Programming Language :: Python :: 2.7"],
    keywords='',
    author='ABITA',
    author_email='taito.horiuchi@abita.fi',
    url='https://abita.fi/',
    license='Non-free',
    packages=find_packages(exclude=['ez_setup']),
    namespace_packages=['trust'],
    include_package_data=True,
    zip_safe=False,
    install_requires=[
        'hexagonit.testing',
        'plone.browserlayer',
        'setuptools',
        'trust.template'],
    entry_points="""
    # -*- Entry points: -*-

    [z3c.autoinclude.plugin]
    target = plone
    """)
