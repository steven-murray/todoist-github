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

    @property
    def _default_rules(self):
        return {
            "global": {
                "state": "open"
            },
            "created_and_owned": {
                "user": self.user.login,
                "author": self.user.login
            },
            "assigned": {
                "assignee": self.user.login
            },
            "authored_prs": {
                "author": self.user.login,
                "type": 'pr'
            }

        }

    def assigned(self, issue):
        """Check whether I'm assigned to an issue. Returns true if there are _no_ assignees as
        well"""
        if not issue.assignees:
            return True
        elif self.user.login in [a.login for a in issue.assignees]:
            return True
        else:
            return False

    def get_relevant_issues(self):

        # grules = self._cfg.get("rules", {}).get("global", self._default_global_rules)

        created_owned = self.user.get_user_issues(filter='created', state='open')
        # mentioned = self.user.get_issues(filter='mentioned', state='open')
        assigned = self.user.get_issues(filter="assigned", state='open')
        prs = self.gh.search_issues(f"state:open is:pr author:{self.user.login}")

        out = []
        for issue in created_owned:
            if issue.repository.owner.login == self.user.login:
                if issue not in out and self.assigned(issue):
                    out.append(issue)
        for issue in assigned:
            if issue not in out and self.assigned(issue):
                out.append(issue)
        for issue in prs:
            if issue not in out and self.assigned(issue):
                out.append(issue)

        return out
