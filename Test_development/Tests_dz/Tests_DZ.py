import pytest
from DZ1_Set_unique_names import set_unique_names
from DZ2_Set_popular_names import set_popular_names
from DZ1_Dict_recordsmans import dict_recordsmans

#ТЕСТ без параметров
# def test_set_unique_names():
#     expected = 'Бил, Дин, Иван, Том'
#     a_list = [['Иван Иваныч', 'Том Соер', 'Бил Клинтон'],['Иван Иваныч','Дин Винчестер']]
#     res = set_unique_names(a_list)
#     assert res == expected

#ТЕСТЫ с параметрами
class TestDZ:
# DZ1-множества
    @pytest.mark.parametrize('a_list,expected',
                             [([['Иван Иваныч', 'Том Соер', 'Бил Клинтон'],['Иван Иваныч','Дин Винчестер']], 'Бил, Дин, Иван, Том'),
                              ([['Семён Иваныч', 'Зинадин Соер', 'Джон Клинтон'],['Семён Иваныч','Сэм Винчестер']], 'Джон, Зинадин, Семён, Сэм')])
    def test_set_unique_names(self, a_list, expected):
        res = set_unique_names(a_list)
        assert res == expected

    #DZ2-множества
    @pytest.mark.parametrize('a_list,expected',
                             [([['Иван Иваныч', 'Том Соер', 'Бил Клинтон'],['Иван Иваныч','Дин Винчестер']], 'Иван: 2 раз(а), Том: 1 раз(а), Бил: 1 раз(а), '),
                              ([['Семён Иваныч', 'Зинадин Соер', 'Джон Клинтон'],['Семён Иваныч','Сэм Винчестер']], 'Семён: 2 раз(а), Зинадин: 1 раз(а), Джон: 1 раз(а), ')])
    def test_set_popular_names(self, a_list, expected):
        res = set_popular_names(a_list)
        assert res == expected

    #DZ1-словари
    @pytest.mark.parametrize('cur_list, men_list, dur_list, expected',
                             [(['one', 'two'], [['Иван Иваныч', 'Том Соер', 'Бил Клинтон'],['Иван Иваныч','Дин Винчестер']], [1, 2], 'Самый короткий курс(ы): one - 1 месяца(ев)\n'
     'Самый длинный курс(ы): two - 2 месяца(ев)'),
                              (['free', 'four'], [['Семён Иваныч', 'Зинадин Соер', 'Джон Клинтон'],['Семён Иваныч','Сэм Винчестер']], [5, 6], 'Самый короткий курс(ы): free - 5 месяца(ев)\n'
     'Самый длинный курс(ы): four - 6 месяца(ев)')])
    def test_dict_recordsmans(self, cur_list, men_list, dur_list, expected):
        res = dict_recordsmans(cur_list, men_list, dur_list)
        assert res == expected