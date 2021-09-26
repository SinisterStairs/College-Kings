# SCENE 04: Looking for Imre
# Locations: Hotel Lobby, Hotel Lobby Bathroom, Hotel Eating Area, Hotel Corridor
# Characters: MC (Outfit: 3)
# Time: Night

label v14s04:
    scene v14s04_1 # TPP. Show MC enteting the hotel lobby, neutral expression, mouth closed
    with dissolve

    pause 0.75

    scene v14s04_2 # TPP. Show MC looking for Imre in the hotel lobby, neutral expression, mouth closed
    with dissolve

    pause 0.75

    scene v14s04_3 # TPP. Show MC looking for Imre in the hotel lobby bathroom, slightly confused, mouth closed
    with dissolve

    u "(Where the fuck is he?!)"

    scene v14s04_4 # TPP. Show MC looking for Imre in the eating area of the hotel lobby, slightly annoyed, mouth closed
    with dissolve

    u "(Fuck it, I'll talk to him later I guess.)"

    scene v14s04_5 # TPP. Show MC walking through the hotel corridor, slightly annoyed, mouth closed
    with dissolve

    pause 0.75

    if v11_riley_roomate:
        jump v14s05a

    else:
        jump v14s05