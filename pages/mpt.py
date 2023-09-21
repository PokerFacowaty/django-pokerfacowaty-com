from datetime import timedelta, datetime
from pathlib import Path
from collections import defaultdict

# check if the line is not a chat message?
# foolproof tests?


def main():
    path_answer = input("\nProvide the full filepath for the log file; leave"
                        + "blank for default (server.log)")
    if path_answer:
        filepath = Path(path_answer)
    else:
        filepath = Path(__file__).parent / "server.log"

    choice_answer = input("\nChoose the mode: [t]op players; [o]ne player\n")
    if choice_answer.lower() == "t":
        number = int(input("\nSelect the number of top players: \n"))
        print(sum_top_players(number, filepath))
    elif choice_answer.lower() == "o":
        nickname = input("\nUsername: ")
        print(sum_one_player(nickname, filepath))


def sum_one_player(nickname, filepath=Path(__file__).parent / "server.log"):
    with open(filepath) as log_file:
        log = log_file.readlines()

    timestamps = []
    for strline in log:
        line = strline.split()
        if line[3] == nickname and (line[5] == "logged"
                                    or line[4] == "lost"):
            timestamps.append(line[0] + " " + line[1])

    if len(timestamps) % 2 == 1:
        timestamps.pop()
        # A case where the user is on the server; not adding now() as the last
        # timestamp since the log does not provide a timezone.

    i = 0
    delta = timedelta()
    while i < len(timestamps):
        delta += (datetime.fromisoformat(timestamps[i + 1])
                  - datetime.fromisoformat(timestamps[i]))
        i += 2

    if not timestamps:
        return "Could not find the user's data."
    else:
        return (f"{delta.days * 24 + delta.seconds // 3600}:"
                + f"{delta.seconds % 3600 // 60}:"
                + f"{delta.seconds % 60}")


def sum_top_players(number, filepath=Path(__file__).parent / "server.log"):
    with open(filepath) as log_file:
        log = log_file.readlines()

    temp = dict()
    nicks = defaultdict(timedelta)
    for strline in log:
        line = strline.split()
        if len(line) > 5 and line[5] == "logged" and line[3][0] != "/":
            temp[line[3]] = line[0] + " " + line[1]
        elif len(line) > 5 and line[4] == "lost" and line[3][0] != "/":
            nicks[line[3]] += (datetime.fromisoformat(line[0] + " " + line[1])
                               - datetime.fromisoformat(temp[line[3]]))

    nicks = sorted(nicks.items(), key=lambda x: x[1], reverse=True)
    final_list = ([f"{x[0]} - "
                   + f"{x[1].days * 24 + x[1].seconds // 3600}:"
                   + f"{x[1].seconds % 3600 // 60:02d}:"
                   + f"{x[1].seconds % 60:02d}" for x in nicks[0:number]])

    return final_list


if __name__ == "__main__":
    main()

