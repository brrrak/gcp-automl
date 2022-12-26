import json
import datetime
import plotly.express as px
import os


def get_perf_over_time(filename):
    print(f"Parsing {filename}")
    with open(filename) as fp:
        logs = json.load(fp)[0]
    timestamps = []
    scores = []
    for event_id, message in logs["event_log"]["message"].items():
        if not message.startswith("New leader:"):
            continue
        print(event_id, message, logs["event_log"]["timestamp"][event_id])
        _, metric, score = message.rsplit(' ', maxsplit=2)
        metric, score = metric[:-1].upper(), float(score)
        scores.append(score)
        timestamps.append(datetime.datetime.strptime(
            logs["event_log"]["timestamp"][event_id], "%H:%M:%S.%f"))
    print("-------------------------------------------------------------------")

    times = [(x - timestamps[0]).total_seconds() / 60 for x in timestamps]
    scores.append(scores[-1])
    times.append(60)

    return scores, times, metric


def plot_perf(log, taskname, show=False, write=True):
    scores, times, metric = log
    fig = px.line(x=times, y=scores, range_x=(0, 60),
                  labels={"x": "Minutes Passed", "y": metric},
                  title="AutoML Performance on " + taskname,
                  markers=True
                  )
    if show:
        fig.show()
    if write:
        fig.write_image(taskname.split(':')[0].replace(' ', '_') + ".png")


if __name__ == "__main__":
    perfs = list(map(get_perf_over_time, filter(
        lambda s: s.endswith(".json"), os.listdir("."))))
    plot_perf(perfs[0], "Classification Task 1: Product Backorders Dataset")
    plot_perf(perfs[1], "Classification Task 2: Electric Devices Dataset")
    plot_perf(perfs[2], "Classification Task 3: Mushroom Dataset")
    plot_perf(
        perfs[3], "Regression Task 1: Combined Cycle Power Plant Dataset")
