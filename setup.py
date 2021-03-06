from distutils.core import setup
from setuptools import find_packages

setup(
    name="bacula_scripts",
    version="0.6.2",
    author="eayin2",
    author_email="eayin2@gmail.com",
    packages=find_packages(),
    url="https://github.com/eayin2/bacula_scripts",
    description="Bunch of bacula scripts. Includes also scripts to realize offsite backup solution.",
    install_requires=["gymail", "helputils", "psycopg2"],
    entry_points={
        'console_scripts': [
            'bacula_del_jobs = bacula_scripts.bacula_del_jobs:main',
            'bacula_db_backup = bacula_scripts.bacula_db_backup:main',
            'bacula_del_media_orphans = bacula_scripts.bacula_del_media_orphans:main',
            'bacula_del_failed_jobs = bacula_scripts.bacula_del_failed_jobs:main',
            'bacula_del_catalog_jobids = bacula_scripts.bacula_del_catalog_jobids:main',
            'bacula_del_purged_vols = bacula_scripts.bacula_del_purged_vols:main',
            'bacula_offsite_backup_age_watch = bacula_scripts.bacula_offsite_backup_age_watch:main',
            'bacula_offsite_clean_and_umount = bacula_scripts.bacula_offsite_clean_and_umount:main',
            'bacula_find_backups_bls = bacula_scripts.bacula_find_backups_bls:main',
            'bacula_encfs_backup = bacula_scripts.bacula_encfs_backup:main',
            'bacula_offsite_udev = bacula_scripts.bacula_offsite_udev:main',
            'bacula_prune_all = bacula_scripts.bacula_prune_all:main',
            'bacula_prune_scattered = bacula_scripts.bacula_prune_scattered:main',
            'disk_full_notifier = bacula_scripts.disk_full_notifier:main',
        ],
    },
)
