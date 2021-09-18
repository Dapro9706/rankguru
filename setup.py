from distutils.core import setup
setup(
  name = 'rankguru',
  packages = ['rankguru'],
  version = '0.5',
  license='MIT',
  description = 'This is a basic Wrapper for Test answer retrieval from https://rankguru.com',
  author = 'Swaminath Shiju',
  author_email = 'swaminathshhiju@gmail.com',
  url = 'https://github.com/SwaminathShiju/rankguru',
  download_url = 'https://github.com/SwaminathShiju/rankguru/archive/refs/tags/v0.5.tar.gz',
  keywords = ['Basic'],   # Keywords that define your package best
  install_requires=[            # I get to this in a second
          'requests',
      ],
  classifiers=[
    'Development Status :: 3 - Alpha',
    'Intended Audience :: Developers',
    'Topic :: Software Development :: Build Tools',
    'License :: OSI Approved :: MIT License',
    'Programming Language :: Python :: 3.8',
    'Programming Language :: Python :: 3.7'
  ],
)