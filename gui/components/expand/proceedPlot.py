from .expandTemplate import TemplateLayout


class Layout(TemplateLayout):
    def __init__(self, parent=None, config=None):
        configItems = [
            {
                'label': '主线剧情需要推的章节数',
                'type': 'text',
                'key': 'main_story_regions'
            },
            {
                'label': '开始推主线剧情',
                'type': 'button',
                'selection': self.proceed_main_plot,
                'key': None
            },
            {
                'label': '开始推小组剧情',
                'type': 'button',
                'selection': self.proceed_group_plot,
                'key': None
            },
            {
                'label': '开始推支线剧情',
                'type': 'button',
                'selection': self.proceed_branch_plot,
                'key': None
            }
        ]

        super().__init__(parent=parent, configItems=configItems, config=config)

    def proceed_main_plot(self):
        import threading
        threading.Thread(target=self.get_thread().start_main_story).start()

    def proceed_group_plot(self):
        import threading
        threading.Thread(target=self.get_thread().start_group_story).start()

    def proceed_branch_plot(self):
        import threading
        threading.Thread(target=self.get_thread().start_branch_story).start()

    def get_thread(self, parent=None):
        if parent is None:
            parent = self.parent()
        for component in parent.children():
            if type(component).__name__ == 'HomeFragment' and self.config['name'] == component.config.get('name'):
                return component.get_main_thread()
        return self.get_thread(parent.parent())