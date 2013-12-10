#!/usr/bin/env python
from __future__ import print_function, division
import argparse
from subprocess import check_call
import subprocess

def call(*args, **kwargs):
    lstr = lambda x: ' '.join(str(a) for a in x) if isinstance(x, list) else str(x)
    cmd = ' '.join(lstr(a) for a in args) + ' ' + ' '.join(['%s=%s' % (k, v) for k, v in kwargs.iteritems()])
    print(cmd)
    # return check_call(*args, **kwargs)
    return subprocess.call(*args, **kwargs)

def b2g(bb_url, gh_url):
    hg_repo = 'hg-repo'
    git_repo = 'git-repo'
    ret = call(['hg', 'clone', bb_url, hg_repo])
    print('ret', ret)
    call(['mkdir', git_repo])
    call(['cd %s; git init; cd ..' % (git_repo)], shell=True)
    call(['cd %s; hg bookmarks hg; hg push ../%s' % (hg_repo, git_repo)],
            shell=True)
    call(['cd %s; git checkout -b master hg; cd ..' % (git_repo)], shell=True)
    # check_call('git', 'pull', gh_url)
    call(['cd %s; git remote add origin %s; git push -u origin master; cd ..;'
        % (git_repo, gh_url)], shell=True)

    # check_call(['git', 'push', '--set-upstream', gh_url])
    call(['rm', '-rf', hg_repo])
    call(['rm', '-rf', git_repo])

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='convert bitbucket repo to github')
    parser.add_argument('bb_url', type=str, help='bitbucket repo url')
    parser.add_argument('gh_url', type=str, help='github repo url')
    args = parser.parse_args()
    b2g(args.bb_url, args.gh_url)
    # print('bb_url: ', args.bb_url)
    # print('gh_url: ', args.gh_url)


