def direction(facing, turn):
    directions = {'N': 0, 'NE': 45, 'E': 90, 'SE': 135, 'S': 180, 'SW': 225, 'W': 270, 'NW': 315}
    facing = facing.upper()
    revers_directions = {v: k for k, v in directions.items()}

    if facing not in directions or not isinstance(turn, int):
        raise ValueError('not valid data')

    if turn % 45 != 0 or turn > 1080 or turn < -1080:
        raise ValueError('not valid turn')

    angle = (directions[facing] + turn) % 360
    return revers_directions[angle]
