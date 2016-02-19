# auto-deploy
This script for automation deployment

### For Python Project

Preparing install in Ubuntu Server

    $ sudo apt-get install python-dev python-virtualenv nginx

Run in your local, make sure all file in temp-falcon has been copied to your project with directory name `deploy`

    $ git clone https://github.com/drayanaindra/auto-deploy.git
    $ cd auto-deploy/template/temp-falcon
    $ sudo pip install fabric
    $ fab deploy_all