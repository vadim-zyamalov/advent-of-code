from collections import defaultdict
import warnings

OUTOFF = -1

OPCODES = {
    1: 3,
    2: 3,
    3: 1,
    4: 1,
    5: 2,
    6: 2,
    7: 3,
    8: 3,
    9: 1,
    99: 0,
}

ZEROCODES = [1, 2, 3, 7, 8]


class ModeError(Exception):
    pass


class OpcodeError(Exception):
    pass


class CodeWarning(Warning):
    pass


class Intcode:
    def __init__(self, program: list[int]):
        self._regs = defaultdict(int)
        for i, num in enumerate(program):
            self._regs[i] = num
        # self._regs = DynList(program)
        self._ip = 0
        self._rbase = 0

    def _decompose_val(self, ip: int, val: int):
        _modes, opcode = divmod(val, 100)

        modes = []
        address = []
        values = []

        _npar = OPCODES[opcode]

        for _ in range(_npar):
            _modes, mode = divmod(_modes, 10)
            modes.append(mode)

        _pp = [ip + i for i in range(1, _npar + 1)]

        for i, mode in enumerate(modes):
            _idx: int = self.regs[_pp[i]]
            match mode:
                case 0:
                    address.append(_idx)
                    values.append(self.regs[_idx])
                case 1:
                    address.append(_pp[i])
                    values.append(_idx)
                case 2:
                    address.append(self._rbase + _idx)
                    values.append(self.regs[self._rbase + _idx])
                case _:
                    raise ModeError(f"unknown mode {mode}")

        return opcode, _npar, modes, address, values

    def reset(self):
        del self.regs
        self._ip = 0
        self._rbase = 0

    def process(
        self, inputs: list[int] | None = None, verbose=False, resume=False
    ):
        if not resume:
            self.regs = self._regs.copy()
            # self.regs = DynList(self._regs)

        ip = self._ip

        _outputs = []

        while ip < len(self.regs):
            (
                opcode,
                _npar,
                modes,
                address,
                values,
            ) = self._decompose_val(ip, self.regs[ip])

            if verbose:
                print(
                    f"> {ip}: op {opcode}, mod: {modes}, adr: {address}, val: {values} => ",
                    end="",
                )

            _outaddr = 0 if address == [] else address[OUTOFF]

            if opcode in ZEROCODES and (modes[OUTOFF] == 1):
                raise ModeError(
                    f"incompatible mode {modes[OUTOFF]} for output position"
                )

            _ip: int | None = None

            match opcode:
                case 1:
                    self.regs[_outaddr] = values[0] + values[1]

                case 2:
                    self.regs[_outaddr] = values[0] * values[1]

                case 3:
                    if inputs is None:
                        self.regs[_outaddr] = int(input(r"[INPUT?]: "))
                    else:
                        if inputs:
                            self.regs[_outaddr] = inputs.pop(0)
                        else:
                            self._ip = ip
                            return _outputs, False

                case 4:
                    if verbose:
                        print(f"[OUTPUT]: {values[OUTOFF]}")
                    _outputs.append(values[OUTOFF])

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

                case 9:
                    self._rbase += values[OUTOFF]

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
