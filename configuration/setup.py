import setuptools

setuptools.setup(
    name="configuration",
    version=open('../version', 'r').read(),
    packages=setuptools.find_packages(),
    python_requires='>=3.6',
)