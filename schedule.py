import copy

def make_people_counts(input_file):
    file = open(input_file, 'r')
    people = file.read().split()
    people_unique = {}
    for x in people:
        if x.lower in people_unique:
            people_unique[x.lower()] += 1
        else:
            people_unique[x.lower()] = 1
    output = open('people_count.txt', 'w')
    for k, v in people_unique.items():
        output.write(str(k) + " " + str(v) + "\n")


class Schedule:
    def __init__(self):
        self.days = ['mon', 'tue', 'wed', 'thu', 'fri', 'sun']
        self.jobs = ['lsu', 'lcu', 'dsu', 'dcu']
        full = {}
        for d in self.days:
            full[d] = {}
            for j in self.jobs:
                full[d][j] = []
        full['sun']['lsu'] = ['NONE']
        self.chart_possible = full.copy()
        self.chart_commit = copy.deepcopy(full)

    def add_to_chart(self, day, job, name):
        self.chart_possible[day][job].append(name)

    def populate_chart(self, plist):
        for k, v in plist.items():
            if not v.avail:
                print("warning no response from:", k)
            for j in range(0, len(v.avail), 2):
                self.add_to_chart(v.avail[j], v.avail[j + 1], k)

    def print_chart(self):
        for x in self.days:
            print(x)
            for j in self.jobs:
                print(j, end='\t')
                print(self.chart_possible[x][j])

    def remove(self, name):
        for k, v in self.chart_possible.items():
            for k2, v2 in v.items():
                if name in v2:
                    v2.remove(name)
        print(self.chart_commit)
    def check_not_empty(self):
        for k, v in self.chart_possible.items():
            for k2, v2 in v.items():
                if not v2:
                    return False
        else:
            return True

    def set_job(self, name, day, job):
        self.chart_commit[day][job] = name
        self.remove(name)
        return copy.deepcopy(self)

class person:
    def __init__(self, name, times):
        self.name = name
        self.times = times
        self.avail = []

    def set_availabilities(self, avail):
        self.avail = avail


def clean_lines(plines):
    c_lines = []
    for x in plines:
        no_comma = x.replace(',', "")
        c_lines.append(no_comma.split())
    return c_lines


def make_people():
    people_count = open('people_count.txt', 'r')
    read_in = people_count.read().split()
    p_list = {}
    for x in range(0, len(read_in), 2):
        p_list[read_in[x].lower()] = person(read_in[x], read_in[x + 1])
    return p_list

file = open('responses', 'r')
lines = [x.lower() for x in file.read().split('\n')]
clean_lines = clean_lines(lines)
people_list = make_people()
dishes = Schedule()
for x in clean_lines:
    if x[0] in people_list:
        people_list[x[0]].set_availabilities(x[2:])
    elif x[1] in people_list:
        people_list[x[1]].set_availabilities(x[2:])
    else:
        print("warning unmatchable: ", x)
dishes.populate_chart(people_list)
