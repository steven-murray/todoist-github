import todoist

from . import config as _cfg


class TodoistUser(todoist.TodoistAPI):
    def __init__(self, *args, **kwargs):
        self._cfg = _cfg.load()['todoist']
        super().__init__(self._cfg['token'])
        self.sync()

    def get_items_with_label(self, label):
        return self.items.all(filt=lambda item: label in item.data['labels'])

    def get_project_ids(self):
        return {p.data['name']: p.data['id'] for p in self.projects.all()}

    def get_rev_project_ids(self):
        pids = self.get_project_ids()
        return {v:k for k,v in pids.items()}
