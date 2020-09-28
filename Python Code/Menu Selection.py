print('1.The Father\n2. The Mother\n3. The Maiden\n4. The Crone\n5. The Warrior\n6. The Smith\n7. The Stranger')
user=int(input('Which of the Seven New Gods would you like to learn about? '))
if user == 1:
    print('The Father represents divine justice, and judges the souls of the dead')
elif user == 2:
    print("The Mother represents mercy, peace, fertility, and childbirth. She is sometimes referred to as 'the strength of women.'")
elif user == 3:
    print('The Maiden represents purity, innocence, love, and beauty')
elif user == 4:
    print(' The Crone represents wisdom and foresight. She is represented carrying a lantern.')
elif user == 5:
    print('The Warrior represents strength and courage in battle.')
elif user == 6:
    print(' The Smith represents creation and craftsmanship.')
elif user == 7:
    print('The Stranger represents death and the unknown. It is rarely prayed to.')
elif (1 > user) or (user > 8):
    print('The night is dark and full of terrors for those who cannot read the menu.')
