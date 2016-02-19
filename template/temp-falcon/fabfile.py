# contribute : M Asep Indrayana
# github : https://github.com/drayanaindra
# twitter : @drayanaindra

from fabric.api import *
from fabric.colors import green
from fabric.contrib.files import exists

USER = ""   # set username of server
SITE_NAME = 'example-project'   # can configurable
ENV_NAME = 'env-project'
GIT_URL = 'https://github.com/drayanaindra/example-project.git' # change with your git repository

PATH_DIR_PROJECT = '/home/{u}/www/{s}'.format(u=USER, s=SITE_NAME)
NGINX_NAME = 'nginx-{}.conf'.format(SITE_NAME)
UPSTART_NAME = '{}.conf'.format(SITE_NAME)


env.hosts = [""]  # host server (domain or IP)
env.user = USER  # name of username server
env.password = ""  # password server


def check_dirs():
    """
    Checking directory
    """

    dirs = [
        "/etc/init/{}".format(UPSTART_NAME),
        "/etc/nginx/sites-available/{}".format(NGINX_NAME),
        "/etc/nginx/sites-enabled/{}".format(NGINX_NAME)
    ]

    print "Checking dirs.........\n"

    for i in dirs:
        if exists(i):
            messages = "'{}' already exist".format(i)
            abort(messages)

    print green("All file are available a")


def create_dir_env_www():
    """
    Create directory www and evn
    """
    if not exists('/home/{}/env'.format(USER)):
        run('mkdir /home/{}/env'.format(USER))

    if not exists('/home/{}/www'.format(USER)):
        run('mkdir /home/{}/www'.format(USER))


def create_env():
    """
    Create virtualenv
    """
    if not exists('/home/{u}/env/{e}'.format(u=USER, e=ENV_NAME)):
        run('virtualenv /home/{u}/env/{e}'.format(u=USER, e=ENV_NAME))


def clone_project():
    """
    Clone project
    """
    with cd('/home/{}/www'.format(USER)):
        if not exists('/home/{u}/www/{s}'.format(u=USER, s=SITE_NAME)):
            run('git clone {}'.format(GIT_URL))


def install_requirements():
    """
    Install requirements
    """
    with cd('/home/{}'.format(USER)):
        with prefix('source env/{}/bin/activate'.format(ENV_NAME)):
            run('pip install -r {}/requirements.txt'.format(PATH_DIR_PROJECT))


def symlink_nginx():
    """
    Symlink nginx conf
    """
    with cd(PATH_DIR_PROJECT):
        with cd('deploy'):
            sudo('ln -s {d}/deploy/{ng} /etc/nginx/sites-enabled/{ng}'.format(d=PATH_DIR_PROJECT, ng=NGINX_NAME))


def symlink_upstart():
    """
    Symlink upstart conf
    """
    with cd(PATH_DIR_PROJECT):
        with cd('deploy'):
            sudo('cp {d}/deploy/{up} /etc/init/'.format(d=PATH_DIR_PROJECT, up=UPSTART_NAME))


def make_executable():
    """
    Make executable
    """
    with cd(PATH_DIR_PROJECT):
        with cd('deploy'):
            run('chmod +x start.sh')


def start_nginx():
    """
    Start nginx server
    """
    sudo('service nginx start')


def restart_nginx():
    """
    Restart nginx server
    """
    sudo('service nginx restart')


def reload_nginx():
    """
    Reload nginx server
    """
    sudo('service nginx reload')


def start_app():
    """
    Start the app
    """
    sudo('start example-project')


def restart_app():
    """
    Start the app
    """
    sudo('restart example-project')


def stop_app():
    """
    Start the app
    """
    sudo('stop example-project')


def pull_project():
    """
    Pull git repository
    """
    with cd(PATH_DIR_PROJECT):
        run('git pull origin master')


def deploy_all():
    """
    Run when first time deploy apps
    """
    check_dirs()
    create_dir_env_www()
    create_env()
    clone_project()
    install_requirements()
    symlink_nginx()
    symlink_upstart()
    make_executable()

    # you can change to the another function exp.
    start_nginx()
    start_app()


def update_app():
    """
    Run when update apps
    """
    pull_project()
    restart_app()
