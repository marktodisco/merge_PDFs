import setuptools

setuptools.setup(
    name="pdfmerge",
    version="0.0.1",
    author="Mark Todisco",
    description="CLI tool for merging PDF documents",
    install_requires=[
        'PyPDF2'
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    packages=setuptools.find_packages(),
    entry_points={
        "console_scripts": [
            "pdfmerge=main:main",
        ],
    },
)
