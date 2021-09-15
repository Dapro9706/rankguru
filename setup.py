from distutils.core import setup
setup(
  name = 'rankguru',
  packages = ['rankguru'],
  version = '0.12',
  license='MIT',
  description = 'This is a basic Wrapper for Test answer retrieval from https://rankguru.com',   # Give a short description about your library
  author = 'Swaminath Shiju',                   # Type in your name
  author_email = 'swaminathshhiju@gmail.com',      # Type in your E-Mail
  url = 'https://github.com/SwaminathShiju/rankguru',   # Provide either the link to your github or to your website
  download_url = 'https://github.com/user/reponame/archive/v_01.tar.gz',    # I explain this later on
  keywords = ['Basic'],   # Keywords that define your package best
  install_requires=[            # I get to this in a second
          'requests',
      ],
  classifiers=[
    'Development Status :: 3 - Alpha',      # Chose either "3 - Alpha", "4 - Beta" or "5 - Production/Stable" as the current state of your package
    'Intended Audience :: Developers',      # Define that your audience are developers
    'Topic :: Software Development :: Build Tools',
    'License :: OSI Approved :: MIT License',   # Again, pick a license
    'Programming Language :: Python :: 3.8',      #Specify which pyhton versions that you want to support
    'Programming Language :: Python :: 3.7'
  ],
)