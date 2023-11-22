from random import randint, choice, uniform
from string import ascii_lowercase
import re
from itertools import chain
from time import time
from datetime import timedelta, datetime


class Rdg:
    def __str__():
        return "Random Number Generator object"

    # def run_time(func):
    #     def wrapper(*args, **kwargs):
    #         t1 = time()
    #         try:
    #             return func(*args, **kwargs)
    #         finally:
    #             t2 = time()
    #             time_taken = t2 - t1
    #             print(f"\n *** Time taken by {func.__name__}: {time_taken} ***\n")

    #     return wrapper

    @staticmethod
    def rand_bool(num_rows: int, true_frac=0.4, false_frac=0.6):
        """
        Args:
            num_rows (int): number of rows
            true_frac (float, optional): fraction True bools desired. Defaults to 0.4.
            false_frac (float, optional): fraction False bools desired. Defaults to 0.6.

        Returns:
            generator: containing desired number of bools
        """
        if true_frac + false_frac != 1:
            error_mess = f"Function: {Rdg.rand_bool.__name__} - fractions True and False must add to 1"
            return ValueError(error_mess)

        if true_frac == 0.5 and false_frac == 0.5:
            return Rdg._equal_bool(num_rows)
        else:
            return Rdg._unequal_bool(num_rows, true_frac, false_frac)

    @staticmethod
    def rand_email(num_rows: int):
        for _ in range(num_rows):
            yield f"{Rdg.rand_text(num_rows,num_words=1).__next__()}@{Rdg.rand_choice(num_rows,['outlook','yahoo','hotmail']).__next__()}{Rdg.rand_choice(num_rows,['.co.uk','.com','.fr']).__next__()}".lower()

    @staticmethod
    def rand_float(num_rows: int, min_float=0, max_float=20, decimals=2):
        """
        Args:
            num_rows (int): number of rows
            min_float (int, optional): minimum value for random floats. Defaults to 0.
            max_float (int, optional): maximum value for random floats. Defaults to 20.
            decimals (int, optional): decimal places to round to. Defaults to 2.

        Raises:
            ValueError: max of float range larger than the minimum

        Yields:
            generator: containing desired number of random floats
        """
        if min_float > max_float:
            error_mess = f"Function: {Rdg.rand_float.__name__} - max_float must be larger than min_float"
            raise ValueError(error_mess)

        for _ in range(num_rows):
            yield round(uniform(float(min_float), float(max_float)), decimals)

    @staticmethod
    def rand_int(num_rows: int, min_int=0, max_int=100):
        """
        Args:
            num_rows (int): number of rows
            min_int (int, optional): minimum value for random ints. Defaults to 0.
            max_int (int, optional): maximum value for random ints. Defaults to 100.

        Raises:
            ValueError: max of int range larger than the minimum

        Yields:
            generator: containing desired number of random ints
        """
        if min_int > max_int:
            error_mess = f"Function: {Rdg.rand_int.__name__} - max_int must be larger than min_int"
            raise ValueError(error_mess)

        for _ in range(num_rows):
            yield (randint(int(min), int(max)))

    @staticmethod
    def rand_dates(
        num_rows: int,
        start_date: str = "2000-12-01",
        end_date: str = "2010-12-01",
    ):
        if re.fullmatch(r"^[\d]{4}-[\d]{2}-[\d]{2}$", start_date) and re.fullmatch(
            r"^[\d]{4}-[\d]{2}-[\d]{2}$", end_date
        ):
            start_date_obj = datetime.strptime(start_date, "%Y-%m-%d").date()
            end_date_obj = datetime.strptime(end_date, "%Y-%m-%d").date()
            print("1")

        elif re.fullmatch(
            r"^[\d]{4}-[\d]{2}-[\d]{2} [\d]{2}:[\d]{2}:[\d]{2}$", start_date
        ) and re.fullmatch(
            r"^[\d]{4}-[\d]{2}-[\d]{2} [\d]{2}:[\d]{2}:[\d]{2}$", end_date
        ):
            start_date_obj = datetime.strptime(start_date, "%Y-%m-%d %H:%M:%S")
            end_date_obj = datetime.strptime(end_date, "%Y-%m-%d %H:%M:%S")
            print("2")

        else:
            error_mess = f"Function: {Rdg.rand_dates.__name__} - dates(times) must both be in format (inc. whitespace if timestamp): YYYY-MM-DD HH:MM:SS"
            raise ValueError(error_mess)

        delta = end_date_obj - start_date_obj
        delta = delta.days * 24 * 60 * 60

        for _ in num_rows:
            random_seconds = randint(0, delta)
            yield start_date_obj + timedelta(seconds=random_seconds)

    @staticmethod
    def rand_choice(num_rows: int, values: list):
        """
        Args:
            num_rows (int): number of rows
            values (list): a list desired values, any dtype

        Yields:
            generator: containing random selection of provided values
        """
        for _ in range(num_rows):
            yield choice(values)

    @staticmethod
    def rand_text(
        num_rows: int,
        min_ltrs=6,
        max_ltrs=14,
        num_words=3,
        capitalise=True,
        strip=True,
    ):
        """
        Args:
            num_rows (int): number of rows
            min_ltrs (int, optional): minimum letters in word(s) total. Defaults to 6.
            max_ltrs (int, optional): maximum letters in word(s) total. Defaults to 12.
            num_words (int, optional): desired number of words. Defaults to 2.
            capitalise (bool, optional): sets title case. Defaults to True.
            strip (bool, optional): removes trailing whitespace. Defaults to True.

        Yields:
            generator: generator containing data for text column
        """

        if max_ltrs <= 2:
            num_words = 1
            print("num_words is set to 1 when mx_ltrs is 2")

        for _ in range(num_rows):
            new_string = "".join(
                [choice(ascii_lowercase) for _ in range(randint(min_ltrs, max_ltrs))]
            )

            new_string = Rdg._split_text(new_string, num_words)

            if strip == True:
                new_string = new_string.strip()
            if capitalise == True:
                new_string = new_string.title()

            yield new_string

    @staticmethod
    def _recursive_split(target_string: str, num_splits: int, used=[0]):
        """
        Slower than _not_recursive_split method.

        Args:
            target_string (str): string to be split
            num_splits (int): number of splits to make
            used (list, optional): points split at. Defaults to [0].

        Returns:
            str: string split into desired number of words
        """

        while num_splits != 0:
            split_spot = randint(1, len(target_string) - 1)
            target_string = f"{target_string[:split_spot]} {target_string[split_spot:]}"
            num_splits -= 1

            if num_splits <= 0:
                return target_string
            else:
                return Rdg._recursive_split(target_string, num_splits, used)

    @staticmethod
    def _not_recursive_split(target_string: str, splits: int):
        """
        Args:
            target_string (str): string to be split
            splits (int): number of spaces to insert

        Returns:
            str: string split into desired number of words
        """
        for _ in range(splits):
            split_spot = randint(1, len(target_string) - 1)
            target_string = f"{target_string[:split_spot]} {target_string[split_spot:]}"
        return target_string

    @staticmethod
    def _split_text(new_string: str, num_words: int):
        """
        Args:
            new_string (str): the string to be split
            num_words (int): the number of words to create

        Raises:
            TypeError: input args not correct type
            ValueError: must have at least 1 word

        Returns:
            str: multiple word string
        """

        if num_words <= 0:
            error_mess = f"Function: {Rdg._split_text.__name__} - num words must be greater than 0"
            raise ValueError(error_mess)

        elif num_words == 1:
            return new_string

        elif num_words == 2:
            split_position = len(new_string) // 2
            return f"{new_string[:split_position]} {new_string[split_position:]}"

        else:
            new_string = Rdg._not_recursive_split(new_string, num_words - 1)
            new_string = re.sub(r"\s{2}", f" {choice(ascii_lowercase)} ", new_string)
            return new_string

    @staticmethod
    def _equal_bool(num_rows: int):
        """
        Args:
            num_rows (int): number of rows

        Yields:
            Generator: containing 50% of each bool
        """
        for _ in num_rows:
            yield choice(True, False)

    @staticmethod
    def _bool_iter(num_bool: int, type: bool):
        """
        Args:
            num_bool (int): number of bools requested
            type (bool): True or False

        Yields:
            generator: generator containing bools of given type
        """
        for _ in range(num_bool):
            yield type

    @staticmethod
    def _unequal_bool(num_rows: int, true_frac: float, false_frac: float):
        """
        Args:
            num_rows (int): number of rows
            true_frac (float): fraction of generator that is True
            false_frac (float): fraction of generator that is False

        Returns:
            generator: containing desired number of True and False
        """
        num_true = round(num_rows * true_frac)
        num_false = round(num_rows * false_frac)

        if num_true + num_false > num_rows:
            num_false -= num_true + num_false - num_rows

        return chain(Rdg._bool_iter(num_true, True), Rdg._bool_iter(num_false, False))
