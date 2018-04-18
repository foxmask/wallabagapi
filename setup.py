from setuptools import setup, find_packages
from wallabag_api import __version__ as version

desc = 'Wallabag API to add every pages you want to your Wallabag account'
long_desc = 'Wallabag is a "read it later" service, and that Wallabag API allow you to save web pages ' \
            'to your own account'
install_requires = [
    'aiohttp',
]

setup(
    name='wallabag_api',
    version=version,
    description=desc,
    long_description=long_desc,
    author='FoxMaSk',
    author_email='foxmask@trigger-happy.eu',
    url='https://github.com/push-things/wallabag_api',
    download_url="https://github.com/push-things/wallabag_api/archive/wallabag_api-" + version + ".zip",
    packages=find_packages(),
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3.6',
        'Topic :: Internet',
        'Topic :: Communications',
    ],
    install_requires=install_requires,
    include_package_data=True,
)
