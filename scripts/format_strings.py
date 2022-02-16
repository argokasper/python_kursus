

#
def format(string, string2, string3):
    return "Sisestud sõna/fraas: [{0}, {1}, {2}]".format(string, string2, string3)


print(format('Hello', '123', 'kursus'))


def parse_email_content(name, date, platform, sender = "Tiim"):
    template = """
    Tere {0},
    Oled kutsutud üritusele, mis toimub {1} ning see toimub {2} vahendusel.
    Parimat,
    {3}
    """.format(name, date, platform, sender)

    return template

print(parse_email_content("Argo Käsper", "1. juulil 2022", "Zoom'i"))
print(parse_email_content("Argo Käsper", "1. juulil 2022", "Zoom'i", "SmartCod"))

def format_new(string, string2, string3):
    return f"{string}-{string2}-{string3}: see on sõnakett"

print(format_new("auto", "oja", "aus"))

# funkts., mis võtab sisendiks kursuse nime, koodi, õpilase täisnime ja alustus kuupäeva
# funkts. väljastab kursuse väljavõtte selle õpilase ning kursuse nime koos koodi ja alguskuupäevaga
# Nt: [õpilase nimi] registreeris end kursusele [kursuse nimi], [kursuse kood] algusega [kuupäev]
# õp nimi - string,
# kursuse nimi - string
# kursuse kood - int
# alg. kuupäev - datetime (var_date = datetime.strptime("2022-01-01", "%Y-%m-%d")) -> tekib date objekt string kuupäevast
#                var_date.strftime("%d.%m.%Y")

from datetime import datetime
def export_student_course_reg_message(student_name: str, course_name: str, course_code: int, course_start_date: datetime):
    formatted_date = course_start_date.strftime("%d.%m.%Y")
    return f"{student_name} registreeris end kursusele {course_name}, {course_code} algusega {formatted_date}"

print(export_student_course_reg_message("Tom", "Eesti keel", 1234567, datetime.strptime("2022-09-01", "%Y-%m-%d")))