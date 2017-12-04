def sumAdjacent(x, y, data):
    mods = []
    mods.append({'x': x + 1, 'y': y + 1})
    mods.append({'x': x + 1, 'y': y})
    mods.append({'x': x + 1, 'y': y - 1})
    mods.append({'x': x, 'y': y + 1})
    mods.append({'x': x, 'y': y - 1})
    mods.append({'x': x - 1, 'y': y + 1})
    mods.append({'x': x - 1, 'y': y})
    mods.append({'x': x - 1, 'y': y - 1})

    summed = 0
    print mods
    print data
    for pair in mods:
        try:
            summed += data[x + pair['x'], y + pair['y']]
            print 'xxx', data[x + pair['x'], y + pair['y']]
        except:
            pass

    return summed


def grid(target):
    pairs = {}
    coords = {}
    numMax = target
    numMaxH = numMax / 2
    x = 0
    y = 0
    dx = 0
    dy = -1
    s = 0
    ds = 2
    i = 1
    while i <= target:
        if abs(x) <= numMax and abs(y) <= numMaxH:
            pairs[i] = {'x': x, 'y': y}

            try:
                coords[x][y] = sumAdjacent(x, y, coords)
            except:
                coords[x] = {}
                coords[x][y] = sumAdjacent(x, y, coords)

        if i == s:
            dx, dy = -dy, dx
            s, ds = s + ds / 2, ds + 1
        x, y = x + dx, y + dy
        i += 1
        print '----------------------------'

    print coords
    print pairs[target - 1], abs(pairs[target - 1]['x']) + abs(pairs[target - 1]['y'])
grid(3)
