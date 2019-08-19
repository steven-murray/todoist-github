from .github import GithubUser
from .todoist import TodoistUser
import logging
import os
import glob
logger = logging.getLogger(__name__)


class Integrator:
    def __init__(self, gh=None, td=None, verbose=False):
        self.gh = gh or GithubUser()
        self.td = td or TodoistUser()
        self.verbose = verbose
        self._ncomm = 0
        self._ncomm_tot = 0

    def commit(self):
        try:
            self.td.commit(raise_on_error=True)
        except Exception:
            print("Clearing cache because there was an error in committing")
            fls = glob.glob(os.path.expanduser("~/.todoist-sync/*"))
            for fl in fls:
                os.remove(fl)
            raise

    def check(self):
        """Keeps track of the number of commands that have taken place"""
        self._ncomm += 1
        self._ncomm_tot += 1
        if self._ncomm == 100:
            self.commit()
            self._ncomm = 0

    def add_issues_as_tasks(self):
        """
        Add any *new* issues as tasks to todoist, and remove any completed.
        """
        issues = self.gh.get_relevant_issues()
        issue_names = [f"[gh] {issue.title}: {issue.html_url}" for issue in issues]

        items = self.td.items.all(filt=lambda x: x.data['content'].startswith("[gh] "))

        contents = list(set([item.data['content'] for item in items]))

        # Add issues
        for issue in issues:
            issue_name = f'[gh] {issue.title}: {issue.html_url}'

            if issue_name not in contents:
                print(f"Added new issue as task in {issue.repository.name}: {issue.title}")
                # Create a task!
                project_id = self.td.get_project_ids().get(issue.repository.name, None)
                if not project_id:
                    # Create a new project!
                    project = self.td.projects.add(issue.repository.name)
                    project_id = project.data['id']
                    self.check()

                self.td.items.add(
                    f"[gh] {issue.title}: {issue.html_url}",
                    priority=4, project_id=project_id
                )
                self.check()

            elif self.verbose:
                print(f"{issue_name} already exists")

        # Prune tasks that are no longer issues
        for task in items:
            if task.data['content'] not in issue_names:
                print(
                    "Remove task %s from %s", task.data['content'],
                    self.td.get_rev_project_ids()[task.data['project_id']],
                )
                self.td.items.close(task.data['id'])
                self.check()

            elif self.verbose:
                print(f"{task.data['content']} still exists")

    def test(self, label=True, new_project=True):
        for i in range(2):
            if new_project:
                proj = self.td.projects.add(f"TEMP_NEW_PROJECT {i}")
                proj_id = proj.data['id']
            else:
                proj_id = self.td.get_project_ids("Inbox")

            self.td.items.add(f"TESTING FROM TODOIST-GITHUB! {i}" + (" @label" if label else ""),
                              project_id=proj_id)

        packet = self.td.commit(raise_on_error=True)
        print(packet)

    def sync_all(self):
        self.add_issues_as_tasks()
        packet = self.td.commit(raise_on_error=True)
        print(packet)
