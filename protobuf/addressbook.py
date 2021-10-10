import addressbook_pb2

person = addressbook_pb2.Person()
person.id = 3498
person.name = "Per Parker"
person.email = "per.parker@mail.no"
phone = person.phones.add()
phone.number = "+47 222 33 444"
phone.type = addressbook_pb2.Person.HOME

print(person)
