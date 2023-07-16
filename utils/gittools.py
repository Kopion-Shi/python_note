# -*- coding: utf-8 -*-
# @Time    : 2023/3/11 13:25
# @Author  : 石鑫磊
# @Site    : 
# @File    : gittools.py
# @Software: PyCharm 
# @Comment :
import os

from git.repo import Repo
from git.repo.fun import is_git_dir


class GitRepository():
    """
    git_tools
    """

    def __init__(self, local_path, repo_url, branch="master"):
        self.local_path = local_path
        self.repo_url = repo_url
        self.branch = branch
        self.repo = None
        self.initial(repo_url, branch)

    def initial(self, repo_url, branch):
        """
        初始化git
        :param repo_url:
        :param branch:
        :return:
        """
        if not os.path.exists(self.local_path):
            os.makedirs(self.local_path)

        git_local_path = os.path.join(self.local_path, '.git')
        if not is_git_dir(git_local_path):
            # 本地没有代码仓，重新拉去
            self.repo = Repo.clone_from(repo_url, to_path=self.local_path, branch=branch)
        else:
            self.repo = Repo(self.local_path)

    def pull(self):
        """
        从主线拉去代码
        :return:
        """
        self.repo.pull()

    def branches(self):

        """获取所有分支
        """
        branches = self.repo.remote().refs
        return [item.remote_head for item in branches if item.remote_head not in ['HEAD', ]]

    def commits(self):
        """
        获取所有提交记录
        :return:
        """
        commit_log = self.repo.git.log('--pretty={"commit":"%h","author":"%an","sumary":"%s","date":"%cd"}',
                                       max_coun=50,
                                       date='format:%Y-%m-%d %H:%M')
        log_list = commit_log.split("\n")
        return [eval(item) for item in log_list]

    def tags(self):
        """
        获取所有tags
        :return:
        """
        return [tag.name for tag in self.repo.tags()]

    def change_to_branch(self,branch):
        """
        切换分支
        :return:
        """
        self.repo.git.checkout(branch)

    def change_to_commit(self, branch, commit):
        """
        切换commit
        :param brach:
        :param commit:
        :return:
        """
        self.change_to_branch(branch=branch)
        self.repo.git.reset('--hand', commit)

    def change_to_tags(self,tag):
        """
        切换tag
        :return:
        """
        self.repo.git.checkout(tag)


if __name__=="__main__":
    local_path=os.path.join('./../temp','gittools_test')
    repo=GitRepository(local_path=local_path,repo_url='https://github.com/Kopion-Shi/python_note')
    branch_list=repo.branches()
    print(branch_list)
