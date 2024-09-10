def tower_of_hanoi(disks_num, source, destination, auxiliary):
    if disks_num == 1:
        print("Move disk 1 from source", source, "to destination", destination)
        return

    tower_of_hanoi(disks_num - 1, source, auxiliary, destination)
    print("Move disk", disks_num, "from source", source, "to destination", destination)
    tower_of_hanoi(disks_num - 1, auxiliary, destination, source)


disks_num = 3
tower_of_hanoi(disks_num, 'A', 'B', 'C')
