from collections import defaultdict
from typing import NamedTuple, DefaultDict
import warnings

OUTOFF = -1

ASCII = 128

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

ZEROCODES = (1, 2, 3, 7, 8)

Output = NamedTuple(
    "Output",
    [
        ("list", tuple[int, ...]),
        ("ascii", str),
        ("rest", tuple[int, ...]),
        ("status", bool),
    ],
)
State = NamedTuple(
    "State",
    [
        ("registers", tuple[tuple[int, int], ...]),
        ("pointer", int),
        ("relbase", int),
    ],
)


class ModeError(Exception):
    pass


class OpcodeError(Exception):
    pass


class CodeWarning(Warning):
    pass


class Intcode:
    def __init__(self, program: list[int], ascii=False):
        self.initials: DefaultDict[int, int] = defaultdict(int)
        for i, num in enumerate(program):
            self.initials[i] = num

        self.registers = self.initials.copy()
        self.pointer = 0
        self.relbase = 0
        self.ascii = ascii

    def _decompose_val(self, pointer: int, value: int):
        _modes, opcode = divmod(value, 100)

        modes = []
        addresses = []
        values = []

        num_params = OPCODES[opcode]

        for _ in range(num_params):
            _modes, mode = divmod(_modes, 10)
            modes.append(mode)

        param_pointers = [pointer + i for i in range(1, num_params + 1)]

        for i, mode in enumerate(modes):
            param_value: int = self.registers[param_pointers[i]]
            match mode:
                case 0:
                    addresses.append(param_value)
                    values.append(self.registers[param_value])
                case 1:
                    addresses.append(param_pointers[i])
                    values.append(param_value)
                case 2:
                    addresses.append(self.relbase + param_value)
                    values.append(self.registers[self.relbase + param_value])
                case _:
                    raise ModeError(f"unknown mode {mode}")

        return opcode, num_params, modes, addresses, values

    @staticmethod
    def _ascii_input(line):
        return list(map(ord, list(line)))

    @staticmethod
    def _ascii_output(data) -> tuple[str, tuple[int, ...]]:
        text, rest = "", ()
        for el in data:
            if el < ASCII:
                text += chr(el)
            else:
                rest += (el,)
        return text, rest

    def _output(self, data, status):
        if self.ascii:
            text, rest = self._ascii_output(data)
        else:
            text, rest = "", ()
        return Output(tuple(data), text, rest, status)

    def save(self) -> State:
        regs = tuple((k, v) for k, v in self.registers.items())
        return State(regs, self.pointer, self.relbase)

    def load(self, state: State):
        self.registers = defaultdict(int)
        for k, v in state.registers:
            self.registers[k] = v
        self.pointer = state.pointer
        self.relbase = state.relbase

    def reset(self) -> None:
        self.registers = self.initials.copy()
        self.pointer = 0
        self.relbase = 0

    def start(
        self, inputs: list[int] | str | None = None, verbose=False
    ) -> Output:
        self.reset()
        return self.process(inputs=inputs, verbose=verbose)

    def process(
        self,
        inputs: list[int] | str | None = None,
        verbose=False,
    ) -> Output:
        pointer = self.pointer
        ascii = self.ascii

        output_values = []

        while pointer < len(self.registers):
            (
                opcode,
                num_params,
                modes,
                addresses,
                values,
            ) = self._decompose_val(pointer, self.registers[pointer])

            if verbose:
                print(
                    f"> {pointer}: op {opcode}, mod: {modes}, adr: {addresses}, val: {values} => ",
                    end="",
                )

            res_address = 0 if addresses == [] else addresses[OUTOFF]

            if opcode in ZEROCODES and (modes[OUTOFF] == 1):
                raise ModeError(
                    f"incompatible mode {modes[OUTOFF]} for output position"
                )

            jump_pointer: int | None = None

            match opcode:
                case 1:
                    self.registers[res_address] = values[0] + values[1]

                case 2:
                    self.registers[res_address] = values[0] * values[1]

                case 3:
                    if (inputs == []) or (inputs == ""):
                        self.pointer = pointer
                        return self._output(output_values, False)

                    if inputs is None:
                        inputs = input(r"[INPUT?]: ")

                    if ascii:
                        if isinstance(inputs, str):
                            if not inputs.endswith("\n"):
                                inputs += "\n"
                            inputs = self._ascii_input(inputs)
                            ascii = False
                        else:
                            raise ValueError(
                                "non-string input provided for ascii-mode"
                            )
                    else:
                        if isinstance(inputs, str):
                            inputs = [int(inputs)]

                    self.registers[res_address] = inputs.pop(0)

                case 4:
                    if verbose:
                        print(f"[OUTPUT]: {values[OUTOFF]}")
                    output_values.append(values[OUTOFF])

                case 5:
                    if values[0] != 0:
                        jump_pointer = values[1]

                case 6:
                    if values[0] == 0:
                        jump_pointer = values[1]

                case 7:
                    self.registers[res_address] = int(values[0] < values[1])

                case 8:
                    self.registers[res_address] = int(values[0] == values[1])

                case 9:
                    self.relbase += values[OUTOFF]

                case 99:
                    return self._output(output_values, True)

                case _:
                    raise OpcodeError(f"unknown opcode [{opcode}]")

            pointer = (
                jump_pointer
                if jump_pointer is not None
                else pointer + num_params + 1
            )
            if verbose:
                print(f" {pointer}")
        else:
            warnings.warn(
                "program halted with no exit opcode reached", CodeWarning
            )
        return self._output(output_values, True)
