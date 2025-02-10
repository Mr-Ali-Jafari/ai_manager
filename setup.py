from setuptools import setup, find_packages

setup(
    name="py-ai-manager",
    version="0.0.4",
    packages=find_packages(),
    install_requires=["requests"],
    author="Ali Jafari",
    author_email="riptt91@gmail.com",
    description="A Python library to interact with AI models via API",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/Mr-Ali-Jafari/ai_manager",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
)

