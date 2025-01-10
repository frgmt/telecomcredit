from setuptools import find_packages, setup

setup(
    name="telecomcredit",
    version="1.0.1",
    description="Python bindings for the telecomcredit API",
    author="frgmt",
    url="https://github.com/frgmt/telecomcredit",
    license="MIT",
    keywords="telecomcredit api",
    packages=find_packages(exclude=["tests", "tests.*"]),
    zip_safe=False,
    install_requires=[
        'typing_extensions >= 4.5.0; python_version >= "3.7"',
        'requests >= 2.20; python_version >= "3.0"',
    ],
    python_requires=">=3.9",
    project_urls={
        "Bug Tracker": "https://github.com/frgmt/telecomcredit/issues",
        "Changes": "https://github.com/frgmt/telecomcredit/blob/master/CHANGELOG.md",
        "Source Code": "https://github.com/frgmt/telecomcredit",
    },
    setup_requires=["wheel"],
)
