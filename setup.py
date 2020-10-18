from setuptools import setup, find_packages

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name="ptithiwa",
    version="0.0.1",
    description="ptithiwa - WhatsApp app bot: Automate WhatsApp app with appium in python.",
    py_modules=[],
    packages=find_packages(),
    package_dir={"ptithiwa": "ptithiwa"},
    long_description=long_description,
    long_description_content_type="text/markdown",
    classifiers=[
        "Programming Language :: Python :: 3.8",
        "Operating System :: OS Independent",
    ],
    license="MIT License",
    entry_points={
        'console_scripts': [
            'ptithiwa = ptithiwa.__main__:main',
        ],
    },
    url="https://github.com/Maskgirl/tithiwa",
    author="SuLagna Mukherjee",
    author_email="tithimukherjee12@gmail.com",
    install_requires=[
        "Appium-Python-Client",
    ],
    extras_require={
        "dev": [
            "",
            "",
            "",
        ],
    },
)
