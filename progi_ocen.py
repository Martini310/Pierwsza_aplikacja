
def progi(max_pts):
    if not max_pts.isdigit():
        return 'Punkty podajemy za pomocą cyfr!'
    cel = round((0.9 * int(max_pts)), 2)
    bdb = round(0.8 * (int(max_pts)), 2)
    db = round(0.7 * (int(max_pts)), 2)
    dos = round(0.6 * (int(max_pts)), 2)
    dop = round(0.5 * (int(max_pts)), 2)
    output = f'Ocena dopuszczająca:\t od {dop} punktów\n' \
             f'Ocena dostateczna:\t od {dos} punktów\n' \
             f'Ocena dobra:\t\t od {db} punktów\n' \
             f'Ocena bardzo: dobra\t od {bdb} punktów\n' \
             f'Ocena celująca:\t\t od {cel} punktów'
    return output
