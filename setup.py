import setuptools

setuptools.setup(
    name="pdfmerge",
    version="0.0.1",
    author="Mark Todisco",
    description="CLI tool for merging PDF documents",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    pakage_dir={"": "src"},
    packages=setuptools.find_packages(where="src"),
    entry_points={
        "console_scripts": [
            "pdfmerge=pdfmerge.pdfmerge:main",
        ],
    },
)
