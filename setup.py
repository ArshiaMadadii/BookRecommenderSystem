from setuptools import setup, find_packages

# Read the full project description from README.md
with open("README.md", "r", encoding="utf-8") as f:
    long_description = f.read()

# Read the list of required packages from requirements.txt
with open("requirements.txt", "r") as f:
    LIST_OF_REQUIREMENTS = f.read().splitlines()

# Define the setup configuration
setup(
    name="BookRecommenderSystem",                    # Name of the package
    version="0.0.1",                                 # Initial version
    author="Arshia Madadi",                          # Author's name
    author_email="ars.madadi@gmail.com",             # Author's email
    description="A book recommendation system using machine learning",  # Short description
    long_description=long_description,               # Detailed description from README
    long_description_content_type="text/markdown",   # Type of long_description (markdown format)
    url="https://github.com/ArshiaMadadii/BookRecommenderSystem-",      # Project URL
    packages=find_packages(),                        # Automatically find all packages and subpackages
    license="MIT",                                   # License type
    python_requires=">=3.7",                         # Minimum required Python version
    install_requires=LIST_OF_REQUIREMENTS            # List of required dependencies from requirements.txt
)
