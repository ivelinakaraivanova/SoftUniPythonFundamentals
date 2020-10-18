fire_level_list = input().split("#")
water = int(input())

effort = 0
total_fire = 0
put_out_cells = []

for cell in fire_level_list:
    split_cell = cell.split(" = ")
    fire_type = split_cell[0]
    cell_value = int(split_cell[1])
    if water >= cell_value:
        if (fire_type == "Low" and 1 <= cell_value <= 50) or \
        (fire_type == "Medium" and 51 <= cell_value <= 80) or \
        (fire_type == "High" and 81 <= cell_value <= 125):
            water -= cell_value
            effort += cell_value * 0.25
            put_out_cells.append(cell_value)
            total_fire += cell_value

print("Cells:")
for c in put_out_cells:
    print(f" - {c}")
print(f"Effort: {effort:.2f}")
print(f"Total Fire: {total_fire}")