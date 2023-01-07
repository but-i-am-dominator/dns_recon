"""
DNS Recon setup.py
"""

from setuptools import setup

setup(
    name='dns_recon',
    version='0.0.1',
    description='DNS reconnaissance tool.',
    packages=["dns_recon"],
    package_dir={'dns_recon': 'dns_recon'},
    classifiers=[
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Topic :: System :: Networking :: Monitoring",
        "Natural Language :: English"
    ],
    install_requires=[
        "dnspython ~= 2.0.0",
        "whois ~= 0.8.0"
    ],
    extras_require = {
        "dev": [
            "pylint>=2.15.0",
        ],
    },
    url="https://github.com/but-i-am-dominator/dns_recon",
    author="Dave Quartarolo",
    author_email="david.quartarolo@gmail.com",
)
