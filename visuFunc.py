def dotCh(text, count, dt):
    if count > 0.6:
        count += 1*dt
        text += "."
        count = 0.0
        if text[-4:-1] == "...":
            text = "Press space "
    else:
        count += 1*dt
    return text, count
