from setuptools import setup

setup(name='genepattern-utils',
      version='0.1.0',
      description="A collection of Python utility functions for use with GenePattern.",
      url='https://github.com/genepattern/genepattern-utils',
      author='Thorin Tabor and Edwin F. Juarez',
      author_email='ejuarez@ucsd.edu',
      license='MIT',
      packages=['utils'],
      zip_safe=False,
      install_requires=[ #I should probably add versions to these 2018-06-01
            'numpy',
            'scipy',
            'pandas',
            'matplotlib',
            'statsmodels',
            'seaborn',
            'validators',
            'IPython',
            'humanfriendly'
            ],
      )
