from types import ModuleType
from typing import Optional, Tuple

from tests.utils.metadata_filters import metadata_filter


def compare_python(expected: str, actual: str) -> Optional[str]:
    """
    Make sure that actual is valid python and, if it is, compare it with expected
    :param expected: expected python -- can either be python text or a file name
    :param actual: generated python -- text or file name
    :return: Differences or issues if any, else None
    """

    def to_text(txt_or_fn: str) -> Tuple[str, Optional[str]]:
        """
        Convert txt_or_fn to text
        :param txt_or_fn:
        :return: text and file name if read from a file
        """
        if '\n' not in txt_or_fn:
            with open(txt_or_fn) as ef:
                txt = ef.read()
        else:
            txt = txt_or_fn
            txt_or_fn = None
        return metadata_filter(txt), txt_or_fn

    exp_txt, exp_fn = to_text(expected)
    act_txt, _ = to_text(actual)

    try:
        spec = compile(act_txt, 'test', 'exec')
        module = ModuleType('test')
        exec(spec, module.__dict__)
    except Exception as e:
        return str(e)

    if exp_txt != act_txt:
        return "Output mismatch" + (f"for file {exp_fn}" if exp_fn else '')
