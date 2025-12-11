# riscv1.asm

init:        # Met 1 dans t0
    addi t0, zero, 1

shift1:      # Décale t1 = t0 << 1
    slli t1, t0, 1

i42:         # Charge 0x2a dans t2
    li t2, 0x2a

mul3:        # Calcule t2 = 3 * t2
    mv t3, t2
    slli t3, t3, 1
    add  t2, t2, t3

s23:         # Décale t2 de 23 vers la gauche
    slli t2, t2, 23

t2pt2:       # Enchaîne additions, montre dépassement et récupération
    add  t2, t2, t2
    add  t2, t2, t2
    add  t2, t2, t2   # breakpoint suggéré ici
    srli t2, t2, 1
    add  t2, t2, t2

tc:          # Complément à 2: t2 = t0 - t2
    sub  t2, t0, t2

