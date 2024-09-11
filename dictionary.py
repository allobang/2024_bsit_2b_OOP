from prettytable import PrettyTable

table = PrettyTable()

table.field_names = ["Last Name", "Sex", "Course", "Subject", "GWA","Equivalent", "Status"]

studentInfo = [
    {
        "firstName" : "Christian Jay",
        "lastName" : "Rialubin",
        "middleName" : "Guzman",
        "sex" : "male",
        "course" : "BSIT",
        "yearLevel" : 2,
        "section" : "A",
        "subjects" : {
            "OOP" : 75,
            "DSAL" : 74,
            "PE3" : 89,
        }
    },
    {
        "firstName" : "Jenny Mae",
        "lastName" : "Rigos",
        "middleName" : "Pontela",
        "sex" : "female",
        "course" : "BSIT",
        "yearLevel" : 2,
        "section" : "A",
        "subjects" : {
            "OOP" : 89,
            "DSAL" : 85,
            "PE3" : 84,
        }
    },
    {
        "firstName" : "Kamille",
        "lastName" : "Salvador",
        "middleName" : "Ragual",
        "sex" : "female",
        "course" : "BSIT",
        "yearLevel" : 2,
        "section" : "A",
        "subjects" : {
            "OOP" : 92,
            "DSAL" : 95,
            "PE3" : 80,
        }
    },
    {
        "firstName" : "Maila",
        "lastName" : "Supremindo",
        "middleName" : "Puyanan",
        "sex" : "female",
        "course" : "BSIT",
        "yearLevel" : 2,
        "section" : "A",
        "subjects" : {
            "OOP" : 96,
            "DSAL" : 88,
            "PE3" : 89,
            "STS" : 89,
        }
    }
]

for student in studentInfo:
    table.add_row(
        [
            student['lastName'],
            student['sex'],
            f"{student['course']} {student['yearLevel']} {student['section']}",
            student['subjects'],
            "",
            "",
            "",
        ])

print(table)