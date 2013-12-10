# Tutorial to migrate from Bitbucket to Github

----
## Install mercurial and hg-git
> 
    sudo apt-get install mercurial 
    sudo apt-get install mercurial-git

Note: The version of mercurial should be >= 2.8. 
If the default version of mercurial in apt-get is < 2.8. You can install using pip
sudo pip install mercurial --upgrade
You need to create a repo on Github.com

----
## Clone your bitbucket repo
>
    hg clone https://hbhzwj@bitbucket.org/hbhzwj/sadit hg-repo

----
## Convert hg repo to git repo

Hg-Git can also be used to convert a Mercurial repository to Git. You can use a local repository or a remote repository accessed via SSH, HTTP or HTTPS. Use the following commands to convert the repository
> 
    $ mkdir git-repo; cd git-repo; git init; cd ..
    $ cd  hg-repo
    $ hg bookmarks hg
    $ hg push ../git-repo

The hg bookmark is necessary to prevent problems as otherwise hg-git pushes to the currently checked out branch confusing Git. This will create a branch named hg in the Git repository. To get the changes in master use the following command (only necessary in the first run, later just use git merge or rebase).
> 
    $ cd git-repo
    $ git checkout -b master hg

----
## Push the Git repo to Github Server
>
    cd git-repo; 
    git remote add origin <github-url>; 
    git push -u origin master; 
    cd ..;


I also write a script to do this automatically. 

