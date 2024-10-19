#todo: Задан словарь, его значения необходимо внести по соответствующим тегам и атрибутам вместо вопросов (?)
# заполненный шаблон записать в файл index.html.

page = {"title": "Тег BODY",
        "charset": "utf-8",
        "alert": "Документ загружен",
        "p": "Ut wisis enim ad minim veniam,  suscipit lobortis nisl ut aliquip ex ea commodo consequat."}

template = """ 
<!DOCTYPE HTML>
<html>
 <head>
  <title> {title} </title>
  <meta charset={charset}>
 </head>
 <body onload="alert {alert}">
 
  <p> {p} </p>

 </body>
</html>
"""

filled_template = template.format(
    title=page['title'],
    charset=page['charset'],
    alert=page['alert'],
    p=page['p'])

f = open('index.html', 'w', encoding='utf-8')
f.write(filled_template)
