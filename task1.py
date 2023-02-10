#Возвращает функцию, которая обрезает строку (задан первый аргумент), если она длиннее максимальной длины строки
# (задан второй аргумент). Результат также должен заканчиваться на "..."
#Эти точки в конце также увеличивают длину строки.
#Итак, в приведенном выше примере trim("Создание ката - это весело", 14) должен возвращать "Создание ка..."
#Если максимальная длина строки меньше или равна 3 символам, то длина точек не добавляется к длине строки.
#например, trim("Он", 1) должен возвращать "H...", потому что 1 <= 3
#Если строка меньше или равна максимальной длине строки, то просто верните строку без необходимости обрезки или точек.
#например, trim("Code Wars is pretty rad", 50) должен возвращать "Code Wars is pretty rad".

#task1 Test example
# import codewars_test as test
# from solution import trim
#
# @test.describe("trim")
# def tests():
#
#     @test.it("works for some examples")
#     def _():
#         test.assert_equals(trim("Creating kata is fun", 14),"Creating ka...")
#         test.assert_equals(trim("He", 1),"H...")
#         test.assert_equals(trim("Hey", 2),"He...")
#         test.assert_equals(trim("Hey", 3),"Hey")
#         test.assert_equals(trim("Coding rocks", 12),"Coding rocks")
#         test.assert_equals(trim("Code Wars is pretty rad", 50), "Code Wars is pretty rad")
#         test.assert_equals(trim("London is freezing",18),"London is freezing")

# Start resolving! Good luck!
def trim(phrase, size):
    raise NotImplementedError("TODO: trim")
