def sorted_by_score(student):
    return(student["score"])

students = [
{"id":1, "score" : 76},
{"id":2, "score": 80},
{"id":2, "score": 91},
{"id":1, "score": 100},
{"id":2, "score": 40},
{"id":2, "score": 64},
{"id":1, "score": 44},
{"id":1, "score": 55},
{"id":2, "score": 53},
]


students = sorted(students, key = sorted_by_score, reverse = True)[0:5]
print(students)

ID = int(input())

students2 = [stud for stud in students if stud["id"] == ID][0]

print(students2)


print({"task_1_result" : students, "task_2_result" : students2})


