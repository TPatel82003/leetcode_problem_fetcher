from setuptools import setup, find_packages

setup(
    name="leetcode_problem_fetcher",
    version="0.1.0",
    description="Python package to fetch LeetCode Problem",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    author="Your Name",
    author_email="your.email@example.com",
    url="https://github.com/TPatel82003/leetcode_problem_fetcher",
    license="MIT",
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
    install_requires=[],
    entry_points={
        "console_scripts": [
            "leetcode_problem_fetcher=leetcode_problem_fetcher.server.socket:script",  # Replace 'main' with your desired function name
        ]
    },
)
