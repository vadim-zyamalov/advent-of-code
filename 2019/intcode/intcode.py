from typing import NamedTuple
from .dynlist import DynList
import warnings

Params = NamedTuple("Params", [("N", int), ("outoff", int | None)])

OPCODES = {
    1: Params(3, -1),
    2: Params(3, -1),
    3: Params(1, -1),
    4: Params(1, -1),
    5: Params(2, -1),
    6: Params(2, -1),
    7: Params(3, -1),
    8: Params(3, -1),
    99: Params(0, None),
}


class AddressError(Exception):
    pass


class ModeError(Exception):
    pass


class OpcodeError(Exception):
    pass


class CodeWarning(Warning):
    pass


class Intcode:
    def __init__(self, program: list[int], strict=False):
        if not strict:
            self._regs = DynList(program)
        else:
            self._regs = list(program)
        self._ip = 0
        self._strict = strict

    def _decompose_val(self, ip: int, val: int):
        _modes, opcode = divmod(val, 100)

        modes = []
        address = []
        values = []

        _npar, _outoff = OPCODES[opcode]

        for _ in range(_npar):
            _modes, mode = divmod(_modes, 10)
            modes.append(mode)

        _pp = [ip + i for i in range(1, _npar + 1)]

        if self._strict:
            if any(_p >= len(self.regs) for _p in _pp):
                raise AddressError(
                    "one of parameter pointers at IP={ip} is out of address space"
                )
            if any(
                self.regs[_p] >= len(self.regs)
                for i, _p in enumerate(_pp)
                if modes[i] == 0
            ):
                raise AddressError(
                    "one of adresses at IP=={ip} is out of address space"
                )

        for i, mode in enumerate(modes):
            _idx = self.regs[_pp[i]]
            match mode:
                case 0:
                    address.append(_idx)
                    values.append(self.regs[_idx])
                case 1:
                    address.append(_pp[i])
                    values.append(_idx)
                case _:
                    raise ModeError(f"unknown mode {mode}")

        return opcode, _npar, _outoff, modes, address, values

    def reset(self):
        del self.regs
        self._ip = 0

    def process(
        self, in3: list[int] | None = None, verbose=False, resume=False
    ):
        if not resume:
            self.regs = self._regs.copy()

        ip = self._ip

        _outputs = []

        while ip < len(self.regs):
            (
                opcode,
                _npar,
                _outoff,
                modes,
                address,
                values,
            ) = self._decompose_val(ip, self.regs[ip])

            if verbose:
                print(
                    f"> {ip}: op {opcode}, mod: {modes}, adr: {address}, val: {values} => ",
                    end="",
                )

            _outaddr = 0 if _outoff is None else address[_outoff]

            if (
                opcode in [1, 2, 3, 7, 8]
                and modes != []
                and _outoff is not None
                and (modes[_outoff] != 0)
            ):
                raise ModeError(
                    f"non-zero mode {modes[_outoff]} for output position"
                )

            _ip: int | None = None

            match opcode:
                case 1:
                    self.regs[_outaddr] = values[0] + values[1]

                case 2:
                    self.regs[_outaddr] = values[0] * values[1]

                case 3:
                    if in3 is None:
                        self.regs[_outaddr] = int(input(r"[INPUT?]: "))
                    else:
                        if in3:
                            self.regs[_outaddr] = in3.pop(0)
                        else:
                            self._ip = ip
                            return _outputs, False

                case 4:
                    if verbose:
                        print(f"[OUTPUT]: {self.regs[_outaddr]}")
                    _outputs.append(self.regs[_outaddr])

                case 5:
                    if values[0] != 0:
                        _ip = values[1]

                case 6:
                    if values[0] == 0:
                        _ip = values[1]

                case 7:
                    self.regs[_outaddr] = int(values[0] < values[1])

                case 8:
                    self.regs[_outaddr] = int(values[0] == values[1])

                case 99:
                    return _outputs, True

                case _:
                    raise OpcodeError(f"unknown opcode [{opcode}]")

            ip = _ip if _ip is not None else ip + _npar + 1
            if verbose:
                print(f" {ip}")
        else:
            warnings.warn(
                "program halted with no exit opcode reached", CodeWarning
            )
        return _outputs
