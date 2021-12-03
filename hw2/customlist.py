from copy import copy


class CustomList(list):
    def __add__(self, other, coefficient_right_operand=1):
        self.check_support_type_to_custom_list_oper(other)
        new_custom_list = copy(self)
        if len(self) < len(other):
            new_custom_list.extend([0] * (len(other) - len(self)))
        for index in range(len(other)):
            new_custom_list[index] += coefficient_right_operand * other[index]
        return new_custom_list

    def __sub__(self, other):
        return self.__add__(other, coefficient_right_operand=-1)

    def __rsub__(self, other):
        return CustomList(other) - self

    def __radd__(self, other):
        return CustomList(other) + self

    def __eq__(self, other):
        self.check_support_type_to_custom_list_oper(other)
        return sum(self) == sum(other)

    def __le__(self, other):
        self.check_support_type_to_custom_list_oper(other)
        return sum(self) <= sum(other)

    def __ge__(self, other):
        self.check_support_type_to_custom_list_oper(other)
        return sum(self) >= sum(other)

    def __lt__(self, other):
        self.check_support_type_to_custom_list_oper(other)
        return sum(self) < sum(other)

    def __gt__(self, other):
        self.check_support_type_to_custom_list_oper(other)
        return sum(self) > sum(other)

    def __ne__(self, other):
        self.check_support_type_to_custom_list_oper(other)
        return sum(self) != sum(other)

    @staticmethod
    def check_support_type_to_custom_list_oper(other):
        if not isinstance(other, list):
            raise TypeError
