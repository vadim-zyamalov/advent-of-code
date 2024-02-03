FIELDS = ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid", "cid"]


def isvalid(entry, N=7, skip="cid"):
    result = 0
    els = entry.split()
    for el in els:
        fld, data = el.split(":")
        result += 1 if fld != skip else 0
    return result == N


def tonum(data, lb, ub):
    try:
        res = int(data)
    except ValueError:
        return False
    return lb <= res <= ub


def isvalid2(entry, N=7, skip="cid"):
    result = 0
    els = entry.split()
    for el in els:
        fld, data = el.split(":")
        match fld:
            case "byr":
                result += 1 if tonum(data, 1920, 2002) else 0
            case "iyr":
                result += 1 if tonum(data, 2010, 2020) else 0
            case "eyr":
                result += 1 if tonum(data, 2020, 2030) else 0
            case "hgt":
                units = data[-2:]
                if units not in ["cm", "in"]:
                    return False
                data = data[:-2]
                if units == "cm":
                    result += 1 if tonum(data, 150, 193) else 0
                else:
                    result += 1 if tonum(data, 59, 76) else 0
            case "hcl":
                result += (
                    1
                    if data[0] == "#"
                    and len(data[1:]) == 6
                    and all(d in "0123456789abcdef" for d in data[1:])
                    else 0
                )
            case "ecl":
                result += (
                    1
                    if data in ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]
                    else 0
                )
            case "pid":
                result += 1 if len(data) == 9 and all(d.isdigit() for d in data) else 0
    return result == N


if __name__ == "__main__":
    with open("_inputs/2020/day-04/input.txt", "r", encoding="utf8") as f:
        lines = f.read().strip().split("\n\n")
        lines = [el.replace("\n", " ") for el in lines]

    result = sum(int(isvalid(el, 7, "cid")) for el in lines)
    print(f"Part 1: {result}")

    result = sum(isvalid2(el, 7, "cid") for el in lines)
    print(f"Part 2: {result}")
