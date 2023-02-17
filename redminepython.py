from redminelib import Redmine

redmine = Redmine(settings.REDMINE_URL, key=settings.REDMINE_KEY)
#redmine = Redmine('http://172.28.22.142:3000', key='43fee4944a913adbfd27c000f28d90d23514c172', verify=False)
project = redmine.project.get('testing-the-functionalities')
project.identifier
project.created_on