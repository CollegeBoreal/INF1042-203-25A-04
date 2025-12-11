# main.s — RISC-V (RARS)
# Affiche "Hello RARS!" puis termine.

    .data
msg: .asciz "Hello RARS!\n"

    .text
    .globl main
main:
    # a0 = adresse de la chaîne
    la  a0, msg
    # a7 = 4  (service: print_string)
    li  a7, 4
    ecall

    # Fin du programme
    # a7 = 10 (service: exit)
    li  a7, 10
    ecall