from setuptools import setup


setup(
    name="Flask-PBKDF2",
    version="0.1",
    url="",
    license="BSD",
    author="Shrijit Singh",
    author_email="shrijitsingh99@gmail.com",
    description="PBKDF2 hashing for flask",
    long_description=__doc__,
    py_modules=["flask_pbkdf2"],
    zip_safe=False,
    include_package_data=True,
    platforms="any",
    python_requires='>=3.6',
    install_requires=[
        "Flask", "pbkdf2"
    ],
    classifiers=[
        "Environment :: Web Environment",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: BSD License",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Topic :: Internet :: WWW/HTTP :: Dynamic Content",
        "Topic :: Software Development :: Libraries :: Python Modules"
    ],
    test_suite='test_pbkdf2'
)