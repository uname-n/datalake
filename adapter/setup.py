import setuptools

setuptools.setup(
    name="adapter",
    version=open('../version', 'r').read(),
    packages=setuptools.find_packages(),
    python_requires='>=3.6',
    install_requires=open('../requirements.txt', 'r').readlines(),
)