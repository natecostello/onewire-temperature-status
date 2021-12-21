import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="ow_temperature-NSC",  # Replace with your own username
    version="0.0.1",
    author="Nate Costello",
    author_email="natecostello@gmail.com",
    description="A package that collects information from a Dallas one-wire temperature sensor",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/natecostello/onewire_temperature_status",
    project_urls={
        "Bug Tracker": "https://github.com/natecostello/onewire_temperature_status/issues",
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    py_modules=['ow_temperature'],
    python_requires=">=3.6",
    install_requires=[
        "instrument_logger-NSC @ git+https://github.com/natecostello/instrument_logger.git"]
)
# In the install_requires values, the name @ address, name must match the name listed in the dependancy module


# For specifying the requirements
# Using this: https://stackoverflow.com/questions/32688688/how-to-write-setup-py-to-include-a-git-repository-as-a-dependency/54794506#54794506
