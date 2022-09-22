'''
Implement 2 classes, the first one is the Boss and the second one is the Worker.

Worker has a property 'boss', and its value must be an instance of Boss.

You can reassign this value, but you should check whether the new value is Boss. Each Boss has a list of his own workers

 You should implement a method that allows you to add workers to a Boss.


 You're not allowed to add instances of Boss class to workers list directly via access to attribute,

 use getters and setters instead!

You can refactor the existing code.



Это основываясь на нашем классно решении, я просто ещё раз его пересмотрел, весь смысл как это сделать я запомнил.
И понял.
'''

class Boss:

    def __init__(self, name='Luck', company='Better Call Luck'):
        self.id = id
        self._name = name
        self.company = company
        self._workers = []

    @property
    def name(self):
        return self._name

    @property
    def workers(self):
        return self._workers

    @workers.setter
    def workers(self, worker):
        self._workers.append(worker)

    def del_worker(self, worker):
        self._workers.remove(worker)

    def __repr__(self):
        return self.name


class Worker:

    def __init__(self, boss, name='Jessie'):
        self.id = id
        self.name = name.title()
        self.company = boss.company
        self._boss = boss
        boss.workers = self

    @property
    def boss(self):
        return self._boss

    @boss.setter
    def boss(self, value):
        if isinstance(value, Boss):
            self._boss.del_worker(self)
            self._boss = value
            self._boss.workers = self

    def __repr__(self):
        return self.name

if __name__ == "__main__":
    b = Boss()
    boss2 = Boss(2, "Vasya")
    w = Worker(b)
    w2 = Worker(b, name='Duck')
    w2.boss = boss2