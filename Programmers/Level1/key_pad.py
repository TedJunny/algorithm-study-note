def solution(numbers, hand):
    coords = {
        1: (0, 0),
        2: (0, 1),
        3: (0, 2),
        4: (1, 0),
        5: (1, 1),
        6: (1, 2),
        7: (2, 0),
        8: (2, 1),
        9: (2, 2),
        0: (3, 1),
    }
    lx, ly = 3, 0
    rx, ry = 3, 2

    answer = ""

    for number in numbers:
        if number in (1, 4, 7):
            lx, ly = coords[number][0], coords[number][1]
            answer += "L"
        elif number in (3, 6, 9):
            rx, ry = coords[number][0], coords[number][1]
            answer += "R"
        else:
            if abs(coords[number][0] - lx) + abs(coords[number][1] - ly) < abs(coords[number][0] - rx) + abs(coords[number][1] - ry):
                lx, ly = coords[number][0], coords[number][1]
                answer += "L"
            elif abs(coords[number][0] - rx) + abs(coords[number][1] - ry) < abs(coords[number][0] - lx) + abs(coords[number][1] - ly):
                rx, ry = coords[number][0], coords[number][1]
                answer += "R"
            else:
                if hand == "left":
                    lx, ly = coords[number][0], coords[number][1]
                    answer += "L"
                else:
                    rx, ry = coords[number][0], coords[number][1]
                    answer += "R"

    return answer


print(solution([7, 0, 8, 2, 8, 3, 1, 5, 7, 6, 2], "left"))
