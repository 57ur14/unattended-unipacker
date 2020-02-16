import unipacker
from setuptools import setup, find_packages

__VERSION__ = unipacker.__VERSION__
__NAME__ = 'unattended-unipacker'

with open('README.md') as readme_file:
    README = readme_file.read()

setup(
    name=__NAME__,
    version=__VERSION__,
    python_requires='>=3.6',
    author='Un{i}packer Team & Sturla Bae',
    author_email='ntnu-rgb@outlook.com',
    description='Fork of unipacker that allows unattended unpacking',
    long_description=README,
    long_description_content_type='text/markdown',
    license='GPL-2.0',
    url='https://github.com/ntnu-rgb/unattended-unipacker',
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        'yara-python',
        'pefile',
        'cmd2==0.9.12',
        'unicorn-unipacker==1.0.3b7',
        'capstone',
        'colorama',
        'pyreadline; platform_system == "Windows"',
        'gnureadline; platform_system == "Darwin"',
    ],
    test_suite='Tests',
    entry_points={
        'console_scripts': [
            'unipacker=unipacker.shell:main'
        ]
    },
    package_data={
        'unipacker': ['*', 'DLLs/*']
    }
)
