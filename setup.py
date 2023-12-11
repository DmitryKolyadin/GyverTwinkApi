from setuptools import setup, find_packages


def readme():
    with open("README.md", "r") as f:
        return f.read()


setup(
    name="GyverTwinkApi",
    version="1.0.1",
    author="DevDK",
    author_email="Dmitry@kolyadin.ru",
    description="Модуль для управления гирляндой GyverTwink через WiFi",
    long_description=readme(),
    long_description_content_type="text/markdown",
    url="https://github.com/DeveloperDmitryKolyadin/GyverTwinkApi",
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
    ],
    project_urls={"Github": "https://github.com/DeveloperDmitryKolyadin/GyverTwinkApi"},
)
