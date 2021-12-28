from abc import ABC, abstractmethod


class ArgParser(ABC):
    """
    Abstract Class.
    A Concrete Class that inherits it should implement a parse_args
    method, responsible to parse the args received as a parameter
    and return them as a Dictionary

    ...

    Methods
    -------
    parse_args(args) : dict, abstract
        Parses the args into a dict

    """
    @abstractmethod
    def parse_args(self, args) -> dict:
        """
        parse_args(args)
            Abstract Method.
            Parses the args into a dict

        Parameters
        ----------
        args
            An object, usually a list or Namespace, with the args to
            be parsed

        Returns
        -------
        dict
            A dictionary of arguments
        """
        pass
