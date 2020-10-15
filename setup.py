from setuptools import setup, find_packages


setup(
    name='pdfmerge',
    packages=find_packages(),
    entry_points=dict(
        console_scripts=['pdfmerge=pdfmerge.pdfmerge:main']
    )
)
