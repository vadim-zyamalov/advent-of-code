from typing import NamedTuple
from .dynlist import DynList

Params = NamedTuple("Params", [("N", int), ("outoff", int)])

OPCODES = {
    1: Params(3, -1),
    2: Params(3, -1),
    3: Params(1, -1),
    4: Params(1, -1),
    5: Params(2, -1),
    6: Params(2, -1),
    7: Params(3, -1),
    8: Params(3, -1),
    99: Params(0, 0),
}


class Intcode:
    def __init__(self, program: list[int]):
        self._regs = DynList(program)

    def reset(self):
        del self.regs

    def parse_val(self, ip: int, val: int):
        _modes, opcode = divmod(val, 100)

        modes = []
        adress = []
        values = []

        _npar, _outoff = OPCODES[opcode]

        for _ in range(_npar):
            _modes, mode = divmod(_modes, 10)
            modes.append(mode)

        pp = [ip + i for i in range(1, _npar + 1)]

        for i, mode in enumerate(modes):
            _idx = self.regs[pp[i]]
            match mode:
                case 0:
                    adress.append(_idx)
                    values.append(self.regs[_idx])
                case 1:
                    adress.append(pp[i])
                    values.append(_idx)
                case _:
                    assert False

        return opcode, pp, modes, adress, values

    def process(self, in3=None, verbose=False):
        self.regs = self._regs.copy()

        ip = 0

        while self.regs[ip] != 99:
            opcode, pp, modes, adress, values = self.parse_val(
                ip, self.regs[ip]
            )
            _npar, _outoff = OPCODES[opcode]
            _ip: int | None = None

            outadr = adress[_outoff]

            match opcode:
                case 1:
                    self.regs[outadr] = values[0] + values[1]
                case 2:
                    self.regs[outadr] = values[0] * values[1]
                case 3:
                    if in3 is None:
                        self.regs[outadr] = int(input(r"[INPUT?]: "))
                    else:
                        self.regs[outadr] = int(in3)
                case 4:
                    print(f"[OUTPUT]: {self.regs[outadr]}")
                case 5:
                    if values[0] != 0:
                        _ip = values[1]
                case 6:
                    if values[0] == 0:
                        _ip = values[1]
                case 7:
                    self.regs[outadr] = int(values[0] < values[1])
                case 8:
                    self.regs[outadr] = int(values[0] == values[1])
                case _:
                    raise ValueError("Unknown opcode [{opcode}] were provided")
            if verbose:
                print(
                    f"> {ip}: op {opcode}, mod: {modes}, adr: {adress}, val: {values} => ",
                    end="",
                )
            ip = _ip if _ip is not None else ip + _npar + 1
            if verbose:
                print(f" {ip}")
