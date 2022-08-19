# Copyright (C) 2021-2022 Thanh Nguyen


DESCRIPTION = "Derivatives Pricing in Python"


with open("README.md", encoding='UTF-8') as fh:
    LONG_DESCRIPTION = fh.read()

DISTNAME = 'dpf'
MAINTAINER = 'Thanh Nguyen'
MAINTAINER_EMAIL = 'thanhuwe8@gmail.com'
URL = 'https://github.com/thanhuwe8/DerivativesPricing'
LICENSE = 'MIT'
KEYWORDS = 'finance, derivatives, quant, pricing, equity'
DOWNLOAD_URL = 'https://github.com/thanhuwe8/DerivativesPricing.git'
VERSION = '1.0'
PYTHON_REQUIRES = ">=3.7"

INSTALL_REQUIRES = [
    'numpy>=1.17.0',
    'pandas>=1.0.0',
    'yahoo_fin>=0.8.9.1'
]

PACKAGES = [
    'dpf'
]

CLASSIFIERS = [
    'Intended Audience :: Financial and Insurance Industry',
    'Intended Audience :: Science/Research',
    'Programming Language :: Python :: 3.7',
    'Programming Language :: Python :: 3.8',
    'Programming Language :: Python :: 3.9',
    'License :: OSI Approved :: BSD License',
    'Topic :: Office/Business :: Finance',
    'Topic :: Scientific/Engineering :: Mathematics',
    'Operating System :: Microsoft',
    'Operating System :: Unix',
    'Operating System :: MacOS'
]


if __name__ == "__main__":

    from setuptools import setup

    import sys
    if sys.version_info[:2] < (3, int(PYTHON_REQUIRES[-1])):
        raise RuntimeError("dpf requires python " + PYTHON_REQUIRES)

    setup(
        name=DISTNAME,
        author=MAINTAINER,
        author_email=MAINTAINER_EMAIL,
        maintainer=MAINTAINER,
        maintainer_email=MAINTAINER_EMAIL,
        description=DESCRIPTION,
        long_description=LONG_DESCRIPTION,
        long_description_content_type='text/markdown; charset=UTF-8; variant=GFM',
        license=LICENSE,
        keywords=KEYWORDS,
        url=URL,
        version=VERSION,
        download_url=DOWNLOAD_URL,
        python_requires=PYTHON_REQUIRES,
        install_requires=INSTALL_REQUIRES,
        packages=PACKAGES,
        classifiers=CLASSIFIERS,
        project_urls={"Documentation": "",
                    "Issues": "https://github.com/thanhuwe8/DerivativesPricing/issues",
                    },
)