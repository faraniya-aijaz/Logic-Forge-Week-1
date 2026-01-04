def towerOfHanoi(n, from_rod, to_rod, aux_rod):
    if n == 0:
        return
    towerOfHanoi(n - 1, from_rod, aux_rod, to_rod)
    print(f"Disk {n} moved from {from_rod} to {to_rod}")
    towerOfHanoi(n - 1, aux_rod, to_rod, from_rod)
print("Output for 2 disks:")
towerOfHanoi(2, 'A', 'C', 'B')
print("\nOutput for 3 disks:")
towerOfHanoi(3, 'A', 'C', 'B')
print("\nOutput for 4 disks:")
towerOfHanoi(4, 'A', 'C', 'B')
