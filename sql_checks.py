from default_checks import Checks


class SqlInjectionCheck:
    @staticmethod
    def run(rabbit: str, symbols_check=True, soft_check=False, hard_check=False):
        assert Checks.

        if symbols_check:
            assert Checks.symbols_check(rabbit) is None


        rabbit = rabbit.strip()


        for word in rabbit.split():
            assert word not in sql_injections
