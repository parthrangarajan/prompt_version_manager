from setuptools import setup, find_packages

setup(
    name='prompt_version_manager',
    version='0.1.0',
    description='A package to track and save prompt versions automatically',
    author='Parth Rangarajan',
    author_email='rangarajanparth@gmail.com',
    url='https://github.com/parthrangarajan/prompt_version_manager',
    py_modules=['prompt_version_manager'],
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)
