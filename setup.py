from setuptools import find_packages,setup

setup(
    name='genai',
    version='0.0.1',
    author='manasa vadlamani',
    author_email='vmanasa2003@gmail.com',
    install_requires=["openai","langchain","streamlit","python-dotenv","PyPDF2"],
    packages=find_packages()
)