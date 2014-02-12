from distutils.core import setup

setup(
    name='checkm-ACE',
    version='0.5.0',
    author='Donovan Parks, Michael Imelfort, Connor Skennerton',
    author_email='donovan.parks@gmail.com',
    packages=['checkm', 'checkm.plot', 'checkm.test', 'checkm.lib'],
    scripts=['bin/checkm'],
    url='http://pypi.python.org/pypi/checkm/',
    license='GPL3',
    description='Assess the quality of putative genome bins.',
    long_description=open('README.md').read(),
    install_requires=[
        "numpy >= 1.8.0",
        "scipy >= 0.9.0",
        "matplotlib >= 1.1.0",
        "pysam >= 0.7.4",
        "dendropy >= 3.13.0"],
)