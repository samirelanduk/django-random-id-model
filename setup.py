from setuptools import setup

with open("README.md") as f:
    long_description = f.read()

setup(
    name="django_random_id_model",
    version="0.1.0",
    description="A django model abstract class for creating random int primary keys.",
    long_description=long_description,
    long_description_content_type="text/x-md",
    url="https://github.com/samirelanduk/django-random-id-model",
    author="Sam Ireland",
    author_email="mail@samireland.com",
    license="MIT",
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Topic :: Scientific/Engineering :: Chemistry",
        "Framework :: Django",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
    ],
    keywords="django orm primary-key",
    py_modules=["django_random_id_model"],
    python_requires="!=2.*, !=3.0.*, !=3.1.*, !=3.2.*, !=3.3.*, !=3.4.*, !=3.5.*",
)
