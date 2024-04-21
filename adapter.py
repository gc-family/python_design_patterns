import datetime
import pprint


class StateSetter:
    def __init__(self, pattern):
        self.__pattern = pattern

    def __slash(self):
        return True if self.__pattern == '/' else self.__hyphen()

    def __hyphen(self):
        return True if self.__pattern == '-' else self.__backslash()

    def __backslash(self):
        return True if self.__pattern == '\\' else self.__error()

    def __error(self):
        print('error : unrecognized patter')
        return False

    def test(self):
        return self.__slash()


class AgeCalculator:
    def __init__(self, birthday):
        """
        receive : <YYYY-MM-DD >- in this format the birthdate of the the given Entity
        """

        self.year, self.month, self.day = self._change(birthday)
        pass

    def _change(self, date):
        """this date must be in a formant <YYYY-MM-DD >"""
        return (int(x) for x in date.split('-'))

    def calculate_age(self, current_date):
        """this current date must be in <YYYY-MM-DD > format"""
        year, month, day = self._change(current_date)
        age = year - self.year
        if (month, day) < (self.month, self.day):
            age -= 1
        return age


class DateAgeAdapter:
    def __init__(self, birthday):
        self.birthday = self._str_date(birthday)
        self._calculator = AgeCalculator(self.birthday)

    def _str_date(self, date):
        return date.strftime("%Y-%m-%d")

    def get_age(self, date):
        date = self._str_date(date)
        return self._calculator.calculate_age(date)


class AgeDate(datetime.date):
    def split(self, charm):
        return self.year, self.month, self.day


if __name__ == '__main__':
    bd = AgeDate(1993, 4, 27)
    today = AgeDate.today()
    a = AgeCalculator(bd)
    a.calculate_age("2014-04-27")
    # -----------------------------------------------------------------
    result = DateAgeAdapter(datetime.datetime.now())
    print(result)
    print(result.get_age(datetime.datetime.now()))
    print(datetime.datetime.now())

    test = StateSetter('d')
    print(dir(test))
    try:
        print(test.test())
    except Exception as e:
        print(type(e))
        print(e)