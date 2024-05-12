def place_def(*places):
    place_info = ''
    for place in places:
        name, address, hours, map_link = place
        place_info += f'<b>"{name}</b>" \n🗺 {address}\n⏰ {hours}\n'

        place_info += f'<a href="{map_link}">📌 На карті</a>\n\n'
    return place_info
