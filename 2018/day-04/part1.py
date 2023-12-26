CAL = {
    1: 31,
    2: 28,
    3: 31,
    4: 30,
    5: 31,
    6: 30,
    7: 31,
    8: 31,
    9: 30,
    10: 31,
    11: 30,
    12: 31,
}


def parse(line):
    idx, awake = -1, True

    dtime, info = line[1:].split("]")

    date, time = dtime.split()
    _, mth, day = date.strip().split("-")
    mth, day = int(mth), int(day)

    hh, mm = time.strip().split(":")
    hh, mm = int(hh), int(mm)

    if hh == 23:
        hh, day = -1, day + 1
    if day > CAL[mth]:
        mth, day = mth + 1, day - CAL[mth]

    info = info.strip()

    if info.startswith("Guard"):
        idx = int(info.split()[1][1:])
    elif info.startswith("falls"):
        awake = False

    return mth, day, hh, mm, idx, awake


def slept(times):
    result = 0
    minutes = [0] * 60
    fell = -1
    for hh, mm, awake in times:
        if awake and (fell != -1):
            woke = 60 if hh > 0 else mm
            result += woke - fell
            for i in range(fell, woke):
                minutes[i] = 1
            fell = -1
        if not awake:
            fell = mm
    return result, minutes


def sleepiest(guards):
    max_sl = 0
    idx = -1

    for guard, data in guards.items():
        if max_sl < data["total"]:
            max_sl = data["total"]
            idx = guard

    return idx


def part1(guards):
    sleepy_g = sleepiest(guards)
    minutes = guards[sleepy_g]["mins"]
    idx = minutes.index(max(minutes))
    return idx * sleepy_g


def part2(guards):
    max_sl = 0
    day_sl = -1
    idx = -1

    for g in guards:
        cur_mins = guards[g]["mins"]
        cur_max = max(cur_mins)
        if cur_max > max_sl:
            max_sl = cur_max
            day_sl = cur_mins.index(max_sl)
            idx = g

    return idx * day_sl


if __name__ == "__main__":
    with open("./_inputs/2018/day-04/input.txt", "r", encoding="utf8") as f:
        schedule = {}
        guards = {}

        for line in f:
            line = line.strip()
            if line == "":
                break

            mth, day, hh, mm, idx, awake = parse(line)

            if (mth, day) not in schedule:
                schedule[(mth, day)] = {"id": -1, "times": []}

            if idx != -1:
                schedule[(mth, day)]["id"] = idx

            schedule[(mth, day)]["times"].append((hh, mm, awake))

        for date in schedule:
            schedule[date]["times"].sort()

        for d in schedule:
            idx = schedule[d]["id"]
            if idx not in guards:
                guards[idx] = {"total": 0, "mins": [0] * 60}

            tt, mins = slept(schedule[d]["times"])
            guards[idx]["total"] += tt
            for i in range(60):
                guards[idx]["mins"][i] += mins[i]

        print(f"Part 1: {part1(guards)}")
        print(f"Part 2: {part2(guards)}")
