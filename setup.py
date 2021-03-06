import genepattern.utils
from distutils.core import setup

setup(
    name='genepattern-utils',
    packages=['genepattern.utils'],
    version=genepattern.utils.__version__,
    description='Library for programmatically interacting with GenePattern from Python.',
    authors='Thorin Tabor, Edwin Juarez',
    author_email='tmtabor@cloud.ucsd.edu',
    url='https://github.com/genepattern/genepattern-utils',
    download_url='https://github.com/genepattern/genepattern-utils/archive/' + genepattern.utils.__version__ + '.tar.gz',
    keywords=['genepattern', 'genomics', 'bioinformatics'],
    license='BSD',
    install_requires = [  # I should probably add versions to these 2018-06-01
                       'genepattern-python',
                       'numpy',
                       'scipy',
                       'pandas',
                       'matplotlib',
                       'statsmodels',
                       'seaborn',
                       'validators',
                       'IPython',
                       'humanfriendly',
                       'scikit-learn',
                   ],
)
