# Forrit sem finnur hæsta gildið sem notandi slær inn.
# Spyrja notanda um jákvætt gildi.
num_int = int(input("Input a number: "))
max_int = 0
while num_int >= 0:
    # Bera saman gildi notenda og finna hæsta gildið.
    if num_int >= max_int:
        # Setja það sem hæsta gildið.
        max_int = num_int
        # Prenta út hæsta gildið.
        # Spyrja notanda um annað jákvætt gildi
    num_int = int(input("Input a number: "))
print("The maximum is", max_int)
# Ef notandi setur inn neikvæða tölu, skal stoppa forritið.


