from setuptools import setup
#from distutils.core import setup

setup(
        name="tsv",
        version="0.2",
        description="operation of tsv file with named fields, especially in bioinfomatics",
        author="Sein Tao",
        author_email="sein.tao@gmail.com",
        url = "https://github.com/sein-tao/tsv",
        license="GNU GPL v2",
        packages=['tsv'],
        package_dir={'tsv':''},
        install_requires= [],
        provides=['tsv'],
        package_data = {},
        keywords= ["tsv", "bioinfomatics",],

        
        )

