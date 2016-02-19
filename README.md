# auto-deploy
This script for automation deployment

### For Python Project

Preparing install in Ubuntu Server

    $ sudo apt-get install python-dev python-virtualenv nginx

Run in your local

    $ git clone https://github.com/drayanaindra/auto-deploy.git
    $ cd auto-deploy/template/temp-falcon
    $ sudo pip install fabric
    $ fab deploy_all