from setuptools import setup, find_packages

setup(
    name='math_quiz',
    version='0.1',
    packages=find_packages(),
    entry_points={
        'console_scripts': [
            'math_quiz=math_quiz.math_quiz:math_quiz',
        ],
    },
    install_requires=[],
    author='Ayush Balapurkar',
    author_email='ayush.balapurkar448@gmail.com',
    description='Math quiz game',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/CryptoAyush/dsss_homework_2.git',
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)
