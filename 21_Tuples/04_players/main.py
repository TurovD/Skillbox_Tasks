players = {
    ("Ivan", "Volkin"): (10, 5, 13),
    ("Bob", "Robbin"): (7, 5, 14),
    ("Rob", "Bobbin"): (12, 8, 2)
}

compression_players =list(i_key + i_value for i_key, i_value in players.items())
print(f'{ compression_players } ')