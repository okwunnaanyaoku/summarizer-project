import setuptools
with open("README.md", "r", encoding="utf-8") as f:
    long_description = f.read()

__version__ = "0.0.0"

REPO_NAME = "summarizer-project"
AUTHOR_USER_NAME = "okwunnaanyaoku"
SRC_REPO = "testSummarizer"
AUTHOR_EMAIL = "okwunnaanyaoku@gmail.com"

setuptools.setup(
    name=REPO_NAME,
    version=__version__,
    author=AUTHOR_USER_NAME,
    author_email=AUTHOR_EMAIL,
    description="NLP application",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/" + AUTHOR_USER_NAME + "/" + SRC_REPO,
    project_urls={
        "Bug Tracker": "https://github.com/" + AUTHOR_USER_NAME + "/" + SRC_REPO + "/issues",
    },
    package_dir={"":"src"},
    packages=setuptools.find_packages(where="src")
)