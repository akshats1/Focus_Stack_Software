import setuptools
import src

setuptools.setup(
    name="focus_stack_mimdlab",
    #version="0.0.1",
    author="Akshat",
    author_email="akshats063@gmail.com",
    version=src.__version__,
    packages=setuptools.find_packages(),
    #entry_points={"console_scripts": ["chimpstackr=src.run:main"]},
)
