import heapq

PREREQUISITES = {
    'cs112': ['cs101', 'cs102'],
    'cs132': ['cs112', 'cs105'],
    'cs243': ['cs101', 'cs112'],
    'cs229': ['cs101'],
    'cs224n': ['cs107', 'cs101', 'cs229'],
    'cs230': ['cs229', 'cs101'],
    'cs229t': ['cs101', 'cs107'],
    'cs224u': ['cs224n'],
    'cs300': ['cs230']
}

NLP_COURSES = ['cs300', 'cs229', 'cs230', 'cs224n', 'cs229t', 'cs224u']

# IMPLMENT THIS FUNCTION.
def cal_my_course_schedule(courses, prerequisites):
    courses_needed = []
    courses_seen = dict()
    for course in courses:
        depth_first_search(course, prerequisites, courses_needed, courses_seen)

    schedule = [heapq.heappop(courses_needed)[1] for _ in range(len(courses_needed))]
    return schedule

def depth_first_search(course, prerequisites, courses_needed, courses_seen):
    if course in courses_seen:
        return courses_seen[course]

    if course in prerequisites:
        prereq_courses = prerequisites[course]
        depths = []
        for prereq_course in prereq_courses:
            depths.append(depth_first_search(prereq_course, prerequisites, courses_needed, courses_seen) + 1)
    else:
        depths = [1]
    depth = max(depths)
    heapq.heappush(courses_needed, (depth, course))
    courses_seen[course] = depth
    return depth

def check_prerequisite(course_schedules, prerequisites):
    course_taken = {}
    for course in course_schedules:
        for prerequisite in prerequisites.get(course, []):
            if prerequisite not in course_taken:
                return False
        course_taken[course] = True
    return True


def get_all_courses(course_schedule):
    for course in course_schedule:
        yield course


def check_course_schedule(course_schedule):
    # Pass prerequisite requirements.
    assert check_prerequisite(course_schedule, PREREQUISITES)
    all_courses = set(get_all_courses(course_schedule))
    # All NLP courses are chosen.
    assert set(NLP_COURSES).issubset(all_courses)
    assert len(set(NLP_COURSES)) == len(NLP_COURSES)

if __name__ == '__main__':
    course_schedule = cal_my_course_schedule(NLP_COURSES, PREREQUISITES)
    print(course_schedule)
    check_course_schedule(course_schedule)