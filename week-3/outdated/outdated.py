months = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December"
]
while True:
    try:
        date = input("Date: ").strip()
        if "/" in date:
            m, d, y = date.split("/")
            month = int(m)
            day = int(d)
            if month > 12 or day > 31:
                continue
            break
        elif "," in date:
            m, d, y = date.split(" ")
            day = int(d.replace(",", ""))
            if day > 31:
                continue
            if m in months:
                month = months.index(m) + 1
            elif m not in months:
                continue
            break
        else:
            continue
    except ValueError:
        pass

print(f"{y}-{month:02}-{day:02}")
