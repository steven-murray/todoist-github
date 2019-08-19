import github

from . import config as _cfg


class GithubUser:
    def __init__(self):
        self._cfg = _cfg.load()['github']

        if "token" in self._cfg:
            self.gh = github.Github(self._cfg['token'])
        else:
            self.gh = github.Github(self._cfg['login'], self._cfg['password'])

        self.user = self.gh.get_user()

    def get_relevant_issues(self):
        created_owned = self.user.get_user_issues(filter='created', state='open')
        mentioned = self.user.get_issues(filter='mentioned', state='open')
        assigned = self.user.get_issues(filter="assigned", state='open')
        prs = self.gh.search_issues(f"state:open is:pr author:{self.user.login}")

        out = []
        for issue in created_owned:
            if issue not in out:
                out.append(issue)
        for issue in mentioned:
            if issue not in out:
                out.append(issue)
        for issue in assigned:
            if issue not in out:
                out.append(issue)
        for issue in prs:
            if issue not in out:
                out.append(issue)

        return out
